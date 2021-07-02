from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(20), nullable=False)
    destination = db.Column(db.String(20), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)


# SELECT * FROM flights; => Flight.query.all()
# SELECT * FROM flights WHERE origin = "paris"; => Flight.query.filter_by(origin="Paris").all()
# SELECT * FROM flights WHERE origin = "paris" LIMIT 1; => Flight.query.filter_by(origin="Paris").first()
# SELECT COUNT(*) FROM flights WHERE origin = "paris"; => Flight.query.filter_by(origin="Paris").count() means return number of rows that match to fliter_by.
# SELECT * FROM flights WHERE id = 28; => Flight.query.get(28)
# UPDATE flights SET duration = 200 WHERE id = 6; => fight = Flight.query.get(6)
#                                                    flight.duration = 280
# DELETE FROM flights WHERE id = 6; => fight = Flight.query.get(6)
#                                      db.session.delete(flight)
# SELECT * FROM flights ORDER BY origin; => Flight.query.order_by(Flight.origin).all()
# SELECT * FROM flights ORDER BY origin DESC; => Flight.query.order_by(Flight.origin.desc()).all()
# SELECT * FROM flights WHERE origin != "paris"; => Flight.query.filter(Flight.origin != "Paris").all()
# SELECT * FROM flights WHERE origin LIKE "%a%"; =>  Flight.query.filter(Flight.origin.like("%a%")).all()
# SELECT * FROM flights WHERE origin IN ("Tokyo", "Paris"); => Flight.query.filter(Flight.origin.in_(["Tokyo", "Paris"])).all()
# SELECT * FROM flights WHERE origin = "paris" AND duration > 500; => Flight.query.filter(and_(Flight.origin == "Paris", Flight.duration > 500)).all() as well as or_

# SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id; => db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()
