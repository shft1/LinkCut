import random

from flask import flash, redirect, render_template

from . import app, db
from .forms import LinkForm
from .models import URLMap


def get_unique_short_id():
    choices = ([chr(i) for i in range(48, 58)] +
               [chr(i) for i in range(65, 91)] +
               [chr(i) for i in range(97, 123)])
    short_id = ''.join(random.choices(choices, k=6))
    while URLMap.query.filter_by(short=short_id).first() is not None:
        short_id = ''.join(random.choices(choices, k=6))
    return short_id


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.',
                  'err')
            return render_template('main.html', form=form)
        if custom_id == '':
            custom_id = get_unique_short_id()
        url_map = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(url_map)
        db.session.commit()
        flash('Ваша новая ссылка готова:',
              'inf')
        return render_template('main.html', form=form, object=url_map)
    return render_template('main.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url.original)
