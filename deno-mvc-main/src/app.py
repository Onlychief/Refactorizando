from flask import Flask,jsonify,request,make_response
from controllers.usuario import UserControl


userControl = UserControl()
app = Flask (__name__)
  


@app.route('/listado', methods = ['GET'])

def listando():
   
    lista = userControl.listado()
    return make_response(jsonify(lista), 200)

@app.route('/crear', methods = ['POST'])

def creando():

    nombre = request.json ["nombre"]
    apellido = request.json ["apellido"]
    celular = request.json ["celular"]
    correo = request.json ["correo"]
    contrasenia = request.json ["contrasenia"]

    creacion = userControl.crear(nombre,apellido,celular,correo,contrasenia)

@app.route('/actualizar/<cod>', methods = ['PUT'])

def actualizando(cod):

    nombre = request.json ["nombre"]
    apellido = request.json ["apellido"]
    celular = request.json ["celular"]
    correo = request.json ["correo"]
    contrasenia = request.json ["contrasenia"]

    creacion = userControl.actualizar(nombre,apellido,celular,correo,contrasenia,cod)

@app.route('/eliminar/<cod>', methods = ['DELETE'])

def borrando(cod):
    userControl.borrar(cod)
      
app.run(debug=True)

  