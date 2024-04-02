import datetime
def greet(name):
    current_hour = datetime.datetime.now().hour
    if 20 <= current_hour < 24 or 0 <= current_hour < 6:
        print(f'¡Buenas noches {name}!')
    elif 6 <= current_hour < 12:
        print(f'¡Buenos días {name}!')
    elif 12 <= current_hour < 20:
        print(f'¡Buenas tardes {name}!')

def reverse_echo(input_str):
    return input_str[::-1]
def is_palindrome(input_str):
    return input_str.lower() == input_str.lower()[::-1]

def main():
    name = input("¡Hola! ¿Cómo te llamas? ")
    greet(name)
    while True:
        user_input = input()
        if user_input.lower() == 'stop!':
            print(f'Adiós {name}!')
            break
        elif is_palindrome(user_input):
            print(reverse_echo(user_input))
            print('¡Bonita palabra!')
        else:
            print(reverse_echo(user_input))

    return None

if __name__=="__main__":
    main()