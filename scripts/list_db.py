import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table','view') ORDER BY name")
items = cur.fetchall()
print('objects found:', len(items))
for name, typ in items:
    print('\n--', typ, name)
    try:
        cur.execute(f"SELECT count(*) FROM '{name}'")
        print('rows:', cur.fetchone()[0])
    except Exception as e:
        print('count error:', e)
    try:
        cur.execute(f"PRAGMA table_info('{name}')")
        cols = cur.fetchall()
        if cols:
            print('columns:')
            for c in cols:
                print(' ', c[1], c[2])
    except Exception as e:
        pass

conn.close()
