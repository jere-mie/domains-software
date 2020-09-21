from flask import render_template, url_for, flash, redirect, request
from website import app, db
from website.forms import UploadForm, Login, Register
from website.domains import generate
from website.fmat import F
# from flask_uploads import configure_uploads, IMAGES, UploadSet
import os
import numpy as np
from website.models import User, Dataset
from flask_login import login_user, current_user, logout_user, login_required
import bcrypt

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already authenticated','success')
        return redirect(url_for('home'))
    form = Register()
    if form.validate_on_submit():
        hashed = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        user = User(username=form.username.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        if not os.path.exists(f"website/static/uploads/{form.username.data}"):
            os.mkdir(f"website/static/uploads/{form.username.data}")
        flash(f'Created account for {form.username.data}. You may now log in.', 'success')
        return redirect(url_for('login'))

    return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already authenticated','success')
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.checkpw(form.password.data.encode('utf-8'), user.password):
            login_user(user, remember=form.rememberMe.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Error Logging In', 'danger')
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = UploadForm()
    if form.validate_on_submit():
        dataset = Dataset(title=form.title.data, author=current_user, rm=float(form.rm.data), o=float(form.o.data), ps=float(form.ps.data), ad=float(form.ad.data))
        db.session.add(dataset)
        db.session.commit()
        uname = current_user.username
        tit = form.title.data
        if not os.path.exists(f"website/static/uploads/{uname}/{tit}"):
            os.mkdir(f"website/static/uploads/{uname}/{tit}")
        form.z.data.save(f"website/static/uploads/{uname}/{tit}/z.txt")
        form.d.data.save(f"website/static/uploads/{uname}/{tit}/d.txt")
        form.m.data.save(f"website/static/uploads/{uname}/{tit}/m.txt")
        form.s.data.save(f"website/static/uploads/{uname}/{tit}/s.txt")
        form.t.data.save(f"website/static/uploads/{uname}/{tit}/t.txt")
        form.w.data.save(f"website/static/uploads/{uname}/{tit}/w.txt")
        # form.z.data.save("website/uploads/"+form.z.data.filename)
        # form.d.data.save("website/uploads/"+form.d.data.filename)
        # form.m.data.save("website/uploads/"+form.m.data.filename)
        # form.s.data.save("website/uploads/"+form.s.data.filename)
        # form.t.data.save("website/uploads/"+form.t.data.filename)
        # form.w.data.save("website/uploads/"+form.w.data.filename)

        # frm = np.longdouble(form.rm.data)
        # fo = np.longdouble(form.o.data)
        # fps = np.longdouble(form.ps.data)
        # fad = np.longdouble(form.ad.data)
        
        print("success")
    #     project = Project(author=form.author.data, title=form.title.data, content=form.content.data)
    #     db.session.add(project)
    #     db.session.commit()
    #     flash(f'Created project {form.title.data}!', 'success')
    #     return redirect(url_for('home'))
    # return render_template('new.html', form=form, legend='New Project')
    return render_template('new.html', form=form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    datasets = Dataset.query.filter_by(author=current_user).all()
    return render_template('account.html', datasets=datasets)

@app.route('/<ds_id>', methods=['GET', 'POST'])
@login_required
def dataset(ds_id):
    dataset = Dataset.query.get_or_404(ds_id)
    if dataset.author != current_user:
        flash('You are not this dataset\'s owner', 'danger')
        return redirect(url_for('home'))
    return render_template('dataset.html', dataset=dataset)

@app.route('/<ds_id>/compute', methods=['GET', 'POST'])
@login_required
def compute(ds_id):
    dataset = Dataset.query.get_or_404(ds_id)
    if dataset.author != current_user:
        flash('You are not this dataset\'s owner', 'danger')
        return redirect(url_for('home'))
    r = list(range(100,2000))
    generate(F, r, f'website/static/uploads/{uname}/{tit}', dataset.rm, dataset.o, dataset.ps, dataset.ad)
    return render_template('dataset.html', dataset=dataset)