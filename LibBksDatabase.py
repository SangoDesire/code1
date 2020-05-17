import sqlite3


# backend
def ConnectData():
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS libbooks (id INTEGER PRIMARY KEY ,Mty text,Ref text,Tit text,fna text, \
        sna text,Adr1 text,Adr2 text,pcd text, MNo text,BkID text ,Bkt text,Atr text,DBo text ,Ddu text ,sPr text,\
         LrF text, DoD text, DonL text)")
    con.commit()
    con.close()


def addDataRec (Mty, Ref, Tit, fna, sna, Adr1, Adr2, pcd, MNo, BKID, Bkt, Atr, DBo, Ddu, sPr, LrF, DoD, DonL):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("INSERT INTO libbooks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (Mty, Ref, Tit, fna, sna, Adr1, Adr2, pcd, MNo, BKID, Bkt, Atr, DBo, Ddu, sPr, LrF, DoD, DonL))

    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM libbooks")
    rows = cur.fetchall()
    con.close()
    return rows


def deleteRec(id):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("DELETE FROM 'libbooks' WHERE id=?", (id,))
    con.commit()
    con.close()


def SearchData(Mty="", Ref="", Tit="", fna="", sna="", Adr1="", Adr2="", pcd="", MNo="", BKID="", Bkt="", Atr="", \
               DBo="", Ddu="", sPr="", LrF="", DoD="", DonL=""):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM libbooks WHERE Mty=? OR Ref=? OR Tit=? OR fna=? OR sna=? OR Adr1=? OR Adr2=? \
            OR pcd=? OR MNo=? OR BKID=? OR Bkt=? OR Atr=? OR DBo=? OR Ddu=? OR sPr=? OR LrF=? OR DoD=? OR DonL=?", \
                (Mty, Ref, Tit, fna, sna, Adr1, Adr2, pcd, MNo, BKID, Bkt, Atr, DBo, Ddu, sPr, LrF, DoD, DonL))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, Mty="", Ref="", Tit="", fna="", sna="", Adr1="", Adr2="", pcd="", MNo="", BKID="", Bkt="", Atr="",
               DBo="", Ddu="", sPr="", LrF="", DoD="", DonL=""):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("UPDATE libbooks SET Mty=?,Ref=?,Tit=?,fna=?,sna=?,Adr1=?,Adr2=?,pcd=?,MNo=?,BKID=?,\
                 Bkt=?,Atr=?,DBo=?,Ddu=?,sPr=?,LrF=?,DoD=?,DonL=? WHERE id =?",
                (Mty, Ref, Tit, fna, sna, Adr1, Adr2, pcd, MNo, BKID, Bkt, Atr, DBo, Ddu, sPr, LrF, DoD, DonL, id))

    con.commit()
    con.close()

ConnectData()