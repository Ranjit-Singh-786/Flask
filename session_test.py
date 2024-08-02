from flask import Flask,session,redirect,request,url_for,render_template,render_template_string

app = Flask(__name__)

app.secret_key = "dkfdh"

@app.route('/')
def home():
    return "Home page"

@app.route('/login/<username>/<password>')
# http://127.0.0.1:5000/loggedin/RanjitSingh/password12345
def login(username,password):
    if "username" and "password" not in session:
        session['username'] = username 
        session['password'] = password

    return redirect(url_for('loggedin',username=session['username'],
                                        password=session['password']))

@app.route('/loggedin/<username>/<password>')
# http://127.0.0.1:5000/loggedin/RanjitSingh/password12345
def loggedin(username,password):
    output = f"""
    <html>
    <head>
    <title>example title</title>
    </head>
    <body>
    <h2>Hello {username} and your password is {password}</h2>
    <p>Your welcome in this portal</p>
    </body>
    </html>
    """
    return render_template_string(output)

if __name__ == "__main__":
    app.run(debug=True)
