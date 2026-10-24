def recommend_events(events, user_interests):
    """
    Rank events according to how closely they match
    the user's selected interests.

    Parameters:
        events: A list of event dictionaries.
        user_interests: A list of user interests.

    Returns:
        A list of events sorted by recommendation score.
    """

    # Normalize interests to lowercase for matching.
    user_interests = {
        interest.strip().casefold()
        for interest in user_interests
        if interest.strip()
    }

    # No preferences means we cannot personalize recommendations.
    if not user_interests:
        return []

    recommendations = []

    for event in events:

        # Normalize the interests associated with the event.
        event_interests = {
            interest.strip().casefold()
            for interest in event.get("interests", [])
            if interest.strip()
        }

        # Find interests shared by the user and the event.
        matching_interests = user_interests & event_interests

        # Calculate the percentage of the user's interests
        # that match this event.
        score = (
            len(matching_interests) / len(user_interests)
        ) * 100

        # Make a copy so the original event remains unchanged.
        recommended_event = event.copy()

        recommended_event["recommendation_score"] = round(
            score, 2
        )

        recommended_event["matching_interests"] = sorted(
            matching_interests
        )

        recommendations.append(recommended_event)

    # Highest-scoring events appear first.
    recommendations.sort(
        key=lambda event: (
            -event["recommendation_score"],
            event["title"].casefold()
        )
    )

    return recommendations