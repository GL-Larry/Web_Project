from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
    return redirect(url_for('index.turn_index'))
#
#
# @app.route('/hht')
# def youke():
#     return redirect(url_for('hello'))
#
#
# @app.route('/test', methods=['POST', 'GET'])
# def say_hello():
#     return 'hello'
#
#
# @app.route('/te')
# def test():
#     return render_template('test.html')


if __name__ == '__main__':
    import index
    app.register_blueprint(index.index)
    from bar import *
    app.register_blueprint(bar)
    app.run()
