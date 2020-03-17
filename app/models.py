from orator import Model
class Eventos(Model):
    __table__ = 'eventos'
    __primary_key__ = 'id'
    __hidden__ = ['creador']

class Publicaciones(Model):
    __table__ = 'publicaciones'
    __primary_key__ = 'id'
    __hidden__ = ['creador']

class Respuestas(Model):
    __table__ = 'respuestas'
    __primary_key__ = 'id'
    __hidden__ = ['creador']
    __timestamps__ = False

class Foros(Model):
    __table__ = 'foros'
    __primary_key__ = 'id'
    __timestamps__ = False

class Hilos(Model):
    __table__ = 'hilos'
    __primary_key__ = 'id'
    __hidden__ = ['creador']
    __timestamps__ = False

class Secciones(Model):
    __table__ = 'secciones'
    __primary_key__ = 'id'
    __timestamps__ = False

class Usuarios(Model):
    __table__ = 'users'
    __primary_key__ = 'id'

class Roles(Model):
    __table__ = 'roles'
    __primary_key__ = 'id'
    __timestamps__ = False

class Hobbies(Model):
    __table__ = 'hobbies'
    __primary_key__ = 'id'
    __timestamps__ = False

class Privacidad(Model):
    __table__ = 'privacidad'
    __primary_key__ = 'id'
    __timestamps__ = False

