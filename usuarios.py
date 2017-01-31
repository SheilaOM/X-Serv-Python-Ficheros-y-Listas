#!/usr/bin/python3

fich = open("/etc/passwd", "r")
users = fich.readlines()
fich.close()

shells = {}

for user in users:
	login = user.split(":")[0]
	shell = user.split(":")[-1][:-1]
	shells[login] = shell

print(shells['root'])
print(shells['imaginario'])

print("Número de usuarios: " + str(len(users)))
