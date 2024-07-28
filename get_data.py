from flask import Flask , render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('get_method.html')


# <<<<<<<<<<<< first way to get data  >>>>>>>>>>>>
# @app.route('/getdatatesting')
# def getdatatesting():
#     complete_data = request.args

#     name = request.args.get('name')
#     option = request.args.get('options')

#     return  [name,option]


# <<<<<<<<<<<<<<< second way to get data  >>>>>>>>>>>>>>>>
@app.route('/getdatatesting',methods=['GET'])
def getdatatesting():
    if request.method == 'GET':
        complete_data = request.args

        name = request.args.get('name')
        option = request.args.get('options')

        return  [name,option]


if __name__=="__main__":
    app.run(debug=True)