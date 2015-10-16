import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "mzvast",
                           passwd = "",
                           db = "c9")
    c = conn.cursor()

    return c, conn