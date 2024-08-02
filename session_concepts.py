from flask import Flask, redirect, session,request,url_for
import string 
import random 
app = Flask(__name__)

# Generating secret key
alpha = string.ascii_letters
digits = string.digits
tokens = list(alpha+digits)
key = random.choices(tokens,k=10)
secret_key = " ".join(key)
print(secret_key)
app.secret_key = secret_key 



@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Logged in as {username}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('hii executed')
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

