class company:
    def __init__(self):
        self.__companyname="google"#private __
    def companyname(self):
        print(self.__companyname)

c=company()
c.companyname()

#_____________________________________________________________________
class company:
    def __init__(self):
        self._companyname="google"#protected
class b(company):
    pass
b1=b()
print(b1._companyname)

