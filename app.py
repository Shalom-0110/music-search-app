import requests
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

INDEX_TEMPLATE = 'index.html'

@app.route('/')
def index():
    return render_template(INDEX_TEMPLATE)

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search_term')
    if not search_term:
        return render_template(INDEX_TEMPLATE, error="Please enter a search term.")

    #When user submit the form, this iTunes API will be called.
    response = requests.get(f'https://itunes.apple.com/search?term={search_term}&media=music&entity=album')
    if response.status_code != 200:
        return render_template(INDEX_TEMPLATE, error="Error fetching data from iTunes API.")

    results = response.json().get('results', [])
    
    for result in results:
        print("Collection Name:", result.get('collectionName'))
        print("Artist Name:", result.get('artistName'))
        #print("Preview URL:", result.get('previewUrl')) 

    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
