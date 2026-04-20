import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy

# Load models
sia = SentimentIntensityAnalyzer()
nlp = spacy.load("en_core_web_sm")


# 🔹 1. Split Speakers
def split_speakers(text):
    speakers = {}
    lines = text.split("\n")

    for line in lines:
        if ":" in line:
            speaker, speech = line.split(":", 1)
            speaker = speaker.strip()
            speech = speech.strip()

            if speaker not in speakers:
                speakers[speaker] = []
            speakers[speaker].append(speech)

    if not speakers:
        speakers["Speaker"] = [text]

    return speakers


# 🔹 2. Sentiment
def sentiment_analysis(speakers):
    results = {}

    for speaker, speeches in speakers.items():
        scores = [sia.polarity_scores(s)['compound'] for s in speeches]
        results[speaker] = sum(scores)/len(scores)

    return results


# 🔹 3. Keywords 
def extract_keywords(text):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform([text])

    words = vectorizer.get_feature_names_out()
    scores = X.toarray()[0]

    word_score = dict(zip(words, scores))
    sorted_words = sorted(word_score.items(), key=lambda x: x[1], reverse=True)

    return sorted_words[:10]


# 🔹 4. Argument Strength
def argument_strength(speakers):
    logic_words = ["because", "therefore", "however", "but", "since"]
    scores = {}

    for speaker, speeches in speakers.items():
        score = 0

        for s in speeches:
            for word in logic_words:
                if word in s.lower():
                    score += 2

            score += len(s.split()) * 0.1

        scores[speaker] = round(score, 2)

    return scores


# 🔹 5. Topics (FIXED VERSION)
def extract_topics(text):
    doc = nlp(text)

    topics = []

    for token in doc:
        if (
            token.pos_ in ["NOUN", "PROPN"] and
            not token.is_stop and
            token.is_alpha and
            len(token.text) > 2 and
            token.text.lower() not in ["speaker", "a", "b"]
        ):
            topics.append(token.text.lower())

    return list(set(topics))[:10]


# 🔹 6. Winner
def calculate_winner(sentiment, strength):
    final_scores = {}

    for speaker in sentiment:
        final_scores[speaker] = sentiment[speaker]*0.5 + strength[speaker]*0.5

    if not final_scores:
        return "No winner", {}

    winner = max(final_scores, key=final_scores.get)
    return winner, final_scores