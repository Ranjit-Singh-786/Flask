from flask import Flask, jsonify ,request

app = Flask(__name__) 

@app.route('/time',methods=['GET'])
def time():
    return jsonify({'status':'welocome at timezone'})

@app.route('/upload',methods=['POST'])
def upload():
    file1 = request.files['file1']
    file2 = request.files['file2'] 

    # user_name = request.form.get('name')
    # json_data = request.json
    # print(data,'\n','\n',user_name)
    if file1 and file2:
        # print(json_data)
        return jsonify({'status':'successfully recieved your data'})

    else:
        return jsonify({'status':'failed to recieved your data'})
    
if __name__ == "__main__":
    app.run(debug=True)
