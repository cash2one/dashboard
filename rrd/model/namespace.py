# -*- coding:utf-8 -*-
from rrd.store import dashboard_db_conn as db_conn
from flask import flash


def namespace():
    sql = "select * from dashboard_screen"
    cursor = db_conn.execute(sql)
    rows = cursor.fetchall()
    cursor and cursor.close()
    namespace_list = {}
    for r in rows:
        sql = "select * from dashboard_screen where pid=%d" % r[0]
        cursor = db_conn.execute(sql)
        hasleaft = cursor.fetchone()
        cursor and cursor.close()
        if not hasleaft:
            namespace_list[r[2]] = r[0]
    namespace_list = sorted(namespace_list.iteritems(), key=lambda d: d[0])
    return namespace_list


def get_screen(user):
    cursor = db_conn.execute('''select namespace,screen_id from user_screen where user=%s''', (user,))
    result = cursor.fetchall()
    cursor and cursor.close()
    return result


def exist(user, namespace):
    cursor = db_conn.execute('''select * from user_screen where user=%s and namespace=%s''', (user, namespace))
    result = cursor.fetchone()
    cursor and cursor.close()
    return result


def add_screen(user, namespace, screen_id):
    if not exist(user, namespace):
        cursor = db_conn.execute('''insert into user_screen(user,namespace,screen_id) values(%s,%s,%s)''', (user, namespace, screen_id))
        db_conn.commit()
        cursor and cursor.close()
    else:
        flash(u"名字已经存在,请重新输入一个名字")


def delete_screen(user, namespace):
    cursor = db_conn.execute('''delete from user_screen where user=%s and namespace=%s''', (user, namespace))
    db_conn.commit()
    cursor and cursor.close()


def update_screen(user, oldname, newname):
    if not exist(user, newname):
        cursor = db_conn.execute('''update user_screen set namespace=%s where user=%s and namespace=%s''', (newname, user, oldname))
        db_conn.commit()
        cursor and cursor.close()
    else:
        flash(u"名字已经存在,请重新输入一个名字!")


def get_screen_by_name(group_name, screen_name):
    sql = "select id from dashboard_screen where name='%s'" % group_name
    cursor = db_conn.execute(sql)
    group_id = cursor.fetchone()
    cursor and cursor.close()
    if group_id is None:
        return None
    cursor = db_conn.execute('''select id from dashboard_screen where name=%s and pid=%s''', (screen_name, group_id[0]))
    screen_id = cursor.fetchone()
    cursor and cursor.close()
    if screen_id is not None:
        return screen_id[0]
    return None


if __name__ == "__main__":
    print get_screen_by_name("oc_haproxy", "a1.go2yd.com")
