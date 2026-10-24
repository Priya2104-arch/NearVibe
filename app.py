import streamlit as st

from recommender import recommend_events
from registrations import (
    load_registrations,
    save_registration
)


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="NearVibe | Discover Your Community",
    page_icon="📍",
    layout="wide"
)


# --------------------------------------------------
# 2. CUSTOM STYLING
# --------------------------------------------------

st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #0B1020;
    color: #F3F4F6;
}

/* Main content area */
.main .block-container {
    max-width: 100%;
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
}

/* Headings */
h1, h2, h3, h4 {
    color: #F3F4F6 !important;
}

/* General text */
.stApp {
    color: #F3F4F6;
}

.stMarkdown p,
.stMarkdown li {
    color: #D7DEEA;
}

/* Secondary text */
.stCaption {
    color: #B6C0D1 !important;
}

/* Form labels */
.stTextInput label,
.stTextArea label,
.stSelectbox label,
.stMultiSelect label,
.stNumberInput label {
    color: #D7DEEA !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #11182A;
    border-right: 1px solid #303B52;
}
/* Cards and bordered containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #151C30;
    border: 1px solid #303B52;
    border-radius: 16px;
    padding: 8px;
    transition: border-color 0.2s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #8B5CF6;
}

/* Buttons */
.stButton > button {
    background-color: #8B5CF6;
    color: #FFFFFF;
    border: 1px solid #A78BFA;
    border-radius: 10px;
    font-weight: 600;
}

/* Button hover */
.stButton > button:hover {
    background-color: #7C3AED;
    color: #FFFFFF;
    border-color: #C4B5FD;
}

/* Text inputs */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background-color: #151C30;
    color: #F3F4F6;
    border: 1px solid #46516B;
    border-radius: 8px;
}

/* Dropdowns and selection controls */
.stSelectbox div[data-baseweb="select"] > div,
.stMultiSelect div[data-baseweb="select"] > div {
    background-color: #151C30;
    color: #F3F4F6;
    border-color: #46516B;
}

/* Radio labels and checkbox labels */
.stRadio label,
.stCheckbox label {
    color: #D7DEEA !important;
}

/* Dividers */
hr {
    border-color: #303B52;
}

/* Links */
a {
    color: #5EEAD4 !important;
}

