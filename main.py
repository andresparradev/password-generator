import random


def generate_character():
    number_random = random.randint(33, 126)
    return chr(number_random)


def generate_password(password_size):
    characters_random = []
    counter = 0
    while counter < password_size:
        character_random = generate_character()
        characters_random.append(character_random)
        counter += 1
    return ''.join(characters_random)


def run():
    password_size = int(input('Input the password size: '))
    password_generated = generate_password(password_size)
    print(f'Your password is: {password_generated}')


if __name__ == '__main__':
    run()
