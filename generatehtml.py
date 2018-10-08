import updatedb
from flask import render_template
import core

def generate_post(post):
    post_ids = [] # maybe incorrect below not sure as getID returns array - need to append maybe?
    if post == "latest":
        post_ids = updatedb.getID("latest")
    elif post == "all":
        post_ids = updatedb.getID("all")
    else:
        post_ids = [post]
    for ids in post_ids:
        post_data = updatedb.getContents(ids)
        write_html2(generate_html2(post_data,"post"), post_data[3])

def generate_html2(entry, content_type):
    if content_type == "post":
        return render_template('custom.html', post_title=entry[1], post_body=entry[4], post_author=entry[0], post_date=entry[2], header_link="no", blog_title=core.blog_title)
    elif content_type == "main":
        return render_template('custom.html', post_title=entry[1], post_body=entry[4], post_author=entry[0], post_date=entry[2], header_link="yes", blog_title=core.blog_title)

def write_html2(data, filename):
    fullpath = core.website_dir + filename
    html = open(fullpath, "w")
    html.write(str(data))
    html.close()
#TODO copy to directory from config.yml

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
