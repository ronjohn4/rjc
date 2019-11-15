from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Var
from app.forms import DetailForm


# navigation --------------------------
@app.route('/')
@app.route('/index')
def index():
    print(f'index():{request.method}')
    var = Var.query.all()
    return render_template('index.html', data=var)


@app.route('/detail/<int:id>')
def detail(id):
    print(f'detail({id}):{request.method}')
    var = Var.query.filter_by(id=id).first_or_404()
    form = DetailForm(id=var.id, name=var.name, val=var.val)
    return render_template('detail.html', form=form)


@app.route('/edit/<int:id>')
def edit(id):
    print(f'edit({id}):{request.method}')
    var = Var.query.filter_by(id=id).first_or_404()
    form = DetailForm(id=var.id, name=var.name, val=var.val)
    return render_template('edit.html', form=form)


# actions --------------------------------
@app.route('/save', methods=["GET", "POST"])
def save():
    print(f'save():{request.method}')
    if request.method == 'POST':
        id = request.form['id']
        var = Var.query.filter_by(id=id).first_or_404()
        var.name = request.form['name']
        var.val = request.form['val']
        db.session.commit()

        flash('Saved')
        app.logger.info('Saved')
    return redirect(url_for('index'))


@app.route('/add', methods=["GET", "POST"])
def add():
    print(f'add():{request.method}')
    form = DetailForm()
    if form.validate_on_submit():
        var = Var(name=request.form['name'], val=request.form['val'])
        db.session.add(var)
        db.session.commit()
        flash('Added')
        app.logger.info('Added')
        return redirect(url_for('index'))

    return render_template('add.html', form=form)


# todo - double check delete
@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    print(f'delete({id}):{request.method}')
    Var.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('index'))
