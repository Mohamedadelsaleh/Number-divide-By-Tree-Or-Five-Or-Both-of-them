while True:
    num = input("Enter Your Number : ")
    if num.isnumeric():
        num = int(num)
        break


def divByTreeOrFive(userNum):
    if (userNum % 3 == 0) and (userNum % 5 == 0):
        print("[FizzBuzz]----> Your Number divided by 3 and 5")
    elif userNum % 3 == 0:
        print("[Fizz]-----> Your Number divided by 3 only")
    elif userNum % 5 == 0:
        print("[Buzz]------> Your Number divided by 5 only")
    else:
        print("Your number not divided into 3 or 5")


divByTreeOrFive(num)