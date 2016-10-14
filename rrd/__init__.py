#-*- coding:utf-8 -*-
from flask import Flask, request, session, g, make_response, redirect
from rrd.uic import uic

import urllib
#-- create app --
app = Flask(__name__)
app.config.from_object("rrd.config")


@app.errorhandler(Exception)
def all_exception_handler(error):
    print "exception: %s" %error
    return u'''dashboard暂时无法访问管理员''', 500


@app.before_request
def before_request():
    if 'user_name' in session and session['user_name']:
        g.user_name = session['user_name']
    else:
        sig = request.cookies.get('sig')
        if not sig:
            return redirect_to_sso()

        username = uic.username_from_sso(sig)
        if not username:
            return redirect_to_sso()

        session['user_name'] = username
        g.user_name = session['user_name']


def redirect_to_sso():
    sig = uic.gen_sig()
    resp = make_response(redirect(uic.login_url(sig, urllib.quote(request.url))))
    resp.set_cookie('sig', sig)
    return resp

from view import api, chart, screen, index
