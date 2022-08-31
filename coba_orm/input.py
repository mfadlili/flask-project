from base import db, Puppy, Owner, Toy

#Create 2 puppies object
db.create_all()

rufus = Puppy('Rufus')
fido = Puppy('Fido')

db.session.add_all([rufus, fido])
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rey = Owner('Rey', rufus.id)

toy1 = Toy('Boomerang', rufus.id)
toy2 = Toy('Bone', rufus.id)

db.session.add_all([rey, toy1, toy2])
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_toys()