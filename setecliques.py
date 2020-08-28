import os
import hashlib
import requests
from flask import Flask
app = Flask(__name__)

os.makedirs('cache')

@app.route('/')
def hello_world():
    # TODO: cache
    with open('templates/home.html') as f:
        html = add_custom_header(f.read())
    return html

@app.route('/wiki/<verbete>')
def artigo(verbete):
    original_html = read_wikipedia(verbete)
    html = add_custom_header(original_html)
    return html

def read_wikipedia(verbete):
    url = f'https://pt.wikipedia.org/wiki/{verbete}'
    urlhash = make_hash(url)
    if os.path.isfile(f'cache/{urlhash}.html'):
        return open(f'cache/{urlhash}.html').read()
    request = requests.get(url)
    with open(f'cache/{urlhash}.html','w') as f:
        f.write(request.text)
    return request.text

def make_hash(url):
    return hashlib.md5(url.encode('utf-8')).hexdigest()

def add_custom_header(original_html):
    # TODO: cache
    with open('templates/head.html') as f:
        headhtml = f.read()
    return original_html.replace('</head>', headhtml+'</head>')
