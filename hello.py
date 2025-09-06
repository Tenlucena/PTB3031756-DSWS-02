from datetime import datetime
from flask import Flask, render_template, request, make_response, redirect, abort
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

from flask import Flask, render_template, session, redirect, url_for, flash
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data;
        return redirect(url_for('index'));
     return render_template('index.html', form=form, name=session.get('name'))


@app.route('/user/<name>/<prontuario>/<institution>')
def user(name, prontuario, institution):
    return render_template('user.html', 
                           name=name, 
                           prontuario=prontuario,
                           institution=institution);

@app.route('/contextorequisicao/<name>')
def contextorequisicao(name):
    user_agent = request.headers.get('User-Agent');
    remote_addr = request.remote_addr;
    remote_host = request.host;
    return render_template('contexto.html',
                           name=name, 
                           user_agent=user_agent, 
                           remote_addr=remote_addr,
                           remote_host=remote_host);

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
