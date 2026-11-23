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
pending = []    # sessions the account holder has not yet confirmed

def check_session(session):
    profile = build_profile(history)

    if len(history) < MIN_SESSIONS:
        history.append(session)
        print("Still getting to know your taste, session added to your profile.")
        return

    score = unusual_score(session, profile)
    if score < THRESHOLD:
        history.append(session)
        print(f"This looks like your usual viewing pattern, so I've added it to your profile.")
        return

    print(f"\nThis doesn't look like your usual viewing pattern:")
    for reason in explain(session, profile):
        print(" -", reason)
    answer = input("Was this you? (yes/no): ").strip().lower()   # waits for typing, like scanf

    if answer in ("yes", "y"):
        history.append(session)
        print("Got it, I'll use this for your recommendations.")
    elif answer in ("no", "n"):
        ignored.append(session)
        print("Session ignored, your recommendations won't change.")
    else:
        pending.append(session)
        print("This won't be used for your recommendations until you confirm it's you. Please check back later.")

def review_pending():
    if not pending:
        return
    print(f"\nYou have {len(pending)} session(s) waiting for your answer.")
    for session in list(pending):     # loop over a copy to remove safely
        print("\nWaiting:", session)
        for reason in explain(session, build_profile(history)):
            print(" -", reason)
        answer = input("Was this you? (yes/no): ").strip().lower()

        if answer in ("yes", "y"):
            history.append(session)
            pending.remove(session)
            print("Got it, I'll use this for your recommendations.")
        elif answer in ("no", "n"):
            ignored.append(session)
            pending.remove(session)
            print("Session ignored, your recommendations won't change.")
        else:
            print("Still waiting: this won't be used until you confirm it's you.")

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
    ["The Silent Harbour"],                # user
    ["Scream", "The Haunted Mansion"],     # friend
    ["Deep Sea Dive"],                     # user tries documentaries
    ["The Final Frontier"],                # more documentaries
]
for session in new_sessions:
    print("\nNew session:", session)
    check_session(session)

print("\nReviewing pending sessions...")
review_pending()
print("\nFinal profile:")
for genre, share in build_profile(history).items():
    print(f"  {genre}: {share * 100:.0f}%")
print("Ignored sessions:", ignored)
print("Pending sessions:", pending)