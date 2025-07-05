import random

def generate_fake_identity():
    names = ["Ivan", "John", "Ali", "Emma"]
    countries = ["Ukraine", "USA", "Germany", "Poland"]
    return {
        "name": random.choice(names),
        "country": random.choice(countries),
        "age": random.randint(18, 60)
    }
