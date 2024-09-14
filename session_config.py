from flask import Flask,render_template_string,redirect,url_for 
app = Flask(__name__) 
app.config["username"] = "ranjitsingh4546@gmail.com"
app.config["password"] = "ranjit4546"



@app.route('/') 
def home():
    home_string = f"""
        <html><head><title>home page</title></head>
        <body>
        <h2>Learn app.config concept</h2>
        <p>my username : <b>{app.config['username']} </b><br>
        my password is : <b>{app.config['password']} </b></p>
        </body>
        </html>
    """
    return render_template_string(home_string)

# this function redirect into another with url input and app.config variable
@app.route('/toswitch') # http://127.0.0.1:5000/toswitched
def toswitch():
    return redirect(url_for('switched',username=app.config['username'],password=app.config['password']))


# this url will be switched by the ===> http://127.0.0.1:5000/toswitched
@app.route('/switched/<username>/<password>')
def switched(username,password):

    switched_page = f"""
    <html><head><title>Loged page</title></head>
    <body>
    <h2>successfully log in the system</h2>
    <p>my username : <b>{app.config['username']} </b><br>
    my password is : <b>{app.config['password']} </b></p>
    </body>
    </html>
    """
    return render_template_string(switched_page)

if __name__ == "__main__": 
    app.run(debug=True)
