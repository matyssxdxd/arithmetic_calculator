import random


def task(level):
    operators = ["+", "-", "*"]
    if level == "1":
        user_task = str(random.randint(2, 9)) + " " + random.choice(operators) + " " + str(random.randint(2, 9))
        return user_task, eval(user_task)
    elif level == "2":
        user_task = random.randint(11, 29)
        return user_task, user_task ** 2


print("Which level do you want? Enter a number:\n"
      "1 - simple operations with numbers 2-9\n"
      "2 - integral squares of 11-29")

correct = 0
levels = ["1 - simple operations with numbers 2-9", "2 - integral squares of 11-29"]
level_choice = input()
if level_choice not in ["1", "2"]:
    print("Incorrect format.")
else:
    for _ in range(5):
        given_task, answer = task(level_choice)
        print(given_task)
        while True:
            try:
                user_input = int(input())
                if user_input == answer:
                    print("Right!")
                    correct += 1
                    break
                else:
                    print("Wrong!")
                    break
            except ValueError:
                print("Wrong format! Try again.")
                continue
print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")
user_input = input()
if user_input in ["yes", "YES", "y", "Yes"]:
    print("What is your name?")
    user_input = input()
    with open("results.txt", "a") as file:
        file.write(f"{user_input}: {correct}/5 in level {level_choice} ({levels[int(level_choice)-1]})")
        file.close()
    print("The results are saved in \"results.txt\"")
