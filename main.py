
import logging
logging.basicConfig(level=logging.DEBUG)

action = input("Jakie zadanie chcesz wykonać? \n [1] Dodawanie \n [2] Odejmowanie \n [3] Mnożenie \n [4] Dzielnie \n")
action_int = int(action)
if action_int == 1:
    number_1 = int(input("Podaj pierwszą liczbę:"))
    number_2 = int(input("Podaj drugą liczbę:"))
    def action_1(number_1, number_2):
        result = number_1 + number_2
        logging.debug(f"Dodaję {number_1} i {number_2}")
        logging.debug(result)
    action_1(number_1, number_2)
elif action_int ==2:
    def action_2(number_1, number_2):
        result = number_1 - number_2
        logging.debug(f"Odejmuję {number_2} od {number_1}")
        logging.debug(result)
    number_1 = int(input("Podaj pierwszą liczbę:"))
    number_2 = int(input("Podaj drugą liczbę:"))
    action_2(number_1, number_2)
elif action_int == 3:
    def action_3(number_1, number_2):
        result = number_1 * number_2
        logging.debug(f"Mnożę {number_1} i {number_2}")
        logging.debug(result)
    number_1 = int(input("Podaj pierwszą liczbę:"))
    number_2 = int(input("Podaj drugą liczbę:"))
    action_3(number_1, number_2)
elif action_int == 4:
    def action_4(number_1, number_2):
        result = number_1 / number_2
        logging.debug(f"Dzielę {number_1} przez {number_2}")
        logging.debug(result)
    number_1 = int(input("Podaj pierwszą liczbę:"))
    number_2 = int(input("Podaj drugą liczbę:"))
    action_4(number_1, number_2)
else:
    logging.debug("Nie ma takiego działania")
