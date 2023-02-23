from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def header():
    return render_template('header.html')
@app.route('/index')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)