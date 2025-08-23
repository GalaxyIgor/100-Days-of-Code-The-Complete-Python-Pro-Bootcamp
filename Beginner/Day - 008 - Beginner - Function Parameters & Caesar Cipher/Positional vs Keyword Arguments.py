# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# P.1 Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is like in location {location}.")

# No parameter
greet_with("Angela", "Londres")
# with parameter
greet_with(name="Angela", location="Londres")