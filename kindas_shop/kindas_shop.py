import random
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Kinda's Shop - What shall I wear today?",
    page_icon="👗",
    layout="wide",
)

# -----------------------------
# TRANSLATIONS
# -----------------------------
T = {
    "English": {
        "title": "👗 Kinda's Shop ✨",
        "subtitle": "What shall I wear today? :)",
        "intro": "Tell me where you're going, choose your mood, and tell me what you have in your closet.",
        "where": "📍 Where are you going?",
        "style": "💖 What style do you want today?",
        "closet": "🧺 What do you have in your closet?",
        "pick": "✨ Pick my outfit!",
        "again": "🎲 Give me another outfit",
        "need": "Please choose at least one top, one bottom, and one pair of shoes 😊",
        "look": "👗 Your Look Today",
        "details": "✨ Outfit Details",
        "score": "Kinda Style Score",
        "ready": "You are ready! 💕",
        "footer": "Made with ❤️ for Kinda — Version 4",
        "summary": "A fun look made from the clothes you already have. Mix, match, and make it yours! ✨",
        "lang": "Language / اللغة",
    },
    "العربية": {
        "title": "👗 متجر كيندا ✨",
        "subtitle": "ماذا أرتدي اليوم؟ :)",
        "intro": "قولي لي إلى أين ستذهبين، اختاري الستايل، وحددي الملابس الموجودة في خزانتك.",
        "where": "📍 إلى أين ستذهبين؟",
        "style": "💖 ما الستايل الذي تريدينه اليوم؟",
        "closet": "🧺 ماذا يوجد في خزانتك؟",
        "pick": "✨ اختاري لي ملابسي!",
        "again": "🎲 أعطني إطلالة أخرى",
        "need": "اختاري على الأقل قطعة علوية وقطعة سفلية وحذاء 😊",
        "look": "👗 إطلالتك اليوم",
        "details": "✨ تفاصيل الإطلالة",
        "score": "تقييم إطلالة كيندا",
        "ready": "أنتِ جاهزة! 💕",
        "footer": "صُنع بكل ❤️ من أجل كيندا — الإصدار 4",
        "summary": "إطلالة لطيفة من الملابس الموجودة لديكِ بالفعل. امزجي القطع بطريقتك الخاصة! ✨",
        "lang": "Language / اللغة",
    },
}

PLACE_LABELS = {
    "The Mall": {"English": "The Mall", "العربية": "المول"},
    "School": {"English": "School", "العربية": "المدرسة"},
    "Birthday Party": {"English": "Birthday Party", "العربية": "حفلة عيد ميلاد"},
    "Restaurant": {"English": "Restaurant", "العربية": "مطعم"},
    "Park": {"English": "Park", "العربية": "الحديقة"},
    "Travel Day": {"English": "Travel Day", "العربية": "يوم سفر"},
}

STYLE_LABELS = {
    "Cute": {"English": "Cute", "العربية": "لطيف"},
    "Casual": {"English": "Casual", "العربية": "كاجوال"},
    "Sporty": {"English": "Sporty", "العربية": "رياضي"},
    "Fancy": {"English": "Fancy", "العربية": "أنيق"},
    "Comfortable": {"English": "Comfortable", "العربية": "مريح"},
}

ITEM_LABELS = {
    "White top": {"English": "White top", "العربية": "بلوزة بيضاء"},
    "Pink top": {"English": "Pink top", "العربية": "بلوزة وردية"},
    "Lavender top": {"English": "Lavender top", "العربية": "بلوزة بنفسجية فاتحة"},
    "Hoodie": {"English": "Hoodie", "العربية": "هودي"},
    "Cardigan": {"English": "Cardigan", "العربية": "كارديغان"},
    "Denim jacket": {"English": "Denim jacket", "العربية": "جاكيت جينز"},
    "Black jeans": {"English": "Black jeans", "العربية": "جينز أسود"},
    "Blue jeans": {"English": "Blue jeans", "العربية": "جينز أزرق"},
    "Beige trousers": {"English": "Beige trousers", "العربية": "بنطال بيج"},
    "White skirt": {"English": "White skirt", "العربية": "تنورة بيضاء"},
    "Black skirt": {"English": "Black skirt", "العربية": "تنورة سوداء"},
    "Pink skirt": {"English": "Pink skirt", "العربية": "تنورة وردية"},
    "White sneakers": {"English": "White sneakers", "العربية": "سنيكرز أبيض"},
    "Black shoes": {"English": "Black shoes", "العربية": "حذاء أسود"},
    "Sandals": {"English": "Sandals", "العربية": "صندل"},
    "Boots": {"English": "Boots", "العربية": "بوت"},
    "Small bag": {"English": "Small bag", "العربية": "حقيبة صغيرة"},
    "Cap": {"English": "Cap", "العربية": "قبعة"},
}

