from flask import render_template
from app import app

@app.errorhandler(404)
def four_zero_four(error):
    '''
    Function that Renders the 404 Page
    '''
    return render_template('fourowfour.html'),404