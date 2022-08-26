from flask import *
app = Flask(__name__)
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/save',methods=['POST'])
def save():
    return render_template('succesfully.html',display=request.form)

@app.route('/login')
def login():
    return render_template('login.html')
def auth():
    response=dict(request.form)
    if(response['usertxt']=='admin' and response['passtxt']=='admin123'):
        return render_template('todo.html',response=response)
    else:
        return render_template('error.html')
app.run()
