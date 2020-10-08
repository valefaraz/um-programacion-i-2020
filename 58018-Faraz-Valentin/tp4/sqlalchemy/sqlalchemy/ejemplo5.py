from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class DBCon:
    def __init__(self):

        # SQLite
        #str_conexion = 'sqlite:///fernando.db'
        #self.engine = create_engine(str_conexion, echo=True, connect_args={"check_same_thread": False})

        # Contenedor Docker con MySQL
        # str_conexion = 'mysql+pymysql://fernando:fernando@mysql:3306/sqlalchemy'
        # self.engine = create_engine(str_conexion, echo=True)

        # Equipo local con MySQL
        str_conexion = 'mysql+pymysql://valentin:valentin@192.168.1.169:3306/sqlalchemy'
        self.engine = create_engine(str_conexion, echo=False)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.crear_estructura()

    def crear_estructura(self):
        Base.metadata.create_all(self.engine)

# Relacion One To Many
# One
class Persona(Base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100))
    registros = relationship('Registro', backref="persona")

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.registro = None

    def __repr__(self):
        resultado = ''
        for reg in self.registros:
            resultado=resultado+"{}\n".format(reg)
        salida = 'Persona {}: apellido, nombre: {}, {}. Lista de registros:\n {}'\
            .format(self.id, self.apellido, self.nombre, resultado)
        return salida

# Many
class Registro(Base):
    __tablename__ = "registro"
    id = Column(Integer, primary_key=True)
    actividad = Column(String(160))
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    persona_id = Column(Integer, ForeignKey('persona.id'))

    def __init__(self, actividad):
        self.actividad = actividad

    def __repr__(self):
        salida = "Registo {}: actividad: {}. Creado el {}".format(
            self.id, self.actividad, self.fecha_creacion)
        return salida


class PersonaDao:
    def __init__(self, db):
        self.db = db
        self.regDao = RegistroDao(db)

    def guardar(self, persona):
        self.db.session.add(persona)
        self.db.session.commit()
        #self.db.session.close()
        #return registro

    def borrar(self, persona):
        for reg in persona.registros:
            self.regDao.borrar(reg)
        self.db.session.delete(persona)
        self.db.session.commit()
        #self.db.session.close()

    def modificar(self, persona):
        actual = self.db.session.query(Persona).filter_by(id=persona.id).one()
        actual.nombre = persona.nombre
        actual.apellido = persona.apellido
        self.db.session.commit()
        #self.db.session.close()
        return actual

    def buscarPorID(self, id):
        consulta = self.db.session.query(Persona).filter_by(id=id)
        if consulta.count() > 0:
            return consulta.one()
        else:
            return None

    def buscarTodos(self):
        actual = self.db.session.query(Persona).all()
        return actual


class RegistroDao:
    def __init__(self, db):
        self.db = db

    def guardar(self, registro):
        self.db.session.add(registro)
        self.db.session.commit()
        #self.db.session.close()
        #return registro

    def borrar(self, registro):
        self.db.session.delete(registro)
        self.db.session.commit()
        #self.db.session.close()

    def modificar(self, registro):
        actual = self.db.session.query(Registro).filter_by(id=registro.id).one()
        actual.actividad = registro.actividad
        self.db.session.commit()
        #self.db.session.close()
        return actual

    def buscarPorID(self, id):
        consulta = self.db.session.query(Registro).filter_by(id=id)
        if consulta.count() > 0:
            return consulta.one()
        else:
            return None

    def buscarTodos(self):
        actual = self.db.session.query(Registro).all()
        return actual


if __name__ == "__main__":
    print("Conectandose a la base de datos")
    print("Creando la estructura de las tablas")
    print("Creando la sesion de acceso a la base de datos")
    db = DBCon()
    print("Creando DAO")
    personaDAO = PersonaDao(db)
    registroDAO = RegistroDao(db)

    r1 = Registro("accion 1")
    r2 = Registro("accion 2")
    pers1 = Persona("Fernando", "Villarreal")
    pers1.registros.append(r1)
    pers1.registros.append(r2)
    personaDAO.guardar(pers1)

    pers2 = personaDAO.buscarPorID(1)
    r5 = Registro("accion 5")
    r5.persona=pers2
    registroDAO.guardar(r5)

    pers3 = personaDAO.buscarPorID(3)
    personaDAO.borrar(pers3)

    personas = personaDAO.buscarTodos()
    for persona in personas:
        print(persona)
