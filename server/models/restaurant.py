from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    # One to Many relationship with RestaurantPizza
    restaurant_pizzas = relationship("RestaurantPizza", back_populates="restaurant", cascade="all, delete-orphan")

                  
    pizzas = relationship("Pizza", secondary="restaurant_pizzas", back_populates="restaurants")
