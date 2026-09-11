import streamlit as st
import random

st.set_page_config(
    page_title="Kinda's Shop - What shall I wear today?",
    page_icon="👗",
    layout="wide",
)

st.markdown(
    '''
    <style>
        .main-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 0.15rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2rem;
            margin-bottom: 1.2rem;
        }
        .small-note {
            text-align: center;
            font-size: 0.9rem;
            opacity: 0.75;
        }
        .look-card {
            border: 1px solid #e7e7e7;
            border-radius: 24px;
            padding: 20px;
            background: linear-gradient(180deg, #fff 0%, #fff7fb 100%);
            box-shadow: 0 8px 24px rgba(0,0,0,0.06);
            text-align: center;
        }
        .look-title {
            font-size: 1.75rem;
            font-weight: 800;
            margin-bottom: 0.25rem;
        }
        .look-subtitle {
            font-size: 1rem;
            opacity: 0.8;
            margin-bottom: 0.7rem;
        }
        .outfit-summary {
            background: #fff0f6;
            border-radius: 18px;
            padding: 14px 16px;
            margin-top: 12px;
            text-align: left;
        }
        .item-pill {
            display: inline-block;
            padding: 7px 12px;
            margin: 4px;
            border-radius: 999px;
            background: #f6f6f6;
            font-size: 0.95rem;
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


def choose_preferred(options, preferred_words, rng):
    preferred = [
        item for item in options
        if any(word.lower() in item.lower() for word in preferred_words)
    ]
    return rng.choice(preferred) if preferred else (rng.choice(options) if options else None)


def build_outfit(place, style, rng):
    if style == "Sporty":
        top = choose_preferred(tops, ["hoodie", "white top"], rng)
        bottom = choose_preferred(bottoms, ["jeans"], rng)
        shoe = choose_preferred(shoes, ["sneakers"], rng)
    elif style == "Fancy":
        top = choose_preferred(tops, ["white top", "pink top"], rng)
        bottom = choose_preferred(bottoms, ["skirt"], rng)
        shoe = choose_preferred(shoes, ["black shoes", "sandals"], rng)
    elif style == "Cute":
        top = choose_preferred(tops, ["pink top", "white top"], rng)
        bottom = choose_preferred(bottoms, ["skirt", "black jeans"], rng)
        shoe = choose_preferred(shoes, ["white sneakers", "sandals"], rng)
    elif style == "Comfortable":
        top = choose_preferred(tops, ["hoodie", "white top"], rng)
        bottom = choose_preferred(bottoms, ["jeans"], rng)
        shoe = choose_preferred(shoes, ["sneakers", "sandals"], rng)
    else:
        top = rng.choice(tops) if tops else None
        bottom = rng.choice(bottoms) if bottoms else None
        shoe = rng.choice(shoes) if shoes else None

    if place == "School":
        shoe = choose_preferred(shoes, ["sneakers", "black shoes"], rng) or shoe
    elif place == "Birthday Party":
        bottom = choose_preferred(bottoms, ["skirt", "black jeans"], rng) or bottom
    elif place == "Park":
        shoe = choose_preferred(shoes, ["sneakers"], rng) or shoe
    elif place == "Travel Day":
        top = choose_preferred(tops, ["hoodie", "white top"], rng) or top
        shoe = choose_preferred(shoes, ["sneakers"], rng) or shoe

    extra = rng.choice(extras) if extras else None
    return top, bottom, shoe, extra


def outfit_avatar_svg(top, bottom, shoe, extra):
    top_l = top.lower()
    bottom_l = bottom.lower()
    shoe_l = shoe.lower()
    extra_l = (extra or "").lower()

    top_color = "#ffffff"
    top_stroke = "#d7d7d7"
    if "pink" in top_l:
        top_color = "#f7a8c4"
        top_stroke = "#dd7da2"
    elif "hoodie" in top_l:
        top_color = "#d9c8f2"
        top_stroke = "#aa92cc"

    bottom_color = "#252525"
    if "blue" in bottom_l:
        bottom_color = "#6487b4"
    elif "white" in bottom_l:
        bottom_color = "#f5f5f5"

    shoe_color = "#ffffff" if "white" in shoe_l else "#242424"
    shoe_stroke = "#cfcfcf" if "white" in shoe_l else "#111111"

    is_skirt = "skirt" in bottom_l
    is_hoodie = "hoodie" in top_l
    has_bag = "bag" in extra_l
    has_cardigan = "cardigan" in extra_l

    if is_skirt:
        bottom_shape = f'''
        <path d="M126 252 L194 252 L210 330 L110 330 Z" fill="{bottom_color}" stroke="#333" stroke-width="2"/>
        <rect x="126" y="329" width="24" height="95" rx="12" fill="#f1c8ae"/>
        <rect x="170" y="329" width="24" height="95" rx="12" fill="#f1c8ae"/>
        '''
    else:
        bottom_shape = f'''
        <path d="M122 252 L158 252 L154 425 L120 425 Z" fill="{bottom_color}" stroke="#222" stroke-width="2"/>
        <path d="M162 252 L198 252 L200 425 L166 425 Z" fill="{bottom_color}" stroke="#222" stroke-width="2"/>
        '''

    if is_hoodie:
        top_shape = f'''
        <path d="M120 150 Q160 126 200 150 L205 260 L115 260 Z" fill="{top_color}" stroke="{top_stroke}" stroke-width="2"/>
        <path d="M118 158 Q96 178 92 238" fill="none" stroke="{top_color}" stroke-width="24" stroke-linecap="round"/>
        <path d="M202 158 Q224 178 228 238" fill="none" stroke="{top_color}" stroke-width="24" stroke-linecap="round"/>
        <path d="M138 150 Q160 176 182 150" fill="none" stroke="{top_stroke}" stroke-width="2"/>
        '''
    else:
        top_shape = f'''
        <path d="M122 150 Q160 132 198 150 L194 254 L126 254 Z" fill="{top_color}" stroke="{top_stroke}" stroke-width="2"/>
        <path d="M123 158 Q106 172 104 211" fill="none" stroke="{top_color}" stroke-width="20" stroke-linecap="round"/>
        <path d="M197 158 Q214 172 216 211" fill="none" stroke="{top_color}" stroke-width="20" stroke-linecap="round"/>
        '''

    cardigan_shape = ""
    if has_cardigan:
        cardigan_shape = '''
        <path d="M119 151 Q105 170 104 254" fill="none" stroke="#e7d4bd" stroke-width="16" stroke-linecap="round" opacity="0.95"/>
        <path d="M201 151 Q215 170 216 254" fill="none" stroke="#e7d4bd" stroke-width="16" stroke-linecap="round" opacity="0.95"/>
        '''

    bag_shape = ""
    if has_bag:
        bag_shape = '''
        <path d="M195 174 Q236 224 218 296" fill="none" stroke="#282828" stroke-width="5"/>
        <rect x="199" y="278" width="45" height="38" rx="8" fill="#222"/>
        <circle cx="221" cy="292" r="3" fill="#d8b25e"/>
        '''

    return f'''
    <svg viewBox="0 0 320 500" width="100%" style="max-width:340px;margin:auto;display:block;">
        <defs>
            <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#fff8fb"/>
                <stop offset="100%" stop-color="#fff0f6"/>
            </linearGradient>
        </defs>
        <rect x="12" y="10" width="296" height="478" rx="30" fill="url(#bg)"/>
        <circle cx="160" cy="98" r="44" fill="#f1c8ae"/>
        <path d="M116 98 Q112 42 160 42 Q210 42 205 106 Q188 72 153 70 Q132 72 116 98" fill="#4c352e"/>
        <path d="M119 88 Q108 116 121 142" fill="none" stroke="#4c352e" stroke-width="15" stroke-linecap="round"/>
        <path d="M201 88 Q212 116 199 142" fill="none" stroke="#4c352e" stroke-width="15" stroke-linecap="round"/>
        <circle cx="145" cy="100" r="3" fill="#333"/>
        <circle cx="175" cy="100" r="3" fill="#333"/>
        <path d="M151 117 Q160 124 169 117" fill="none" stroke="#b76e79" stroke-width="2.5" stroke-linecap="round"/>
        <circle cx="132" cy="111" r="7" fill="#f3a5b3" opacity="0.35"/>
        <circle cx="188" cy="111" r="7" fill="#f3a5b3" opacity="0.35"/>
        <rect x="150" y="135" width="20" height="22" rx="8" fill="#f1c8ae"/>
        {top_shape}
        {cardigan_shape}
        {bottom_shape}
        <rect x="113" y="421" width="45" height="24" rx="10" fill="{shoe_color}" stroke="{shoe_stroke}" stroke-width="2"/>
        <rect x="162" y="421" width="45" height="24" rx="10" fill="{shoe_color}" stroke="{shoe_stroke}" stroke-width="2"/>
        {bag_shape}
        <text x="35" y="65" font-size="24">💕</text>
        <text x="245" y="95" font-size="22">✨</text>
        <text x="35" y="455" font-size="20">🌸</text>
    </svg>
    '''


if "outfit_seed" not in st.session_state:
    st.session_state.outfit_seed = 0

if st.button("✨ Pick my outfit!", use_container_width=True):
    st.session_state.outfit_seed += 1

if st.session_state.outfit_seed > 0:
    if not tops or not bottoms or not shoes:
        st.warning(
            "I need at least one top, one bottom, and one pair of shoes. "
            "Tick a few more things you have in your closet 😊"
        )
    else:
        seed = st.session_state.outfit_seed + sum(ord(c) for c in (place + style))
        rng = random.Random(seed)
        top, bottom, shoe, extra = build_outfit(place, style, rng)

        st.divider()
        left_result, right_result = st.columns([1.05, 0.95], gap="large")

        with left_result:
            st.markdown(
                f"""
                <div class='look-card'>
                    <div class='look-title'>🧥 Your Look Today</div>
                    <div class='look-subtitle'>Here's your {style.lower()} outfit for {place.lower()}! 💕</div>
                    {outfit_avatar_svg(top, bottom, shoe, extra)}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with right_result:
            st.subheader("✨ Outfit Details")
            st.markdown(f"<span class='item-pill'>{top}</span>", unsafe_allow_html=True)
            st.markdown(f"<span class='item-pill'>{bottom}</span>", unsafe_allow_html=True)
            st.markdown(f"<span class='item-pill'>{shoe}</span>", unsafe_allow_html=True)
            if extra:
                st.markdown(f"<span class='item-pill'>{extra}</span>", unsafe_allow_html=True)

            extra_text = f" Add {extra.split(' ', 1)[1]} for the final touch." if extra else ""
            st.markdown(
                f"""
                <div class='outfit-summary'>
                    <b>💗 Outfit Summary</b><br><br>
                    A {style.lower()} look for {place.lower()}! Your {top.split(' ', 1)[1].lower()} and
                    {bottom.split(' ', 1)[1].lower()} make a lovely combination, and
                    {shoe.split(' ', 1)[1].lower()} finish the look.{extra_text}
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.success(f"You are ready for {place.lower()}! 💕")

            if st.button("🎲 Give me another outfit", use_container_width=True):
                st.session_state.outfit_seed += 1
                st.rerun()

st.divider()
st.markdown(
    "<div class='small-note'>Made with ❤️ for Kinda — Version 2 ✨</div>",
    unsafe_allow_html=True,
)
