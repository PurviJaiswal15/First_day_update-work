from flask import Flask, render_template, request, redirect, session
 
app = Flask(__name__)
 
# secret key for encrypting session data
app.secret_key = 'my_secret_key'
 
# dictionary 
users = {
    'Purvi Jaiswal': '12345',
    'user2': 'password2'
}
 
# To render a login form 
@app.route('/')
def view_form():
    return render_template('login.html')
 
# handling get request -> form inputs value & after submitting you will see in the urls.
@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        username = request.args['username']
        password = request.args['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome Everyone!!!</h1>'
        else:
            return '<h1>Invalid User!</h1>'
    else:
        return render_template('login.html')
 
# handling post request -> form inputs value & values after submitting you will never see in the urls.
@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome Everyone!!!</h1>'
        else:
            return '<h1>i=Invalid User!</h1>'
    else:
        return render_template('login.html')
 
 #run the app locally
if __name__ == '__main__':
    app.run()