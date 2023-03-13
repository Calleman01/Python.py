miles_per_g = float(input("Miles per gallon? "))
liter_per_m = (3.785 / miles_per_g / 1.609 * 10)
print(f'{liter_per_m:.2f} l/mil')