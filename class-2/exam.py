import pickle

class movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

movie1 = movie("Inception", 9.0)
with open("movie_data.pkl", "wb") as f:
    pickle.dump(movie1, f)
    