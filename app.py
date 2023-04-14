from flask import Flask,jsonify,request,render_template,url_for

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/testing',methods=['GET','POST'])
def testing():
    if request.method == 'POST':
        option = request.form['options']
        user_name = request.form['user_name']
        password = request.form['password']
        secret_code = request.form['secret_code']
        user_detail = {'user_name':user_name,'password':password,'secre_code':secret_code,'orgainsation':option}

        details_lst = [user_name,password,secret_code,option]
        return render_template('index.html',user_details=user_detail,detail_list=details_lst)
if __name__=="__main__":
    app.run(debug=True)