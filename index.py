from flask import *
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/register')

def register():
 
    return render_template('register.html')
@app.route('/save',methods=['POST'])
def save():
    registered_users = {}
    
    registered_users.update(request.form)
    print(registered_users)
    with open('registered.txt','a') as f1:
        f1.write(str(registered_users))
    return render_template('successfully.html',display=request.form)

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
