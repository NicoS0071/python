import random

user_wins = 0
computer_wins = 0

options = ["akmuo", "popierius", "žirkles"]

while True: 
    user_input = input("Įrašyk akmuo/popierius/žirkles arba Q išeiti.").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # akmuo: 0, popierius: 1, žirkles: 2
    computer_pick = options[random_number]
    print("Kompiuteris pasirinko", computer_pick + ".")

    if user_input == "akmuo" and computer_pick == "žirkles":
        print("Tu laimėjai!")
        user_wins += 1
        continue

    elif user_input == "akmuo" and computer_pick == "žirkles":
        print("Tu laimėjai!")
        user_wins += 1
        continue

    elif user_input == "akmuo" and computer_pick == "žirkles":
        print("Tu laimėjai!")
        user_wins += 1
        continue
    else:
        print("Tu pralaimėjai!")
        computer_wins += 1 

print("Tu laimėjai!", user_wins, "kartus.")
print("Kompiuteris laimėjo!", computer_wins, "kartus.")
print("Viso gero!")