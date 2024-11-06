from dogClass import Dog
from csv import reader

dogs = []

with open('dog_breeds.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    next(csv_reader)
    for name, breed in csv_reader:
        dogs.append(Dog(name, breed))

for dog in dogs:
    print(dog)