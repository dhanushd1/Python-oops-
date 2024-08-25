class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        c=self.a+self.b
        print("sum is ",c)
    def sub(self):
        c=self.a-self.b
        print("sum is ",c)
    def mul(self):
        c=self.a*self.b
        print("sum is ",c)
    

a=calculator(10,5)
a.add()
a.sub()
a.mul()
