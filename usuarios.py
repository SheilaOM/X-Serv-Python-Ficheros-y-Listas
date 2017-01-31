#!/usr/bin/python3

fich = open("/etc/passwd", "r")
users = fich.readlines()
fich.close()

for user in users:
	login = user.split(":")[0]
	shell = user.split(":")[-1]
	print("usuario: " + login + ", shell: " + shell, end="")
	#En vez de poner end="", se puede quitar el \n de la variable shell: user.split(":")[-1][:-1]

print("Número de usuarios: " + str(len(users)))
