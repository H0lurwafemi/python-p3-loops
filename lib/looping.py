#!/usr/bin/env python3

def happy_new_year():
    # Initialize a variable 'count' with the value 10
    count = 10    
    # Start a while loop with the condition that 'count' is greater than or equal to 1
    while count >= 1:
        # Print the current value of 'count'
        print(count)
        
        # Decrement 'count' by 1 in each iteration
        count = count - 1
    
    # After the loop, print "Happy New Year!"
    print("Happy New Year!")

# Call the function to execute it
happy_new_year()
pass

def square_integers(numbers):
    # Create an empty list to store squared elements
    squared_list = []
    
    # Start a loop to iterate through each number in the 'numbers' list
    for number in numbers:
        # Square the current number and append it to the 'squared_list'
        squared = number * number
        squared_list.append(squared)
    
    # Return the 'squared_list' containing squared elements
    return squared_list

# Call the function with a list of integers to get squared elements
result = square_integers([1, 2, 3, 4, 5])
print(result)
pass


def fizzbuzz():
    # Start a loop to iterate through numbers from 1 to 100
    for number in range(1, 101):
        # Check if the number is a multiple of both 3 and 5 (FizzBuzz)
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # Check if the number is a multiple of 3 (Fizz)
        elif number % 3 == 0:
            print("Fizz")
        # Check if the number is a multiple of 5 (Buzz)
        elif number % 5 == 0:
            print("Buzz")
        # If none of the above conditions are met, print the number itself
        else:
            print(number)

# Call the function to execute it
fizzbuzz()

pass
