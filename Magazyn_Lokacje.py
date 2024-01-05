import random
import datetime
from Magazyn_Product import Product, products


def RegalMaker(i, j, k):
    if j < 10:
        numer = i + '-0' + str(j) + '-0'+str(k)
        location.append(numer)
    else:
        numer = i + '-' + str(j) + '-0'+str(k)
        location.append(numer)
    return location


def RegalMaker2(i, j):
    if j < 10:
        numer = i + '-0' + str(j)
        location.append(numer)
    else:
        numer = i + '-' + str(j)
        location.append(numer)
    return location


locationStarter = {'RA': [], 'RB': [], 'RC': [], 'RD': [], 'RE': [
], 'RF': [], 'RG': [], 'RH': [], 'RI': [], 'RJ': [], 'RK': [], 'RL': [], 'AT': []}
wajatek = 'RA'
wyjatek2 = 'AT'
location = []
for i in locationStarter:
    if i == wajatek:
        for j in range(1, 12):
            for k in range(5):
                RegalMaker(i, j, k)
    elif i == wyjatek2:
        for j in range(1, 9):
            for k in range(5):
                RegalMaker(i, j, k)
        for j in range(9, 26):
            RegalMaker2(i, j)
        for j in range(26, 30):
            for k in range(5):
                RegalMaker(i, j, k)
        for j in range(30, 34):
            RegalMaker2(i, j)
    else:
        for j in range(1, 22):
            for k in range(5):
                RegalMaker(i, j, k)


class Location(Product):

    productInLocation = []  # sprawdzic czy nie bedzie bardziej uzyteczne niz Locatprod

    def __init__(self, location, product_Name, kod_prod, ean, amount, weight, data):
        super().__init__(product_Name, kod_prod, ean, amount, weight)
        self.location = location
        self.data = data
        Location.productInLocation.append(self)

    def __str__(self):
        return (f'Location : {self.location}, Product Name : {self.product_Name}, Amount :{self.amount}, Data:{self.data}')

    def show_info_location():
        while True:
            SearchLocation = input('Enter location: ')
            if SearchLocation in [i.location for i in locatProd]:
                for i in locatProd:
                    if i.location == SearchLocation:
                        print(
                            f'Location: {i.location}  Product Name: {i.product_Name} Amount: {i.amount} Data: {i.data} Total weight on location: {sum([i.amount * i.weight for i in locatProd if i.location == SearchLocation])}')
                break
            else:
                print('Uncorrect location. Try again')
                continue

    def Checking_Product_Info():
        while True:
            try:
                SearchProduct = int(input('Give a product EAN number: '))
                if SearchProduct in [i.ean for i in locatProd]:
                    for i in locatProd:
                        if i.ean == SearchProduct:
                            print(
                                f'Location: {i.location}  Product Name: {i.product_Name} Amount: {i.amount} Data: {i.data}')
                    break
            except ValueError:
                print('You have to enter a number')
            else:
                print('Uncorrect ean number. Try again')

    def delivery(self, product, amount, data, location):
        for i in self.locatProd:
            if product == i.product and data == i.data:
                i.amount += amount
            else:
                EAN = input('Podaj kod EAN:')
                for i in products:
                    if EAN == i.ean:
                        self.product = i.product
                    else:
                        print('There is no such EAN code in our Data Base')
        self.amount = input(int('Give amount of that product: '))
        self.data = input('Give a data of this product')
        for i in self.locatProd:
            if ean == i.ean:
                print(
                    f'Product Name: {i.product_Name}  - Location: {i.location}  - Amount: {i.amount}  - Data: {i.data}')
        self.location = input('Give location to store that product')
        self.locatProd.append({})

    def change_location():
        while True:
            answer = input('Do you want to relocate some product?Y/N: ')
            counter = 0
            if answer.upper() == 'Y':
                locat = input('Enter location: ')
                if locat in [i.location for i in locatProd]:
                    for i in locatProd:
                        if i.location == locat:
                            print(i)
                    while True:
                        try:
                            ean = int(input('Enter products ean: '))
                            relocateAmount = int(input('Enter the amount: '))
                            for i in locatProd:
                                if i.location == locat:
                                    if i.ean == ean:
                                        print(i)
                                        if i.amount >= relocateAmount:
                                            i.amount -= relocateAmount
                                            print(
                                                'Ilosc dostepnych sztuk', i.amount)
                                            newLocat = input(
                                                'Enter new location: ')
                                            for j in locatProd:
                                                if j.location == newLocat:
                                                    if j.ean == ean:
                                                        if j.data == i.data:
                                                            print(
                                                                'produkt jest na lokacji w tej samej dacie')
                                                            counter += 1
                                                            j.amount += relocateAmount
                                                            break
                                                    else:
                                                        print(
                                                            'nie ma na lokacji ')
                                            if counter == 0:
                                                newProdOnLoc = Location(
                                                    newLocat, i.product_Name, i.kod_prod, i.ean, relocateAmount, i.data)
                                                locatProd.append(newProdOnLoc)
                                            if i.amount == 0:
                                                locatProd.remove(i)
                                            answer = int(
                                                input('Confirm - press - 1/n Cancel - press - 2:  '))
                                            if answer == 1:
                                                aktualize = saving_list(
                                                    locatProd)
                                            else:
                                                break
                                            return locatProd
                                        else:
                                            print(
                                                'Not enough amount on location to relocate')
                        except ValueError:
                            print('You have to enter a number')
                        else:
                            print('Uncorrect ean number. Try again')
                else:
                    print('Uncorrect location. Try again')
            else:
                break


