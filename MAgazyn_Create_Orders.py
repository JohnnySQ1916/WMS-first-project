from Magazyn_Product import Product, products, weights
from Magazyn_Lokacje import locatProd, ProductoIteration
import datetime
import random
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


def orderNO():
    data = datetime.datetime.now()
    year = data.year
    month = data.month
    day = data.day
    order = str(year) + str(month) + str(day) + '000'
    return int(order)


def Escape_From_Order(listaDone, listaNotDone, Order):
    print('Product Name         Amount')
    for i in listaDone:
        print(i['Product Name'],         i['Amount'])
    print(
        f'Bootles: {sum([i["Amount"] for i in listaDone])} / {sum([i.amount for i in Order])}')
    Decision = input(
        'What do you want to do?: X - exit from order   EX - extend')


def QueueOfOrder(lista):
    # lista.sort(key=lambda x: x.location)
    sortedLista = list(sorted(lista, key=lambda x: x.location))
    OlderDate = []
    for i in sortedLista:
        Twice = [j for j in sortedLista if i.ean == j.ean]
        if len(Twice) > 1:
            Twice.remove(Twice[0])
            OlderDate.append(Twice)
            for i in sortedLista:
                if i in Twice:
                    sortedLista.remove(i)
    NewOrderList = [i for i in sortedLista if i.location.split('-')[0][0] == 'R' and i.location.split('-')[2] == '00'
                    or i.location.split('-')[0][0] == 'R' and i.location.split('-')[2] == '01'
                    or i.location.split('-')[0][0] == 'R' and i.location.split('-')[2] == '02']
    ATList = [i for i in sortedLista if i.location.split('-')[0] == 'AT']
    for i in ATList:
        NewOrderList.append(i)
    RHighLevel = [i for i in sortedLista if i.location.split('-')[0][0] == 'R' and i.location.split('-')[2] == '03'
                  or i.location.split('-')[0][0] == 'R' and i.location.split('-')[2] == '04']
    for i in RHighLevel:
        NewOrderList.append(i)
    NewOrderList.extend(OlderDate)
    for i in NewOrderList:
        print(i)
    return NewOrderList


def Count_Weight_Of_Order(lista, ord):
    TotalWeight = 0
    count = 0
    for i in ord:
        for w in lista:
            if i.product_Name.endswith(w) or i.product_Name.endswith(w.lower()):
                TotalWeight += (lista[w] * i.amount)
                count += 1
    # TotalWeight = round(TotalWeight)
    return TotalWeight


pallets = {'Europaleta': 22,
           'Jednorazowka': 10,
           'Przemyslowa': 25,
           'Polpaleta': 5}


class Orders_Product(Product):

    def __init__(self, product_name, kod_prod, ean, weight, amount, expiry_date):
        super().__init__(product_name, kod_prod, ean, weight, amount)
        self.amount = amount
        self.expiry_date = expiry_date


