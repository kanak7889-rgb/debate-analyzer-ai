# AI-Based Debate Analyzer

This project is a web application that analyzes debates using Natural Language Processing (NLP) and basic Machine Learning techniques. It evaluates different speakers based on sentiment, argument strength, keywords, and topics, and predicts the winner of the debate.

## Features

- Speaker-wise analysis
- Sentiment analysis using VADER (NLTK)
- Argument strength calculation
- Keyword extraction using TF-IDF
- Topic extraction using NLP (spaCy)
- Winner prediction
- Simple and attractive user interface

## Technologies Used

- Python
- Flask
- NLTK
- spaCy
- Scikit-learn
- HTML, CSS

## Project Structure

Debate/
- app.py  
- analyzer.py  
- requirements.txt  
- README.md  
- templates/
  - index.html  
- static/
  - style.css  

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Download spaCy model:
   python -m spacy download en_core_web_sm

3. Run the application:
   python app.py

4. Open in browser:
   http://127.0.0.1:5000

## Sample Input

Speaker A: Artificial intelligence improves productivity.  
Speaker B: However, it can cause unemployment.  
Speaker A: Therefore, training is important.  

## Working

- VADER is used for sentiment analysis  
- TF-IDF is used for keyword extraction  
- spaCy is used for topic extraction  
- Custom logic is used for argument strength and winner calculation  

## Author

Kanak Sharma
