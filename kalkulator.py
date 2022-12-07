import logging
logging.basicConfig(filename='kalkulator.log', encoding='utf-8',level=logging.DEBUG)
def add (x,y):
    logging.info(f'dodawanie {x},{y}')
    return x+y
def subtract (x,y):
    logging.info(f'odejmowanie {y},{x}')    
    return x-y
def multiply (x,y):
    logging.info(f'mnożenie {x},{y}')    
    return x*y
def divide (x,y):
    logging.info(f'dzielenie {x},{y}')    
    return x/y
def sprawdz_czy_liczba (x):
    if isinstance (x,float):
        return True
    else:
        return False
def wprowadz_liczbe(kolejna):
    num1=None
    while True:
        try:
            num1=float(input(f"Podaj {kolejna} liczbę :"))
        except:
            logging.warning('Wprowadzono nie liczbę')
            print("Nie podałeś liczby")
        if sprawdz_czy_liczba(num1): 
            return num1

print("Podaj działanie posługując się odpowiednią liczbą: 1.Dodawanie , 2.Odejmowanie , 3.Mnożenie , 4.Dzielenie , Z.Zakończ")
while True:
    choice=input("Które działanie chcesz wykonać? Wybierz (1/2/3/4/Z) :")
    if choice=='1':
        num1=wprowadz_liczbe('pierwszą')
        num2=wprowadz_liczbe('drugą')
        print("Dodaję ",num1,"i",num2)
        print("Wynik działania to: ", add(num1,num2))
    elif choice=='2':
        num1=wprowadz_liczbe('pierwszą')
        num2=wprowadz_liczbe('drugą')
        print("Odejmuję ",num2,"od",num1)
        print("Wynik działania to: ", subtract(num1,num2))
    elif choice=='3':
        num1=wprowadz_liczbe('pierwszą')
        num2=wprowadz_liczbe('drugą')
        print("Mnożę ",num1,"przez",num2)
        print("Wynik działania to: ",multiply(num1,num2))
    elif choice=='4':
        num1=wprowadz_liczbe('pierwszą')
        num2=wprowadz_liczbe('drugą')
        print("Dzielę ",num1,"przez",num2)
        print("Wynik działania to: ", divide(num1,num2))
    elif choice=='Z':
        logging.info('Zakończenie kalkulatora')
        break
    else:
        pass
        print("Wybrałeś działanie z poza listy")
        logging.warning(f'Nieprawidłowy wybór {choice}')
