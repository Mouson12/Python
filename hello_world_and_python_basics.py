print("Hello world!")

#variables
message = "Hello Python World"
print(message)

message = "Hello Python Crash Course reader!" 
print(message)

exercise_message = "Test_1"
print(exercise_message)

exercise_message = "Test_2"
print(exercise_message)

#strings
#Changing Case in a String with Methods
name = "ada lovelace" 
print(name.title())
# * A method is an action that Python can perform on a piece of data. 
# * The dot (.) after name in name.title() tells Python to make the title() method act on the variable name. 

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#Combining or Concatenating Strings

first_name = "Ada"
last_name = "Lovelace"
# * This method of combining strings is called concatenation
full_name = first_name + " " + last_name
print(full_name)
message = "Hello, " + full_name.title() + "!"
print(message)


#Adding Whitespace to Strings with Tabs or Newlines
print("Python")
print("\tPython") # \t is a tab
print("Languages:\nPython\nC\nJavaScript") # \n is a newline character
print("Languages:\n\tPython\n\tC\n\tJavaScript") # \n\t is a newline character with a tab


#Stripping Whitespace
language = "python "
print(language)
language.rstrip() # rstrip() method removes whitespace from the right side of a string
print(language) # the whitespace is still there
language = language.rstrip() # to remove the whitespace permanently, you have to associate the stripped value with the variable name
print(language)
# You can also strip whitespace from the left side of a string using the lstrip() method or strip whitespace from both sides at once using strip() method


# Numbers

# Integers
# you can add (+), subtract (-), multiply (*), and divide (/) integers in Python.
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
# Python uses two multiplication symbols to represent exponents
print(3 ** 2)
# Python supports order of operations
print(3 * 4 + 3 * 4)
print(3 ** 2 * 3)
# For better visability please use pparenthesis

# Floats
print(0.2 + 0.1) # * Some example of python rounding errors (we will learn how to deal with them later)

# Avoiding Type Errors with the str() Function
age = 11
message = "My Ipad is almost" + ' ' + str(age) + ' ' + "years old."
print(message)