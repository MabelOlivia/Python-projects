from datetime import *


class Event:
    def __init__(self, name, startDate, endDate):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.venue = []

    def useVenue(self, venue):
        self.venue.append(venue)


class Venue:
    def __init__(self, name):
        self.name = name
        self.address = []

    def useAddress(self, address):
        self.address.append(address)


class Address:
    def __init__(self, street, city, state, country, zipcode):
        self.zipcode = zipcode
        self.country = country
        self.street = street
        self.city = city
        self.state = state


event = Event("JazzFest", date(2020, 11, 29), date(2020, 11, 30))
event1 = Event("NaiFest", date(2020, 11, 29), date(2020, 11, 30))
venue = Venue("KICC")
address = Address("parliament", "Nairobi", "Nairobi county", "Kenya", "+254")
event.useVenue(venue)
event1.useVenue(venue)
venue.useAddress(address)

print("Event name:", event.name)
print("Event Date:", event.startDate)
for eachEvent in event.venue:
    print(f'Venue: {eachEvent.name}')
    for eachVenue in eachEvent.address:
        print("street:", eachVenue.street)
        print("city:", eachVenue.city)
        print("state:", eachVenue.state)
        print("country:", eachVenue.country)

print("")
print("Event name:", event1.name)
print("Event Date:", event1.startDate)
for eachEvent in event1.venue:
    print(f'Venue: {eachEvent.name}')
    for eachVenue in eachEvent.address:
        print("street:", eachVenue.street)
        print("city:", eachVenue.city)
        print("state:", eachVenue.state)
        print("country:", eachVenue.country)


