#!/usr/bin/env python3
import sqlite3

def init(dbPath):
    print("[DB] Starting database")
    db = sqlite3.connect(dbPath + "/groups.db")
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS groupses
             (date text, trans text, symbol text, qty real, price real)''')
    db.commit()
    db.close()

def test():
    print("dank test man")

if __name__ == "__main__":
    print("This is a library you fool!")
