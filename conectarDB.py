#-*-coding:utf-8-*-
#!/usr/bin/python3

import pymysql

class Conexion():

	def conectar(self):
		try:
			self.coneccion = pymysql.connect("localhost","root","123","classicmodels")
			return self.coneccion

		except pymysql.InternalError as error:
			code, message = error.args
			print("ERROR: ", code, message)
		
		
		







		
			
			  
			
		 

	
			
