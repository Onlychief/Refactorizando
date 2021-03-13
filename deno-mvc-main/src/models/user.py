from config.mariadb import DB

import mariadb

class UsuariosModel():
    
    def listar(self):

        cursor = DB.cursor()
        cursor.execute('select * from datosuser ')
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios

    def crear(self, nombre, apellido, celular, correo, contrasenia):
        
        cursor = DB.cursor()
        cursor.execute('insert into datosuser(nombre,apellido,celular,correo,contrasenia) values(?,?,?,?,?)', 
        (nombre,apellido,celular,correo,contrasenia,))
        cursor.close()

     
    def eliminar(self, cod):

        cursor = DB.cursor()
        cursor.execute('delete from datosuser WHERE id = ? ', cod)
        cursor.close()

    def creardatabase (self, name):

        cursor = DB.cursor()
        cursor.execute('CREATE DATABASE '+ name)
        cursor.close()
        
    def actualizar(self,nombre,apellido,celular,correo,contrasenia,cod):

        cursor = DB.cursor()
        cursor.execute('update datosuser set nombre = ?, apellido = ?, celular = ?, correo = ?, contrasenia = ? WHERE id = ? ', 
        (nombre,apellido,celular,correo,contrasenia,cod))
        cursor.close()


        
    


        