
#David Cardona
#October 8, 2024
#Lab 3


#1: This prints “Hello World” to the screen
def problem_1():
    print("Hello World")

#2: This asks the user for their name and greets them with their name
def problem_2():
    name = input("What is your name? ")
    print(f"Hello, {name}!")

#3: previous program BUT only the users you and your instructor are greeted with their names
def problem_3():
    name = input("What is your name? ")
    if name == "David" or name == "Linh":
        print(f"Hello, {name}!")
    else:
        print("Boy, I have no idea who you are.")

#4: This computes the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.
def problem_4():
    import math
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle with radius {radius} is {area:.2f}")

#5: This computes MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used.
def problem_5():
    miles = float(input("Enter the number of miles driven: "))
    gallons = float(input("Enter the number of gallons used: "))
    mpg = miles / gallons
    print(f"The car's MPG (miles per gallon) is {mpg:.2f}")

#6: This converts degrees Fahrenheit to degrees Celsius.
def problem_6():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius")

#7: This is a general program to find return day after a holiday.
def problem_7():
    starting_day = int(input("Enter the starting day number (0 for Sunday, 6 for Saturday): "))
    length_of_stay = int(input("Enter the number of nights you stayed: "))
    return_day = (starting_day + length_of_stay) % 7
    print(f"You will return on day number {return_day}.")

# Main program to select which problem to test
def main():
    while True:
        print("\nWhich problem would you like to try buddy boy?")
        print("1 - Print 'Hello World'")
        print("2 - Greet the user")
        print("3 - Greet specific users")
        print("4 - Compute the area of a circle")
        print("5 - Compute MPG")
        print("6 - Convert Fahrenheit to Celsius")
        print("7 - Find return day after a holiday")
        print("0 - Exit")

        choice = input(" Thanks for cheking (0 to exit): ")

        if choice == "1":
            problem_1()
        elif choice == "2":
            problem_2()
        elif choice == "3":
            problem_3()
        elif choice == "4":
            problem_4()
        elif choice == "5":
            problem_5()
        elif choice == "6":
            problem_6()
        elif choice == "7":
            problem_7()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Boy, please try again.")

# Run the main program
main()