class TvShow:
    def __init__(self, name, year, ):
        self._name = name.title()
        self.year = year
        self._likes = 0

    def like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @property
    def likes(self):
        return self._likes

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f'{self._name} - {self.year}: {self._likes} likes'


class Movie(TvShow):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self._name} - {self.year} - {self.duration} minutes: {self._likes} likes'


class Series(TvShow):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    def __str__(self):
        return f'{self._name} - {self.year} - {self.season} seasons: {self._likes} likes'


class Playlist:
    def __init__(self, name, shows):
        self.name = name
        self._shows = shows

    def __getitem__(self, item):
        return self._shows[item]

    def __len__(self):
        return len(self._shows)


avengers = Movie("avengers - infinity war", 2018, 160)
got = Series("game of thrones", 2015, 7)
tamarindo_adventures = Movie("tamarindo adventures", 2018, 20000)
holy_querupita = Series("holy querupita", 2017, 5)

tamarindo_adventures.like()
tamarindo_adventures.like()
tamarindo_adventures.like()
holy_querupita.like()
holy_querupita.like()
avengers.like()
got.like()
got.like()

tv_shows = [avengers, got, tamarindo_adventures, holy_querupita]
weekend_playlist = Playlist('Weekend playlist', tv_shows)

print(f"Playlist length: {len(weekend_playlist)}")
for show in weekend_playlist:
    print(show)
