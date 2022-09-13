from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
pet1 = Pet(name="Alan", species="dog", photo_url="https://cdn.pixabay.com/photo/2017/09/25/13/12/cocker-spaniel-2785074_960_720.jpg", age=2)
pet2 = Pet(name="Joel", species="cat", photo_url="https://cdn.pixabay.com/photo/2015/03/27/13/16/maine-coon-694730_960_720.jpg", age=3, available=False)
pet3 = Pet(name="Jane", species="dog", photo_url="https://cdn.pixabay.com/photo/2014/12/03/05/48/dog-555067_960_720.jpg", age=7, notes="Jane is lovely, but has bad breath.")
pet4 = Pet(name="Bubbles", species="mouse", photo_url="https://cdn.pixabay.com/photo/2016/10/01/20/54/mouse-1708347_960_720.jpg", age=1)

# Add new objects to session
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)

db.session.commit()
