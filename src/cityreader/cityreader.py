import csv


class City:

    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'City: {self.name},{self.lat}, {self.lon}'


cities = []


def cityreader(cities=[]):

    with open('cities.csv', 'r') as city:
        reader = csv.reader(city)
        next(reader)

        for c in reader:
            cities.append(City(c[0], float(c[3]), float(c[4])))

        return cities


cityreader(cities)

for c in cities:
    print(c)
