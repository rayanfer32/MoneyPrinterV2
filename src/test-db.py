from tinydb import TinyDB, Query

# Initialize DB
db = TinyDB('data.json')

# Insert Data
db.insert({'type': 'subject', 'value': 'univrse bullshit'})
db.insert({'type': 'subject', 'value': 'another universe bullshit'})

# Query Data
query = Query()
print(query)
result = db.search(query.type == 'subject')
for r in result:
    print(r.get('value'))

# Update Data
# db.update({'age': 31}, User.name == 'John')

# Delete Data
# db.remove(User.name == 'John')
