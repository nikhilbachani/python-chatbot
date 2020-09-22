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
print("Your age is " , age, "; that's a good time to start programming!")
