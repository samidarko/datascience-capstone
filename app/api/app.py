import pandas as pd
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

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
            elif nb_words == 1:
                return jsonify([])
            elif nb_words == 2:
                return jsonify([])
            else:
                # just take the two last words
                return jsonify([])
        else:
            return 'should provide a words number and a value', 400
    else:
        return 'not a json request', 400


if __name__ == '__main__':
    app.run()
