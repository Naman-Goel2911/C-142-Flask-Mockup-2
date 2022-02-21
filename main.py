from storage import liked_articles
from storage import disliked_articles
from storage import did_not_read
from storage import all_articles
from demographic_filtering import output
from content_based_filtering import get_recommendations
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/get-articles")

def get_articles():
    return jsonify({
        "data": all_articles[0],
        "status": "Success!"
    })

@app.route('/liked-article', methods = ['POST'])

def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "Success!"
    }), 201

@app.route('/disliked-article', methods = ['POST'])

def disliked_article():
    article = all_articles[0]
    disliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "Success!"
    }), 201

@app.route('/did-not-read', methods = ['POST'])

def not_read():
    article = all_articles[0]
    did_not_read.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "Success!"
    }), 201

@app.route('/popular-articles')

def popular_articles():
    article_data = []
    for article in output:
        d = {
            "title": article[0]
        }
        article_data.append(d)
    
    return jsonify({
        "data": article_data,
        "status": "Success!"
    }), 200

@app.route('/recommended-articles')

def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        d = {
            "title": recommended[0]
        }
        article_data.append(d)

    return jsonify({
        "data": article_data,
        "status": "Success!"
    }), 200

app.run()