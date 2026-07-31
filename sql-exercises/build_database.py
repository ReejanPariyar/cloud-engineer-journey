import sqlite3

conn = sqlite3.connect('practice.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    project_name TEXT,
    owner_id INTEGER
)
''')

cursor.execute("INSERT INTO users (name, role) VALUES ('Reejan', 'Senior Cloud Engineer')")
cursor.execute("INSERT INTO users (name, role) VALUES ('Alex', 'Cloud Security')")
cursor.execute("INSERT INTO projects (project_name, owner_id) VALUES ('cloud-engineer-journey', 1)")
cursor.execute("INSERT INTO projects (project_name, owner_id) VALUES ('security-audit', 2)")

conn.commit()

cursor.execute('''
SELECT users.name, projects.project_name
FROM projects
JOIN users ON projects.owner_id = users.id
''')
print("Projects and their owners:")
for row in cursor.fetchall():
    print(f"- {row[1]} owned by {row[0]}")

conn.close()
