from  flask import Flask , render_template , url_for

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/about',methods=['GET','POST'])
def about():
    return "Hii about"
# route of this: http://127.0.0.1:5000/about

@app.route('/contact',methods=['GET','POST'])
def contact():
    return "Hii contact"
# route of this: http://127.0.0.1:5000/contact

@app.route('/service',methods=['GET','POST'])
def service():
    return "Hii service"
# route of this: http://127.0.0.1:5000/service

@app.route('/course',methods=['GET','POST'])
def course():
    return "Hii course"
# route of this: http://127.0.0.1:5000/contact

if __name__ == "__main__":
    app.run(debug=True)