EMOJI = {
    "White top": "🤍", "Pink top": "🌸", "Lavender top": "💜", "Hoodie": "🧥",
    "Cardigan": "🧶", "Denim jacket": "🩵", "Black jeans": "🖤", "Blue jeans": "💙",
    "Beige trousers": "🤎", "White skirt": "🤍", "Black skirt": "🖤", "Pink skirt": "🌷",
    "White sneakers": "👟", "Black shoes": "👞", "Sandals": "🩴", "Boots": "🥾",
    "Small bag": "👜", "Cap": "🧢",
}

# -----------------------------
# STYLING
# -----------------------------
st.markdown(
    """
    <style>
        .block-container {max-width: 1100px; padding-top: 1.2rem;}
        .main-title {text-align:center;font-size:2.55rem;font-weight:850;margin-bottom:0.1rem;}
        .subtitle {text-align:center;font-size:1.15rem;opacity:.75;margin-bottom:1rem;}
        .look-card {border:1px solid #eee;border-radius:24px;padding:18px;background:linear-gradient(180deg,#fff,#fff6fb);box-shadow:0 8px 24px rgba(0,0,0,.05);}
        .pill {display:inline-block;padding:7px 12px;margin:4px;border-radius:999px;background:#f5f5f5;font-size:.95rem;}
        .score-box {border-radius:18px;padding:14px 16px;background:#fff0f6;margin-top:12px;}
        .footer {text-align:center;opacity:.65;font-size:.9rem;margin-top:2rem;}
        @media (max-width: 700px) {
            .main-title {font-size:2rem;}
            .block-container {padding-left:1rem;padding-right:1rem;}
        }
    </style>
    """,
    unsafe_allow_html=True,
)

language = st.radio("Language / اللغة", ["English", "العربية"], horizontal=True)
t = T[language]

st.markdown(f"<div class='main-title'>{t['title']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>{t['subtitle']}</div>", unsafe_allow_html=True)
st.write(t["intro"])

# -----------------------------
# HELPERS
# -----------------------------
def label_item(item):
    return f"{EMOJI.get(item, '')} {ITEM_LABELS[item][language]}"


def choose_preferred(available, preferences, rng):
    preferred = [x for x in preferences if x in available]
    if preferred:
        return rng.choice(preferred)
    return rng.choice(available) if available else None


def build_outfit(place, style, tops, bottoms, shoes, extras, rng):
    top_preferences = {
        "Cute": ["Pink top", "Lavender top", "White top", "Cardigan"],
        "Casual": ["White top", "Lavender top", "Pink top", "Hoodie"],
        "Sporty": ["Hoodie", "White top", "Lavender top"],
        "Fancy": ["White top", "Pink top", "Lavender top", "Cardigan"],
        "Comfortable": ["Hoodie", "White top", "Cardigan"],
    }[style]

    bottom_preferences = {
        "Cute": ["Pink skirt", "White skirt", "Black skirt", "Blue jeans"],
        "Casual": ["Blue jeans", "Black jeans", "Beige trousers"],
        "Sporty": ["Black jeans", "Blue jeans", "Beige trousers"],
        "Fancy": ["Black skirt", "White skirt", "Pink skirt", "Beige trousers"],
        "Comfortable": ["Blue jeans", "Beige trousers", "Black jeans"],
    }[style]

    shoe_preferences = {
        "Cute": ["White sneakers", "Sandals", "Black shoes"],
        "Casual": ["White sneakers", "Boots", "Sandals"],
        "Sporty": ["White sneakers", "Boots"],
        "Fancy": ["Black shoes", "Sandals", "Boots"],
        "Comfortable": ["White sneakers", "Sandals"],
    }[style]

    # Place-specific nudges
    if place == "School":
        shoe_preferences = ["White sneakers", "Black shoes"] + shoe_preferences
    elif place == "Park":
        shoe_preferences = ["White sneakers", "Boots"] + shoe_preferences
    elif place == "Birthday Party":
        bottom_preferences = ["Pink skirt", "White skirt", "Black skirt"] + bottom_preferences
    elif place == "Travel Day":
        top_preferences = ["Hoodie", "Cardigan", "White top"] + top_preferences
        shoe_preferences = ["White sneakers", "Boots"] + shoe_preferences
    elif place == "Restaurant":
        top_preferences = ["White top", "Pink top", "Lavender top"] + top_preferences
        bottom_preferences = ["Black skirt", "Beige trousers", "White skirt"] + bottom_preferences

    top = choose_preferred(tops, top_preferences, rng)
    bottom = choose_preferred(bottoms, bottom_preferences, rng)
    shoe = choose_preferred(shoes, shoe_preferences, rng)

    extra = None
    if extras:
        extra_preferences = ["Small bag", "Denim jacket", "Cardigan", "Cap"]
        if style == "Sporty":
            extra_preferences = ["Cap", "Denim jacket", "Small bag"]
        elif style == "Fancy":
            extra_preferences = ["Small bag", "Cardigan", "Denim jacket"]
        extra = choose_preferred(extras, extra_preferences, rng)

    return top, bottom, shoe, extra


