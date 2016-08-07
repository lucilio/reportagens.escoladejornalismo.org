from flask import Flask, Blueprint, Markup, render_template, config, url_for, request
from os import path, scandir
import json, mistune, pprint

markdown = mistune.Markdown()
app_name = 'reportagens'
app_root = path.dirname( path.abspath( __file__ ) )
content_folder = 'content'
data_folder = 'data'
app_venv = app_name + '-venv'
sites_home = '.'

def setup_sites():
    sites = []
    sites_roots = [
        entry.name for entry in scandir( app_root + path.sep + sites_home )
        if entry.is_dir() and
        entry.name not in [ app_venv, sites_home ]
        and not entry.name.startswith('__')
        and not entry.name.startswith('.')
    ]
    for site_path in sites_roots:
        sites.append( load_site( site_path ) )

def load_site( site_name ):
    layout_data = {}
    layout_content = {}
    site_root = app_root + path.sep + sites_home + path.sep + site_name
    blueprint = Blueprint( site_name, __name__, static_folder = site_root + '/static', template_folder = site_root + '/templates' )
    for entry in scandir( site_root + path.sep + data_folder ):
        if entry.name.endswith('.json'):
            layout_data.update( { entry.name.replace( '.json', '' ): json.load( open( entry.path, encoding="utf-8", mode='r' ) ) } )
    for entry in scandir( site_root + path.sep + content_folder ):
        if entry.name.endswith('.md'):
            layout_content.update( { entry.name.replace( '.md', '' ): Markup( markdown( open( entry.path, encoding="utf-8", mode='r' ).read() ) ) } )
    @blueprint.route( '/' + site_name + '/', defaults={'layout': 'layout.html'} )
    @blueprint.route( '/' + site_name + '/<layout>' )
    def load_page( layout ):
        return render_template( layout, data=layout_data, content=layout_content )
    app.register_blueprint( blueprint )
    return blueprint

app = Flask( app_name, static_folder=None )
setup_sites()
if __name__ == '__main__':
    app.run(debug=True)