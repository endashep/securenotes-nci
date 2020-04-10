from securenotes import app
from flask_talisman import Talisman

if __name__ == '__main__':
    Talisman(app)
    app.run()
