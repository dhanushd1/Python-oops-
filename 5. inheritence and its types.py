class dad:
    def phone(self):
        print("dad's phone")
class mom(dad):
    def sweet(self):
        print("moms sweet")

class son(mom,dad):
    def laptop(self):
        print("son's laptop")

raj=son()
raj.laptop()
raj.sweet()
raj.phone()

d1=mom()
d1.phone()
