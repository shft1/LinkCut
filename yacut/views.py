import random

from flask import render_template

from . import app
from .forms import LinkForm


def get_unique_short_id():
    choices = ([chr(i) for i in range(48, 58)] +
               [chr(i) for i in range(65, 91)] +
               [chr(i) for i in range(97, 123)])
    return ''.join(random.choices(choices, k=6))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    if form.validate_on_submit():
        pass
    return render_template('main.html', form=form)
