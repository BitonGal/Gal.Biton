from flask import Flask,url_for, redirect ,render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def main():
    return render_template('CV.html')

@app.route('/ex2')
def ex2():
    return render_template('exercise2.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/assignment8')
def assignment8():
    nyc = ("Museum of natural history", "Brooklyn Bridge", "9/11 memorial", "soho")
    return render_template('assignment8.html', nyc = nyc)



if __name__ == '__main__':
    app.run()