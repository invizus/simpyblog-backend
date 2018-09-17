#!flask/bin/python
from flask import request, Flask, jsonify
from flask_cors import CORS
import core
import generatehtml
import updatedb

app = Flask(__name__)
#see if I can move below line into __main__ before app.run
CORS(app, resources={r"/submit/*":{"origins": core.apiURL }})

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
    generatehtml.generate_post("latest")
    generatehtml.rebuild_main()
    return msg

#def update_post(post_id, contents):
#def delete_post(post_id):
#def get_posts():

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', ssl_context=('fullchain.pem', 'privkey.pem'))
