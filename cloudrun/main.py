import os
from flask import Flask, jsonify, request

import word_similar

app = Flask(__name__)


@app.route('/word_similar', methods=['POST'])
def action():
    info = request.get_json()
    word = info['word']

    try:
        word_similar.model.wv[word]
    except:
        return 'Word "{0}" not in vocabulary'.format(word),400

    try:
        similar_words = word_similar.get_similar_words(word)
    except:
        return 'Can not found similar word',400

    # print({'similar_words': similar_words})
    return jsonify({'similar_words': similar_words}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)), debug=True)
