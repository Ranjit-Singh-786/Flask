from  flask import Flask , render_template , url_for,request

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
# route of this: http://127.0.0.1:5000/course




@app.route('/MLAPI',methods=['GET','POST'])
def MLAPI():
    return render_template('testing.html')
# route of this: http://127.0.0.1:5000/MLAPI



@app.route('/testing',methods=['GET','POST'])
def testing():
    if request.method == 'POST':
        option = request.form['options']
        user_name = request.form['user_name']
        password = request.form['password']
        secret_code = request.form['secret_code']
        user_detail = {'user_name':user_name,'password':password,'secre_code':secret_code,'orgainsation':option}

        details_lst = [user_name,password,secret_code,option]
        return render_template('testing.html',user_details=user_detail,detail_list=details_lst)


if __name__ == "__main__":
    app.run(debug=True)