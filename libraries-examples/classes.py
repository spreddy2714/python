class Snake:
    clname = []
    def __init__(self, name):
        self.name = name
    def changeCln(self, cl):
        self.clname.append(cl)

s1 = Snake('Python')
print(s1.name)
s2 = Snake('Cobra')
print(s2.name)
print(Snake.clname)
print(s2.clname)
print(s1.clname)
s2.changeCln('changed')
print(s1.clname)
s1.changeCln('again')
print(Snake.clname)
