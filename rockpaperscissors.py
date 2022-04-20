import time
import random

def rockPaperScissors():
    computerScore = 0
    score = 0
    
    inputList = ["Akmuo", "Popierius", "Žirklės"]
    goAgain = int(input("Spausk 1 kad žaisti, 2 kad išeitum"))
    while goAgain!= 1 and goAgain !=2:
        print("Numeris netinka")
        goAgain = int(input("Spausk 1 žaisti, 2 kad išeiti"))

    while goAgain == 1:
        print("Pasirink Akmuo, Popierius arba žirklės naudodamas 1, 2 ir 3...")
        choice = int(input("1. Akmuo \n2. Popierius \n3. Žirklės \n"))
        while choice != 1 and choice != 2 and choice != 3:
            print("Numeris netinka")
            print("Pasirink Akmuo, Popierius arba žirklės naudodamas 1, 2 ir 3...")
            choice = int(input("1. Akmuo \n2. Popierius \n3. Žirklės \n"))


        computerChoice = random.randint(1,3)

        print("Ready.....")
        time.sleep(0.2)
        print("Set.....")
        time.sleep(0.2)
        print("GO!!!")
        time.sleep(0.2)

        print("Tu renkiesi:", inputList[choice-1])

        print("Kompiuteris renkasi:", inputList[computerChoice-1])


        if computerChoice == choice:
            print("Lygiosios!")

        else:
            #Akmuo
            if computerChoice == 1 and choice == 3:
                print("Kompiuteris laimėjo!")
                computerScore = computerScore + 1

            elif computerChoice == 3 and choice == 1:
                print("Tu laimėjai!")
                score = score + 1

            #Popierius
            elif computerChoice == 2 and choice == 1:
                print("Kompiuteris laimėjo!")
                computerScore = computerScore + 1

            elif computerChoice == 1 and choice == 2:
                print("Tu laimėjai!")
                score = score + 1

            #Žirklės
            elif computerChoice == 3 and choice == 2:
                print("Kompiuteris laimėjo!")
                computerScore = computerScore + 1

            elif computerChoice == 2 and choice == 3:
                print("Tu laimėjai!")
                score = score + 1

            else:
                print("Error404")
                
        print("")
        print("Dabartinis rezultatas:")
        print("Kompiuteris:", computerScore)
        print("Vartotojas:", score)
        print("")

        goAgain = int(input("Spausk 1 žaisti dar kartą, arba 2 kad išeiti\n"))

        while goAgain !=1 and goAgain != 2:
            print("Netinka numeris")
            goAgain = int(input("Spausk 1, kad žaisti dar kartą, arba 2 kad išeiti\n"))
                      

rockPaperScissors()