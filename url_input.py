from flask import Flask ,redirect,url_for
app = Flask(__name__)

@app.route('/')
def home():
    return "Home page"

@app.route('/input1/<name>')  #http://127.0.0.1:5000/input1/hariram
def input1(name):
    return str(name)

@app.route('/input2/<int:age>')  #http://127.0.0.1:5000/input/25
def input2(age):
    return str(age)

@app.route('/input3/<name>/<int:age>')
# http://127.0.0.1:5000/input3/rah/25
def input3(name, age):
    if name and age:
        return f"My name is {name} and I am {age} years old"


#use case of redirect function 
@app.route('/switched')
def switched():
    return "I open by the redirect function!"

@app.route('/switchto')
# http://127.0.0.1:5000/switchto <-- to open  http://127.0.0.1:5000/switched
def switchto():
    return redirect('switched')


@app.route('/fail/<int:marks>')
def fail(marks):
    return f"Fail with {marks} score"

@app.route('/success/<int:marks>')
def success(marks):
    return f"success with {marks} score"


@app.route('/result/<int:totalMarks>')
#http://127.0.0.1:5000/result/52
def result(totalMarks):
    result = ""
    if totalMarks <= 34:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result,marks=totalMarks))


@app.route('/autoresult')  # <-- to open result by the program
def autoresult():
    return redirect(url_for('result',totalMarks=52))



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=2525,debug=True)