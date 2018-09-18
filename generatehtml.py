#import core
import updatedb

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

if __name__ == '__main__':
    generate_post("latest")
