import itertools

# define the character set to generate passwords from
CHARACTER_SET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+/รทร—'

# define the minimum and maximum password length
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 8

def generate_passwords():
    # loop through all possible password lengths
    for length in range(MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH + 1):
        # generate all possible combinations of characters of the given length
        for password in itertools.product(CHARACTER_SET, repeat=length):
            # convert the combination of characters to a string
            password_string = ''.join(password)
            # yield the password
            yield password_string

# example usage: generate all possible passwords and write them to a file
with open('pass.txt', 'w') as file:
    for password in generate_passwords():
        file.write(password + '\n')
      
