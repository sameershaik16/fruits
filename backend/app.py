from flask import Flask, render_template, request, redirect, url_for
import os

# Tell Flask where to find templates and static folder
app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '../templates')
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