def style_score(style, top, bottom, shoe, extra):
    score = 3
    joined = " ".join(x or "" for x in [top, bottom, shoe, extra]).lower()
    if style == "Cute" and any(x in joined for x in ["pink", "skirt", "lavender"]):
        score += 1
    if style == "Sporty" and any(x in joined for x in ["hoodie", "sneakers", "cap"]):
        score += 1
    if style == "Fancy" and any(x in joined for x in ["skirt", "black shoes", "small bag"]):
        score += 1
    if style == "Comfortable" and any(x in joined for x in ["hoodie", "sneakers", "trousers"]):
        score += 1
    if style == "Casual" and any(x in joined for x in ["jeans", "sneakers", "denim"]):
        score += 1
    if extra:
        score += 1
    return min(score, 5)


def outfit_colors(top, bottom, shoe, extra):
    top_map = {
        "White top": "#ffffff", "Pink top": "#f7a8c4", "Lavender top": "#cbb8ef",
        "Hoodie": "#c9b7e8", "Cardigan": "#e8d5bf"
    }
    bottom_map = {
        "Black jeans": "#252525", "Blue jeans": "#5f7fa8", "Beige trousers": "#cbb797",
        "White skirt": "#f7f7f7", "Black skirt": "#222222", "Pink skirt": "#e996b6"
    }
    shoe_map = {
        "White sneakers": "#ffffff", "Black shoes": "#222222", "Sandals": "#d5b08a", "Boots": "#7d5b46"
    }
    outer_map = {"Denim jacket": "#6e97c7", "Cardigan": "#e8d5bf"}
    return (
        top_map.get(top, "#ffffff"),
        bottom_map.get(bottom, "#333333"),
        shoe_map.get(shoe, "#ffffff"),
        outer_map.get(extra, "none"),
    )


