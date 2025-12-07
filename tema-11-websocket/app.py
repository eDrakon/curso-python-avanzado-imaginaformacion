import json
import threading
import requests
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_123'
socketio = SocketIO(app)

thread = None
thread_lock = threading.Lock()

url_base = "http://api.weatherstack.com/current?access_key=c665e9026b8d33768992ee5564c619b1&query="

def background_thread(ciudad):
    count = 0
    while True:
        socketio.sleep(3)
        count += 1

        try:
            url = url_base + ciudad
            respuesta = requests.get(url).json()

            location = respuesta['location']['name']
            hora = respuesta['current']['observation_time']
            temperatura = respuesta['current']['temperature']

            lst_dict = {
                'hora': str(hora),
                'localizacion': location,
                'temperatura': str(temperatura)
            }

            socketio.emit('my_api_response',
                          {'data': lst_dict, 'count': count, 'error': False},
                          namespace='/test')

        except Exception as e:
            print(f"Error en el hilo de fondo: {e}")
            socketio.emit('my_api_response',
                          {'data': 'Error al conectar o parsear la API.', 'count': count, 'error': True},
                          namespace='/test')

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect', namespace='/test')
def connect_request():
    global thread
    ciudad = 'Madrid'

    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread, ciudad)

    emit('my_response', {'data': 'Conectado al servidor de Oxsia', 'count': 0})

@socketio.on('disconnect', namespace='/test')
def disconnect_request():
    print('Cliente desconectado', threading.get_ident())


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)