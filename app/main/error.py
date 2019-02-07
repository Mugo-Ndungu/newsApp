from flask import render_template
from . import main

@main.errorhandler(404)
def four_zero_four(error):
    '''
    Function that Renders the 404 Page
    '''
    return render_template('fourowfour.html'),404


@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourowfour.html'),404