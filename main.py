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

def build_profile(sessions):
    counts = {}      # genre -> how many titles
    total = 0        # total titles watched
    for session in sessions:
        for name in session:
            genre = get_genre(name)
            counts[genre] = counts.get(genre, 0) + 1
            total += 1

    profile = {}
    for genre in counts:
        profile[genre] = counts[genre] / total

    return profile

RARE = 0.10        # a genre under 10% of the profile counts as rare
THRESHOLD = 0.5    # flag the session if at least half of it is rare genres

def unusual_score(session, profile):
    rare_count = 0
    for name in session:
        genre = get_genre(name)
        share = profile.get(genre, 0)   # 0 if user has never watched this genre
        if share < RARE:
            rare_count += 1
    return rare_count / len(session)

history = [
    ["The Silent Harbour", "Another Crime"],
    ["The Act"],
    ["Hidden Treasure", "The Missing Piece", "Jokers"],
    ["The Last Kingdom", "The Lost City"],
    ["The Comedian"],
    ["The Act", "Another Crime"],
]

profile = build_profile(history)
for genre in profile:
    print(f"{genre}: {profile[genre] * 100:.0f}%")

tests = [
    ["Bluey", "Busy Rocket"],       # child: should be unusual
    ["The Act", "Jokers"],          # Sam's usual: should not
    ["Scream", "Hidden Treasure"],  # half horror: borderline
]
for session in tests:
    score = unusual_score(session, profile)
    print(session, f"score {score:.2f}", "UNUSUAL" if score >= THRESHOLD else "typical")