# Student name
# Current date
# String Concatenation

# Part 1
# Use concatenation to build and display a string that displays which city and state you live in
city = ('Rapid City')
state = ('Michigan')
place = city+ (',') + " " + state
print(f'I live in {place}')



# Part 2
# Create a custom message that welcomes the user by first name to a game you created
# Create one variable to store the user's first name
# Create another variable that stores the welcome message
# Use concatenation to create the customized message
person_name = ('persons name')
message = ('Welcome to the game I created,')
print(message + " " + person_name)



# Part 3
# Assign a number to your age variable
# Use the built-in Python str( ) function to convert your age to a string (when doing concatenation)
# Use concatenation to display a sentence that tells us your first name and age
age = (17)
first_name = ('Alex')
full_message = 'Hi, my name is' + " " + first_name + " " + 'and I am' + " " + str(age) + " " + 'years old'
print(full_message)





# Part 4
# Use an f-string to build and display a string that contains your first name, last name, and your height in inches
first_nam = 'Alexander'
last_nam = 'Williams'
height = (6)
full_name = first_nam + " " + last_nam
print(f'My name is {full_name} and I am a little over {str(height)} feet tall')

