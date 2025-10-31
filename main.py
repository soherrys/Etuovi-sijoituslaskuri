import os
from flask import Flask, render_template
from scraper import hae_asunnot
from calculator import laske_kannattavuus

app = Flask(__name__)

@app.after_request
def add_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def index():
    kohteet = hae_asunnot()
    laskelmat = [laske_kannattavuus(k) for k in kohteet]
    return render_template('index.html', kohteet=laskelmat)

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
