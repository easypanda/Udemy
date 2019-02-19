#Create entries into the tables

from model import db,Puppy,Owner,Toy

#Creating 2 puppies

rufus = Puppy("Rufus")
fido = Puppy("Fido")

#Add puppies to db

db.session.add_all([rufus,fido])
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name="Rufus").first()

# Create owner object

jose = Owner("Jose",rufus.id)

#Give Rufus some report_toys

toy1 = Toy("Chew Toy",rufus.id)
toy2 = Toy("Ball",rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

#GRAB RUFUS AFTER THOSE ADDITIONS

rufus = Puppy.query.filter_by(name="Rufus").first()
print(rufus)

print(rufus.report_toys)
