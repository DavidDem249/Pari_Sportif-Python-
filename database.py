import sqlite3

# def connect():
#     conn = sqlite3.connect("paris_sportifs.db")
#     cur = conn.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, "
#                 "author TEXT, year INTEGER, isbn INTEGER)")
#     conn.commit()
#     conn.close()

def insertResu(equipe1, score1, score2, equipe2):
    conn = sqlite3.connect("paris_sportifs.db")
    cur = conn.cursor()
    #the NULL parameter is for the auto-incremented id
    cur.execute("INSERT INTO resultat VALUES(NULL,?,?,?,?)", (equipe1, score1, score2, equipe2))
    conn.commit()
    conn.close()

def insertChoix(equipe1, equipe2, choix, pari, mise, gain):
    conn = sqlite3.connect("paris_sportifs.db")
    cur = conn.cursor()
    #the NULL parameter is for the auto-incremented id
    cur.execute("INSERT INTO paris VALUES(NULL,?,?,?,?,?,?)", (equipe1, equipe2, choix, pari, mise, gain))
    conn.commit()
    conn.close()


def insertDemande(username, montat, code):
    conn = sqlite3.connect("paris_sportifs.db")
    cur = conn.cursor()
    #the NULL parameter is for the auto-incremented id
    cur.execute("INSERT INTO demande VALUES(NULL,?,?,?)", (username, montat, code))
    conn.commit()
    conn.close()


def viewUser():
    conn = sqlite3.connect("paris_sportifs.db")
    cur = conn.cursor()
    cur.execute("SELECT username, compte FROM users")
    rows = cur.fetchall()
    conn.close()
    return rows

def viewDemande():
    conn = sqlite3.connect("paris_sportifs.db")
    cur = conn.cursor()
    cur.execute("SELECT username, montat, code FROM demande")
    rows = cur.fetchall()
    conn.close()
    return rows


def viewMatch():
    conn = sqlite3.connect("paris_sportifs.db")
    cur = conn.cursor()
    cur.execute("SELECT equipe1,score1,score2,equipe2 FROM resultat")
    rows = cur.fetchall()
    conn.close()
    return rows


def viewChoixPari():
    conn = sqlite3.connect("paris_sportifs.db")
    cur = conn.cursor()
    cur.execute("SELECT equipe1, equipe2, choix, pari, mise, gain FROM paris")
    rows = cur.fetchall()
    conn.close()
    return rows


# def delete(id):
#     conn = sqlite3.connect("books.db")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM book WHERE id = ?", (id,))
#     conn.commit()
#     conn.close()

def update(id, compte):
    conn = sqlite3.connect("paris_sportifs.db")
    cur = conn.cursor()
    cur.execute("UPDATE users SET compte = ? WHERE id = ?", (compte, id))
    conn.commit()
    conn.close()

#connect()
#insert("another novel", "James W.", 2017, 1234)
#update(2, title = "new book", author= "DH", year= 2005, isbn= 5555)
#print(view())