/* Success messages */
div[data-testid="stAlert"] {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# 3. EVENT DATA
# --------------------------------------------------

events = [
    {
        "id": 1,
        "title": "AI & Machine Learning Workshop",
        "category": "Technology",
        "location": "University Innovation Centre",
        "area": "Gurugram",
        "latitude": 28.4595,
        "longitude": 77.0266,
        "date": "28 October 2026",
        "price": "Free",
        "interests": ["AI", "Coding", "Technology"]
    },
    {
        "id": 2,
        "title": "Python Coding Meetup",
        "category": "Technology",
        "location": "Community Learning Hub",
        "area": "Gurugram",
        "latitude": 28.4650,
        "longitude": 77.0350,
        "date": "29 October 2026",
        "price": "Free",
        "interests": ["Python", "Coding", "Technology"]
    },
    {
        "id": 3,
        "title": "Community Clean-Up Drive",
        "category": "Volunteering",
        "location": "City Community Park",
        "area": "Gurugram",
        "latitude": 28.4500,
        "longitude": 77.0200,
        "date": "31 October 2026",
        "price": "Free",
        "interests": ["Volunteering", "Environment"]
    },
    {
        "id": 4,
        "title": "Startup & Entrepreneurship Meetup",
        "category": "Business",
        "location": "Innovation Hub",
        "area": "Gurugram",
        "latitude": 28.4700,
        "longitude": 77.0150,
        "date": "2 November 2026",
        "price": "Free",
        "interests": ["Entrepreneurship", "Networking"]
    },
    {
        "id": 5,
        "title": "Creative Photography Walk",
        "category": "Arts",
        "location": "Heritage District",
        "area": "Gurugram",
        "latitude": 28.4450,
        "longitude": 77.0400,
        "date": "4 November 2026",
        "price": "Free",
        "interests": ["Photography", "Arts"]
    },
    {
        "id": 6,
        "title": "Beginner-Friendly Hackathon",
        "category": "Technology",
        "location": "University Innovation Centre",
        "area": "Gurugram",
        "latitude": 28.4550,
        "longitude": 77.0100,
        "date": "6 November 2026",
        "price": "Free",
        "interests": ["AI", "Coding", "Hackathons"]
    },
    {
        "id": 7,
        "title": "Digital Literacy Volunteer Session",
        "category": "Volunteering",
        "location": "Community Learning Hub",
        "area": "Gurugram",
        "latitude": 28.4750,
        "longitude": 77.0300,
        "date": "8 November 2026",
        "price": "Free",
        "interests": ["Volunteering", "Technology"]
    }
]


# --------------------------------------------------
# 4. USER INTEREST OPTIONS
# --------------------------------------------------

interest_options = [
    "AI",
    "Python",
    "Coding",
    "Technology",
    "Hackathons",
    "Volunteering",
    "Environment",
    "Entrepreneurship",
    "Networking",
    "Photography",
    "Arts"
]


# --------------------------------------------------
# TOP HORIZONTAL NAVIGATION
# --------------------------------------------------

st.markdown(
    """
    <div style="
        font-size: 28px;
        font-weight: 800;
        color: #A78BFA;
        margin-bottom: 0;
    ">
        📍 NearVibe
    </div>
    """,
    unsafe_allow_html=True
)

st.caption("Discover your community. Find your people.")

page = st.radio(
    "Navigation",
    [
        "Discover Events",
        "My Registrations",
        "Organizer Dashboard",
        "About NearVibe"
    ],
    horizontal=True,
    label_visibility="collapsed",
    key= "nearvibe_navigation"
)

st.divider()

# --------------------------------------------------
# 6. DISCOVER EVENTS PAGE
# --------------------------------------------------

if page == "Discover Events":
        # ----------------------------------------------
    # CROWDPULSE: COMMUNITY EVENT INTELLIGENCE
    # ----------------------------------------------

    registrations = load_registrations()

    event_counts = {
        event["id"]: sum(
            1
            for registration in registrations
            if registration.get("event_id") == event["id"]
        )
        for event in events
    }

    total_registrations = len(registrations)

    events_with_registrations = sum(
        1 for count in event_counts.values() if count > 0
    )

    st.html("""
        <div style="
            background: linear-gradient(120deg, #241044, #102F46);
            border: 1px solid #6D5AE6;
            border-radius: 18px;
            padding: 22px;
            margin-bottom: 18px;
        ">
            <div style="
                color: #5EEAD4;
                font-size: 12px;
                font-weight: 800;
                letter-spacing: 2px;
            ">
                COMMUNITY EVENT INTELLIGENCE
            </div>
            <h2 style="color: #FFFFFF; margin: 8px 0;">
                🔥 CrowdPulse
            </h2>
            <p style="color: #E0E7FF; margin-bottom: 0;">
                Explore community favourites, uncover hidden gems,
                and see which events are attracting registrations.
            </p>
        </div>
    """)

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "📝 Total Registrations",
            total_registrations
        )

    with metric2:
        st.metric(
            "🎯 Events with Registrations",
            events_with_registrations
        )

    with metric3:
        st.metric(
            "📅 Events Listed",
            len(events)
        )

    st.divider()
        # ----------------------------------------------
    # COMMUNITY FAVOURITES AND HIDDEN GEMS
    # ----------------------------------------------

    st.subheader("⭐ Community Favourites & 💎 Hidden Gems")

    registered_events = [
        event for event in events
        if event_counts.get(event["id"], 0) > 0
    ]

    if registered_events:
        community_favourites = sorted(
            registered_events,
            key=lambda event: (
                -event_counts.get(event["id"], 0),
                event["title"].casefold()
            )
        )

        favourite_col, hidden_gem_col = st.columns(2)

        with favourite_col:
            st.markdown("### ⭐ Community Favourites")

            for event in community_favourites[:3]:
                count = event_counts.get(event["id"], 0)

                with st.container(border=True):
                    st.markdown(f"**{event['title']}**")
                    st.caption(f"📍 {event['location']}")
                    st.write(f"📝 {count} registration(s)")

        with hidden_gem_col:
            st.markdown("### 💎 Hidden Gems")

            hidden_gems = sorted(
                [
                    event for event in events
                    if event_counts.get(event["id"], 0) == 0
                ],
                key=lambda event: event["title"].casefold()
            )

            if hidden_gems:
                for event in hidden_gems[:3]:
                    with st.container(border=True):
                        st.markdown(f"**{event['title']}**")
                        st.caption(f"📍 {event['location']}")
                        st.write("✨ Be among the first to register!")
            else:
                st.success(
                    "Every listed event has received a registration!"
                )
    else:
        st.info(
            "Community trends will appear here as people register "
            "for events. Explore the events below to get started!"
        )

    st.divider()
        # ----------------------------------------------
    # COMMUNITY ENGAGEMENT INSIGHT
    # ----------------------------------------------

    st.subheader("📊 Community Insight")

    if total_registrations > 0:
        popular_event = max(
            events,
            key=lambda event: event_counts.get(event["id"], 0)
        )

        popular_count = event_counts.get(popular_event["id"], 0)

        if popular_count > 0:
            st.success(
                f"🏆 **Leading event:** {popular_event['title']} "
                f"has {popular_count} registration(s)."
            )
    else:
        st.info(
            "Community insights will become available "
            "when users start registering for events."
        )
    # Vibrant NearVibe hero section
    st.html(
        """
        <div style="
            background: linear-gradient(
    120deg,
    #1E1245 0%,
    #251653 45%,
    #102E46 100%
);
border: 1px solid rgba(167, 139, 250, 0.45);
box-shadow: 0 8px 32px rgba(124, 58, 237, 0.18);
            border: 1px solid #3B4563;
            padding: 30px;
            border-radius: 22px;
            margin-bottom: 20px;
        ">
            <p style="
                color: #7657F6;
                font-weight: bold;
                letter-spacing: 1px;
            ">
                YOUR CITY. YOUR PEOPLE. YOUR EXPERIENCES.
            </p>

            <h1 style="color: #29234D;">
                Discover Events.<br>
                Find Your Community. 💜
            </h1>

            <p style="
                color: #51496F;
                font-size: 17px;
                line-height: 1.7;
            ">
                Discover workshops, hackathons, creative experiences,
                and volunteering opportunities that match your interests.
            </p>

            <p style="color: #6741D9; font-weight: bold;">
                ✨ Discover locally • 🎯 Explore interests • 🤝 Connect
            </p>
        </div>
        """
    )

    # Event overview
    st.markdown(
        f"### 🌟 Ready to explore? {len(events)} events await you!"
    )

    st.caption(
        "Explore the listings below and find an experience that feels right for you."
    )

    # ----------------------------------------------
    # PERSONALIZED RECOMMENDATIONS
    # ----------------------------------------------

    st.header("✨ Personalized For You")

    st.write(
        "Select your interests to discover events that "
        "match your preferences."
    )

    selected_interests = st.multiselect(
        "What are you interested in?",
        options=interest_options,
        placeholder="Choose one or more interests"
    )

        # --------------------------------------------------
    # PERSONALIZED RECOMMENDATIONS
    # --------------------------------------------------

    st.html(
    """
    <div style="
        background: linear-gradient(120deg, #F0EAFF, #FFF0EC);
        padding: 22px;
        border-radius: 18px;
        margin-top: 20px;
        margin-bottom: 20px;
    ">
        <div style="
            color: #7657F6;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 1px;
        ">
            YOUR PERSONALIZED DISCOVERY
        </div>

        <h2 style="
            color: #29234D !important;
            margin-top: 8px;
            margin-bottom: 8px;
        ">
            💜 Picked for You
        </h2>

        <p style="
            color: #29234D;
            font-size: 16px;
        ">
            Discover experiences selected according to your interests
            and find your next favourite event.
        </p>
    </div>
    """
)

    if selected_interests:

        recommendations = recommend_events(
            events,
            selected_interests
        )

        relevant_events = [
            event
            for event in recommendations
            if event["recommendation_score"] > 0
        ]

        if relevant_events:

            st.success(
                f"✨ We found {len(relevant_events)} events "
                "matching your interests."
            )

            for event in relevant_events:

                with st.container(border=True):

                    # Event title and category
                    st.subheader(
                        f"✨ {event['title']}"
                    )

                    st.caption(
                        f"{event['category']}  •  {event['price']}"
                    )

                    # Location and date
                    col1, col2 = st.columns(2)

                    with col1:
                        st.write("📍 **Location**")
                        st.write(event["location"])

                    with col2:
                        st.write("📅 **Date**")
                        st.write(event["date"])

                    st.divider()

                    # Recommendation score
                    score = event["recommendation_score"]

                    st.write("🎯 **Your interest match**")

                    st.progress(
                        max(0, min(100, int(score)))
                    )

                    st.html(f"""
                        <div style="
                        color: #6741D9;
                        font-size: 18px;
                        font-weight: 800;
                        margin-bottom: 12px;
                           ">
                            {score:.2f}% match
                            </div>
                           """)

                    # Explain why the event was recommended
                    matching = ", ".join(
                        event["matching_interests"]
                    )

                    st.html(f"""
    <div style="
        background: #11182A;
        color: #D7DEEA;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #303B52;
        border-left: 4px solid #A78BFA;
        line-height: 1.6;
        margin-top: 8px;
    ">
        <div style="
            color: #C4B5FD;
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 8px;
        ">
            💡 Why we picked this for you
        </div>

        <div style="color: #D7DEEA;">
            This event matches your interests in:
            <strong style="color: #5EEAD4;">{matching}</strong>.
        </div>
    </div>
""")

        else:

            st.info(
                "💜 We couldn't find an event matching your "
                "selected interests. Try choosing different interests."
            )

    else:

        st.info(
            "🎯 Select your interests above to discover "
            "personalized event recommendations."
        )
    st.divider()

    # ----------------------------------------------
    # GENERAL EVENT DISCOVERY
    # ----------------------------------------------

    st.header("Explore All Events")

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        search_query = st.text_input(
        "Search events",
        placeholder="Try AI, Python, volunteering..."
    )

    with col2:
        selected_category = st.selectbox(
        "Filter by category",
        [
            "All",
            "Technology",
            "Volunteering",
            "Business",
            "Arts"
        ]
    )

    with col3:
        available_areas = sorted({event["area"] for event in events})

    selected_area = st.selectbox(
        "Filter by location",
        ["All Areas"] + available_areas
    )

    filtered_events = []

    for event in events:

        matches_search = (
            search_query.casefold() in event["title"].casefold()
            or search_query.casefold() in event["category"].casefold()
            or search_query.casefold() in event["location"].casefold()
        )

        matches_category = (
    selected_category == "All"
    or event["category"] == selected_category
)

        matches_area = (
    selected_area == "All Areas"
    or event["area"] == selected_area
)

        if matches_search and matches_category and matches_area:
            filtered_events.append(event)

    st.write(
        f"**{len(filtered_events)} events found**"
    )
    st.subheader("🗺️ Explore Events on the Map")
    st.caption(
    "📍 Demo map: markers show illustrative locations around Gurugram, "
    "not verified event venue coordinates."
)

    if filtered_events:
        map_data = [
        {
            "latitude": event["latitude"],
            "longitude": event["longitude"]
        }
        for event in filtered_events
    ]

        st.map(
        map_data,
        latitude="latitude",
        longitude="longitude",
        size=150
    )
    else:
        st.info("No events available to display on the map.")

    if not filtered_events:

        st.info(
            "No events found. Try another search "
            "or select a different category."
        )

    for event in filtered_events:

       with st.container(border=True):

        # Event category and price labels
        st.markdown(
            f"""
            <div style="
                display: inline-block;
                background: #EEE9FF;
                color: #6741D9;
                padding: 5px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 700;
                margin-bottom: 10px;
            ">
                {event['category']}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Event title
        st.subheader(f"✨ {event['title']}")

        # Event details
        col1, col2 = st.columns(2)

        with col1:
            st.write(f"📍 **Location**")
            st.write(event["location"])

        with col2:
            st.write(f"📅 **Date**")
            st.write(event["date"])

        # Price label
        st.markdown(
            f"""
            <div style="
                background: #E1F7F0;
                color: #167D62;
                padding: 8px 12px;
                border-radius: 10px;
                display: inline-block;
                font-weight: 700;
                margin: 8px 0;
            ">
                🎟️ {event['price']}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Event details and registration
        with st.expander("✨ Explore event & register"):

            st.write("**What matches your interests?**")
            st.write(", ".join(event["interests"]))

            st.divider()

            st.subheader("📝 Reserve your spot")

            with st.form(key=f"registration_{event['id']}"):

                name = st.text_input(
                    "Full name",
                    key=f"name_{event['id']}"
                )

                email = st.text_input(
                    "Email address",
                    key=f"email_{event['id']}"
                )

                submitted = st.form_submit_button(
                    "🎉 Register Now",
                    use_container_width=True
                )

                if submitted:

                    if not name.strip() or not email.strip():
                        st.error(
                            "Please enter your name and email."
                        )

                    elif (
                        "@" not in email
                        or "." not in email.split("@")[-1]
                    ):
                        st.error(
                            "Please enter a valid email address."
                        )

                    else:
                        registration = {
                            "event_id": event["id"],
                            "event_title": event["title"],
                            "name": name.strip(),
                            "email": email.strip().casefold()
                        }

                        try:
                            success = save_registration(registration)

                            if success:
                                st.success(
                                    f"🎉 Registration saved for "
                                    f"{event['title']}!"
                                )

                            else:
                                st.warning(
                                    "This email is already registered "
                                    "for this event."
                                )

                        except OSError:
                            st.error(
                                "Registration could not be saved. "
                                "Please try again."
                            )

elif page == "My Registrations":
    st.title("📋 My Registrations")
    st.write("Find the events associated with your registered email address.")

    lookup_email = st.text_input(
        "Enter your registered email address",
        placeholder="you@example.com"
    )

    if st.button("Find My Registrations"):
        if not lookup_email.strip() or (
            "@" not in lookup_email
            or "." not in lookup_email.split("@")[-1]
        ):
            st.error("Please enter a valid-looking email address.")
        else:
            try:
                registrations = load_registrations()

                matching_registrations = [
                    registration
                    for registration in registrations
                    if registration.get("email", "").strip().casefold()
                    == lookup_email.strip().casefold()
                ]

                if matching_registrations:
                    st.success(
                        f"Found {len(matching_registrations)} registration(s)."
                    )

                    for registration in matching_registrations:
                        with st.container(border=True):
                            st.subheader(registration.get("event_title", "Event"))
                            st.write(
                                f"**Registration name:** "
                                f"{registration.get('name', 'Not provided')}"
                            )

                            event = next(
                                (
                                    item for item in events
                                    if item["id"] == registration.get("event_id")
                                ),
                                None
                            )

                            if event:
                                st.write(f"📍 **Location:** {event['location']}")
                                st.write(f"📅 **Date:** {event['date']}")
                else:
                    st.info(
                        "No registrations found for this email address."
                    )

            except (OSError, ValueError):
                st.error("Unable to load registrations. Please try again.")
# --------------------------------------------------
# 7. ORGANIZER DASHBOARD
# --------------------------------------------------

elif page == "Organizer Dashboard":

    st.title("📊 NearVibe Organizer Dashboard")
    st.caption("Monitor events, registrations, and community engagement.")

    # Load registration data
    try:
        registrations = load_registrations()
    except (OSError, ValueError):
        registrations = []
        st.error("Unable to load registration data.")

    # Calculate dashboard statistics
    total_events = len(events)
    total_registrations = len(registrations)

    unique_attendees = len({
        registration.get("email", "").strip().casefold()
        for registration in registrations
        if registration.get("email", "").strip()
    })

    # Count registrations for each event
    event_counts = {}

    for event in events:
        event_counts[event["id"]] = sum(
            1
            for registration in registrations
            if registration.get("event_id") == event["id"]
        )

    # Find the most popular event
    if event_counts and max(event_counts.values()) > 0:
        popular_event_id = max(
            event_counts,
            key=event_counts.get
        )

        popular_event = next(
            (
                event for event in events
                if event["id"] == popular_event_id
            ),
            None
        )

        popular_event_name = (
            popular_event["title"]
            if popular_event
            else "Not available"
        )
    else:
        popular_event_name = "No registrations yet"

    # Dashboard metric cards
    st.subheader("📌 Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📅 Total Events",
            value=total_events
        )

    with col2:
        st.metric(
            label="📝 Total Registrations",
            value=total_registrations
        )

    with col3:
        st.metric(
            label="👥 Unique Attendees",
            value=unique_attendees
        )

    with col4:
        st.metric(
            label="🏆 Most Popular Event",
            value=(
                popular_event_name
                if len(popular_event_name) <= 22
                else popular_event_name[:19] + "..."
            )
        )

    st.divider()

    # Registration chart
    st.subheader("📈 Registrations by Event")

    chart_data = {
        event["title"]: event_counts[event["id"]]
        for event in events
    }

    st.bar_chart(chart_data)

    st.divider()

    # Event-wise registration summary
    st.subheader("📋 Event Performance")

    for event in events:
        count = event_counts[event["id"]]

        with st.container(border=True):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.write(f"**{event['title']}**")
                st.caption(
                    f"📍 {event['location']}  |  📅 {event['date']}"
                )

            with col2:
                st.metric(
                    label="Registrations",
                    value=count
                )

            if count == 0:
                st.caption("💡 No registrations yet.")

    st.divider()

    # Category breakdown
    st.subheader("🗂️ Events by Category")

    category_counts = {}

    for event in events:
        category = event.get("category", "Other")
        category_counts[category] = (
            category_counts.get(category, 0) + 1
        )

    st.bar_chart(category_counts)

    st.caption(
        "Dashboard statistics are calculated from the current "
        "event list and saved registration records."
    )

elif page == "About NearVibe":
    st.write(
        """
        NearVibe is an AI-assisted hyperlocal event discovery
        platform designed to connect people with relevant
        educational, professional, cultural, and community
        opportunities.
        """
    )

    st.subheader("Key Features")

    st.markdown(
        """
        - Personalized event recommendations
        - Interest-based event ranking
        - Explainable recommendation scores
        - Event search and category filtering
        - A foundation for community engagement
        """
    )

    st.subheader("Technology Stack")

    st.markdown(
        """
        - Python
        - Streamlit
        - Custom recommendation algorithm
        - Git and GitHub
        """
    )

    st.subheader("Our Mission")

    st.write(
        "Make discovering meaningful local opportunities "
        "simpler, more relevant, and more accessible."
    )

    st.warning(
        "Hackathon prototype: the events currently use "
        "sample data and have not been verified as real listings."
    )