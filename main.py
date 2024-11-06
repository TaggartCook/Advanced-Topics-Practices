from app import App
from csv import reader
from tech import Phone, Laptop
"""
apps=[]

with open('app_list.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    next(csv_reader)
    for name, description, category in csv_reader:
        apps.append(App(name,description,category))

for app in apps:
    print(app)
"""
myPhone = Phone("Pixel 5", 128, "sage")
myLaptop = Laptop("MacBook Pro", 256, 15)

print(myPhone)
print(repr(myPhone))
print(myLaptop)
print(repr(myLaptop))

