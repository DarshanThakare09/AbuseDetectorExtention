from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🔹 EXTENDED ABUSIVE WORD LIST (English + Indian Languages)
ABUSIVE_WORDS = set([
    # ✅ English abusive words
    "idiot", "stupid", "dumb", "moron", "loser", "clown", "pathetic", "trash",
    "worthless", "suck", "shut up", "ugly", "annoying", "disgusting", "failure",
    "nonsense", "awful", "terrible", "lame", "hopeless", "hate", "kill yourself",
    "dumbass", "jackass", "bullshit", "shithead", "piss off", "asshole",
    "bastard", "bitch", "fuck", "motherfucker", "cunt", "dickhead", "prick",
    "slut", "whore", "cock", "retard", "freak", "screw you", "son of a bitch",
    "pussy", "motherfuck", "douchebag", "arsehole", "twat", "scumbag", "dick",

    # ✅ Hindi abusive words
    "LAWDA=","chutiya", "bhosdike", "madarchod", "behenchod", "gandu", "randi", "bhen ke lode",
    "gaand", "kutte", "harami", "kamina", "nalayak", "chakka", "bhadwa", "bakchod",
    "saala", "kutta", "jhantu", "chodu", "gaand mara", "kaminey", "bkl", "bc", "mc","nice","LAWDA","lawda",

    # ✅ Tamil abusive words
    "thevdiya", "munda", "poda", "mokkai", "pannada", "sombu", "thelvi",
    "thiruttu", "thevdiya paya", "sooda", "thambi", "muttal", "kudiyan",

    # ✅ Telugu abusive words
    "lanja", "dengudu", "vedhava", "puka", "nakodaka", "gampa", "aapu",
    "donga", "pichoda", "pichakunda", "mukka", "nee amma", "nayala kodaka",

    # ✅ Bengali abusive words
    "haraamjada", "khankir chele", "bokachoda", "banchod", "chodu", "maa ke loda",
    "shyala", "ghanta", "khoti", "gaan mara", "khankir put", "kaal boka",

    # ✅ Marathi abusive words
    "bhadwa", "chutiya", "gaand mara", "lavde", "ghanta", "chikya", "hukya",
    "bhosda", "lavdya", "chootiya", "bhikari", "kadva", "jhatka",

    # ✅ Punjabi abusive words
    "bhen di lodi", "tati", "chutia", "haraamkhor", "lodu", "makhichoos",
    "khoteya", "kamina", "pataka", "phuddu", "khotta", "lath maran",

    # ✅ Malayalam abusive words
    "thendi", "mone", "patti", "thayoli", "thirutha", "kolla", "pundachi",
    "pundamone", "kundi", "nari", "kalathinte", "mone",

    # ✅ Kannada abusive words
    "soole", "saala", "pombatt", "mund", "kirik", "gandu", "hulmagaa",
    "baddi", "thale", "pale", "mukya", "kalape",

    # ✅ Urdu abusive words
    "haramzada", "kutta", "kamina", "beghairat", "kanjar", "charsi", "nashedi",
    "khotay ka putar", "badtameez", "bakwas", "luchha", "tind", "bewaqoof",

    # ✅ Gujarati abusive words
    "bhosdiwala", "gando", "chhinal", "lavdya", "salo", "kamino", "bhocho",
    "gandu", "kutta", "thobdo", "chhapri", "chhapda"
])

# Function to check for abusive words
def contains_abusive_words(text):
    words = text.lower().split()  # Convert text to lowercase & split into words
    for word in words:
        if word in ABUSIVE_WORDS:
            return True
    return False

# API endpoint to detect abusive words
@app.route('/detect', methods=['POST'])
def detect_abuse():
    data = request.get_json()
    text = data.get("text", "")

    if contains_abusive_words(text):
        return jsonify({"abusive": True})
    else:
        return jsonify({"abusive": False})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
