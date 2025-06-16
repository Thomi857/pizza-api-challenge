# server/seed.py

from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Luigi's Slice", address="789 Oak Ave")
    r2 = Restaurant(name="Bella Napoli", address="321 Maple Rd")

    p1 = Pizza(name="Four Cheese", ingredients="Dough, Tomato Sauce, Mozzarella, Parmesan, Gorgonzola, Ricotta")
    p2 = Pizza(name="BBQ Chicken", ingredients="Dough, BBQ Sauce, Chicken, Red Onion, Cilantro, Cheese")
    p3 = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Ham, Pineapple, Cheese")

    db.session.add_all([r1, r2, p1, p2, p3])
    db.session.commit()

    rp1 = RestaurantPizza(price=14, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=16, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=13, restaurant_id=r2.id, pizza_id=p3.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()
    print(" Seeded database!")
