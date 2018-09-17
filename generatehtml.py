import mysql.connector
import yaml
import core
# latest or all

#def lastPostID():
#   updatedb.last

def GetLatestID():
    cmd = dbsession.cursor()
    cmd.execute("SELECT MAX(id) FROM posts")
    DBLatestID = cmd.fetchone()[0]
    return DBLatestID

def GetAllIDs():
    cmd = dbsession.cursor()
    cmd.execute("SELECT id FROM posts")
    DBAllIDs = []
    row = cmd.fetchone()
    while row is not None:
        DBAllIDs.append(row[0])
        row = cmd.fetchone()
    # print(manyposts)
    # [3, 4, 5, 6, 8]
    return DBAllIDs


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
    f.close();

#def getPostContents(post_id):
#    post_contents = []
#    post_contents = updatedb.getContentsof(post_id)
#    return post_contents

def generate_post(post_id):
    post_contents = []
    if post_id = "last":
        post_contents = updatedb.getContentsOf(last)
        write_html(post_contents[3], post_contents)
    #  generatePo udpatedb.idof
    else if post_id = "all":
    #  updatedb.idof(all)
    else
        post_contents = updatedb.getContentsOf(post_id)
        write_html([post_contents[3], post_contents)



#def rebuild_main():

#generate_post(3)
#generate_post(last)
#generate_post(all)

if __name__ == '__main__':
    compose()
