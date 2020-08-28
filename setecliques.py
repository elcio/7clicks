import requests
from flask import Flask
app = Flask(__name__)

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
    # TODO: cache
    request = requests.get(f'https://pt.wikipedia.org/wiki/{verbete}')
    return request.text

def add_custom_header(original_html):
    # TODO: cache
    with open('templates/head.html') as f:
        headhtml = f.read()
    return original_html.replace('</head>', headhtml+'</head>')
