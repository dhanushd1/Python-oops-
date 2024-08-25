class laptop:
    def __intit__(self):
        self.ram=ram
        self.proces=proces
    def display(self):
        print("ram is:",self.ram)
        print("process is:",self.proces)

hp=laptop()
dell=laptop()

hp.ram="12gp"
hp.proces="i7"

dell.ram="10gp"
dell.proces="i5"

hp.display()
dell.display()
