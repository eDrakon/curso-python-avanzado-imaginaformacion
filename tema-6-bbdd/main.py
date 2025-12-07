from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, backref
from sqlalchemy import Column, Integer, String

# Ejecutar 1
# Crear los modelos asociados a las siguientes entidades con sus atributos y relaciones:
# Empresa (cif, nombre, ciudad, numero_empleados)
# Empleado(nif,nombre,ciudad)
# La relación de las entidades es que una Empresa puede tener varios Empleados.

engine = create_engine("sqlite:///tema6.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresa"
    id = Column(Integer, primary_key=True)
    cif = Column(String(9), unique=True)
    nombre = Column(String(100))
    ciudad = Column(String(100))
    numero_empleados = Column(Integer)
    empleados = relationship("Empleado", backref="empresa")

class Empleado(Base):
    __tablename__ = "empleado"
    id = Column(Integer, primary_key=True)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))
    nif = Column(String(9), unique=True)
    nombre = Column(String(100))
    ciudad = Column(String(100))

Base.metadata.create_all(engine)

# Ejercicio 2
# Sobre el modelo anterior:
# Agregar una empresa y varios empleados a la misma.
# Consultar el número de empleados de la empresa contabilizando sus hijos, no a través de su campo numero_empleados.

empleados = [
    ('Juan Sanchez','04565543J', 'Madrid'),
    ('Francisco Rodríguez', '02354554V', 'Barcelona')
]


def add_nueva_empresa(session, cif, nombre, ciudad, empleados_list):

    empresa = Empresa(cif=cif, nombre=nombre, ciudad=ciudad)

    for nombre, nif, ciudad in empleados_list:
        empleado = Empleado(nombre=nombre, nif=nif, ciudad=ciudad)
        empresa.empleados.append(empleado)

    session.add(empresa)
    session.commit()


add_nueva_empresa(session,'4343434V','Prueba S.L','Toledo', empleados)


def get_numero_empleados(session,nombre_empresa):
    res = (session.query(Empleado)
           .join(Empresa)
           .filter(Empresa.nombre == nombre_empresa)
           .count())
    return res

n = get_numero_empleados(session, 'Prueba S.L')
print(f'Numero de empleados: {n}')

# Ejercicio 3
# Sobre el modelo anterior:
# Actualizar el campo numero_empleados de la tabla Empresa con el número obtenido de la consulta anterior.
# Eliminar todos los empleados de la empresa.

session.query(Empresa).filter(Empresa.nombre == 'Prueba S.L').update({'numero_empleados': n})
session.commit()

session.query(Empleado).filter(
    Empleado.empresa_id.in_(
        session.query(Empresa.id).filter(Empresa.nombre == "Prueba S.L")
    )
).delete()

session.commit()