class Orders(Orders_Product):
    ListOfOrders = {'Geis': {'Duzy Ben': [], 'Hurtownia': [],
                             'Pozostale': []}, 'Raben': [], 'Odbior osobisty': []}

    def __init__(self, Customer, CreatedOrder, TotalAmount, KindsAmount):
        self.OrderNumber = orderNO()
        self.Customer = Customer
        self.CreatedOrder = CreatedOrder
        self.TotalAmount = TotalAmount
        self.KindsAmount = KindsAmount
        self.TotalWeightOrder = Count_Weight_Of_Order(
            weights, self.CreatedOrder)
        if self.Customer[0:8] == 'Duzy Ben':
            self.ListOfOrders['Geis']['Duzy Ben'].append(self)
        elif self.Customer == 'Stanbud':
            self.ListOfOrders['Geis']['Hurtownia'].append(self)

    def __str__(self):
        return (f'Customer: {self.Customer}  Order Number: {self.OrderNumber}  Amount: {self.TotalAmount}  Kinds of beer: {self.KindsAmount}  Total weight of Order: {self.TotalWeightOrder}')

    def Making_Order(self, lista):
        OrderedProductsInWarehouse1 = []
        DoneProducts = []
        for i in self.CreatedOrder:
            for j in lista:
                if i.ean == j.ean:
                    expiry_time = datetime.date.today() + datetime.timedelta(days=i.expiry_date)
                    if j.data > expiry_time:
                        print('data wporzo')
                        OrderedProductsInWarehouse1.append(
                            j)
                    else:
                        continue
        TotalWeightOrder = sum([(i.weight * j.amount)
                                for i, j in zip(OrderedProductsInWarehouse1, self.CreatedOrder)])
        print('Order Number:', self.OrderNumber, 'Amount:',
              self.TotalAmount, 'Total weight of order: ', TotalWeightOrder, ' kg')
        OrderedProductsInWarehouse = QueueOfOrder(OrderedProductsInWarehouse1)
        for k, i in enumerate(pallets):
            print(k+1, i)
        PalletChoice = int(input('Which pallet do you choose? '))
        for k, i in enumerate(pallets):
            if PalletChoice == k+1:
                TotalWeightOrder += pallets[i]
        print(TotalWeightOrder)
        # sprawdzic czy nie powinno byc len(self.CreatedOrder) != 0 i remove from self.CreatedOrder poniewaz w OrderedProductsInWarehouse moga byc powtarzajace sie eany
        while len(OrderedProductsInWarehouse) != 0:
            for i in OrderedProductsInWarehouse:
                escape = input(
                    'If you wanna escape from order and find out details of order press E. If You wanna continue press C')
                if escape.capitalize() == 'E':
                    Escape_From_Order(
                        DoneProducts, OrderedProductsInWarehouse, self.CreatedOrder)
                for j in self.CreatedOrder:
                    for k in lista:
                        # if len([i for i in OrderedProductsInWarehouse if i.ean == j.ean]) > 1:
                        # uzyc try: w przypadku braku kodu EAN pojawia sie blad AttributeError:
                        if i.ean == j.ean and i.ean == k.ean:
                            print(i.kod_prod, '\n', i.product_Name, '\n',
                                  'Amount needed/ Amount available\n', j.amount, '/', k.amount)
                            print(i.location)
                            UserLocation = str()
                            while UserLocation != i.location:
                                UserLocation = input('Enter location: ')
                                if UserLocation == i.location:
                                    break
                                else:
                                    print('Wrong location')
                            UserEAN = int()
                            while UserEAN != i.ean:
                                UserEAN = int(input('Enter products ean: '))
                                if UserEAN == i.ean or 1:
                                    break
                                else:
                                    print('Wrong ean')
                            if j.amount <= k.amount:  # gdy porzadana ilosc jest wieksza od posiadanej
                                while j.amount != 0:
                                    print(j.amount)
                                    UserAmount = int(input('Enter amount: '))
                                    if UserAmount == j.amount:
                                        k.amount -= j.amount
                                        DoneProducts.append(
                                            {'Product Name': i.product_Name, 'Amount': UserAmount})
                                        OrderedProductsInWarehouse.remove(i)
                                        break
                                    elif UserAmount > j.amount:
                                        print('Too many')
                                    elif UserAmount < j.amount and UserAmount != 0:
                                        print('too less')
                                        j.amount -= UserAmount
                                        k.amount -= UserAmount
                                    else:
                                        print('Wrong wariable, try again')
                            elif j.amount > sum([k.amount for k in lista if k.ean == UserEAN]):
                                while j.amount != k.amount:
                                    print(j.amount)
                                    UserAmount = int(input('Enter amount: '))
                                    if UserAmount == k.amount:
                                        k.amount -= UserAmount
                                        DoneProducts.append(
                                            {'Product Name': i.product_Name, 'Amount': UserAmount})
                                        OrderedProductsInWarehouse.remove(i)
                                        break
                                    elif UserAmount > j.amount:
                                        print('Too many')
                                    elif UserAmount < j.amount and UserAmount != 0:
                                        print('too less')
                                        j.amount -= UserAmount
                                        k.amount -= UserAmount
                                    else:
                                        print('Wrong wariable, try again')
        answer = int(input('Confirm - press - 1/n Cancel - press - 2'))
        if answer == 1:
            aktualize = saving_list(locatProd)


def Creating_Order(number):
    ListOfOrder = random.choices(products, k=number)
    new_order = []
    for i in ListOfOrder:
        orderProductAmount = random.randint(5, 20)
        for j in locatProd:
            if i.ean == j.ean:
                if orderProductAmount < sum([j.amount for j in locatProd if j.ean == i.ean]):
                    random_date_expire = random.choice([0, 60, 90, 120])
                    newOrderProduct = Orders_Product(
                        i.product_Name, i.kod_prod, i.ean, i.weight, orderProductAmount, random_date_expire)
                    if newOrderProduct not in new_order:
                        new_order.append(newOrderProduct)
                else:
                    # orderProductAmount < sum([j.amount for j in locatProd if j.ean == i.ean]):
                    random_date_expire = random.choice([0, 60, 90, 120])
                    newOrderProduct = Orders_Product(
                        i.product_Name, i.kod_prod, i.ean, i.weight, j.amount, random_date_expire)
                    if newOrderProduct not in new_order:
                        new_order.append(newOrderProduct)
    return (new_order)


numberOfKIndDuzyBen = random.randint(15, 45)
New_Order_ProductDuzyBen = Creating_Order(numberOfKIndDuzyBen)
New_Order1 = Orders('Duzy Ben 134', New_Order_ProductDuzyBen, sum(
    [i.amount for i in New_Order_ProductDuzyBen]), len(New_Order_ProductDuzyBen))
