def generate_pin_codes(length=4):
    return [str(i).zfill(length) for i in range(10**length)]
