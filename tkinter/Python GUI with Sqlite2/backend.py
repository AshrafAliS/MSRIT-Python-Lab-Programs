import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS std (id INTEGER PRIMARY KEY, usn TEXT, name TEXT, mobile INTEGER, branch TEXT)")
        self.conn.commit()

    def insert(self,usn, name, mobile, branch):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO std VALUES(NULL,?,?,?,?)", (usn,name,mobile,branch))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM std")
        rows = self.cur.fetchall()
        return rows

    def search(self,usn="", name="", mobile="", branch=""):
        self.cur.execute("SELECT * FROM std WHERE usn = ? OR name = ? OR mobile = ? OR branch = ?", (usn, name, mobile, branch))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM std WHERE id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id, usn, name, mobile, branch):
        self.cur.execute("UPDATE std SET usn = ?, name = ?, mobile = ?, branch = ? WHERE id = ?", (usn, name, mobile, branch, id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()
