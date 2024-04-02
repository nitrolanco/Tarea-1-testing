import datetime
def greet(name):
    current_hour = datetime.datetime.now().hour
    if 20 <= current_hour < 24 or 0 <= current_hour < 6:
        print(f'¡Buenas noches {name}!')
    elif 6 <= current_hour < 12:
        print(f'¡Buenos días {name}!')
    elif 12 <= current_hour < 20:
        print(f'¡Buenas tardes {name}!')
def main():
    name = input("¡Hola! ¿Cómo te llamas? ")
    greet(name)
    while True:
        user_input = input()
        if user_input.lower() == 'stop!':
            print(f'Adiós {name}!')
            break

    return None

if __name__=="__main__":
    main()