def avatar_html(top, bottom, shoe, extra):
    top_color, bottom_color, shoe_color, outer_color = outfit_colors(top, bottom, shoe, extra)
    is_skirt = "skirt" in bottom.lower()
    has_bag = extra == "Small bag"
    has_cap = extra == "Cap"
    has_outer = extra in ["Denim jacket", "Cardigan"]

    skirt_or_pants = (
        f'<path d="M112 275 L208 275 L220 350 L100 350 Z" fill="{bottom_color}" stroke="#333" stroke-width="2"/>'
        f'<rect x="121" y="350" width="28" height="100" rx="13" fill="#f1c8ae"/>'
        f'<rect x="171" y="350" width="28" height="100" rx="13" fill="#f1c8ae"/>'
        if is_skirt else
        f'<path d="M115 275 L158 275 L154 448 L112 448 Z" fill="{bottom_color}" stroke="#222" stroke-width="2"/>'
        f'<path d="M162 275 L205 275 L208 448 L166 448 Z" fill="{bottom_color}" stroke="#222" stroke-width="2"/>'
    )

    bag = ""
    if has_bag:
        bag = '''
        <path d="M198 195 Q242 245 225 324" fill="none" stroke="#2a2a2a" stroke-width="5"/>
        <rect x="204" y="305" width="48" height="40" rx="8" fill="#252525"/>
        <circle cx="228" cy="318" r="3" fill="#d8b25e"/>
        '''

    cap = ""
    if has_cap:
        cap = '''
        <path d="M116 76 Q160 42 204 76 L200 93 Q160 72 120 93 Z" fill="#e89db6"/>
        <path d="M191 88 Q220 88 226 98 Q204 103 190 96 Z" fill="#e89db6"/>
        '''

    outer = ""
    if has_outer:
        outer = f'''
        <path d="M119 169 Q101 190 99 270" fill="none" stroke="{outer_color}" stroke-width="18" stroke-linecap="round" opacity=".95"/>
        <path d="M201 169 Q219 190 221 270" fill="none" stroke="{outer_color}" stroke-width="18" stroke-linecap="round" opacity=".95"/>
        <path d="M123 166 L142 272" stroke="{outer_color}" stroke-width="13" stroke-linecap="round" opacity=".9"/>
        <path d="M197 166 L178 272" stroke="{outer_color}" stroke-width="13" stroke-linecap="round" opacity=".9"/>
        '''

    html = f'''
    <div style="display:flex;justify-content:center;align-items:center;width:100%;">
    <svg viewBox="0 0 320 540" style="width:100%;max-width:390px;height:auto;display:block;">
        <defs>
          <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#fff8fb"/>
            <stop offset="100%" stop-color="#f8f2ff"/>
          </linearGradient>
        </defs>
        <rect x="10" y="8" width="300" height="520" rx="32" fill="url(#bg)"/>
        <text x="30" y="55" font-size="24">💕</text>
        <text x="255" y="70" font-size="22">✨</text>
        <text x="250" y="470" font-size="20">🌸</text>

        <!-- hair -->
        <ellipse cx="160" cy="105" rx="58" ry="63" fill="#49342e"/>
        <!-- face -->
        <circle cx="160" cy="105" r="43" fill="#f1c8ae"/>
        <path d="M117 102 Q116 50 160 47 Q207 47 204 108 Q186 77 154 76 Q135 76 117 102" fill="#49342e"/>
        <path d="M120 97 Q108 132 122 157" fill="none" stroke="#49342e" stroke-width="16" stroke-linecap="round"/>
        <path d="M200 97 Q212 132 198 157" fill="none" stroke="#49342e" stroke-width="16" stroke-linecap="round"/>
        {cap}
        <circle cx="145" cy="107" r="3.5" fill="#333"/>
        <circle cx="175" cy="107" r="3.5" fill="#333"/>
        <path d="M151 124 Q160 132 169 124" fill="none" stroke="#b76e79" stroke-width="3" stroke-linecap="round"/>
        <circle cx="132" cy="118" r="7" fill="#f3a5b3" opacity=".35"/>
        <circle cx="188" cy="118" r="7" fill="#f3a5b3" opacity=".35"/>
        <rect x="149" y="145" width="22" height="24" rx="9" fill="#f1c8ae"/>

        <!-- top -->
        <path d="M119 166 Q160 145 201 166 L197 278 L123 278 Z" fill="{top_color}" stroke="#cfcfcf" stroke-width="2"/>
        <path d="M121 176 Q102 193 101 236" fill="none" stroke="{top_color}" stroke-width="21" stroke-linecap="round"/>
        <path d="M199 176 Q218 193 219 236" fill="none" stroke="{top_color}" stroke-width="21" stroke-linecap="round"/>
        {outer}
        {skirt_or_pants}

        <!-- shoes -->
        <rect x="103" y="447" width="57" height="27" rx="11" fill="{shoe_color}" stroke="#777" stroke-width="1.5"/>
        <rect x="160" y="447" width="57" height="27" rx="11" fill="{shoe_color}" stroke="#777" stroke-width="1.5"/>
        {bag}

        <!-- little floor shadow -->
        <ellipse cx="160" cy="488" rx="85" ry="11" fill="#d9d2d8" opacity=".35"/>
    </svg>
    </div>
    '''
    return html

# -----------------------------
# INPUTS
# -----------------------------
place_keys = list(PLACE_LABELS.keys())
style_keys = list(STYLE_LABELS.keys())

