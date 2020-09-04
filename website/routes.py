from flask import render_template, url_for, flash, redirect, request
from website import app, db
# from website.forms import ProjectForm, Login
# from website.models import Project, User
# from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/new', methods=['GET', 'POST'])
# @login_required
def new():
    # form = ProjectForm()
    # if form.validate_on_submit():
    #     project = Project(author=form.author.data, title=form.title.data, content=form.content.data)
    #     db.session.add(project)
    #     db.session.commit()
    #     flash(f'Created project {form.title.data}!', 'success')
    #     return redirect(url_for('home'))
    # return render_template('new.html', form=form, legend='New Project')
    return render_template('new.html')
