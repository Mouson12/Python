# Lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1]) # * Negative index returns the last item in a list
print(bicycles[-2]) # * Negative index returns the second last item in a list

bicycles[0] = 'ducatti'
print(bicycles)

bicycles.append('trek') # * Append adds an item to the end of a list
print(bicycles)

bicycles.insert(1, 'honda') # * Insert adds an item to a specific index
print(bicycles)

del bicycles[1] # * Del deletes an item from a list
print(bicycles)

popped_bicycle = bicycles.pop() # * Pop removes the last item from a list and returns it
print(bicycles)
print(popped_bicycle)

popped_bicycle = bicycles.pop(1) # * Pop can also remove an item from a specific index
print(popped_bicycle)

bicycles.remove('redline') # * Remove removes an item from a list by value
print(bicycles)

too_expensive = 'specialized'
bicycles.remove(too_expensive)
print(bicycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

bicycles.insert(0, 'trek')
bicycles.insert(2, 'redline')
bicycles.insert(4, 'specialized')
bicycles.append('honda')
bicycles.append('ducatti')
bicycles.append('yamaha')
print(bicycles)

bicycles.sort() # * Sorts a list alphabetically
print(bicycles)

bicycles.sort(reverse=True) # * Sorts a list in reverse alphabetical order
print(bicycles)

print(sorted(bicycles)) # * Temporarily sorts a list alphabetically

bicycles.reverse() # * Reverses the order of a list
print(bicycles)

length_of_a_list = len(bicycles) # * Returns the length of a list
print(length_of_a_list)

# Part 4 : Working with Lists

cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    print(car.title())

# 4.1 : range() function

# Making Numerical Lists

for value in range(1,5):
    print(value)

# Using range() to Make a List of Numbers

list_of_numbers = list(range(1,6))
print(list_of_numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    number = value**2
    squares.append(number)
print(squares)

# 4.2 : Simple Statistics with a List of Numbers

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
print(len(digits))


# 4.3 : List Comprehensions

squares = [value**2 for value in range(1,21)]
print(squares)

# 4.4 : Working with Part of a List

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # * Prints the first three items in a list

players_temp = players[0:3]
print(players_temp)

print(players[:4]) # * If the first index is omitted, it defaults to 0
print(players[2:]) # * If the second index is omitted, it defaults to the end of the list
print(players[-2:]) # * Negative index returns the last two items in a list


print("I'm gonna introduce you to the first three players on my team:")
for player in players[:3]:
    print(player.title())
print("That's my amazing team!")

# 4.5 : Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # * This is how you copy a list
friend_foods = my_foods # * This is how you copy a list by reference (when you change one, you change the other)

# 5 : Tuples

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 350 # * Tuples are immutable, you can't change their values

# 5 : if statements
# 5.1 : A Simple Example

car = 'bmw'
print(car == 'bmw')

motorcycles = ['honda', 'yamaha', 'suzuki']
if 'honda' in motorcycles:
    print('Honda is in the list')
elif 'ducati' in motorcycles:
    print('Ducati is in the list')
else:
    print("We don't have this motorcycle in the list")

# 5.3 
alien_color = 'blue'

if alien_color == 'green':
    print('You just earned 5 points')
elif alien_color == 'yellow':
    print('You just earned 10 points')
elif alien_color == 'red':
    print('You just earned 15 points')

# 5.8 and 5.9 : Hello Admin
usernames = []
if len(usernames) == 0:
        print('We need to find some users!')
for username in usernames :
    if username == 'admin':
        print('Hello admin, would you like to see a staus raport?')
    else:
        print('Hello' + ' ' + username + '. ' + "It's nice to see you again.")

# 5.10 : Checking Usernames
current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
new_users = ['User1', 'user2', 'user5', 'user6', 'user7']

current_users_lower = [user.lower() for user in current_users]
new_users_lower = [user.lower() for user in new_users]

for new_user in new_users_lower:
    if new_user in current_users_lower:
        print('This username is already taken. Please choose another one.')
    else:
        print('This username is available.')

# 5.11 : Ordinal Numbers

numbers = list(range(1,10))

for number in numbers:
    if(number == 1):
        print(str(number) + 'st')
    elif(number == 2):
        print(str(number) + 'nd')
    elif(number == 3):
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')

# 6 : Dictionaries
# 6.1: A Simple Dictionary

person = {'first_name': 'Mateo', 'last_name': 'Koby', 'age': 19, 'city': 'Norymberga'}
print(person['first_name'])
print(person['last_name'])
print(str(person['age']) + ' years old')
print(person['city'])

# 6.2 : favourite numbers

favourite_numbers = {
    'Mateo': 7,
    'Ruby': 5,
    'Max' : 2,
    'Sara' : 6,
    'Marianna' : 3,
}

print('Mateo favourite number is ' + str(favourite_numbers['Mateo']))
print('Ruby favourite number is ' + str(favourite_numbers['Ruby']))
print('Max favourite number is ' + str(favourite_numbers['Max']))
print('Sara favourite number is ' + str(favourite_numbers['Sara']))
print('Marianna favourite number is ' + str(favourite_numbers['Marianna']))

