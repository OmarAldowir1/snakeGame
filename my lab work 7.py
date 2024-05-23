class Track:
    def __init__(self, track_id, track_name, artist_name, price):
        self.track_id = track_id
        self.name = track_name
        self.artist_name = artist_name
        self.price = price

class Playlist:
    def __init__(self, user):
        self.user = user
        self.tracks_list = []

    def add_track(self, track):
        if track in self.tracks_list:
            print("the track already exists")
        else:
            if self.user.budget >= track.price:
                self.tracks_list.append(track)
                self.user.budget = track.price
            else:
                print("You don't have budget")

    def calculate_sum(self):
        total = sum(track.price for track in self.tracks_list)
        if self.user.type == "Premium":
            total *= 0.8
        return total

    def calculate_average(self):
        return sum(self.tracks_list) / len(self.tracks_list)

    def print_info(self):
        self.user.print_info()
        print("Total:", self.calculate_sum(), "Average:", self.calculate_average())

class User:
    def __init__(self, _id, full_name, budget, type):
        self.id = _id
        self.full_name = full_name
        self.budget = budget
        self.type = type

    def print_info(self):
        return self._id, self.full_name, self.budget



user_1 = User(1000, "Ali Ak", 40, 'Standard')
user_2 = User(1001, "Ayşe Yılmaz", 100, 'Premium')

track_1 = Track(2000, "A", "Artist_1", 10)
track_2 = Track(2001, "B", "Artist_2", 15)
track_3 = Track(2002, "C", "Artist_3", 5)
track_4 = Track(2003, "D", "Artist_1", 25)
track_5 = Track(2004, "E", "Artist_2", 20)

playlist_1 = Playlist(user_1)
playlist_1.add_track(track_1)
playlist_1.add_track(track_4)
playlist_1.add_track(track_5)

playlist_2 = Playlist(user_2)
playlist_2.add_track(track_1)
playlist_2.add_track(track_2)
playlist_2.add_track(track_3)
playlist_2.add_track(track_3)

playlist_1.print_info()
print("*" * 25)
playlist_2.print_info()