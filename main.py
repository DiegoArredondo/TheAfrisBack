from flask_orator import jsonify
from flask import Flask, render_template, send_from_directory, request
from app import db_config
from flask import Flask
from flask_cors import CORS
from flask_orator import Orator
import json
import time
import datetime

app = Flask(__name__, static_url_path= '')
app.config['ORATOR_DATABASES']= db_config.db_config
db= Orator(app)
# Cors (CROSS ORIGIN RESOURCE SHARING) 
CORS(app=app,supports_credentials=True)

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
        print("Received request for: register")
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
        return jsonify({"success":"Agregado con éxito"})
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
        print("Received request for: postEvent")
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

        return jsonify({"success":"Agregado con éxito"})
    except Exception as e:
        return jsonify({"error":str(e)})

""" EDITAR UN EVENTO
EJEMPLO DE REQUEST:
{
"id" : 1
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
@app.route('/updateEvent',methods=['POST'])
def updateEvent():
    try:
        content = request.get_json(force=True)
        print("Received request for: updateEvent")
        print(content)

        eventid=content['id']
        titulo=content['titulo']
        descripcion=content['descripcion']
        fechaHora=content['fechaHora']
        etiquetas=content['etiquetas']
        duracion=content['duracion']
        cupo=content['cupo']
        ubicacion=content['ubicacion']

        if cupo <= 0:
            if cupo != -1:
                raise ValueError('El cupo debe ser de al menos 1 persona')

        evento = tablaEventos.where_id(eventid).first()
        if evento != None:
            tablaEventos.where_id('id', eventid).update({"titulo": titulo,"descripcion": descripcion,"fechaHora": fechaHora,"etiquetas": etiquetas,"duracion": duracion,"cupo": cupo,"ubicacion": ubicacion})
            return jsonify({"success":"Actualizado con éxito"})
        else:
            raise ValueError("El evento que está intentando eliminar no existe")
    except Exception as e:
        return jsonify({"error":str(e)})


""" ELIMINAR UN EVENTO
EJEMPLO DE REQUEST:
{
"id" : 1
}
 """
@app.route('/deleteEvent',methods=['POST'])
def deleteEvent():
    try:
        content = request.get_json(force=True)
        print("Received request for: deleteEvent")
        print(content)

        eventid=content['id']

        evento = tablaEventos.where_id(eventid).first()
        if evento != None:
            tablaEventos.where_id('id', eventid).delete()
            return jsonify({"success":"Eliminado con éxito"})
        else:
            raise ValueError("El evento que está intentando eliminar no existe")
    except Exception as e:
        return jsonify({"error":str(e)})




""" AGREGAR UNA PUBLICACION
EJEMPLO DE REQUEST:
{
"titulo" : "Titulo de la publicacion",
"contenido" : "Descripcion de prueba",
"etiquetas" : "#etiqueta1,#etiqueta2,#etiqueta3",
"creador" : 1,
"seccion" : 1
}
 """
@app.route('/postPost',methods=['POST'])
def postPost():
    try:
        content = request.get_json(force=True)
        print("Received request for: postPost")
        print(content)

        titulo=content['titulo']
        contenido=content['contenido']
        etiquetas=content['etiquetas']
        creador=content['creador']
        seccion=content['seccion']

        postNvo= tablaPublicaciones()

        postNvo.titulo = titulo
        postNvo.contenido = contenido
        postNvo.etiquetas = etiquetas
        postNvo.creador = creador
        postNvo.seccion = seccion

        postNvo.save()

        return jsonify({"success":"Agregado con éxito"})
    except Exception as e:
        return jsonify({"error":str(e)})

""" EDITAR UNA PUBLICACION
EJEMPLO DE REQUEST:
{
"id" : 1
"titulo" : "Titulo de la publicacion",
"contenido" : "Descripcion de prueba",
"etiquetas" : "#etiqueta1,#etiqueta2,#etiqueta3",
"creador" : 1,
"seccion" : 1
}
 """
@app.route('/updatePost',methods=['POST'])
def updatePost():
    try:
        content = request.get_json(force=True)
        print("Received request for: updatePost")
        print(content)

        postid=content['id']
        titulo=content['titulo']
        contenido=content['contenido']
        etiquetas=content['etiquetas']
        seccion=content['seccion']

        post = tablaPublicaciones.where_id(postid).first()
        if post != None:
            tablaPublicaciones.where_id('id', postid).update({"titulo":titulo,"contenido" : contenido,"etiquetas" : etiquetas,"seccion" : seccion})
            return jsonify({"success":"Actualizado con éxito"})
        else:
            raise ValueError("La publicación que está intentando eliminar no existe")
    except Exception as e:
        return jsonify({"error":str(e)})

""" ELIMINAR UNA PUBLICACION
EJEMPLO DE REQUEST:
{
"id" : 1
}
 """
@app.route('/deletePost',methods=['POST'])
def deletePost():
    try:
        content = request.get_json(force=True)
        print("Received request for: deletePost")
        print(content)

        postid=content['id']

        post = tablaPublicaciones.where_id(postid).first()
        if post != None:
            tablaPublicaciones.where_id('id', postid).delete()
            return jsonify({"success":"Eliminado con éxito"})
        else:
            raise ValueError("La publicación que está intentando eliminar no existe")
    except Exception as e:
        return jsonify({"error":str(e)})

""" OBTENER UNA PUBLICACION
EJEMPLO DE REQUEST:
{ "id" : 1 }
 """
@app.route('/getPost',methods=['POST'])
def getPost():
    try:
        content = request.get_json(force=True)
        print("Received request for: getPost")
        print(content)

        postid=content['id']
        post = tablaPublicaciones.where_id(postid).first()
        if post != None:
            return jsonify(post.serialize())
        else:
            raise ValueError("La publicación que está buscando no existe")
    except Exception as e:
        return jsonify({"error":str(e)})

""" OBTENER UN EVENTO
EJEMPLO DE REQUEST:
{ "id" : 1 }
 """
@app.route('/getEvent',methods=['POST'])
def getEvent():
    try:
        content = request.get_json(force=True)
        print("Received request for: getEvent")
        print(content)

        eventid=content['id']
        evento = tablaEventos.where_id(eventid).first()
        if evento != None:
            return jsonify(evento.serialize())
        else:
            raise ValueError("El evento que está buscando no existe")
    except Exception as e:
        return jsonify({"error":str(e)})

""" OBTENER UN USUARIO
EJEMPLO DE REQUEST:
{ "id" : 1 }
 """
@app.route('/getUser',methods=['POST'])
def getUser():
    try:
        content = request.get_json(force=True)
        print("Received request for: getUser")
        print(content)

        userid=content['id']
        user = tablaEventos.where_id(userid).first()
        if evento != None:
            return jsonify(user.serialize())
        else:
            raise ValueError("El usuario que está buscando no existe")
    except Exception as e:
        return jsonify({"error":str(e)})

@app.route('/getAllUsers')
def dataUsers():
    return jsonify(tablaUsuarios.get().serialize())
@app.route('/getAllPosts')
def dataPosts():
    return jsonify(tablaPublicaciones.get().serialize())
@app.route('/getAllEvents')
def dataEvents():
    return jsonify(tablaEventos.get().serialize())

if __name__ == '__main__':
    app.run(debug=True)

def getJson(url):
    jsonFile = open(url)
    print(url)
    answer = json.load(jsonFile)
    print(answer)
    return answer