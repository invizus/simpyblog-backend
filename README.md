# simpyblog-backend

# Status: in development

This is working blog made for learning and educational purpose. It is implemented as front-end using REST API and back-end to use MySQL as datastore and generate static HTML pages.

Python 3 compatible.

At the moment flask app is running with same user as your mysql account, so you must have your account with permissions granted in mysql and not need to save passwords in plain text anywhere.

### What is not working yet:
#### main backend
* generate main index.html page
* copy files to your web server folder
#### init-project script
* config to include path to your web server folder
* various checks
* maybe copy or git frontend and generate index pages if any

## Start new project
If you want to start new project, run `python3 init-project.py install`
