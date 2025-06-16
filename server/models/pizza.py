from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)

    # One-to-Many relationship with RestaurantPizza
    restaurant_pizzas = relationship("RestaurantPizza", back_populates="pizza")

    # Optional: access restaurants through join table
    restaurants = relationship("Restaurant", secondary="restaurant_pizzas", back_populates="pizzas")
