class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print(self.name)
        print(self.reg)

t1=teacher("kitha","01")
t2=teacher("setha","05")

t1.display()
t2.display()
