import pandas as pd
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

vocab = pd.read_csv('vocab.csv', names=['word'])
monograms = pd.read_csv('monograms.csv')
bigrams = pd.read_csv('bigrams.csv')


def predict_words(df, words, chars, limit=10):
    ngram = ' '.join(words)
    if chars:
        index = (df.ngram == ngram) & (df.prediction.str.startswith(chars, na=False))
        return df[index].prediction.values[:limit].tolist()
    else:
        return df[df.ngram == ngram].prediction.values[:limit].tolist()


@app.route('/api', methods=['POST'])
def predict():
    if request.is_json:
        data = request.get_json()
        words = data.get('words', [])
        n = len(words)

        if n == 1 and words[0] == '':
            result = vocab.word.values[:10].tolist()
            return jsonify(result)
        elif n == 1 and words[0]:
            result = vocab[vocab.word.str.startswith(words[0], na=False)].word.values[:10].tolist()
            return jsonify(result)
        elif n == 2:
            return jsonify(predict_words(monograms, words[:1], words[1]))
        elif n == 3:
            return jsonify(predict_words(bigrams, words[:2], words[2]))
        else:
            # TODO trigram
            words = words[-3:]
            return jsonify(predict_words(bigrams, words[:2], words[2]))
    else:
        return 'not a json request', 400


if __name__ == '__main__':
    app.run()
