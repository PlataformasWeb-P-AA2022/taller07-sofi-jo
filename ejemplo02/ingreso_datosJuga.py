from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivoJug = open("data/datos_jugadores.txt", "r")
registroJ = archivoJug.readlines()


for a in registroJ:
    
    nombre = a.split(";")[3]
    dorsal = a.split(";")[2]
    posicion = a.split(";")[1]
    cl = session.query(Club).filter_by(nombre= a.split(";")[0]).one()
    j = Jugador(nombre= nombre, dorsal= dorsal,
        posicion= posicion, club = cl )
    session.add(j)

session.commit()