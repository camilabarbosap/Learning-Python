#Creating a password

# input('jayjay')
# input('secret')

# print('{username}, your password {****** } is {6} letters long')

# print('*' * 10)

#example
username = input('What is your username? ')
password = input('What is your password? ')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password, {hidden_password}, is {password_length} letters long')