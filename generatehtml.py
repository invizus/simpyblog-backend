import updatedb
from flask import render_template
import core

POST_TEMPLATE = "post.html"
INDEX_TEMPLATE = "index.html"
INDEX_HTML = "index.html"

def create_post(post):
    """ Create HTML file for one post from database.
    Function takes arguments: string "latest", string "all" or int ID of the post which exist in databse.
    At the end, rebuild_index() function called to rebuild index.html main page.

    post_ids - array, it can contain even one ID -> then loop will run only once.
    post_data - will contain list (array) of the post items from mysql for given post id
    post_dict - array, yaml like dictionary of lists of post items
    dictionary is useful if you want to write into main page.
    """
    post_ids = []
    post_dict = []
    if post == "latest":
        post_ids = updatedb.getID("latest")
    elif post == "all":
        post_ids = updatedb.getID("all")
    else:
        post_ids = [post]
    for ids in post_ids:
        post_dict.clear()
        post_data = updatedb.getContents(ids)
        post_dict.append(dict(post_title = post_data[1], post_author = post_data[0], post_url = post_data[3], post_date = post_data[2], post_body = post_data[4]))
        write_html(render_post(post_dict), post_data[3])
    rebuild_index()

def render_post(dict_list):
    """ Renreds html structure of the post with jinja2 template. Expecting dictionary containing only one post. """
    return render_template(POST_TEMPLATE, dict_list=dict_list, blog_title=core.blog_title)

def render_index(dict_list):
    """ Renders html structure of the post with jinja2 template. Expecting dictionary with all the posts as list. """
    return render_template(INDEX_TEMPLATE, dict_list=dict_list, blog_title=core.blog_title)

def write_html(data, filename):
    """ Simple function to write contents into file. """
    fullpath = core.website_dir + filename
    html = open(fullpath, "w")
    html.write(str(data))
    html.close()

def rebuild_index():
    """ Rebuilds index page of the blog. """
    post_ids = updatedb.getID("all")
    post_dict = []
    for ids in post_ids:
        post_data = updatedb.getContents(ids)
        post_dict.append(dict(post_title = post_data[1], post_author = post_data[0], post_url = post_data[3], post_date = post_data[2], post_body = post_data[4]))
    write_html(render_index(post_dict), INDEX_HTML)

if __name__ == '__main__':
    print("run pythion3 backend.py")