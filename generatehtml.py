import mysql.connector
import yaml
import core

def generate_post(post):
    post_ids = []
    if post == "latest":
        post_ids = updatedb.getID("latest")
    elif post == "all":
        post_ids = updatedb.getID("all")
    else:
        post_ids = [post]
    for ids in post_ids:
        generate_file(updatedb.getContents(ids))

def generate_file(entry):
    #Author = PostContents[0]    #Title = PostContents[1]    #Date = PostContents[2]
    contents = '''            <div class="post">
                <section class="post">
                    <h1>{0}</h1>

                        <p> {1} </p>

                <p class="content-subhead">{2}, Date: {3} UTC</p>
                </section>
            </div>

           '''.format(entry[1], entry[4], entry[0], entry[2])
    create_html(contents, entry[3])

def create_html(contents, filename):
    html = open(filename, "w")
    html.write(open("header.html").read())
    html = open(filename, "a")
    html.write(contents)
    html.write(open("footer.html").read())
    html.close()

def GetPostContents(PostID):
    QueryGetContents = "SELECT post_author, post_title, post_date, link, post_text from posts where id like " + str(PostID)
    cmd.execute(QueryGetContents)
    PostContents = cmd.fetchone()

    #Author = PostContents[0]    #Title = PostContents[1]    #Date = PostContents[2]
    htmlfile = PostContents[3]
    contents = '''            <div class="post">
                <section class="post">
                    <h1>{0}</h1>

                        <p> {1} </p>

                <p class="content-subhead">{2}, Date: {3} UTC</p>
                </section>
            </div>

           '''.format(PostContents[1], PostContents[4], PostContents[0], PostContents[2])
    #return contents

# def writefile(fname):
    f = open(htmlfile, "w")
    f.write(open("header.html").read())
    f = open(htmlfile, "a")
    f.write(contents)
    f.write(open("footer.html").read())
    f.close()

#def getPostContents(post_id):
#    post_contents = []
#    post_contents = updatedb.getContentsof(post_id)
#    return post_contents

if __name__ == '__main__':
    generate_post(latest)
