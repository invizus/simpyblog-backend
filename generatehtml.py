import updatedb
from flask import render_template

def generate_post(post):
    post_ids = [] # maybe incorrect below not sure as getID returns array - need to append maybe?
    if post == "latest":
        post_ids = updatedb.getID("latest")
    elif post == "all":
        post_ids = updatedb.getID("all")
    else:
        post_ids = [post]
    for ids in post_ids:
#        generate_file(updatedb.getContents(ids))
        post_data = updatedb.getContents(ids)
#        write_html(generate_html(post_data), post_data[3])
#        generate_html2(generate_html(post_data), post_data[3], post) #post_data, url, main or post entry
        write_html2(generate_html2(post_data,"post"), post_data[3])

def generate_html(entry):
    #Author = PostContents[0]    #Title = PostContents[1]    #Date = PostContents[2]    #Contents = entry[4]
    contents = '''            <div class="post">
                <section class="post">
                    <h1>{0}</h1>

                        <p> {1} </p>

                <p class="content-subhead">{2}, Date: {3} UTC</p>
                </section>
            </div>

           '''.format(entry[1], entry[4], entry[0], entry[2])

def generate_html2(entry, content_type):
    if content_type == "post":
        return render_template('post.html', post_title=entry[1], post_body=entry[4], post_author=entry[0], post_date=entry[2])
    elif content_type == "main":
        return render_template('main.html', post_title=entry[1], post_body=entry[4], post_author=entry[0], post_date=entry[2])

def write_html2(data, filename):
    html = open(filename, "w")
    html.write(str(data))
    html.close()
#TODO copy to directory from config.yml

def write_html(contents, filename):
    html = open(filename, "w")
    html.write(open("header.html").read())
    html = open(filename, "a")
    html.write(contents)
    html.write(open("footer.html").read())
    html.close()

def generate_main():
    post_ids = updatedb.getID("all")
    main_content = []
    for ids in post_ids:
        post_data = updatedb.getContents(ids)
        main_content.append(post_data)
    write_html2(generate_html2(main_content,"main"), "main.html")
#        generate_html(post_data)
#        generate_html2(post_data, "index.html", main)
#        write_html2(generate_html2(post_data, main), "index.html")

if __name__ == '__main__':
    generate_post("latest")
