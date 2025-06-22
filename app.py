from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    if request.method == 'POST':
        query = request.form['query']
        response = f"You searched for: {query}"
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
