from flask import render_template,url_for,flash,redirect
from website.forms import RegistrationForm
from website.models import User
from website import app
from website import db
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,note=form.note.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Message Send Successfully !','success')
        return redirect(url_for('home'))

    return render_template('avengersregister.html',title='Register',form=form)