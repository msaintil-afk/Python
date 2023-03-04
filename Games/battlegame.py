
#classes
Wizard = "Wizard"
Elf = "Elf"
Human = "Human"

#health points
wizard_hp = "70"
elf_hp = "100"
human_hp = "150"
dragon_hp = "300"

#damage points
wizard_dp = "150"
elf_dp = "100"
humana_dp = "20"
dragon_dp = "50"

#Start the Game using while Loop
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    #user input to choose class 
    choose_class = input("Choose your character:")
    #print("You choose:", choose_class)



    if choose_class.lower() == Wizard.lower() or choose_class == "1":
        print("you've been assinged the wizard class")
        character = Wizard
        my_hp = int(wizard_hp)
        my_damage = int(wizard_dp)
        dragon_battle_hp = int(dragon_hp)
        dragon_battle_dp = int(dragon_dp)
        print("Health:" + wizard_hp)
        print("Damage:" + wizard_dp)
        
        dragon_battle_hp = dragon_battle_hp - my_damage
        print("The " + character + " damaged the Dragon!")
        print("The dragon's hitpoints are now:" + str(dragon_battle_hp))
        
        my_hp = my_hp - dragon_battle_dp
        print("The Dragon Strikes back at the" +  character)
        print("The " + character + " hitpoints are now:" + str(my_hp))

        dragon_battle_hp = dragon_battle_hp - my_damage
        print("The " + character + " damaged the Dragon!")
        print("The dragon's hitpoints are now:" + str(dragon_battle_hp))

        if dragon_battle_hp == 0:
            print("The dragon has lost the battle")
            print("Victory goes to the Wizard")
            play_again = input("Would you like to play again. Yes or No?")
            if play_again.lower() == "yes":
                continue
            elif play_again.lower() == "no":
                print("Thanks for playing")
                print("Enjoy the rest of your day!")
            elif play_again.lower() != "yes" or "no":
                print("invalid section")
                print("Goodbye")
                break
        else:
            print("Error in code")
        
        break
    elif choose_class.lower() == Elf.lower() or choose_class == "2":
        print("You've been assigned the elf class")
        character = Elf
        my_hp = int(elf_hp)
        my_damage = int(elf_dp)
        dragon_battle_hp = int(dragon_hp)
        dragon_battle_dp = int(dragon_dp)
        print("Health:" + elf_hp)
        print("Damage:" + elf_dp)

        dragon_battle_hp = dragon_battle_hp - my_damage
        print("The " + character + " damaged the Dragon!")
        print("The dragon's hitpoints are now:" + str(dragon_battle_hp))
        
        my_hp = my_hp - dragon_battle_dp
        print("The Dragon Strikes back at the " +  character)
        print("The " + character + " hitpoints are now:" + str(my_hp))

        dragon_battle_hp = dragon_battle_hp - my_damage
        print("The " + character + " damaged the Dragon!")
        print("The dragon's hitpoints are now:" + str(dragon_battle_hp))

        my_hp = my_hp - dragon_battle_dp
        print("The Dragon Strikes back at the " +  character)
        print("The " + character + " hitpoints are now:" + str(my_hp))

        if my_hp == 0:
            print("The " + character + " has lost the battle" )
            play_again = input("Would you like to play again. Yes or No?")
            if play_again.lower() == "yes":
                continue
            elif play_again.lower() == "no":
                print("Thanks for playing")
                print("Enjoy the rest of your day!")
            elif play_again.lower() != "yes" or "no":
                print("invalid section")
                print("Goodbye")
                break
        else:
            print("Error in code")

        break
    elif choose_class.lower() == Human.lower() or choose_class == "3":
        print("you've been assisgned the human class")
        character = Human
        my_hp = int(human_hp)
        my_damage = int(humana_dp)
        dragon_battle_hp = int(dragon_hp)
        dragon_battle_dp = int(dragon_dp)
        print("Health:" + human_hp)
        print("Damage:" + humana_dp)

        dragon_battle_hp = dragon_battle_hp - my_damage
        print("The " + character + " damaged the Dragon!")
        print("The dragon's hitpoints are now:" + str(dragon_battle_hp))
        
        my_hp = my_hp - dragon_battle_dp
        print("The Dragon Strikes back at the " +  character)
        print("The " + character + " hitpoints are now:" + str(my_hp))

        dragon_battle_hp = dragon_battle_hp - my_damage
        print("The " + character + " damaged the Dragon!")
        print("The dragon's hitpoints are now:" + str(dragon_battle_hp))

        my_hp = my_hp - dragon_battle_dp
        print("The Dragon Strikes back at the " +  character)
        print("The " + character + " hitpoints are now:" + str(my_hp))

        dragon_battle_hp = dragon_battle_hp - my_damage
        print("The " + character + " damaged the Dragon!")
        print("The dragon's hitpoints are now:" + str(dragon_battle_hp))

        my_hp = my_hp - dragon_battle_dp
        print("The Dragon Strikes back at the " +  character)
        print("The " + character + " hitpoints are now:" + str(my_hp))

        if my_hp == 0:
            print("The " + character + " has lost the battle" )
            play_again = input("Would you like to play again. Yes or No?")
            if play_again.lower() == "yes":
                continue
            elif play_again.lower() == "no":
                print("Thanks for playing")
                print("Enjoy the rest of your day!")
            elif play_again.lower() != "yes" or "no":
                print("invalid section")
                print("Goodbye")
                break
        else:
            print("Error in code")

        break
    elif choose_class.lower() != Human.lower() or Elf.lower() or Wizard.lower():
        print("Unknown Character")
        print("Please made a valid section")
        continue
    

