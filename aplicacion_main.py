#-*-coding:utf-8-*-
#!/usr/bin/python3
from os import system
from prettytable import PrettyTable
import pymysql
from conectarDB import Conexion

class Aplicacion(Conexion):
	
	
	def encabezado_menu(self):
		system("cls")
		print("***********************************")
		print("***********************************")
		print("******                      *******")
		print("******   Operaciones CRUD   *******")
		print("******                      *******")
		print("***********************************")
		print("***********************************")
		print("           MENU PRINCIPAL          ")
		print("***********************************")
		print("***********************************")
		print("1=Listar offices tabla")
		print("2=Insertar en tabla offices")
		print("3=Modificar tabla")
		print("4=Eliminar campo de una tabla")
		print("5=Leer campo en especial")
		print("6=Salir")
		print("***********************************")
		print("***********************************")

	def menu_principal(self):
		while True:
			self.encabezado_menu()
			try:
				op = int(input("DIGITE SU OPCION: "))
				print ("***********************************")

				if op == 1:
					self.listar()

				elif op == 2:
					self.insertar()

				elif op == 3:
					self.modificar()

				elif op == 4:
					self.eliminar()

				elif op == 5:
					self.leer()
				
				
			except ValueError:
				print ("*******************************************")
				print ("ERROR - La opcion debe ser un numero entero")
				print ("*******************************************")
				input()


	
	
	def listar(self):
		conexion = self.conectar()
		cursor = conexion.cursor()
		x = PrettyTable()
		sql = "SELECT * FROM offices"
		try:
			cursor.execute(sql)
			resultado = cursor.fetchall()
			x.field_names = ["officeCode", "City", "Phone", "AddressLine1", "AddressLine2", "State", "Country", "PostalCode", "Territory"]
			for row in resultado:
				x.add_row([ row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
			
			system("cls")
			print(x)

     
		except:
			print ("Error: unable to fetch data")	

		conexion.close()
		input()
		




	def insertar(self):
		conexion = self.conectar()
		cursor = conexion.cursor()
		sql = "INSERT INTO offices VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"
		try:
			officecode = input("Digite el codigo de la oficina: ")
			city = input("Digite el Nombre de la ciudad: ")
			phone = input("Digite el telefono: ")
			AddressLine1 = input("Digite la direccion numero 1: ")
			AddressLine2 = input("Digite la direccion numero 2: ")
			state = input("Digite el estado: ")
			country = input("Digite el pais: ")
			postalcode = input("Digite el codigo postal: ")
			territory = input("Digite el territorio: ")  
			cursor.execute(sql%(officecode,city,phone,AddressLine1,AddressLine2,state,country,postalcode,territory))
			conexion.commit()
			print ("**************************************")
			print ("¡El campo se inserto correctamente!")
			print ("**************************************")

			

		except ValueError:
			print ("**************************************")
			print ("ERROR AL INGRESAR DATOS")
			print ("**************************************")

		finally:
			conexion.close()
			input()


	def modificar(self):
		conexion = self.conectar()
		cursor = conexion.cursor()
		sql = "UPDATE offices SET City = %s , Phone = %s , AddressLine1 = %s , AddressLine2 = %s , State = %s , Country = %s, PostalCode = %s , Territory = %s WHERE officeCode = %s"

		try:
			officecode = input("Digite el codigo de la oficina a modificar: ")
			if self.verificar(officecode) != 0:
		
				city = input("Digite el nuevo Nombre de la ciudad: ")
				phone = input("Digite el nuevo telefono: ")
				AddressLine1 = input("Digite la nueva direccion numero 1: ")
				AddressLine2 = input("Digite la nueva direccion numero 2: ")
				state = input("Digite el nuevo estado: ")
				country = input("Digite el nuevo pais: ")
				postalcode = input("Digite el nuevo codigo postal: ")
				territory = input("Digite el nuevo territorio: ")
				cursor.execute(sql,(city,phone,AddressLine1,AddressLine2,state,country,postalcode,territory,officecode))
				conexion.commit()
				print ("**************************************")
				print ("¡El campo se modifico correctamente!")
				print ("**************************************")

			else:
				print ("**************************************")
				print ("INFO-¡El ID no existe")
				print ("**************************************")



		except ValueError:
			print ("**************************************")
			print ("ERROR AL INGRESAR DATOS")
			print ("**************************************")

		finally:
			conexion.close()
			input()


	def eliminar(self):
		conexion = self.conectar()
		cursor = conexion.cursor()
		
		try:
			officecode = input("Digite el codigo de la oficina a eliminar: ")
			sql = "DELETE FROM offices WHERE officeCode = '%s'"%officecode
			if self.verificar(officecode) != 0:
				print ("**************************************")
				print ("ESTA SEGURO QUE DESEA BORRAR LA FILA?")
				print ("1=SI")
				print ("2=NO") 
				print ("**************************************")
				op = int(input("Digite su opción: "))
				if op == 1:
					cursor.execute(sql)
					conexion.commit()
					print ("**************************************")
					print ("¡El campo se elimino correctamente!")
					print ("**************************************")

			else:
				print ("**************************************")
				print ("INFO-¡El ID no existe")
				print ("**************************************")

		except ValueError:
			print ("**************************************")
			print ("ERROR AL INGRESAR DATOS")
			print ("**************************************")

		finally:
			conexion.close()
			input()



	def leer(self):
		conexion = self.conectar()
		cursor = conexion.cursor()
		x = PrettyTable()
		officecode = input("Digite el codigo de la oficina: ")
		sql = "SELECT * FROM offices WHERE officeCode = '%s'"%officecode
		try:
			if self.verificar(officecode) != 0:
				cursor.execute(sql)
				resultado = cursor.fetchall()
				x.field_names = ["officeCode", "City", "Phone", "AddressLine1", "AddressLine2", "State", "Country", "PostalCode", "Territory"]
				for row in resultado:
					x.add_row([ row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
				
				system("cls")
				print(x)

			else:
				print ("**************************************")
				print ("INFO-¡El ID no existe")
				print ("**************************************")

		except:
			print ("Error: unable to fetch data")	

		conexion.close()
		input()


	


	def verificar(self,officecode):
		conexion = self.conectar()
		cursor = conexion.cursor()
		sql = "SELECT * FROM offices WHERE officeCode = %s"
		try:
			result = cursor.execute(sql,officecode)
			resultado = cursor.fetchone()
				
			return result

		except ValueError:
			print ("**************************************")
			print ("ERROR AL INGRESAR DATOS")
			print ("**************************************")

		finally:
			conexion.close()
		













		
		


			
		





		



















if __name__ == '__main__':
	aplicacion = Aplicacion()
	aplicacion.menu_principal()