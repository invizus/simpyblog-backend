#import core
from core import dbsession
import time

def new(content):
    timeUTC = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    QueryInsertPost = "INSERT INTO posts (post_author, post_date, post_title, link, post_text) VALUES (%s, %s, %s, %s, %s)"
    ValuesPost = (content['post_author'], timeUTC, content['post_title'], content['post_link'], content['post_text'])
    cmd = dbsession.cursor()
    cmd.execute(QueryInsertPost, ValuesPost)
    dbsession.commit()

#def update(post_id, content):
#def delete(post_id)
#def get_posts():

def getContents(post_id):
    cmd = dbsession.cursor()
    cmd.execute("SELECT post_author, post_title, post_date, link, post_text from posts where id like " + str(PostID))
    post_contents = cmd.fetchone()
    return post_contents

def getID(what):
    cmd = dbsession.cursor()
    if what == "latest":
        cmd.execute("SELECT MAX(id) FROM posts")
        IDs = cmd.fetchone()[0]
    elif what == "all":
        cmd.execute("SELECT id FROM posts")
        IDs = []
        row = cmd.fetchone()
        while row is not None:
            IDs.append(row[0])
            row = cmd.fetchone()
    return IDs

if __name__ == '__main__':
    print(getID("all"))
