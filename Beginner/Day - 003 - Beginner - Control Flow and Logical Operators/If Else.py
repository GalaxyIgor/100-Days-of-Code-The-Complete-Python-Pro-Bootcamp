print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? ")) # height is int and cm

# indentation is important, because python don't have {}''
if height >= 100:
    print(f"Your height is {height} cm, you can ride the rollercoaster!")
else:
    print("Your height isn't 100 cm or more, you can't ride the rollercoaster!")
