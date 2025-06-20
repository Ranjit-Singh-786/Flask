from flask import Flask , request 
app = Flask(__name__) 

@app.route("/recieve",methods=['POST'])
def home():
    data = request.json 
    if data:
        print(data)
        return data 
    else:
        print("unable")
        return "unable to recieve"

if __name__== "__main__":
    app.run(port=1452,debug=True)

    