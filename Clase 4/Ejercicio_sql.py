import pymysql
#definimos un objetos Base de datos

class usuario():
    def __init__(self,nombre,contrasenia,saldo):
        self.nombre=nombre
        self.contrasenia=contrasenia
        self.saldo=saldo



class Database():
    #creamos el constructor con la bbdd elegida a traves de pymysql
    def __init__(self):
        self.connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='mydb'
    )
    #chequeo que la bbdd este en funcionamiento, sino no se conecta
    #y lanza un error (no llega al print)
        self.cursor = self.connection.cursor()
        print("La conexion fue exitosa")
   
    #METODOS
    def all_users (self):
        sql='SELECT * FROM usuarios'
 
        self.cursor.execute(sql)
        users=self.cursor.fetchall()
 
        for user in users:
            print("ID:",user[0] )
            print("Nombre:",user[1] )
            print("Contrasenia:", user[2])
 
    def get_user (self, ide):
        query= "SELECT * FROM usuarios WHERE idusuarios='{}' ".format(ide)
 
        try:
            self.cursor.execute(query)
            user=self.cursor.fetchone()
            print("ID:",user[0] )
            print("Nombre:",user[1] )
            print("Contrasenia:", user[2])
            print("Saldo:",user[3])
 
        except Exception as e:
            print("No existe ese usuario")
            raise
 
    def create_user (self, n_nuevo, n_contrasenia):
        query= "INSERT INTO usuarios(nombre, contrasenia) VALUES ('{}','{}')".format(n_nuevo,n_contrasenia)
 
        try:  
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print("No se inserto el usuario")
            raise
 
    def delete_user(self,ide):
        query="DELETE FROM usuarios WHERE idusuarios='{}' ".format(ide)
 
        try:  
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print("No se elmino el usuario")
            raise
 
    def update_saldo(self,ide, n_saldo,cantidad):
        query="SELECT saldo FROM usuarios WHERE idusuarios = '{}'".format(n_saldo,ide)
        try:  
            self.cursor.execute(query)
            saldo_actual=self.cursor.fetchone(query)
            saldo_final=int(saldo_actual-cantidad)
            query="UPDATE usuarios SET saldo= '{}' WHERE idusuarios= '{}'".format(saldo_final,ide)
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print("No se actualizo el saldo")
            raise
 
   
 
 
 
mydb= Database()
#mydb.all_users()
#mydb.get_user(2)
#mydb.create_user("Florencia", "12345")
#mydb.delete_user(3)
mydb.update_saldo(2, "20000",5000)
#mydb.all_users()
