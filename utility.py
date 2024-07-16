def validate_price(price):
    try:
        float(price)
        return True
    except ValueError:
        return False
