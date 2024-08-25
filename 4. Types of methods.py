class laptop:
    chargertype="c type"

    def __init__(self):
        self.brand=""
        self.price=133

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

        
    @classmethod
    def changechargertype(cls):
        cls.chargertype="b type"
        print("charger type changed")

    @staticmethod
    def info():
        print("this is laptop class")
        

samsung=laptop()
samsung.setprice(1200)
samsung.getprice()

laptop.changechargertype()
 


