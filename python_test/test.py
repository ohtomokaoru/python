from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route('/wiki/<pagename>')            # matches /wiki/Learning_Python
def show_wiki_page(pagename):
    return template('Hello {{pagename}}, how are you?', name=name)    

@route('/<action>/<user>')            # matches /follow/defnull
def user_api(action, user):
    return template('Hello {{user}}, how are you?', name=name)

run(host='0.0.0.0', port=8080)