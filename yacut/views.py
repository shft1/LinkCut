from flask import flash, redirect, render_template

from services.snippets import get_unique_short_id

from . import app, db
from .forms import LinkForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    if form.validate_on_submit():
        short_id = form.custom_id.data
        if URLMap.query.filter_by(short=short_id).first() is not None:
            flash(f'Предложенный вариант короткой ссылки уже существует.'
                  f'{short_id}', 'err')
            return render_template('main.html', form=form)
        unique_short = get_unique_short_id(short_id)
        url_map = URLMap(
            original=form.original_link.data,
            short=unique_short
        )
        db.session.add(url_map)
        db.session.commit()
        flash('Ваша новая ссылка готова:', 'inf')
        return render_template('main.html', form=form, object=url_map)
    return render_template('main.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url.original)
