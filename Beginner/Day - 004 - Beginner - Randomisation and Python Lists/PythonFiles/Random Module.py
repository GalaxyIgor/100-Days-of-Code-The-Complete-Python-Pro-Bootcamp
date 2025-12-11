# Random Module (Library) for Pseudorandom Number Generators
import random

# Integer = randint Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
random_integer = random.randint(1, 10)
print(random_integer)

# Float = random (adaptive) Return the next random floating-point number in the range 0.0 <= X < 1.0
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# Float = uniform Return a random floating-point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
random_float = random.uniform(1, 10)
print(random_float)

# PAUSE 1 - Heads or Tails
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else: # maybe you can put == 1
    print("Tails")