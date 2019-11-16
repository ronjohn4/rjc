from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Var
from app.forms import DetailForm


# navigation --------------------------
@app.route('/')
@app.route('/index')
def index():
    var = Var.query.all()
    return render_template('index.html', data=var)


@app.route('/detail/<int:id>')
def detail(id):
    var = Var.query.filter_by(id=id).first_or_404()
    form = DetailForm(id=var.id, name=var.name, val=var.val)
    return render_template('display.html', form=form)


@app.route('/edit/<int:id>')
def edit(id):
    var = Var.query.filter_by(id=id).first_or_404()
    form = DetailForm(id=var.id, name=var.name, val=var.val)
    return render_template('edit.html', form=form)


# navigation and action ----------------------
@app.route('/add', methods=["GET", "POST"])
def add():
    form = DetailForm()
    if form.validate_on_submit():
        var = Var(name=request.form['name'], val=request.form['val'])
        db.session.add(var)
        db.session.commit()
        flash(f'Added:{var}')
        app.logger.info(f'Added:{var}')
        return redirect(url_for('index'))

    return render_template('add.html', form=form)


# actions --------------------------------
@app.route('/save', methods=["GET", "POST"])
def save():
    if request.method == 'POST':
        id = request.form['id']
        var = Var.query.filter_by(id=id).first_or_404()
        var.name = request.form['name']
        var.val = request.form['val']
        db.session.commit()

        flash(f'Saved:{var}')
        app.logger.info(f'Saved:{var}')
    return redirect(url_for('index'))


# todo - double check delete
@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    Var.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('index'))
