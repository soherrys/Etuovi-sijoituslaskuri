from flask import Flask, render_template
from scraper import hae_asunnot
from calculator import laske_kannattavuus

app = Flask(__name__)

@app.route('/')
def index():
    kohteet = hae_asunnot()
    laskelmat = [laske_kannattavuus(k) for k in kohteet]
    return render_template('index.html', kohteet=laskelmat)

if __name__ == '__main__':
    app.run(debug=True)
