from flask import Flask, send_from_directory, send_file, escape, Markup, render_template, abort
import os

app = Flask(__name__)

#Static pages
app.config['STATIC_ABOUT_PAGE'] = os.path.join('.', 'static', 'about.html')
app.config['STATIC_SPLASH_PAGE'] = os.path.join('.', 'static', 'index.html')

#Pillar pages
app.config['STATIC_GODS_FOLDER'] = os.path.join('.', 'static', 'gods')
app.config['STATIC_HEROS_FOLDER'] = os.path.join('.', 'static', 'heroes')
app.config['STATIC_CREATURES_FOLDER'] = os.path.join('.', 'static', 'creatures')
app.config['STATIC_MYTHS_FOLDER'] = os.path.join('.', 'static', 'myths')

#List pages
app.config['STATIC_GODS_LIST'] = os.path.join('.', 'static', 'gods.html')
app.config['STATIC_HEROS_LIST'] = os.path.join('.', 'static', 'heroes.html')
app.config['STATIC_CREATURES_LIST'] = os.path.join('.', 'static', 'creatures.html')
app.config['STATIC_MYTHS_LIST'] = os.path.join('.', 'static', 'myths.html')

#Static files
app.config['STATIC_CSS_FOLDER'] = os.path.join('.', 'static', 'css')
app.config['STATIC_FONTS_FOLDER'] = os.path.join('.', 'static', 'fonts')
app.config['STATIC_JS_FOLDER'] = os.path.join('.', 'static', 'js')
app.config['STATIC_IMAGES_FOLDER'] = os.path.join('.', 'static', 'img')

def error_wrapper(content):
	return render_template('error_template.html', error_message=content)


@app.route('/')
def index():
	if os.path.exists(app.config['STATIC_SPLASH_PAGE']):
		return send_file(app.config['STATIC_SPLASH_PAGE'])
	return error_wrapper('Hello, World! <SPLASH PAGE NOT YET ADDED>'), 404

@app.route('/about')
@app.route('/about/')
def about_page():
	if os.path.exists(app.config['STATIC_ABOUT_PAGE']):
		return send_file(app.config['STATIC_ABOUT_PAGE'])
	return error_wrapper('About page to be added'), 404

@app.route('/gods')
@app.route('/gods/')
def gods_model():
	if os.path.exists(app.config['STATIC_GODS_LIST']):
		return send_file(app.config['STATIC_GODS_LIST'])
	return error_wrapper('Gods Model page to be added'), 404

@app.route('/heroes')
@app.route('/heroes/')
def heroes_model():
	if os.path.exists(app.config['STATIC_HEROS_LIST']):
		return send_file(app.config['STATIC_HEROS_LIST'])
	return error_wrapper('Heroes Model page to be added'), 404

@app.route('/creatures')
@app.route('/creatures/')
def creatures_model():
	if os.path.exists(app.config['STATIC_CREATURES_LIST']):
		return send_file(app.config['STATIC_CREATURES_LIST'])
	return error_wrapper('Creatures Model page to be added'), 404

@app.route('/myths')
@app.route('/myths/')
def myths_model():
	if os.path.exists(app.config['STATIC_MYTHS_LIST']):
		return send_file(app.config['STATIC_MYTHS_LIST'])
	return error_wrapper('Myths Model page to be added'), 404

#using string instead of path because we don't want '/' to count
@app.route('/gods/<string:god>')
@app.route('/gods/<string:god>/')
def god_page(god):
	if os.path.exists(os.path.join(app.config['STATIC_GODS_FOLDER'], god.lower() + ".html")):
		return send_from_directory(app.config['STATIC_GODS_FOLDER'],
                               god.lower() + '.html', as_attachment=False)
	return error_wrapper('Page for god: ' + god + ' to be added'), 404

@app.route('/heroes/<string:hero>')
@app.route('/heroes/<string:hero>/')
def hero_page(hero):
	if os.path.exists(os.path.join(app.config['STATIC_HEROS_FOLDER'], hero.lower() + ".html")):
		return send_from_directory(app.config['STATIC_HEROS_FOLDER'],
                               hero.lower() + '.html', as_attachment=False)
	return error_wrapper('Page for hero: ' + hero + ' to be added'), 404

@app.route('/creatures/<string:creature>')
@app.route('/creatures/<string:creature>/')
def creature_page(creature):
	if os.path.exists(os.path.join(app.config['STATIC_CREATURES_FOLDER'], creature.lower() + ".html")):
		return send_from_directory(app.config['STATIC_CREATURES_FOLDER'],
                               creature.lower() + '.html', as_attachment=False)
	return error_wrapper('Page for creature: ' + creature + ' to be added'), 404

@app.route('/myths/<string:myth>')
@app.route('/myths/<string:myth>/')
def myth_page(myth):
	if os.path.exists(os.path.join(app.config['STATIC_MYTHS_FOLDER'], myth.lower() + ".html")):
		return send_from_directory(app.config['STATIC_MYTHS_FOLDER'],
                               myth.lower() + '.html', as_attachment=False)
	return error_wrapper('Page for myth: ' + myth + ' to be added'), 404

@app.route('/static/<path:folder>/<string:file>')
def static_files(folder, file):
	""" Serves the static files that will be used through all iterations of the project
	"""
	if folder == 'css':
		return send_from_directory(app.config['STATIC_CSS_FOLDER'],
                               file.lower(), as_attachment=False)
	elif folder == 'fonts':
		return send_from_directory(app.config['STATIC_FONTS_FOLDER'],
                               file.lower(), as_attachment=False)
	elif folder == 'js':
		return send_from_directory(app.config['STATIC_JS_FOLDER'],
                               file.lower(), as_attachment=False)
	elif folder == 'img':
		return send_from_directory(app.config['STATIC_IMAGES_FOLDER'],
                               file.lower(), as_attachment=False)
	elif folder == 'img/about':
		return send_from_directory(os.path.join(app.config['STATIC_IMAGES_FOLDER'], 'about'),
                               file.lower(), as_attachment=False)
	else:
		abort(code = 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
