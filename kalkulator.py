def add (x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y
print("Podaj działanie posługując się odpowiednią liczbą: 1.Dodawanie , 2.Odejmowanie , 3.Mnożenie , 4.Dzielenie")
choice=input("Które działanie chcesz wykonać? Wybierz (1/2/3/4) :")
#num1=float(input("Podaj pierwszą liczbę :"))
#num2=float(input("Podaj drugą liczbę :"))
if choice=='1':
    num1=float(input("Podaj pierwszą liczbę :"))
    num2=float(input("Podaj drugą liczbę :"))
    print("Dodaję ",num1,"i",num2)
    print("Wynik działania to: ", add(num1,num2))
elif choice=='2':
    num1=float(input("Podaj pierwszą liczbę :"))
    num2=float(input("Podaj drugą liczbę :"))
    print("Odejmuję ",num2,"od",num1)
    print("Wynik działania to: ", subtract(num1,num2))
elif choice=='3':
    num1=float(input("Podaj pierwszą liczbę :"))
    num2=float(input("Podaj drugą liczbę :"))
    print("Mnożę ",num1,"przez",num2)
    print("Wynik działania to: ",multiply(num1,num2))
elif choice=='4':
    num1=float(input("Podaj pierwszą liczbę :"))
    num2=float(input("Podaj drugą liczbę :"))
    print("Dzielę ",num1,"przez",num2)
    print("Wynik działania to: ", divide(num1,num2))
else:
    pass
    print("Wybrałeś niewłaściwe działanie")
