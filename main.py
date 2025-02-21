name = input("What is your name?")
age = int(input("What is your age?"))
height = int(input("What is your height (in inches)?"))

print(f"Hi {name}! Here are the rides you can enjoy:")

# Kids Rides (All ages)
if age >= 0 and height >= 0:
    print("Kids Rides:")
    print("- Carousel")
    print("- Mini Train")
    print("- Tea Cups")

# Family Rides (Age 8+ AND height >= 48 inches)
if age >= 8 and height >= 48:
    print("Family Rides:")
    print("- Ferris Wheel")
    print("- Log Flume")
    print("- Bumper Cars")

# Thrill Rides (Age 13+ AND height >= 60 inches)
if age >= 13 and height >= 60:
    print("Thrill Rides:")
    print("- Roller Coaster")
    print("- Drop Tower")
    print("- Loop Coaster")