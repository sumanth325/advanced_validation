# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    email=request.form['email']
    session['email']= email
    print (email)
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!", 'name')
    elif len(request.form['name']) <= 3:
        flash("Name must be 3+ characters", 'name')
    name = request.form['name']
    session['name']=name
    
    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!" 'comment')
    elif len(request.form['comment']) > 100:
        flash("Comment must be less than 100 characters", 'comment')
    comment = request.form['comment']
    session['comment']=comment
            
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return redirect("/success")

@app.route('/success', methods=['GET'])
def sunny():
    print ('success')
    return render_template("success.html")

if __name__=="__main__":
    app.run(debug=True)