def set_level_location(lista, level):
    level_list = []
    for i in lista:
        if len(i) > 5:
            if i.split('-')[2] == level:
                level_list.append(i)
    return level_list


def check_if_location_is_busy(lista, levelLocation):
    while True:
        locat = random.choice(levelLocation)
        counter = 0
        for i in lista:
            if i.location == locat:
                counter += 1
        if counter <= 3:
            return location


locatLowAmount = [i for i in location if i.split('-')[1] == '26' or i.split(
    '-')[1] == '27' or i.split('-')[1] == '28' or i.split('-')[1] == '29']
locatLowAmount.append([i for i in location if i.split(
    '-')[1] == '20' or i.split('-')[1] == '21'])
locatHighAmount = [i for i in location if len(i) == 5]
locat00 = [i for i in location if len(i) > 5 and i.split(
    '-')[2] == '00' and i not in locatLowAmount]
locat01 = [i for i in location if len(i) > 5 and i.split(
    '-')[2] == '01' and i not in locatLowAmount]
locat2_4 = [i for i in location if len(
    i) > 5 and i not in locat00 and i not in locat01 and i not in locatLowAmount]
locatProd = []

x = datetime.date(2024, 6, 1)
for i in products:
    if 0 < i.amount < 20:
        locat = random.choice(locatLowAmount)
        print(locat, i)
        if sum([i.amount for i in locatProd if i.location == locat]) < 100:
            newLocatProd = Location(locat, i.product_Name,
                                    i.kod_prod, i.ean, i.amount, i.weight, x)
            locatProd.append(newLocatProd)
        else:
            continue
    elif 19 < i.amount <= 100:
        locat = random.choice(locat01)
        newLocatProd = Location(
            locat, i.product_Name, i.kod_prod, i.ean, i.amount, i.weight, x)
        locatProd.append(newLocatProd)
    elif i.amount > 100 and i.amount <= 500:
        locat = random.choice(locat00)
        newLocatProd = Location(locat, i.product_Name,
                                i.kod_prod, i.ean, i.amount, i.weight, x)
        locatProd.append(newLocatProd)
    elif 500 < i.amount < 901:
        locat = random.choice(locat2_4)
        newLocatProd = Location(locat, i.product_Name,
                                i.kod_prod, i.ean, i.amount, i.weight, x)
        locatProd.append(newLocatProd)
    elif i.amount > 900:
        locat = random.choice(locatHighAmount)
        newLocatProd = Location(locat, i.product_Name,
                                i.kod_prod, i.ean, i.amount, i.weight, x)
        locatProd.append(newLocatProd)

dlugosc = sum([i.amount for i in locatProd if i.location == 'AT-26-01'])
print(dlugosc)
expiry_time = datetime.date.today() + datetime.timedelta(days=90)
print(expiry_time)
