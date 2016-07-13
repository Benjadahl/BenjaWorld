#!/usr/bin/env python3
import sqlite3

def init(dbPath):
    print("[DB] Starting database")
    global path
    path = dbPath
    prepare("gamedata.db")
    c.execute("CREATE TABLE IF NOT EXISTS groups (userID INTEGER, posX INTEGER DEFAULT 0, posY INTEGER DEFAULT 0)")
    end()

def prepare(dbName):
    global db
    global c
    db = sqlite3.connect(path + dbName)
    c = db.cursor()

def newGroup(username):
    print("[DB] Creating new group")
    prepare("gamedata.db")
    c.execute("INSERT INTO groups (userID) VALUES (" + username + ")")
    db.commit()
    db.close()

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
