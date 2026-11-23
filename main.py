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

def explain(session, profile):
    reasons = []
    for name in session:
        genre = get_genre(name)
        share = profile.get(genre, 0)
        if share < RARE:
            reasons.append(f"'{name}' is {genre}, which is {share * 100:.0f}% of what you usually watch")
    return reasons

MIN_SESSIONS = 5
ignored = []    # sessions the account holder said were not them

def check_session(session):
    profile = build_profile(history)

    if len(history) < MIN_SESSIONS:
        history.append(session)
        print("Still learning: added without checking.")
        return

    score = unusual_score(session, profile)
    if score < THRESHOLD:
        history.append(session)
        print(f"Looks like your usual viewing (score {score:.2f}): learned.")
        return

    print(f"\nThis session looks unusual (score {score:.2f}):")
    for reason in explain(session, profile):
        print(" -", reason)
    answer = input("Was this you? (yes/no): ").strip().lower()   # waits for typing, like scanf

    if answer == "yes":
        history.append(session)
        print("Learned, session added to your history.")
    elif answer == "no":
        ignored.append(session)
        print("Session ignored, your profile is unchanged.")
    else:
        print("Invalid answer, session ignored.")

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

new_sessions = [
    ["Bluey", "Busy Rocket"],              # child
    ["The Silent Harbour"],                # Sam
    ["Scream", "The Haunted Mansion"],     # friend
    ["Deep Sea Dive"],                     # Sam tries documentaries
    ["The Final Frontier"],                # more documentaries
]
for session in new_sessions:
    print("\nNew session:", session)
    check_session(session)

print("\nFinal profile:")
for genre, share in build_profile(history).items():
    print(f"  {genre}: {share * 100:.0f}%")
print("Ignored sessions:", ignored)