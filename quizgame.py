import random

print("Welcome to the Math Quiz!")

play = input("Do you want to play?(yes/no) ")

if play != "yes":
    quit()
print("Let's Begin!")

signs = ["+", "-", "x", "÷"]
score = 0

while True:
    v1 = random.randint(1,50)
    v2 = random.randint(1,50)
    v3 = random.choice(signs)

    corr_ans = 0

    if v3 == "+" :
        corr_ans = v1+v2
    elif v3 == "-":
        corr_ans = v1-v2
    elif v3 == "x":
        corr_ans = v1*v2
    elif v3 == "÷":
        while v1 % v2 != 0:
            v1 = random.randint(1, 50)
            v2 = random.randint(1, 50)
        corr_ans= v1//v2


    ans = input(str(v1)+ " " + v3 + " " + str(v2)+" ")

    if float(ans) == corr_ans:
        score+=1
        print("That is correct :)")
        print("Score: " + str(score))
    else:
        print("That is incorrect :(")
        print("The correct answer was: " + str(corr_ans))
        print("Game Over! Your final score is: "+ str(score))
        break