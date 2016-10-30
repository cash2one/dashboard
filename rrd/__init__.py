#-*- coding:utf-8 -*-
from flask import Flask, request, session, g, make_response, redirect
from rrd.uic import uic

import urllib
#-- create app --
app = Flask(__name__)
app.config.from_object("rrd.config")

IGNORE_PREFIX = ['/api', '/screen/logout']


@app.errorhandler(Exception)
def all_exception_handler(error):
    print "exception: %s" %error
    return u'''dashboard暂时无法访问''', 500


@app.before_request
def before_request():
    p = request.path
    for ignore_pre in IGNORE_PREFIX:
        if p.startswith(ignore_pre):
            return

    if 'user_name' in session and session['user_name']:
        g.user_name = session['user_name']
    else:
        sig = request.cookies.get('sig')
        if not sig:
            username = ""
        else:
            username = uic.username_from_sso(sig)
            if not username:
                username = ""

        session['user_name'] = username
        g.user_name = session['user_name']


from view import api, chart, screen, index
