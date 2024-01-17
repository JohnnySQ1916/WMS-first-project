import random
import datetime
from Magazyn_Product import Product, products
import pandas as pd


def saving_list(lista):
    data = {'Kod': [i.kod_prod for i in lista],
            'Nazwa Produktu': [i.product_Name for i in lista],
            'EAN': [i.ean for i in lista],
            'Ilosc': [i.amount for i in lista],
            'Location': [i.location for i in lista],
            'Product Weight': [i.weight for i in lista],
            'Expired Date': [i.data for i in lista]}
    df = pd.DataFrame(data)
    df.to_excel('Karta_Towarow_Zaaktualizowana.xlsx', index=False)


def RegalMaker(i, j, k):
    if j < 10:
        numer = i + '-0' + str(j) + '-0'+str(k)
        location.append(numer)
    else:
        numer = i + '-' + str(j) + '-0'+str(k)
        location.append(numer)
    return (location)


def RegalMaker2(i, j):
    if j < 10:
        numer = i + '-0' + str(j)
        location.append(numer)
    else:
        numer = i + '-' + str(j)
        location.append(numer)
    return (location)


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
                                                    newLocat, i.product_Name, i.kod_prod, i.ean, relocateAmount, i.weight, i.data)
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


locatLowAmount = [i for i in location if i.split('-')[1] == '26' or i.split(
    '-')[1] == '27' or i.split('-')[1] == '28' or i.split('-')[1] == '29']
locatLowAmount.extend([i for i in location if i.split(
    '-')[1] == '20' or i.split('-')[1] == '21'])
locatHighAmount = [i for i in location if len(i) == 5]
locat00 = [i for i in location if len(i) > 5 and i.split(
    '-')[2] == '00' and i not in locatLowAmount]
locat01 = [i for i in location if len(i) > 5 and i.split(
    '-')[2] == '01' and i not in locatLowAmount]
locat2_4 = [i for i in location if len(
    i) > 5 and i not in locat00 and i not in locat01 and i not in locatLowAmount]
locatProdNoIteration = []
ProductoIteration = products.copy()
x = datetime.date(2024, 6, 1)

for i in ProductoIteration:
    if 0 < i.amount < 22:
        for j in locatLowAmount:
            if sum([i.amount for i in locatProdNoIteration if i.location == j]) + i.amount < 80:
                newLocatProd = Location(j, i.product_Name,
                                        i.kod_prod, i.ean, i.amount, i.weight, x)
                locatProdNoIteration.append(newLocatProd)
                break
    elif 21 < i.amount <= 100:
        for j in locat01:
            if sum([i.amount for i in locatProdNoIteration if i.location == j]) + i.amount < 300:
                newLocatProd = Location(
                    j, i.product_Name, i.kod_prod, i.ean, i.amount, i.weight, x)
                locatProdNoIteration.append(newLocatProd)
                break
    elif 100 < i.amount <= 500:
        for j in locat00:
            if sum([i.amount for i in locatProdNoIteration if i.location == j]) + i.amount < 540:
                newLocatProd = Location(j, i.product_Name,
                                        i.kod_prod, i.ean, i.amount, i.weight, x)
                locatProdNoIteration.append(newLocatProd)
                break
    elif 500 < i.amount < 901:
        for j in locat2_4:
            if sum([i.amount for i in locatProdNoIteration if i.location == j]) + i.amount < 1100:
                newLocatProd = Location(j, i.product_Name,
                                        i.kod_prod, i.ean, i.amount, i.weight, x)
                locatProdNoIteration.append(newLocatProd)
                break
    elif i.amount > 900:
        for j in locatHighAmount:
            if sum([i.amount for i in locatProdNoIteration if i.location == j]) < 3000:
                newLocatProd = Location(j, i.product_Name,
                                        i.kod_prod, i.ean, i.amount, i.weight, x)
                locatProdNoIteration.append(newLocatProd)
                break


path2 = r"C:\Users\user\Desktop\VSC Python\Karta_Towarow_Zaaktualizowana.xlsx"
prod2 = pd.read_excel(path2)
product_Name_Exl2 = pd.DataFrame(prod2)

product_name2 = product_Name_Exl2["Nazwa Produktu"].tolist()
product_name2 = [i for i in product_name2[1:]]

kod_prod2 = product_Name_Exl2["Kod"].tolist()
kod_prod2 = [i for i in kod_prod2[1:]]

ean2 = product_Name_Exl2["EAN"].tolist()
ean2 = [i for i in ean2[1:]]

amount2 = product_Name_Exl2["Ilosc"].tolist()
amount2 = [i for i in amount2[1:]]

location2 = product_Name_Exl2['Location'].tolist()
location2 = [i for i in location2[1:]]

weight2 = product_Name_Exl2['Product Weight'].tolist()
weight2 = [i for i in weight2[1:]]

data2 = product_Name_Exl2['Expired Date'].tolist()
data2 = [i for i in data2[1:]]


locatProd = []
y = datetime.date(2024, 9, 1)
for l, p, k, e, a, w in zip(location2, product_name2, kod_prod2, ean2, amount2, weight2):
    newProductOnLocation = Location(l, p, k, e, a, w, y)
    locatProd.append(newProductOnLocation)
