from . import app


@app.route('/')
def hello():
    return 'Привет!'