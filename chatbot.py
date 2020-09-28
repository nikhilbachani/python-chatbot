# Stage 1: Hello! What's your name?
print('Hello! My name is Aid.')
print('I was created in 2020.')

# Stage 2: What's my name?
name = input('Please remind me your name: ')
print('What a great name you have,', name + '!')

# Stage 3: How old are you?
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(age) + "; that's a good time to start programming!")

# Stage 4: Let's count!
print("Now I will prove to you that I can count to any number you want.")
number = int(input("Enter a number: "))
start = 0
while start <= number:
	print(start, "!")
	start += 1

# Stage 5: The programming test
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

while int(input("Enter a numeric option: ")) != 2:
	print("Incorrect! Please, try again.")
print("Correct answer!")

print("Bye now, have a nice day!")
