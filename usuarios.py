#!/usr/bin/python3

fich = open("/etc/passwd", "r")
users = fich.readlines()
fich.close()

shells = {}

for user in users:
	login = user.split(":")[0]
	shell = user.split(":")[-1][:-1]
	shells[login] = shell

usuarios = ['root', 'imaginario']
for usuario in usuarios:
	try:
		print(shells[usuario])
	except KeyError:
		print("El usuario 'imaginario' no existe")

print("Número de usuarios: " + str(len(users)))
