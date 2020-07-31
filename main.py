import random
a = input("Enter your first activity:  ")
b = input("Enter your second activity:  ")
c = input("Enter your third activity:  ")
d = input("Enter your fourth activity:  ")

activities = [a,b,c,d]
print("The random activity you are going to do now is ", random.choice(activities))