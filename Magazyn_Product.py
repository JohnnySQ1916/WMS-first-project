import pandas as pd

path = r'C:\Users\user\Desktop\VSC Python\System Magazynowy\karta_towarow.xlsx'
prod = pd.read_excel(path)
product_Name_Exl = pd.DataFrame(prod)
product_name = product_Name_Exl['Nazwa'].tolist()
product_name = [i for i in product_name[1:]]

kod_prod = product_Name_Exl['Kod'].tolist()
kod_prod = [i for i in kod_prod[1:]]

ean = product_Name_Exl['EAN'].tolist()
ean = [i for i in ean[1:]]

amount = product_Name_Exl['Workers.StanMagazynu.StanFizyczny'].tolist()
amount = [i for i in amount[1:]]

weights = {
    'BUT. 0,5 L': 0.770,
    'PUSZKA 0,5 L': 0.540,
    'BUT. 0,75 L': 1.1,
    'BUT. 0,33 L': 0.5,
    'PUSZKA 0,33 L': 0.35,
    'PUSZKA 0,44 L': 0.48,
    'PUSZKA 0,473 L': 0.53,
    'BUT. 0,25 L': 0.35,
    'BUT. 0,375 L': 0.5,
    'KEG 30 L': 32,
    'KEG 20 L': 21.5,
    'KEG 25 L': 28
}


class Product:

    def __init__(self, product_name, kod_prod, ean, amount, weight):
        # for p, k, e, a in zip(product_name, kod_prod, ean, amount):
        self.product_Name = product_name
        self.kod_prod = kod_prod
        self.ean = ean
        self.amount = amount
        self.weight = weight

    def __str__(self):
        return (f'Product Name : {self.product_Name}, Kod Produktu : {self.kod_prod}, EAN:{self.ean}, Amount :{self.amount}, Weight: {self.weight} kg')

    def Checking_Product_Info():
        SearchProduct = input('Give a product EAN number: ')
        for i in products:
            if i.ean == SearchProduct:
                print(i)


products = []
for p, k, e, a in zip(product_name, kod_prod, ean, amount):
    if p.endswith('BUT. 0,5 L'):
        newProducts = Product(p, k, e, a, weights['BUT. 0,5 L'])
        products.append(newProducts)
    elif p.endswith('PUSZKA 0,5 L'):
        newProducts = Product(p, k, e, a, weights['PUSZKA 0,5 L'])
        products.append(newProducts)
    elif p.endswith('BUT. 0,75 L'):
        newProducts = Product(p, k, e, a, weights['BUT. 0,75 L'])
        products.append(newProducts)
    elif p.endswith('BUT. 0,33 L'):
        newProducts = Product(p, k, e, a, weights['BUT. 0,33 L'])
        products.append(newProducts)
    elif p.endswith('PUSZKA 0,33 L'):
        newProducts = Product(p, k, e, a, weights['PUSZKA 0,33 L'])
        products.append(newProducts)
    elif p.endswith('PUSZKA 0,44 L'):
        newProducts = Product(p, k, e, a, weights['PUSZKA 0,44 L'])
        products.append(newProducts)
    elif p.endswith('PUSZKA 0,473 L'):
        newProducts = Product(p, k, e, a, weights['PUSZKA 0,473 L'])
        products.append(newProducts)
    elif p.endswith('BUT. 0,25 L'):
        newProducts = Product(p, k, e, a, weights['BUT. 0,25 L'])
        products.append(newProducts)
    elif p.endswith('BUT. 0,375 L'):
        newProducts = Product(p, k, e, a, weights['BUT. 0,375 L'])
        products.append(newProducts)
    elif p.endswith('KEG 30 L'):
        newProducts = Product(p, k, e, a, weights['KEG 30 L'])
        products.append(newProducts)
    elif p.endswith('KEG 20 L'):
        newProducts = Product(p, k, e, a, weights['KEG 20 L'])
        products.append(newProducts)
    elif p.endswith('KEG 25 L'):
        newProducts = Product(p, k, e, a, weights['KEG 25 L'])
        products.append(newProducts)
    else:
        newProducts = Product(p, k, e, a, 0)
        products.append(newProducts)
