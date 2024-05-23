class Track:
    def __init__(self, _id, name, artist_name, price):
        self.id = _id
        self.name = name
        self.artist_name = artist_name
        self.price = price


class Playlist:
    def __init__(self, user):
        self.user = user
        self.track_list = []

    def add_track(self, track):
        if track in self.track_list:
            print("The track is already in the list")
        else:
            if self.user.budget >= track.price:
                self.track_list.append(track)
                self.user.budget -= track.price
            else:
                print("You have no budget")

    def calculate_sum(self):
        total_price = sum(track.price for track in self.track_list)
        if self.user.type == "Premium":
            total_price *= 0.8  # Apply 20% discount for Premium users
        return total_price

    def calculate_average(self):
        return sum(track.price for track in self.track_list) / len(self.track_list)

    def print_info(self):
        self.user.print_info()
        print("Total:", self.calculate_sum(), "Average:", self.calculate_average())


class User:
    def __init__(self, _id, full_name, budget, user_type):
        self.id = _id
        self.full_name = full_name
        self.budget = budget
        self.type = user_type

    def print_info(self):
        print(self.id, self.full_name, self.budget)


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
