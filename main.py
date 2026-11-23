# Each title: a name and a genre
catalogue = [
    {"name": "The Silent Harbour", "genre": "crime"},
    {"name": "Busy Rocket", "genre": "kids"},
    {"name": "The Last Kingdom", "genre": "drama"},
    {"name": "Another Crime", "genre": "crime"},
    {"name": "The Great Adventure", "genre": "kids"},
    {"name": "The Final Frontier", "genre": "documentary"},
    {"name": "The Lost City", "genre": "drama"},
    {"name": "Hidden Treasure", "genre": "crime"},
    {"name": "Scream", "genre": "horror"},
    {"name": "The Haunted Mansion", "genre": "horror"},
    {"name": "The Missing Piece", "genre": "crime"},
    {"name": "Jokers", "genre": "comedy"},
    {"name": "The Comedian", "genre": "comedy"},
    {"name": "Bluey", "genre": "kids"},
    {"name": "Deep Sea Dive", "genre": "documentary"},
    {"name": "The Act", "genre": "drama"}
]

def get_genre(name):
    for title in catalogue:
        if title["name"] == name:
            return title["genre"]
    return None


history = [
    ["The Silent Harbour", "Another Crime"],
    ["The Act"],
    ["Hidden Treasure", "The Missing Piece", "Jokers"],
    ["The Last Kingdom", "The Lost City"],
    ["The Comedian"],
    ["The Act", "Another Crime"],
]

for session in history:
    genres = []
    for name in session:
        genres.append(get_genre(name))
    print(genres)