from app import app  
from models import db, Restaurant, Pizza, RestaurantPizza

def seed_data():
    with app.app_context():
        db.session.query(RestaurantPizza).delete()
        db.session.query


        # Create Restaurants
        r1 = Restaurant(name="Mama Mia", address="123 Main St")
        r2 = Restaurant(name="Papa John's", address="456 Oak Ave")
        r3 = Restaurant(name="Kiki's Pizza", address="789 Elm Blvd")

        # Create Pizzas
        p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
        p2 = Pizza(name="Margherita", ingredients="Dough, Tomato, Mozzarella, Basil")
        p3 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

        # Add all to session
        db.session.add_all([r1, r2, r3, p1, p2, p3])
        db.session.commit()

        # Create RestaurantPizza associations
        rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
        rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p3.id)
        rp3 = RestaurantPizza(price=9, restaurant_id=r2.id, pizza_id=p2.id)
        rp4 = RestaurantPizza(price=15, restaurant_id=r3.id, pizza_id=p1.id)

        db.session.add_all([rp1, rp2, rp3, rp4])
        db.session.commit()

        print("Database seeded!")

if __name__ == "__main__":
    seed_data()