place = st.selectbox(t["where"], place_keys, format_func=lambda x: PLACE_LABELS[x][language])
style = st.selectbox(t["style"], style_keys, format_func=lambda x: STYLE_LABELS[x][language])

st.subheader(t["closet"])

c1, c2, c3 = st.columns(3)

with c1:
    white_top = st.checkbox(label_item("White top"), value=True)
    pink_top = st.checkbox(label_item("Pink top"))
    lavender_top = st.checkbox(label_item("Lavender top"))
    hoodie = st.checkbox(label_item("Hoodie"))
    cardigan = st.checkbox(label_item("Cardigan"))
    denim_jacket = st.checkbox(label_item("Denim jacket"))

with c2:
    black_jeans = st.checkbox(label_item("Black jeans"), value=True)
    blue_jeans = st.checkbox(label_item("Blue jeans"))
    beige_trousers = st.checkbox(label_item("Beige trousers"))
    white_skirt = st.checkbox(label_item("White skirt"))
    black_skirt = st.checkbox(label_item("Black skirt"))
    pink_skirt = st.checkbox(label_item("Pink skirt"))

with c3:
    white_sneakers = st.checkbox(label_item("White sneakers"), value=True)
    black_shoes = st.checkbox(label_item("Black shoes"))
    sandals = st.checkbox(label_item("Sandals"))
    boots = st.checkbox(label_item("Boots"))
    small_bag = st.checkbox(label_item("Small bag"), value=True)
    cap = st.checkbox(label_item("Cap"))

selected = {
    "White top": white_top,
    "Pink top": pink_top,
    "Lavender top": lavender_top,
    "Hoodie": hoodie,
    "Cardigan": cardigan,
    "Denim jacket": denim_jacket,
    "Black jeans": black_jeans,
    "Blue jeans": blue_jeans,
    "Beige trousers": beige_trousers,
    "White skirt": white_skirt,
    "Black skirt": black_skirt,
    "Pink skirt": pink_skirt,
    "White sneakers": white_sneakers,
    "Black shoes": black_shoes,
    "Sandals": sandals,
    "Boots": boots,
    "Small bag": small_bag,
    "Cap": cap,
}

tops = [x for x in ["White top", "Pink top", "Lavender top", "Hoodie", "Cardigan"] if selected[x]]
bottoms = [x for x in ["Black jeans", "Blue jeans", "Beige trousers", "White skirt", "Black skirt", "Pink skirt"] if selected[x]]
shoes = [x for x in ["White sneakers", "Black shoes", "Sandals", "Boots"] if selected[x]]
extras = [x for x in ["Small bag", "Denim jacket", "Cardigan", "Cap"] if selected[x]]

if "outfit_seed" not in st.session_state:
    st.session_state.outfit_seed = 0

if st.button(t["pick"], use_container_width=True):
    st.session_state.outfit_seed += 1

# -----------------------------
# RESULT
# -----------------------------
if st.session_state.outfit_seed > 0:
    if not tops or not bottoms or not shoes:
        st.warning(t["need"])
    else:
        rng = random.Random(st.session_state.outfit_seed + sum(ord(c) for c in place + style))
        top, bottom, shoe, extra = build_outfit(place, style, tops, bottoms, shoes, extras, rng)
        score = style_score(style, top, bottom, shoe, extra)

        st.divider()
        left, right = st.columns([1.05, 0.95], gap="large")

        with left:
            st.markdown(f"<div class='look-card'><h2 style='text-align:center'>{t['look']}</h2></div>", unsafe_allow_html=True)
            components.html(avatar_html(top, bottom, shoe, extra), height=570, scrolling=False)

        with right:
            st.subheader(t["details"])
            for item in [top, bottom, shoe] + ([extra] if extra else []):
                st.markdown(f"<span class='pill'>{EMOJI.get(item,'')} {ITEM_LABELS[item][language]}</span>", unsafe_allow_html=True)

            stars = "⭐" * score + "☆" * (5 - score)
            st.markdown(
                f"<div class='score-box'><b>{t['score']}</b><br><span style='font-size:1.45rem'>{stars}</span><br><br>{t['summary']}</div>",
                unsafe_allow_html=True,
            )
            st.success(t["ready"])

            if st.button(t["again"], use_container_width=True):
                st.session_state.outfit_seed += 1
                st.rerun()

st.markdown(f"<div class='footer'>{t['footer']}</div>", unsafe_allow_html=True)
