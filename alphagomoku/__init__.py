from flask import Flask, g, render_template


def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html')

    @app.errorhandler(500)
    def server_error(error):
        err_msg = str(error)
        return render_template('500.html', err_msg=err_msg), 500

    @app.route('/')
    def index():
        return render_template('index.html')

    return app