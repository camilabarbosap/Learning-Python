#Strings

'hi hello there'
"hi hello there"
print(type('hello'))


username = 'supercoder'
password = 'supersecret'

long_string = '''
WOW
O O
___
''' 

print(long_string)

first_name = 'Camila '
last_name = 'Barbosa'
full_name = first_name + last_name
print(full_name)


#Escape sequence
weather = "it\'s \"kind of\" sunny "
print(weather) #situação com vários '' ou ""

weather1 = "\t it\'s \"kind of\" sunny  \n hope you have a good day"
print(weather1) #\n pula uma linha e o \t é o tab

#Formatted strings

name = 'John'
age = 55

print('hi ' + name + ', you are ' + str(age) + ' years old')

#same as

print(f'hi {name}. you are {age} years old')

#or

print('hi {}. you are {} years old'.format('John', '55'))

#or

print('hi {}. you are {} years old'.format(name, age))

#changing information

print('hi {new_name}. you are {new_age} years old'.format(new_name = 'Camila', new_age ='26'))