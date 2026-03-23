import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# The 5 Indian Legends
legends = [
    ('Chhatrapati Shivaji Maharaj', 'The founder of the Maratha Empire known for his military strategy.'),
    ('Rani Lakshmibai', 'The fearless Queen of Jhansi and a symbol of Indian resistance.'),
    ('Emperor Ashoka', 'The great ruler who spread peace and Buddhism across Asia.'),
    ('Birsa Munda', 'A tribal hero who led a major rebellion against the British.'),
    ('Maharana Pratap', 'The brave Rajput king who fought for Mewar at Haldighati.')
]

cur.executemany("INSERT INTO posts (title, content) VALUES (?, ?)", legends)

connection.commit()
connection.close()
print("Success! Table created and 5 legends added.")