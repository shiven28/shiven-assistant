from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "YOUR_OPENAI_API_KEY"  # replace this

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    if request.method == 'POST':
        query = request.form['query']
        
        # Call OpenAI API
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ]
        )
        response = completion.choices[0].message['content']

    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
