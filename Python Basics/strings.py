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


#String indexes
#acessar diferentes locais em uma string

selfish = 'me me me'
         # 01234567
print(selfish[7]) 

# [start:stop]
numbers = '0123456789'
print(numbers[3:7]) #onde começa e onde termina

# [start:stop:stepover]
algumacoisa = '0123456789' 
print(algumacoisa[1:7:2]) # seleciona números entre 1 e 7 a cada 2 números
print(algumacoisa[-5]) #quinto de  traz pra frente
print(algumacoisa[::-2]) #salta 2 numeros de traz pra frente

print(len('helloooooo')) #comprimento da string

