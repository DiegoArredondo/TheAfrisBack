from flask_orator import jsonify
from flask import Flask, render_template, send_from_directory, request
from app import db_config
from flask import Flask
from flask_orator import Orator
import json
import time
import datetime

app = Flask(__name__, static_url_path= '')
app.config['ORATOR_DATABASES']= db_config.db_config
db= Orator(app)

""" IMPORT MODELS """
from app.models import Eventos as tablaEventos
from app.models import Usuarios as tablaUsuarios
from app.models import Publicaciones as tablaPublicaciones
from app.models import Respuestas as tablaRespuestas
from app.models import Foros as tablaForos
from app.models import Hilos as tablaHilos
from app.models import Secciones as tablaSecciones
from app.models import Roles as tablaRoles
from app.models import Privacidad as tablaPrivacidad
from app.models import Hobbies as tablaHobbies

""" PARA MONTAR SITIO WEB 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/css/<path:path>')
def sendcss(path):
    return send_from_directory('css',path)
@app.route('/js/<path:path>')
def sendjs(path):
    return send_from_directory('js',path)
@app.route('/assets/<path:path>')
def sendassets(path):
    return send_from_directory('assets',path)
    
@app.route('/<path:path>')
def ruta(path):
    return send_from_directory('favicon',path)
 """


""" ENDPOINTS """

@app.route('/hola')
def hola():
    return "hola"


@app.route('/ruta', methods=['POST']) #GET requests will be blocked
def nombreDelMetodo(request):
    data = request.get_json(force = True)
    return data



""" AGREGAR UN USUARIO
EJEMPLO DE REQUEST:
{
    "nombre" : nombre
    "apellidos" : apellidos
    "correo" : correo
    "password1" : password1
    "password2" : password2
    "fechaNacimiento" : fechaNacimiento
    "descripcion" : descripcion
}
 """
@app.route('/register',methods=['POST'])
def register():
    try:
        content = request.get_json(force=True)
        print(content)
        nombre=content['nombre']
        apellidos=content['apellidos']
        correo=content['correo']
        password1=content['password1']
        password2=content['password2']
        fechaNacimiento=content['fechaNacimiento']
        descripcion=content['descripcion']

        if (password1 != password2):
            raise ValueError('Las contraseñas introducidas no coinciden')

        usuarioNuevo= tablaUsuarios()
        usuarioNuevo.nombre = nombre
        usuarioNuevo.apellidos = apellidos
        usuarioNuevo.correo = correo
        usuarioNuevo.password = password1
        usuarioNuevo.fechaNacimiento = fechaNacimiento
        usuarioNuevo.descripcion = descripcion

        usuarioNuevo.save()
        return "True"
    except Exception as e:
        return jsonify({"error":str(e)})

""" AGREGAR UN EVENTO
EJEMPLO DE REQUEST:
{
"titulo" : "Titulo del evento",
"descripcion" : "Descripcion de prueba",
"fechaHora" : "2020-04-20 12:00:17",
"etiquetas" : "#etiqueta1,#etiqueta2,#etiqueta3",
"duracion" : "5 dias",
"creador" : 1,
"cupo" : 50,
"ubicacion" : "Lugar del evento"
}
 """
@app.route('/postEvent',methods=['POST'])
def postEvent():
    try:
        content = request.get_json(force=True)
        print(content)

        titulo=content['titulo']
        descripcion=content['descripcion']
        fechaHora=content['fechaHora']
        etiquetas=content['etiquetas']
        duracion=content['duracion']
        cupo=content['cupo']
        ubicacion=content['ubicacion']
        creador=content['creador']

        if cupo <= 0:
            if cupo != -1:
                raise ValueError('El cupo debe ser de al menos 1 persona')

        eventoNvo= tablaEventos()

        eventoNvo.titulo = titulo
        eventoNvo.descripcion = descripcion
        eventoNvo.fechaHora = fechaHora
        eventoNvo.etiquetas = etiquetas
        eventoNvo.duracion = duracion
        eventoNvo.cupo = cupo
        eventoNvo.ubicacion = ubicacion
        eventoNvo.creador = creador

        eventoNvo.save()

        return "True"
    except Exception as e:
        return jsonify({"error":str(e)})

""" AGREGAR UNA PUBLICACION
EJEMPLO DE REQUEST:
{
"titulo" : "Titulo de la publicacion",
"descripcion" : "Descripcion de prueba",
"etiquetas" : "#etiqueta1,#etiqueta2,#etiqueta3",
"creador" : 1
}
 """
@app.route('/postPost',methods=['POST'])
def postPost():
    try:
        content = request.get_json(force=True)
        print(content)

        titulo=content['titulo']
        descripcion=content['descripcion']
        etiquetas=content['etiquetas']
        creador=content['creador']

        postNvo= tablaPublicaciones()

        postNvo.titulo = titulo
        postNvo.descripcion = descripcion
        postNvo.etiquetas = etiquetas
        postNvo.creador = creador

        postNvo.save()

        return "True"
    except Exception as e:
        return jsonify({"error":str(e)})





def getJson(url):
    jsonFile = open(url)
    print(url)
    answer = json.load(jsonFile)
    print(answer)
    return answer

@app.route('/showUsers')
def dataUsers():
    return jsonify(tablaUsuarios.get().serialize())
@app.route('/showPosts')
def dataPosts():
    return jsonify(tablaPublicaciones.get().serialize())
@app.route('/showEvents')
def dataEvents():
    return jsonify(tablaEventos.get().serialize())

if __name__ == '__main__':
    app.run(debug=True)