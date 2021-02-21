from flask import Flask ,render_template,request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method =='POST':
      return render_template('index.html')
    else:
        return render_template('error.html') 


app.run()