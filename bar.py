from flask import Blueprint, render_template, url_for, redirect

bar = Blueprint('bar', __name__)


# home
@bar.route('/home')
def to_home():
    return redirect(url_for('index.turn_index'))


# about us
@bar.route('/about us')
def turn_us():
    return render_template('about-us.html')


@bar.route('/aboutus')
def to_us():
    return redirect(url_for('bar.turn_us'))


# services
@bar.route('/services')
def turn_service():
    return "not design"


# portfolio
@bar.route('/protfolio')
def turn_protfolio():
    return "bot design"


# blog single
@bar.route('/blogsingle')
def turn_blogsingle():
    return "not design"


# pricing
@bar.route('/pricing')
def turn_pricing():
    return "not design"


# 404
@bar.route('/404')
def error_404():
    return render_template('404.html')


# blog
@bar.route('/blog')
def turn_blog():
    return "not design"


# contact
@bar.route('/contact')
def turn_contact():
    return "not design"
