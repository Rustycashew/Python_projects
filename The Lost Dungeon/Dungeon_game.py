import random
import time

def slow_print(text):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(0.04)
    print()


def read_diary():
    slow_print("You read the diary")
    slow_print("The Diary was actually the journal of the witch\nIt explains how the witch came to this dungeon for the 'Jade Of Heaven'!\nThis medicine was created by sacrificing millions of souls and contains their life essence!!\n")
    input("\nPress Enter to Continue...")
    slow_print("This medicine was said to be hidden in this dungeon by the master which made it!")
    slow_print("According to the journal, The Room which contains the Jade has been locked\nand its key has been broken in two!\n")
    input("\nPress Enter to Continue...")
    slow_print("You decide to find the two keys!!")
    input("\nPress Enter to Continue...")


inventory = []
player_hp = 100
potions = 1


def show_inventory():
    slow_print("===== YOUR INVENTORY =====")

    if not inventory:
        slow_print("Your inventory is empty")
    else:
        for item in inventory:
            print("- " + item)

    print(f"Healing Potions: {potions}")


def secret_room():
    slow_print("You step in the empty, desolate room...")
    input("\nPress Enter to Continue...")
    slow_print("Upon inspecting the room you found\nA stone which looks unsettling")
    input("\nPress Enter to Continue...")
    slow_print("You pressed it!!!")
    input("\nPress Enter to Continue...")
    slow_print("YOU FOUND THE MOON KEY!!!!\n(Half of the original key...)")
    input("\nPress Enter to Continue...")
    inventory.append("Moon Key")


def undead_knight():
    global potions

    player_hp = 100
    knight_hp = 150

    slow_print("\n===== UNDEAD KNIGHT =====")
    slow_print("An Undead Knight appears before the throne\nGuarding the throne of the king long dead!!!")
    input("\nPress Enter to Continue...")
    slow_print("He unsheathes his sword...and points it at you..!!!")
    input("\nPress Enter to Continue...")

    while player_hp > 0 and knight_hp > 0:
        print("\nYour HP: ", player_hp)
        print("\nKnight's HP: ", knight_hp)

        print("1. Attack")
        print("2. Heal")
        print("3. Use Healing Potion")
        print("4. Check Inventory")
        print("5. Run")

        act = input("Choose your action: ").strip()

        if act == "1":
            damage = random.randint(15, 30)

            if random.randint(1, 5) == 1:
                damage *= 2
                slow_print("CRITICAL HIT!")

            knight_hp -= damage
            knight_hp = max(knight_hp, 0)

            slow_print(f"You strike the knight and deal {damage} damage!")

            if knight_hp <= 0:
                break

        elif act == "2":
            if player_hp < 100:
                player_hp = min(player_hp + 20, 100)
                slow_print(f"You healed yourself! Your HP is now {player_hp}")
            else:
                slow_print("\nYour HP is already full")

            input("\nPress Enter to Continue...")

        elif act == "3":
            if potions > 0:
                if player_hp < 100:
                    player_hp = min(player_hp + 40, 100)
                    potions -= 1
                    slow_print(f"You used a Healing Potion! Your HP is now {player_hp}.")
                else:
                    slow_print("Your HP is already full. Save the potion!")
                    continue
            else:
                slow_print("You have no Healing Potions left!")
                continue

        elif act == "4":
            show_inventory()
            continue

        elif act == "5":
            slow_print("You try to escape!")
            slow_print("The knight blocks your path and strikes you down!")
            player_hp = 0
            break

        else:
            slow_print("Invalid choice! Enter a number from 1 to 5.")
            continue

        if knight_hp > 0:
            slow_print("\nThe undead knight swings his heavy sword!!!")
            player_hp -= 15
            player_hp = max(player_hp, 0)
            slow_print(f"Your remaining HP: {player_hp}")

    if player_hp <= 0:
        slow_print("\nYou have been slain by the Undead Knight...")
        slow_print("May your soul find peace.")
        slow_print("GAME OVER!")
        return False

    if knight_hp <= 0:
        slow_print("\nYour sword pierces the Undead Knight's chest!")
        slow_print("He turns his head towards the throne...")
        slow_print(
            "His loyalty to his long-dead king remains unbroken "
            "even as he falls."
        )
        slow_print("YOU HAVE DEFEATED THE UNDEAD KNIGHT!")
        return True

    return False


print("====== THE LOST DUNGEON ======")
slow_print("You wake up inside a mysterious dungeon")
slow_print("There are two paths in front of you")
print("1. Go Left")
print("2. Go Right")

choice = input("Which way you want to go: ").strip()

