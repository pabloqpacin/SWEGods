from flask import Flask, send_from_directory, send_file, escape, Markup, render_template, abort, request
import os
import json


app = Flask(__name__)

#Static pages
app.config['STATIC_ABOUT_PAGE'] = os.path.join('.', 'static', 'about.html')
app.config['STATIC_SPLASH_PAGE'] = os.path.join('.', 'static', 'index.html')

#Pillar pages
app.config['STATIC_GODS_FOLDER'] = os.path.join('.', 'static', 'gods')
app.config['STATIC_HEROES_FOLDER'] = os.path.join('.', 'static', 'heroes')
app.config['STATIC_LOCATIONS_FOLDER'] = os.path.join('.', 'static', 'locations')
app.config['STATIC_MYTHS_FOLDER'] = os.path.join('.', 'static', 'myths')

#List pages
app.config['STATIC_GODS_LIST'] = os.path.join('.', 'static', 'gods.html')
app.config['STATIC_HEROES_LIST'] = os.path.join('.', 'static', 'heroes.html')
app.config['STATIC_LOCATIONS_LIST'] = os.path.join('.', 'static', 'locations.html')
app.config['STATIC_MYTHS_LIST'] = os.path.join('.', 'static', 'myths.html')

#Static files
app.config['STATIC_CSS_FOLDER'] = os.path.join('.', 'static', 'css')
app.config['STATIC_FONTS_FOLDER'] = os.path.join('.', 'static', 'fonts')
app.config['STATIC_JS_FOLDER'] = os.path.join('.', 'static', 'js')
app.config['STATIC_IMAGES_FOLDER'] = os.path.join('.', 'static', 'img')

# Shows error message
def error_wrapper(content):
	return render_template('error_template.html', error_message=content)

# Splash page
@app.route('/')
def index():
	if os.path.exists(app.config['STATIC_SPLASH_PAGE']):
		return send_file(app.config['STATIC_SPLASH_PAGE'])
	return error_wrapper('Hello, World! <SPLASH PAGE NOT YET ADDED>'), 404

# Connects to the about page
@app.route('/about')
@app.route('/about/')
def about_page():
	if os.path.exists(app.config['STATIC_ABOUT_PAGE']):
		return send_file(app.config['STATIC_ABOUT_PAGE'])
	return error_wrapper('About page to be added'), 404

# Connects to gods page
@app.route('/gods')
@app.route('/gods/')
def gods_model():
	if os.path.exists(app.config['STATIC_GODS_LIST']):
		return send_file(app.config['STATIC_GODS_LIST'])
	return error_wrapper('Gods Model page to be added'), 404

# Connects to heroes page
@app.route('/heroes')
@app.route('/heroes/')
def heroes_model():
	if os.path.exists(app.config['STATIC_HEROES_LIST']):
		return send_file(app.config['STATIC_HEROES_LIST'])
	return error_wrapper('Heroes Model page to be added'), 404

# Connects to creatures page
@app.route('/locations')
@app.route('/locations/')
def creatures_model():
	if os.path.exists(app.config['STATIC_LOCATIONS_LIST']):
		return send_file(app.config['STATIC_LOCATIONS_LIST'])
	return error_wrapper('Locations Model page to be added'), 404

# Connects to myths page
@app.route('/myths')
@app.route('/myths/')
def myths_model():
	if os.path.exists(app.config['STATIC_MYTHS_LIST']):
		return send_file(app.config['STATIC_MYTHS_LIST'])
	return error_wrapper('Myths Model page to be added'), 404


@app.route('/search')
@app.route('/search/')
def search_model():
	q = request.args.get('query')
	q = str(q)
	search_result = []
	search_result.append(q)
	print(search_result)
	return render_template('searchtemp.html', search = search_result)

#using string instead of path because we don't want '/' to count
# @app.route('/gods/<string:god>')
# @app.route('/gods/<string:god>/')
# def god_page(god):
# 	if os.path.exists(os.path.join(app.config['STATIC_GODS_FOLDER'], god.lower() + ".html")):
# 		return send_from_directory(app.config['STATIC_GODS_FOLDER'],
#                                god.lower() + '.html', as_attachment=False)
# 	return error_wrapper('Page for god: ' + god + ' to be added'), 404

