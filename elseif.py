a = int(input("Enter your age: "))
if(a >= 23):
    print("You are above the age of consent")
    print("You are good")

elif(a < 0):
    print("You are entering an invalid negative age")

elif(a == 0):
    print("You are entering 0 which is invalid")

else:
    print("You are below the age of consent")

print("End the program")