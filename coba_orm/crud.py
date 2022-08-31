from base import db, Puppy

#We would implement CRUD concept here

##Create
# my_dog = Puppy('Kuy', 4)
# db.session.add(my_dog)
# db.session.commit()

##Read
list_puppies = Puppy.query.all()
print(list_puppies)

### Select by id
id_one = Puppy.query.get(1)
print(id_one.name)

### select by name
doggy = Puppy.query.filter_by(name='Doggy')
print(doggy.all())

##Update
first_puppy = Puppy.query.get(1)
db.session.add(first_puppy)
db.session.commit()

##Delete
fifth_puppy = Puppy.query.get(4)
db.session.delete(fifth_puppy)
db.session.commit()