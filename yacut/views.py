from flask import render_template

from . import app
from .forms import LinkForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    if form.validate_on_submit():
        pass
    return render_template('main.html', form=form)
