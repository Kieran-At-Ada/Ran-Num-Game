import random
num = 0

def generate_random_number():
  number = random.randint(10, 20)
  return number

def difference_from_answer(guess, answer):
  answer = generate_random_number()
  if guess == answer:
    return "Correct"
  elif guess <= answer:
    return "Too Low"
  else: return "Too High"
difference_from_answer()

print(difference_from_answer(12, answer))
