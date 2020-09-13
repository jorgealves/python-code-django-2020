from .application import app

application = app

# http://flask.pocoo.org/docs/0.10/deploying/wsgi-standalone/#proxy-setups
from werkzeug.contrib.fixers import ProxyFix

application.wsgi_app = ProxyFix(application.wsgi_app)

debug = None

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=debug)
