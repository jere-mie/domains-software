from flask import render_template, url_for, flash, redirect, request
from website import app, db
from website.forms import UploadForm
# from flask_uploads import configure_uploads, IMAGES, UploadSet
import os
import numpy as np

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
        form.z.data.save("website/uploads/z.txt")
        form.d.data.save("website/uploads/d.txt")
        form.m.data.save("website/uploads/m.txt")
        form.s.data.save("website/uploads/s.txt")
        form.t.data.save("website/uploads/t.txt")
        form.w.data.save("website/uploads/w.txt")
        # form.z.data.save("website/uploads/"+form.z.data.filename)
        # form.d.data.save("website/uploads/"+form.d.data.filename)
        # form.m.data.save("website/uploads/"+form.m.data.filename)
        # form.s.data.save("website/uploads/"+form.s.data.filename)
        # form.t.data.save("website/uploads/"+form.t.data.filename)
        # form.w.data.save("website/uploads/"+form.w.data.filename)
        frm = np.longdouble(form.rm.data)
        fo = np.longdouble(form.o.data)
        fps = np.longdouble(form.ps.data)
        fad = np.longdouble(form.ad.data)
        
        print("success")
    #     project = Project(author=form.author.data, title=form.title.data, content=form.content.data)
    #     db.session.add(project)
    #     db.session.commit()
    #     flash(f'Created project {form.title.data}!', 'success')
    #     return redirect(url_for('home'))
    # return render_template('new.html', form=form, legend='New Project')
    return render_template('new.html', form=form)
