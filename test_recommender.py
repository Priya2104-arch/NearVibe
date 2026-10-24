from recommender import recommend_events


events = [
    {
        "title": "AI Workshop",
        "interests": ["AI", "Coding", "Technology"]
    },
    {
        "title": "Python Meetup",
        "interests": ["Python", "Coding"]
    },
    {
        "title": "Photography Walk",
        "interests": ["Photography", "Arts"]
    }
]


user_interests = ["AI", "Python", "Hackathons"]

results = recommend_events(events, user_interests)

for event in results:
    print(
        event["title"],
        "| Score:",
        event["recommendation_score"],
        "| Matches:",
        event["matching_interests"]
    )