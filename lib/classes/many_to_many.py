class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Invalid band name")
        if not isinstance(hometown, str) or len(hometown) == 0:
            raise Exception("Invalid hometown")
        self.name = name
        self.hometown = hometown
        self.concerts_list = []

    def concerts(self):
        return self.concerts_list

    def venues(self):
        unique_venues = set()
        for concert in self.concerts_list:
            unique_venues.add(concert.venue)
        return list(unique_venues)

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        self.concerts_list.append(concert)
        venue.add_concert(concert)
        return concert

    def all_introductions(self):
        introductions = []
        for concert in self.concerts_list:
            introduction = f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            introductions.append(introduction)
        return introductions
class Concert:
    all = []

    def __init__(self, date, band, venue):
        if not isinstance(date, str) or len(date) == 0:
            raise Exception("Invalid date")
        if not isinstance(band, Band):
            raise Exception("Invalid band")
        if not isinstance(venue, Venue):
            raise Exception("Invalid venue")
        self.date = date
        self.band = band
        self.venue = venue
        self.all.append(self)

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Invalid venue name")
        if not isinstance(city, str) or len(city) == 0:
            raise Exception("Invalid city")
        self.name = name
        self.city = city
        self.concerts_list = []
        

    def add_concert(self, concert):
        if concert not in self.concerts_list:
            self.concerts_list.append(concert)

    def concerts(self):
        return self.concerts_list

    def bands(self):
        unique_bands = set()
        for concert in self.concerts_list:
            unique_bands.add(concert.band)
        return list(unique_bands)
