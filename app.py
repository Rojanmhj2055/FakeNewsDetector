from flask import Flask ,render_template,request
import requests
import function
import keys
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',source="",answer="")

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method =='POST':
     mynews =  request.form.get('mynews')
     
     label = function.get_prediction(mynews)
     
     data = requests.get("http://api.giphy.com/v1/gifs/random?api_key={}&tag={}&limit=1".format(keys.apikey,label))
     res=data.json()
     pic= res['data']['images']['original']['url']
     
     return render_template('index.html',source=pic,answer=label)
    else:
        return render_template('error.html') 


app.run()