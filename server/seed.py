# server/seed.py

from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Osaka", address="789 Oak Ave")
    r2 = Restaurant(name="madrid", address="321 Maple Rd")

    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil, Olive Oil")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni")
    p3 = Pizza(name="Veggie Delight", ingredients="Dough, Tomato Sauce, Mozzarella, Bell Peppers, Olives, Onions, Mushrooms")

    db.session.add_all([r1, r2, p1, p2, p3])
    db.session.commit()

    rp1 = RestaurantPizza(price=14, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=16, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=13, restaurant_id=r2.id, pizza_id=p3.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()
    print(" Seeded database!")
