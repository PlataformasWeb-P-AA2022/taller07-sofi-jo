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

archivo = open("data/datos_clubs.txt", "r")
registros = archivo.readlines()


for a in registros:
    nombre = a.split(";")[0]
    deporte = a.split(";")[1]
    fundacion = a.split(";")[2]
    c = Club(nombre= nombre, deporte= deporte,
        fundacion= fundacion)
    session.add(c)


session.commit()




 