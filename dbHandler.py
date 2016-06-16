#!/usr/bin/env python3
import sqlite3

def init(dbPath):
    print("[DB] Starting database")
    global c
    global db
    db = sqlite3.connect(dbPath + "/groups.db")
    c = db.cursor()

def newGroup(username):
    print("[DB] Creating new group")
    c.execute("CREATE TABLE IF NOT EXISTS " + username + " (posX INTEGER, posY INTEGER)")

def end():
    try:
        db.commit()
        db.close()
        print("[DB] Closing the connection to the database was succesful")
        return True
    except:
        print("[DB] Closing the connection to the database failed")
        return False

if __name__ == "__main__":
    print("This is a module you fool!")
