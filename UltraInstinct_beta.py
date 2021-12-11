from random import randint
import time
from colorama import *
class jeux():
	def devine_nombre():
		trial = 1
		nb_trial = 5
		nb_al = randint(1, 10)
		print("\n")
		choice = int(input("Choisissez un nombre : "))

		while True:
			if trial == nb_trial:
				print("Nombres d'essais dépassés")
				input("Apppuyez sur ENTRER pour quitter")
				break
			else:
				if choice == nb_al:
					print("Félicitation , vous avez trouvé le juste prix !")
					print("Nombres d'essais : ", trial)
					input("Appuyez sur ENTRER pour quitter")
					break
				else:
					trial +=1
					if choice < nb_al:
						print("C'est plus !")
						choice = int(input("Réessayez : "))
					else:
						print("C'est moins !")
						choice = int(input("Réessayez : "))	
	def pfc():
		def joueur():
			player = input("pierre, feuille, ciseaux : \n").lower()
			while player not in ["pierre", "feuille", "ciseaux" ]:
				player = input("pierre, feuille, ciseaux : \n").lower()
			return(player)
		def ordi():
			ordinateur = randint(1,3)
			if ordinateur == 1:
				ordinateur = "pierre"
			if ordinateur ==2:
				ordinateur = "feuille"
			if ordinateur == 3:
				ordinateur = "ciseaux"
			return(ordinateur)
		a = joueur()
		b = ordi()
		def r():
			print ("choix utilisateur :" ,a, )
			print("Choix ordinateur:" ,b, )
		r()
		if a == "ciseaux" and b == "feuille":
			print("Bravo vous avez gagner")
		if a == "pierre" and b == "ciseaux":
			print("Bravo vous avez gagner")
		if a == "feuille" and b == "pierre":
			print("Bravo vous avez gagner")
		if a == "feuille" and b == "ciseaux":
			print("Vous avez perdu")
		if a == "ciseaux" and b == "pierre":
			print("Vous avez perdu")
		if a == "pierre" and b == "feuille":
			print("Vous avez perdu")
		if a == "feuille" and b == "feuille":
			print("égalité")
		if a == "pierre" and b == "pierre":
			print("égalité")
		if a == "ciseaux" and b == "ciseaux":
			print("égalité")
		lol = input("Veux tu rejouer? OUI/NON \n").lower()
		if lol == "OUI".lower():
			jeux.pfc()
		if lol == "NON".lower():
			print("ok")
			time.sleep(5)
			quit()

print(Fore.BLUE + """  
		  _    _  _  _                 _____              _    _               _    
 		 | |  | || || |               |_   _|            | |  (_)             | |   
		 | |  | || || |_  _ __  __ _    | |   _ __   ___ | |_  _  _ __    ___ | |_  
		 | |  | || || __|| '__|/ _` |   | |  | '_ \ / __|| __|| || '_ \  / __|| __| 
		 | |__| || || |_ | |  | (_| |  _| |_ | | | |\__ \| |_ | || | | || (__ | |_  
		  \____/ |_| \__||_|   \__,_| |_____||_| |_||___/ \__||_||_| |_| \___| \__|                                                              
                                                                              BETA By Gam's""")													 
print("========================================================================================================================")
print(Fore.GREEN + "Bienvenue dans la version Beta du jeux Ultra Instinct de Gam's \n Cette version n'est pas complete mais vous permet de patienter la sortie du vrai jeu qui sera plus esthetique et plus complet avec plusieurs niveaux")
def menu():
	choix = int(input(""""
A quel jeu veux tu jouer
1: Trouver le prix
2: Pierre, feuille, ciseaux \n"""))
	if choix == 1:
		jeux.devine_nombre()
	if choix == 2:
		jeux.pfc()
menu()