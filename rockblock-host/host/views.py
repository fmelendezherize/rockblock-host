from .rockblock_host import app

@app.route('/')
def index():
    return 'Index Page'

