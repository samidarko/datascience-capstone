import pandas as pd
from flask import Flask, request

app = Flask(__name__)

# monogram_frequencies_df[monogram_frequencies_df.ngram.str.startswith('t', na=False)]
# monogram_frequencies_df[monogram_frequencies_df.ngram.str.startswith('t', na=False)].ngram.values[:10]
words = pd.read_csv('vocab.csv', names=['words'])
monograms = pd.read_csv('monograms.csv', names=['monogram', 'prediction'])
bigrams = pd.read_csv('bigrams.csv', names=['bigram', 'prediction'])


@app.route('/', methods=['POST'])
def predict():
    print(request.get_json())
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
