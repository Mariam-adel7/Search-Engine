from flask import Flask, render_template, request
import database  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        print(f"Searching for: {query}")  
        results = database.search_word(query)  
        print(f"Search results: {results}") 
        query_terms = query.strip().split()
        return render_template('results.html', results=results, query=query, query_terms=query_terms)

    return render_template('index.html')

if __name__ == '__main__':
    print("Starting the Flask app...")
    app.run(debug=True)
