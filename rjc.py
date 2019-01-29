from app import app, db
from app.models import User, Post

# Registers objects for use after 'flask shell' is used from command line
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
