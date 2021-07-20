class Programmer :
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    
    def getInfo(self):
        print(f'Name is {self.name} and product is {self.product}')

ishi = Programmer('ishi',"skype")
hardik = Programmer('hardik',"GitHub")

ishi.getInfo()