if choice == "1":
    slow_print("You chose the left path!!")
    input("\nPress Enter to Continue...")
    slow_print("You Discovered a room filled with weird concoctions and potions\n")
    slow_print("Probably belongs to the witch!? - who cares")
    input("\nPress Enter to Continue...")
    slow_print("Before you is a cabinet of some sort which might contain something interesting!(somewhat suspicious)")
    input("\nPress Enter to Continue...")

    print("1. Search the Cabinet")
    print("2. Leave it")

    second_choice = input("What would you do: ").strip()

    if second_choice == "1":
        slow_print("You search every drawer of the potion cabinet\n")
        slow_print("You find a diary!!")
        input("\nPress Enter to Continue...")
        read_diary()

        slow_print("You proceed further into the dungeon...")
        input("\nPress Enter to Continue...")
        slow_print("As you were proceeding through the dungeon\nyou found a small room!?")
        slow_print("It looks very small and is literally empty!")
        input("\nPress Enter to Continue...")

        print("1. Investigate the room...")
        print("2. Leave it...")

        r_choice = input("What would you do: ").strip()

        if r_choice == "1":
            secret_room()
            slow_print("You proceed through the dungeon...")
            input("\nPress Enter to Continue...")
            slow_print("You come across what seems like was once a lavish throne room of a king...")
            input("\nPress Enter to Continue...")
            slow_print("SUDDENLY!!, YOU FEEL THE GROUND SHAKING")
            input("\nPress Enter to Continue...")
            slow_print("FROM THEM EMERGED AN UNDEAD KNIGHT!!!!!!!")

            print("1. Fight the Undead Knight!")
            print("2. Escape!")

            fourth_choice = input("What would you do: ").strip()

            if fourth_choice == "1":
                if undead_knight():
                    slow_print("You find a crown placed on the throne...")
                    input("\nPress Enter to Continue...")

                    print("1. Inspect the Crown")
                    print("2. Leave the Crown")

                    c_choice = input("What would you do: ").strip()

                    if c_choice == "1":
                        slow_print("You inspect the crown...")
                        input("\nPress Enter to Continue...")
                        slow_print("YOU FIND THE SUN KEY!!!!")
                        inventory.append("Sun Key")

                    elif c_choice == "2":
                        slow_print("You did not touch the crown")
                        input("\nPress Enter to Continue...")

                    else:
                        slow_print("You leave the crown alone.")

                    slow_print("You proceed through the dungeon...")
                    input("\nPress Enter to Continue...")
                    slow_print("At last...\nYou come across the gates of the treasure...")
                    input("\nPress Enter to Continue...")
                    slow_print("It has two key places...")
                    input("\nPress Enter to Continue...")

                    if "Moon Key" in inventory and "Sun Key" in inventory:
                        slow_print("You use both the keys to unlock the door...!")
                        input("\nPress Enter to Continue...")
                        slow_print("Now Finally after all the struggle\nYou got your hands on the Heavenly Jade..")
                        input("\nPress Enter to Continue...")
                        slow_print("YOU WINNN!!!!!!")
                    else:
                        slow_print("The door is locked. It needs two keys....")

            elif fourth_choice == "2":
                slow_print("You try to escape the undead...")
                input("\nPress Enter to Continue...")
                slow_print("The undead knight rips your head off your body...")
                input("\nPress Enter to Continue...")
                slow_print("You died!!!")
                print("GAME OVER!!!")

            else:
                slow_print("Invalid choice!")

        elif r_choice == "2":
            slow_print("You ignored the room....")
            input("\nPress Enter to Continue...")

        else:
            slow_print("Invalid choice!")

    elif second_choice == "2":
        slow_print("You leave the cabinet as it is\n")
        slow_print("YOU FEEL A DAGGER PIERCING YOUR CHEST FROM BEHIND\n")
        slow_print("Your vision gets blurry\n")
        slow_print("You die!!!\n")
        slow_print("Game Over!!!")

    else:
        slow_print("Invalid choice!")

elif choice == "2":
    slow_print("You chose the right path!!")
    input("\nPress Enter to Continue...")
    slow_print("It's a dark and large cave")
    input("\nPress Enter to Continue...")
    slow_print("The cave is filled with complete darkness with not a single hint of light")
    slow_print("You stare into the abyss")
    slow_print("You feel like someone is watching you from within the dark....")
    input("\nPress Enter to Continue...")

    print("1. Will you go further and investigate!")
    print("2. Leave it and choose the left path")

    third_choice = input("What would you do: ").strip()

    if third_choice == "1":
        slow_print("You chose to investigate the cave!")
        input("\nPress Enter to Continue...")
        slow_print("As you walk further and further inside\n")
        slow_print("You become unable to trace your path\n")
        slow_print("You lost track of time\n")
        slow_print("You are forever lost in the dark!!!")
        print("Game Over!!!")

    elif third_choice == "2":
        slow_print("You chose to go for the left path instead!!!")
        slow_print("As you turn back you see the path has been blocked by big boulders!")
        slow_print("You hear an echo in your mind, an unfamiliar voice...")
        slow_print("The Choice was in your hand not the consequence..!")
        slow_print("You are forever stuck in the dark")
        print("Game Over!!!")

    else:
        slow_print("Invalid choice!")

else:
    print("Invalid choice! Please enter 1 or 2.")

print()