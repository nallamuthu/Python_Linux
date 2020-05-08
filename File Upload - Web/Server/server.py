from flask import *  
app = Flask(__name__)  


@app.route('/', methods = ['POST'])  
def success():
    headers = request.headers
    pwd = headers.get("Authorization")
    if request.method == 'POST' and pwd=='any_password':  
        f = request.files['file']
        f.save(f.filename)  
        return "success"
    else:
        return "Authentication Failed"
      
  
if __name__ == '__main__':  
    app.run(debug = True,host='0.0.0.0', port=7410)