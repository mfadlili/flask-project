from base import db, Puppy

db.create_all()

doggy = Puppy('Doggy')
anjing = Puppy('Anjing')

db.session.add_all([doggy, anjing])
db.session.commit()

print(doggy.id)
print(anjing.id)