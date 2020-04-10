from securenotes import app
from flask_talisman import Talisman

if __name__ == '__main__':
    talisman = Talisman(app)
    app.run()
