import pandas as pd
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

# monogram_frequencies_df[monogram_frequencies_df.ngram.str.startswith('t', na=False)]
# monogram_frequencies_df[monogram_frequencies_df.ngram.str.startswith('t', na=False)].ngram.values[:10]
words = pd.read_csv('vocab.csv', names=['word'])
monograms = pd.read_csv('monograms.csv')
bigrams = pd.read_csv('bigrams.csv')


@app.route('/', methods=['POST'])
def predict():
    if request.is_json:
        data = request.get_json()
        if 'nb_words' in data and 'value' in data:
            nb_words = data['nb_words']
            value = data['value']
            if nb_words == 0:
                result = words[words.word.str.startswith(value, na=False)].word.values[:10].tolist()
                return jsonify(result)

            return 'Hello World!'
        else:
            return 'should provide a words number and a value', 400
    else:
        return 'not a json request', 400


if __name__ == '__main__':
    app.run()
