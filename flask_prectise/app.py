from flask import Flask,render_template,render_template_string,redirect,session,url_for,request

app = Flask(__name__) 

 
@app.route('/')    # decorator 
def home(): 
    return render_template('home.html')


@app.route('/userdata')    # decorator 
def userdata():
    return render_template('user_data.html')  


@app.route('/getdata',methods=['GET','POST'])
def getdata():
    if request.method == "POST": 
        user_name = request.form['username']
        user_email = request.form['email']
        user_password = request.form['password'] 
        app.config['username'] = user_name 
        app.config['useremail'] = user_email 
        app.config['userpassword'] = user_password 
        # data = {'username':user_name,'email':user_email,'password':user_password} 
        # return redirect('profile') 
        # match with database  

        return redirect(url_for('profile',username=user_name,email=user_email,password=user_password))


        # data = request.form 
        # return data 

        # data = request.args 
        # return data 

        # data = request.args.get('username')
        # return data 

@app.route('/profile/<username>/<email>/<password>')
# http://127.0.0.1:5000/profile/ranjisingh/ranj343@gmail.com/dhdk123 
def profile(username,email,password):
    # print(app.config['username'])
    # print(app.config['useremail'])
    # print(app.config['userpassword'])
   
    # return f"""Heyy this is {username} and my email {email} 
    #  and password is {password} successfully signed in """

    return render_template('profile.html',name=username,email=email,password=password)


@app.route('/signout/<username>/<email>') 
def signout(username,email):
    # return f"hey i sign out {username} and {email}" 
    return render_template('signout.html',name=username,email=email )







if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)