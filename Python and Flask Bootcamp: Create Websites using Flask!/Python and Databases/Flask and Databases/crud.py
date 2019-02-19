from basic import db,Puppy

## Create ##
my_puppy = Puppy("Rufus",5)
db.session.add(my_puppy)
db.session.commit()

## Read ##
all_puppies = Puppy.query.all() #list of puppies objects in the table!

print(all_puppies)

# SELECT BY ID

puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# FILTERS
puppy_frankie = Puppy.query.filter_by(name="Frankie")
print(puppy_frankie.all())

## UPDATE

first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

## DELETE

second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

#
all_puppies = Puppy.query.all()
print(all_puppies)
