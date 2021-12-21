import random
from colorama import  *

init()

print(Fore.BLUE + """   __                                    
  / /    ___   _   _  _ __   _   _ __  __
 / /    / _ \ | | | || '_ \ | | | |\ \/ /
/ /___ | (_) || |_| || | | || |_| | >  < 
\____/  \___/  \__,_||_| |_| \__,_|/_/\_\\
                                           """)

print(Fore.GREEN + "Bienvenue sur Lounux , le jeu du Juste Prix !\nVous avez dix essais pour devinner un chiffre entre 0 à 100")

trial = 0
nb_trials = 10

number = random.randint(0, 100)
choice = int(input("Trouvez le juste prix : "))

while True:
	if trial == nb_trials:
		print("Nombres d'essais dépassés")
		input("Apppuyez sur ENTRER pour quitter")
		break

	else:
		if choice == number:
			print("Félicitation , vous avez trouvé le juste prix !")
			print("Nombres d'essais : ", trial)
			input("Appuyez sur ENTRER pour quitter")
			break

		else:
			trial +=1
			if choice < number:
				print("C'est plus !")
				choice = int(input("Réessayez : "))

			else:
				print("C'est moins !")
				choice = int(input("Réessayez : "))
