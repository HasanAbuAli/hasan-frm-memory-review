import streamlit as st
import random

st.set_page_config(
    page_title="Kinda's Shop - What shall I wear today?",
    page_icon="👗",
    layout="centered",
)

st.markdown(
    '''
    <style>
        .main-title {
            text-align: center;
            font-size: 2.3rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1.15rem;
            margin-bottom: 1.4rem;
        }
        .outfit-box {
            border: 2px solid #ddd;
            border-radius: 18px;
            padding: 18px;
            margin-top: 12px;
            text-align: center;
        }
        .small-note {
            text-align: center;
            font-size: 0.9rem;
            opacity: 0.75;
        }
    </style>
    ''',
    unsafe_allow_html=True,
)

st.markdown("<div class='main-title'>👗 Kinda's Shop ✨</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>What shall I wear today? :)</div>", unsafe_allow_html=True)

st.write(
    "Tell me where you're going, choose the style you feel like wearing, "
    "and tell me what you already have in your closet."
)

place = st.selectbox(
    "📍 Where are you going?",
    ["The Mall", "School", "Birthday Party", "Restaurant", "Park", "Travel Day"],
)

style = st.selectbox(
    "💖 What style do you want today?",
    ["Cute", "Casual", "Sporty", "Fancy", "Comfortable"],
)

st.subheader("🧺 What do you have in your closet?")

col1, col2 = st.columns(2)

with col1:
    black_jeans = st.checkbox("Black jeans", value=True)
    blue_jeans = st.checkbox("Blue jeans")
    white_skirt = st.checkbox("White skirt")
    black_skirt = st.checkbox("Black skirt")
    white_top = st.checkbox("White top", value=True)
    pink_top = st.checkbox("Pink top")

with col2:
    hoodie = st.checkbox("Hoodie")
    cardigan = st.checkbox("Cardigan")
    white_sneakers = st.checkbox("White sneakers", value=True)
    black_shoes = st.checkbox("Black shoes")
    sandals = st.checkbox("Sandals")
    small_bag = st.checkbox("Small bag", value=True)

tops = []
bottoms = []
shoes = []
extras = []

if white_top:
    tops.append("🤍 White top")
if pink_top:
    tops.append("🌸 Pink top")
if hoodie:
    tops.append("🧥 Hoodie")
if cardigan:
    extras.append("🧶 Cardigan")

if black_jeans:
    bottoms.append("🖤 Black jeans")
if blue_jeans:
    bottoms.append("💙 Blue jeans")
if white_skirt:
    bottoms.append("🤍 White skirt")
if black_skirt:
    bottoms.append("🖤 Black skirt")

if white_sneakers:
    shoes.append("👟 White sneakers")
if black_shoes:
    shoes.append("👞 Black shoes")
if sandals:
    shoes.append("🩴 Sandals")

if small_bag:
    extras.append("👜 Small bag")

def choose_preferred(options, preferred_words):
    preferred = [item for item in options if any(word.lower() in item.lower() for word in preferred_words)]
    return random.choice(preferred) if preferred else (random.choice(options) if options else None)

def build_outfit(place, style):
    if style == "Sporty":
        top = choose_preferred(tops, ["hoodie", "white top"])
        bottom = choose_preferred(bottoms, ["jeans"])
        shoe = choose_preferred(shoes, ["sneakers"])
    elif style == "Fancy":
        top = choose_preferred(tops, ["white top", "pink top"])
        bottom = choose_preferred(bottoms, ["skirt"])
        shoe = choose_preferred(shoes, ["black shoes", "sandals"])
    elif style == "Cute":
        top = choose_preferred(tops, ["pink top", "white top"])
        bottom = choose_preferred(bottoms, ["skirt", "black jeans"])
        shoe = choose_preferred(shoes, ["white sneakers", "sandals"])
    elif style == "Comfortable":
        top = choose_preferred(tops, ["hoodie", "white top"])
        bottom = choose_preferred(bottoms, ["jeans"])
        shoe = choose_preferred(shoes, ["sneakers", "sandals"])
    else:
        top = random.choice(tops) if tops else None
        bottom = random.choice(bottoms) if bottoms else None
        shoe = random.choice(shoes) if shoes else None

    if place == "School":
        shoe = choose_preferred(shoes, ["sneakers", "black shoes"]) or shoe
    elif place == "Birthday Party":
        bottom = choose_preferred(bottoms, ["skirt", "black jeans"]) or bottom
    elif place == "Park":
        shoe = choose_preferred(shoes, ["sneakers"]) or shoe
    elif place == "Travel Day":
        top = choose_preferred(tops, ["hoodie", "white top"]) or top
        shoe = choose_preferred(shoes, ["sneakers"]) or shoe

    return top, bottom, shoe

if "outfit_seed" not in st.session_state:
    st.session_state.outfit_seed = 0

if st.button("✨ Pick my outfit!"):
    st.session_state.outfit_seed += 1

random.seed(st.session_state.outfit_seed + hash(place + style))

top, bottom, shoe = build_outfit(place, style)

if st.session_state.outfit_seed > 0:
    if not tops or not bottoms or not shoes:
        st.warning(
            "I need at least one top, one bottom, and one pair of shoes. "
            "Tick a few more things you have in your closet 😊"
        )
    else:
        st.markdown("<div class='outfit-box'>", unsafe_allow_html=True)
        st.subheader("🌟 Kinda's Outfit Today")
        st.write(f"**Going to:** {place}")
        st.write(f"**Style:** {style}")
        st.write(f"### {top}")
        st.write(f"### {bottom}")
        st.write(f"### {shoe}")
        if extras:
            st.write("**Optional extra:** " + random.choice(extras))
        st.success("You are ready! 💕")
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("🎲 Give me another outfit"):
            st.session_state.outfit_seed += 1
            st.rerun()

st.divider()
st.markdown(
    "<div class='small-note'>Made with ❤️ for Kinda — Version 1</div>",
    unsafe_allow_html=True,
)