@app.route('/gods/<string:god>')
@app.route('/gods/<string:god>/')
def god_page(god):
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, 'static/js', 'godsinfo.json')
	data = json.load(open(json_url))
	god_info = []
	for i in data:
		if i['name'].lower() == god:
			god_info.append(i['name'])
			god_info.append(i['romanname'])
			god_info.append(i['symbol'])
			god_info.append(i['power'])
			god_info.append(i['father'])
			god_info.append(i['mother'])
			god_info.append(i['url'])
	return render_template('godtemp.html', god = god_info)

# Links to specific hero given by hero name
# @app.route('/heroes/<string:hero>')
# @app.route('/heroes/<string:hero>/')
# def hero_page(hero):
# 	if os.path.exists(os.path.join(app.config['STATIC_HEROES_FOLDER'], hero.lower() + ".html")):
# 		return send_from_directory(app.config['STATIC_HEROES_FOLDER'],
#                                hero.lower() + '.html', as_attachment=False)
# 	return error_wrapper('Page for hero: ' + hero + ' to be added'), 404

@app.route('/heroes/<string:hero>')
@app.route('/heroes/<string:hero>/')
def hero_page(hero):
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, 'static/js', 'heroesinfo.json')
	data = json.load(open(json_url))
	hero_info = []
	for i in data:
		if i['name'].lower() == hero:
			hero_info.append(i['name'])
			hero_info.append(i['hero_type'])
			hero_info.append(i['power'])
			hero_info.append(i['home'])
			hero_info.append(i['father'])
			hero_info.append(i['mother'])
			hero_info.append(i['url'])
	return render_template('herotemp.html', hero = hero_info)

# Links to specific creature given by creature name
# @app.route('/locations/<string:location>')
# @app.route('/locations/<string:location>/')
# def creature_page(location):
# 	if os.path.exists(os.path.join(app.config['STATIC_LOCATIONS_FOLDER'], location.lower() + ".html")):
# 		return send_from_directory(app.config['STATIC_LOCATIONS_FOLDER'],
#                                location.lower() + '.html', as_attachment=False)
# 	return error_wrapper('Page for creature: ' + location + ' to be added'), 404

@app.route('/locations/<string:location>')
@app.route('/locations/<string:location>/')
def location_page(location):
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, 'static/js', 'locationsinfo.json')
	data = json.load(open(json_url))
	location_info = []
	for i in data:
		if i['name'].lower() == location:
			location_info.append(i['name'])
			location_info.append(i['altname'])
			location_info.append(i['location_type'])
			location_info.append(i['myth'])
			location_info.append(i['gods'])
			location_info.append(i['url'])
	return render_template('locationtemp.html', location = location_info)

# Links to specific myth given by myth name
# @app.route('/myths/<string:myth>')
# @app.route('/myths/<string:myth>/')
# def myth_page(myth):
# 	if os.path.exists(os.path.join(app.config['STATIC_MYTHS_FOLDER'], myth.lower() + ".html")):
# 		return send_from_directory(app.config['STATIC_MYTHS_FOLDER'],
#                                myth.lower() + '.html', as_attachment=False)
# 	return error_wrapper('Page for myth: ' + myth + ' to be added'), 404

@app.route('/myths/<string:myth>')
@app.route('/myths/<string:myth>/')
def myth_page(myth):
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, 'static/js', 'mythsinfo.json')
	data = json.load(open(json_url))
	myth_info = []
	for i in data:
		if i['name'].lower() == myth:
			myth_info.append(i['name'])
			myth_info.append(i['description'])
			myth_info.append(i['theme'])
			myth_info.append(i['place'])
			myth_info.append(i['gods'])
			myth_info.append(i['characters'])
			myth_info.append(i['url'])
	return render_template('mythtemp.html', myth = myth_info)

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
