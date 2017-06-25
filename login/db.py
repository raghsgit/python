import sqlite3
conn=sqlite3.connect("login.db")
conn.row_factory = sqlite3.Row
c=conn.cursor();
c.execute("create table if not exists pythlog(name text ,pwd text ,disc text)")

def add(name,pwd,disc="No description"):
    c.execute("insert into pythlog values(?,?,?)",(name,pwd,disc,))
    conn.commit()

def adddisc(name,pwd,disc="NO DISCRIPTION"):
    c.execute("update pythlog set disc=? where name=? and pwd =?",(disc,name,pwd,))
    conn.commit()

def contains(name):
    count=c.execute("select count(name) from pythlog where name=?",(name,))
    conn.commit()
    count=count.fetchone()[0]
    if count>0:
        return True
    else:
        return False

def contain(name,pwd):
    count=c.execute("select count(name) from pythlog where name=? and pwd=?",(name,pwd,))
    conn.commit()
    count=count.fetchone()[0]
    if count>0:
        return True
    else:
        return False

def discription(name,pwd):
    disc=c.execute("select disc from pythlog where name=? and pwd=?",(name,pwd,))
    conn.commit()
    return disc.fetchone()[0]

def delete(name,pwd):
    c.execute("delete from pythlog where name=? and pwd=?",(name,pwd,))
    conn.commit()
def view():
    op=c.execute("select * from pythlog")
    conn.commit()
    print("{0:<15s}{1:<20s}{2:<s}".format("name","password","discription"))
    print("{:-<60s}".format(""))
    for o in op:
        print("{0:<15s}{1:<20s}{2:<s}".format(o[0],o[1],o[2]))

def close():
    conn.close()
