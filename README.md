# simpyblog-backend

# Status: in development

This is working blog made for learning and educational purpose. It is implemented as front-end using REST API and back-end to use MySQL as datastore and generate static HTML pages.

Python 3 compatible.

At the moment flask app is running with same user as your mysql account, so you must have your account with permissions granted in mysql and not need to save passwords in plain text anywhere.

### What is not working yet:
#### main backend
* ~~generate main index.html page~~
* ~~copy files to your web server folder~~
#### init-project script
* config to include path to your web server folder
* various checks
* maybe copy or git frontend and generate index pages if any

## Your project
If you want to use this for your website
create config.yml (using cofnig.yml.example)
run `python3 init-project.py install`
this will perform various checks, then will create a database.
TODO: write manual or script how to setup Apache/nginx 
TODO: add link to frontend
