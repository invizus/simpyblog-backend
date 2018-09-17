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

#def update(content, post_id):
#def delete(post_id)
#def get_posts():

def getContentsof(post_id):
    cmd = dbsession.cursor()
    if post_id = "last":
        cmd.execute("SELECT MAX(id) FROM posts")
        post_id = cmd.fetchone()[0]
    cmd.execute("SELECT post_author, post_title, post_date, link, post_text from posts where id like " + str(PostID))
    post_contents = cmd.fetchone()
    return post_contents

def GetLatestID():
    cmd = dbsession.cursor()
    cmd.execute("SELECT MAX(id) FROM posts")
    DBLatestID = cmd.fetchone()[0]
    return DBLatestID