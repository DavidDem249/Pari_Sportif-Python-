import sqlite3


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



def update(id, compte):
    conn = sqlite3.connect("paris_sportifs.db")
    cur = conn.cursor()
    cur.execute("UPDATE users SET compte = ? WHERE id = ?", (compte, id))
    conn.commit()
    conn.close()

