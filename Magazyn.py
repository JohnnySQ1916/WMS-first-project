from Magazyn_Lokacje import Location, locatProd, location
from Magazyn_Product import products, Product
from MAgazyn_Create_Orders import Orders_Product, Orders, Creating_Order
import random
import datetime
import pandas as pd


def saving_list(lista):
    data = {'Kod': [i.kod_prod for i in lista],
            'Nazwa Produktu': [i.product_Name for i in lista],
            'EAN': [i.ean for i in lista],
            'Ilosc': [i.amount for i in lista],
            'Location': [i.location for i in lista]}
    df = pd.DataFrame(data)
    df.to_excel('Karta_Towarow_Zaaktualizowana.xlsx', index=False)


class Warehouse_System_Menagement(Location, Orders):

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def Main_Menu(self):
        UserChoice = 100
        while True:
            UserChoice = int(input('''1 - Deliver Product       2 - Making orders
3 - Relocate product        4 - Checking locate/product
0 - Exit
'''))
            if UserChoice == 1:
                Location.delivery()
            elif UserChoice == 2:
                for k, i in enumerate(Orders.ListOfOrders):
                    print(k+1, i, len(Orders.ListOfOrders[i]))
                UserChoiceTransport = int(
                    input('What would you like to choose? Enter a number: '))
                if UserChoiceTransport == 1:
                    for k, i in enumerate(Orders.ListOfOrders['Geis']):
                        print(k+1, i, len(Orders.ListOfOrders['Geis'][i]))
                    UserChoiceGroupOfOrder = int(
                        input('What would you like to choose? Enter a number: '))
                    if UserChoiceGroupOfOrder == 1:
                        for k, i in enumerate(Orders.ListOfOrders['Geis']['Duzy Ben']):
                            print(k+1, i)
                        UserChoiceOrder = int(
                            input('What order would you like to choose? Enter a number:'))
                        for k, i in enumerate(Orders.ListOfOrders['Geis']['Duzy Ben']):
                            if UserChoiceOrder == k+1:
                                i.Making_Order(locatProd)
                    elif UserChoiceGroupOfOrder == 2:
                        for k, i in enumerate(Orders.ListOfOrders['Geis']['Hurtownia']):
                            print(k+1, i)
                        UserChoiceOrder = int(
                            input('What order would you like to choose? Enter a number:'))
                        for k, i in enumerate(Orders.ListOfOrders['Geis']['Hurtownia']):
                            if UserChoiceOrder == k+1:
                                i.Making_Order(locatProd)
                    elif UserChoiceGroupOfOrder == 3:
                        for k, i in enumerate(Orders.ListOfOrders['Geis']['Pozostale']):
                            print(k+1, i)
                        UserChoiceOrder = int(
                            input('What order would you like to choose? Enter a number:'))
                        for k, i in enumerate(Orders.ListOfOrders['Geis']['Pozostale']):
                            if UserChoiceOrder == k+1:
                                i.Making_Order(locatProd)

            elif UserChoice == 3:
                Location.change_location()
            elif UserChoice == 4:
                UserChoiceCheck = int(
                    input('1- Checking location info    2- Checking product info: '))
                if UserChoiceCheck == 1:
                    Location.show_info_location()
                elif UserChoiceCheck == 2:
                    Location.Checking_Product_Info()
            elif UserChoice == 0:
                break

    def delivery(self, ean, yy, mm, dd, lista):
        data = datetime.datetime(yy, mm, dd)
        data = data.strftime('%x')
        print(data)
        for i in lista:
            if i.ean == ean:
                print(i)
        amount = int(input('Give amount of that product: '))
        locat = input('Enter location: ')
        counter = 0
        for i in lista:
            if i.ean == ean:
                counter += 1
                if locat == i.location:
                    if data == i.data:
                        print('ta sama data')
                        i.amount += amount
                        break
                    else:
                        print('inna data')
                        newProdOnLoc = Location(
                            locat, i.product_Name, i.kod_prod, i.ean, amount, data)
                        locatProd.append(newProdOnLoc)
                        break
                else:
                    print('inna lokacja')
                    newProdOnLoc = Location(
                        locat, i.product_Name, i.kod_prod, i.ean, amount, data)
                    locatProd.append(newProdOnLoc)
                    break
        if counter == 0:
            print('There is no such EAN code in our Data Base')
        answer = int(input('Confirm - press - 1/n Cancel - press - 2'))
        if answer == 1:
            aktualize = saving_list(locatProd)

    def change_location(self, lista):
        while True:
            answer = input('Do you want to relocate some product?Y/N: ')
            counter = 0
            if answer.upper() == 'Y':
                locat = input('Enter location: ')
                for i in lista:
                    if i.location == locat:
                        print(i)
                ean = int(input('Enter products ean: '))
                relocateAmount = int(input('Enter the amount: '))
                for i in lista:
                    if i.location == locat:
                        if i.ean == ean:
                            print(i)
                            if i.amount >= relocateAmount:
                                i.amount -= relocateAmount
                                print('Ilosc dostepnych sztuk', i.amount)
                                newLocat = input('Enter new location: ')
                                for j in lista:
                                    if j.location == newLocat:
                                        if j.ean == ean:
                                            if j.data == i.data:
                                                print(
                                                    'produkt jest na lokacji w tej samej dacie')
                                                counter += 1
                                                j.amount += relocateAmount
                                                break
                                        else:
                                            print('nie ma na lokacji ')
                                if counter == 0:
                                    newProdOnLoc = Location(
                                        newLocat, i.product_Name, i.kod_prod, i.ean, relocateAmount, i.data)
                                    lista.append(newProdOnLoc)
                                if i.amount == 0:
                                    lista.remove(i)
                                answer = int(
                                    input('Confirm - press - 1/n Cancel - press - 2:  '))
                                if answer == 1:
                                    aktualize = saving_list(lista)
                                else:
                                    break
                                return lista
                            else:
                                print('Not enough amount on location to relocate')
            else:
                break


Kuba = Warehouse_System_Menagement('Kuba', 1)
# przyjecie.delivery(5906874605462, 2024, 7, 1, locatProd)
# Kuba.change_location(locatProd)

numberOfKIndDuzyBen = random.randint(2, 5)
numberOfKIndHurt = random.randint(50, 120)
New_Order_ProductDuzyBen = Creating_Order(numberOfKIndDuzyBen)
New_Order_ProductDuzyHurt = Creating_Order(numberOfKIndHurt)

New_Order1 = Orders('Duzy Ben 134', New_Order_ProductDuzyBen, sum(
    [i.amount for i in New_Order_ProductDuzyBen]), len(New_Order_ProductDuzyBen))
New_Order2 = Orders('Stanbud', New_Order_ProductDuzyHurt, sum(
    [i.amount for i in New_Order_ProductDuzyHurt]), len(New_Order_ProductDuzyHurt))
for i in Orders.ListOfOrders['Geis']:
    print(i, len(Orders.ListOfOrders['Geis'][i]))
Kuba.Main_Menu()
# New_Order1.Making_Order(locatProd)
