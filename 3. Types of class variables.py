class phone:
    chargertype = "ctype"  # Class variable

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        self.chargertype = phone.chargertype  # Reference the class variable

    def display(self):
        print("brand:", self.brand)
        print("price:", self.price)
        print("charger:", self.chargertype)

phone.chargertype="btype"

samsung = phone("samsung", 14000)
samsung.display()

redmi = phone("redmi", 4000)
redmi.display()


