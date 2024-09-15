from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instruction from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table (new table)
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

class FavoritePlaces(base):
    __tablename__ = "FavoritePlaces"
    id = Column(Integer, primary_key=True)
    place_name = Column(String)
    city = Column(String)
    country = Column(String)
    year_first_visited = Column(Integer, primary_key=False)
    special_about = Column(String)

class CitiesVisited(base):
    __tablename__ = "CitiesVisited"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    country = Column(String)
    year_first_visited = Column(Integer, primary_key=False)
    famous_for = Column(String)



# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# toes_beach = FavoritePlaces(
#     place_name = "Toes Beach",
#     city = "Playa del Rey CA",
#     country = "USA",
#     year_first_visited = 1970,
#     special_about = "Childhood hangout"
# )

# moonlight_beach = FavoritePlaces(
#     place_name = "Moonlight Beach",
#     city = "Encinitas CA",
#     country = "USA",
#     year_first_visited = 2008,
#     special_about = "Fun summers"
# )

# moms_house = FavoritePlaces(
#     place_name = "Mom's House",
#     city = "La Jolla CA",
#     country = "USA",
#     year_first_visited = 2022,
#     special_about = "Family"
# )

# beacons_beach = FavoritePlaces(
#     place_name = "Beacons",
#     city = "Encinitas CA",
#     country = "USA",
#     year_first_visited = 2016,
#     special_about = "Uncrowded, narrow beach with fun waves"
# )

# gillis_beach = FavoritePlaces(
#     place_name = "Gillis Beach",
#     city = "Playa del Rey CA",
#     country = "USA",
#     year_first_visited = 1973,
#     special_about = "Endless, carefree summers"
# )

# san_diego = FavoritePlaces(
#     place_name = "San Diego",
#     city = "San Diego",
#     country = "USA",
#     year_first_visited = 1971,
#     special_about = "Great House Music scene"
# )


# madrid = CitiesVisited(
#     city = "Madrid",
#     country = "Spain",
#     year_first_visited = 1988,
#     famous_for = "El Prado Museum"
# )

# seattle = CitiesVisited(
#     city = "Seattle",
#     country = "USA",
#     year_first_visited = 2020,
#     famous_for = "Space Needle"
# )
# sevilla = CitiesVisited(
#     city = "Sevilla",
#     country = "Spain",
#     year_first_visited = 1988,
#     famous_for = "Flamenco"
# )

# geneva = CitiesVisited(
#     city = "Geneva",
#     country = "Switzerland",
#     year_first_visited = 1997,
#     famous_for = "UN Headquarters"
# )

# session.add(toes_beach)
# session.add(moonlight_beach)
# session.add(moms_house)
# session.add(beacons_beach)
# session.add(gillis_beach)
# session.add(san_diego)
# session.add(madrid)
# session.add(seattle)
# session.add(sevilla)
# session.add(geneva)

# session.commit()


# # creating records on our Programmer table
# ada_lovelace = Programmer(
#     first_name = "Ada",
#     last_name = "Lovelace",
#     gender = "F",
#     nationality = "British",
#     famous_for = "First Programmer"
# )

# alan_turing = Programmer(
#     first_name = "Alan",
#     last_name = "Turing",
#     gender = "M",
#     nationality = "British",
#     famous_for = "Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name = "Grace",
#     last_name = "Hopper",
#     gender = "F",
#     nationality = "American",
#     famous_for = "COBOL language"
# )

# margaret_hamilton = Programmer(
#     first_name = "Margaret",
#     last_name = "Hamilton",
#     gender = "F",
#     nationality = "American",
#     famous_for = "Apollo 11"
# )

# bill_gates = Programmer(
#     first_name = "Bill",
#     last_name = "Gates",
#     gender = "M",
#     nationality = "American",
#     famous_for = "Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name = "Tim",
#     last_name = "Berners-Lee",
#     gender = "M",
#     nationality = "British",
#     famous_for = "World Wide Web"
# )

# chrissy_carter = Programmer(
#     first_name = "Chrissy",
#     last_name = "Carter",
#     gender = "F",
#     nationality = "American-Irish",
#     famous_for = "Bodysurfer"
# )

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(chrissy_carter)

# commit our session to the database
# session.commit()

# Updating a single record
# programmer = session.query(Programmer).filter_by(id=9).first()
# programmer.famous_for = "World President"


# Updating multiple records

# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")


# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )

# query the database to find all FavoritePlaces
places = session.query(FavoritePlaces)
for place in places:
    print(
        place.id,
        place.place_name,
        sep=" | "
    )

# cities = session.query(CitiesVisited)
# for city in cities:
#     print(
#         city.id,
#         city.city,
#         city.country,
#         city.year_first_visited,
#         sep=" | "
#     )


# deleting a single record
# placetodelete = input("Enter a place to delete: ")
# place = session.query(FavoritePlaces).filter_by(place_name=placetodelete).first()
# # # defensive programming
# if place is not None:
#     print("Place Found: ", "place.place_name")
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(place)
#         session.commit()
#         print("Place has been deleted")
#     else:
#         print("Place not deleted")
# else:
#     print("No records found")
