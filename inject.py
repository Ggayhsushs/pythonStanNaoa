import time

passs = open("login.txt", "w")
passs.write("74DLVQ538jK ваш пароль")
passs.close()

login = input("Пароль: ")
if login == "74DLVQ538jK":
	print("Create zero")
	print("")
	time.sleep(2)
	print("inject standoff 2 подождите")
	time.sleep(3)
	token = open("Token.txt", "w")
	token.write("kahxybsnwiidygwbkai")
	token.close()
	tokens = input("Айди вход: ")
	if tokens == "kahxybsnwiidygwbkai":
		offsets = input("Веди офсет только один: ")
		print("успешно применено:)")
	else:
		print("неправильный вход айди")
else:
	print("неправильный пароль")