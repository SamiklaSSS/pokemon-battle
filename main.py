print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

def sort_total(pokemons):
     return(pokemons['total'])
     pass



while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons (by total)")
    print("3. Top 10 weakest pokemons (by total)")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        s = input("Write an index of pokemon, that you want to get!")
        S = int(s) - int(1)
        print(pokemons[S])
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        pass



    elif choice == '2':
        pokemons.sort(key = sort_total)
        pokemons.sort["total"]
        print(pokemons["total"][:11])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass



    elif choice == '3':
        pokemons.sort(key = sort_total)
        pokemons.sort["total"]
        print(pokemons["total"][-10:])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass



    elif choice == '4':
        print("Battle!")
        Min = int(input("Pick your Pokemon!(Write index of Pokemon)"))
        print("You choose:") 
        print(pokemons[Min])
        Opp = int(random.randint(1, 43))
        print("Your opponent has chooses:") 
        print((pokemons[Opp]))

        print("Your hp:")
        print(pokemons[Min]["hp"])
        print("Your opponent's hp:")
        print(pokemons[Opp]["hp"])
        
        print("Your damage:")
        print(pokemons[Min]["damage"])
        print("Your opponent's damage:")
        print(pokemons[Opp]["damage"])

        R = random.randint(5, 20)

        

        while( (pokemons[Opp]["hp"])>0 ) or (pokemons[Min]["hp"]>0 ):
            print("Your turn!")
            (BattleP):
            def BattleP:
                (pokemons[Opp]["hp"]) = (pokemons[Opp]["hp"]) - (int(pokemons[Min]["damage"]) + int(R)) 
                return(pokemons[Opp]["hp"])
            pass

            print("Your opponent's turn!")
            (BattleO):
            def BattleO:
                (pokemons[Min]["hp"]) = (pokemons[Min]["hp"]) - (int(pokemons[Opp]["damage"]) + int(R)) 
                return(pokemons[Min]["hp"])
            pass
        # 
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health (total) - lost
        pass



    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")
