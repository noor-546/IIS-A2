# Each title: a name and a genre
catalogue = [
    {"name": "The Silent Harbour", "genre": "crime"},
    {"name": "Busy Rocket", "genre": "kids"},
]

# Check it works: print every title and its genre
for title in catalogue:
    print(title["name"], "-", title["genre"])