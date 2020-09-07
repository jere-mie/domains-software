from flask import render_template, url_for, flash, redirect, request
from website import app, db
from website.forms import UploadForm
# from flask_uploads import configure_uploads, IMAGES, UploadSet
import os

# from website.models import Project, User
# from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/new', methods=['GET', 'POST'])
# @login_required
def new():
    form = UploadForm()
    if form.validate_on_submit():
        if not os.path.exists("website/uploads/data"):
            os.mkdir("website/uploads/data")

        form.image.data.save("website/uploads/data/"+form.image.data.filename)
        print(form.image.data)
    #     project = Project(author=form.author.data, title=form.title.data, content=form.content.data)
    #     db.session.add(project)
    #     db.session.commit()
    #     flash(f'Created project {form.title.data}!', 'success')
    #     return redirect(url_for('home'))
    # return render_template('new.html', form=form, legend='New Project')
    return render_template('new.html', form=form)
