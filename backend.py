#!flask/bin/python
from flask import request, Flask, jsonify
from flask_cors import CORS
import core
import generatehtml
import updatedb

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
        return "Restricted API server"

@app.route('/submit', methods=['POST', 'PUT'])
def new_post():
    if not request.json:
        abort(400)
    content = {
         'post_author' : request.json['post_author'],
         'post_title': request.json['post_title'],
         'post_text' : request.json['post_text'],
         'post_link' : request.json['post_link']
    }
    updatedb.new(content)
    msg = "API received data."
    generatehtml.create_post("latest")
    return msg

@app.route('/api/rebuild/index', methods=['GET'])
def rebuild_main():
    msg = "Rebuilt main page."
    generatehtml.rebuild_index()
    return msg

@app.route('/api/rebuild/all', methods=['GET'])
def rebuild_all():
    msg = "Rebuilt main page."
    generatehtml.rebuild_index()
    generatehtml.create_post("all")
    return msg


#def update_post(post_id, contents):
#def delete_post(post_id):
#def get_posts():

if __name__ == '__main__':
    CORS(app, resources={r"/submit/*":{"origins": core.apiURL }})
    app.run(debug=True, host='0.0.0.0', ssl_context=('fullchain.pem', 'privkey.pem'))
