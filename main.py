from flask import Flask , render_template , redirect, url_for

app = Flask(__name__ , template_folder='templates')

@app.route('/')
def index():
    # return redirect(url_for("index"))
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/achievements')
def achievements():
    return render_template('awards_achievements.html')

@app.route('/contact')
def contact():
    return render_template('contact_details.html')

@app.route('/skills')
def skills():
    return render_template('skills_projects.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/learn_more')
def learn_more():
    return render_template('learn_more.html')

    
if __name__ == '__main__':
    app.run(host='0.0.0.0')    