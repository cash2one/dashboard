#-*-coding:utf8-*-
import os
#-- dashboard db config --
DASHBOARD_DB_HOST = "10.103.18.17"
DASHBOARD_DB_PORT = 3306
DASHBOARD_DB_USER = "falcon"
DASHBOARD_DB_PASSWD = "b4b16bfe"
DASHBOARD_DB_NAME = "dashboard"

#-- graph db config --
GRAPH_DB_HOST = "10.103.18.17"
GRAPH_DB_PORT = 3306
GRAPH_DB_USER = "falcon"
GRAPH_DB_PASSWD = "b4b16bfe"
GRAPH_DB_NAME = "graph"



#-- app config --
DEBUG = True
SECRET_KEY = "secret-key"
SESSION_COOKIE_NAME = "falcon-dashboard"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30
SITE_COOKIE = "open-falcon-ck"

UIC_ADDRESS = {
    'internal': 'http://10.103.18.17:8080',
    'external': 'http://10.103.18.17:8080',
}

UIC_TOKEN = ''

#-- query config --
QUERY_ADDR = "http://10.103.18.17:9966"
#QUERY_ADDR = "http://10.101.2.35:9966"

BASE_DIR = "/home/worker/falcon_server/dashboard/"
LOG_PATH = os.path.join(BASE_DIR, "log/")

try:
    from rrd.local_config import *
except:
    pass
