class goa:
    name="hcbdjj"
    drink=""
    def party(self):
        print("party.......")
    def beach(self):
        print("enjoy........")
ramesh=goa()
suresh=goa()

ramesh.name="ramesh"
suresh.name="suresh"

ramesh.drink="yes"
suresh.drink="no"

print(ramesh.name)
print(suresh.name)
print("drink",ramesh.drink)
print("drink",suresh.drink)

ramesh.party()
suresh.beach()
