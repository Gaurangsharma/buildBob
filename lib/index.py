from flask import *

class Index:
    def __init__(self):
        pass

    @staticmethod
    def show_index(app):
        global render_to
        try:
            render_to='index.html'
        except KeyError:
            render_to='login.html'
        return render_template(
            render_to,
            title="Gs",
            message="gp",
            app=app
        )


