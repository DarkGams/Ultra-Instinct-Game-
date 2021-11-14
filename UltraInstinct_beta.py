# coding: utf-8

import random

print("""  
		  _    _  _  _                 _____              _    _               _    
 		 | |  | || || |               |_   _|            | |  (_)             | |   
		 | |  | || || |_  _ __  __ _    | |   _ __   ___ | |_  _  _ __    ___ | |_  
		 | |  | || || __|| '__|/ _` |   | |  | '_ \ / __|| __|| || '_ \  / __|| __| 
		 | |__| || || |_ | |  | (_| |  _| |_ | | | |\__ \| |_ | || | | || (__ | |_  
		  \____/ |_| \__||_|   \__,_| |_____||_| |_||___/ \__||_||_| |_| \___| \__|                                                              
                                                                              BETA By Gam's""")

															 
print("========================================================================================================================")
print("Bienvenue dans la version Beta du jeux Ultra Instinct de Gam's \n Cette version n'est pas complete mais vous permet de patienter la sortie du vrai jeux qui sera plus esthetique et plus complet avec plusieurs niveaux \n Vous disposez de 5 essais pour trouver un nombre tiré aléatoirement entre 1 et 10")

trial = 1
nb_trial = 5
nb_al = random.randint(1, 10)
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
