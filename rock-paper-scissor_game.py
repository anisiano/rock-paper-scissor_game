import random



me = int(input("please enter the number 1-rock 2-paper 3-scissor:"))
shaps = {1:"rock",2:"paper",3:"scissor"}
if me not in shaps :
    print("enter 1 or 2 or 3")
    exit()
computer = random.randint(1, 3)
print("the shape of me is:", shaps[me])
print("the shape of computer is:", shaps[computer])
if (me == 1) and (computer == 3) or (me == 3) and (computer == 2) or (me == 2) and (computer == 1) :
    print("you are the wiiner")
elif me == computer :
    print("you are the same")
else:
    print("you lost")

