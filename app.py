from flask import Flask, render_template, request

# ✅ Clean import (no duplicates)
from analyzer import (
    split_speakers,
    sentiment_analysis,
    extract_keywords,
    argument_strength,
    extract_topics,
    calculate_winner
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text = ""   # store input text

    if request.method == "POST":
        text = request.form.get("debate", "")  # safer way

        if text.strip():  # ✅ avoid empty input
            speakers = split_speakers(text)
            sentiment = sentiment_analysis(speakers)
            keywords = extract_keywords(text)
            strength = argument_strength(speakers)
            topics = extract_topics(text)
            winner, scores = calculate_winner(sentiment, strength)

            result = {
                "speakers": list(speakers.keys()),
                "sentiment": sentiment,
                "keywords": keywords,
                "strength": strength,
                "topics": topics,
                "winner": winner,
                "scores": scores
            }

    return render_template("index.html", result=result, text=text)



if __name__ == "__main__":
    app.run(debug=True)