def convert(number):
  (pling, plang, plong) = (number % 3 == 0, number % 5 == 0, number % 7 == 0)
  return f'{choose("Pling", pling)}{choose("Plang", plang)}{choose("Plong", plong)}{choose(number, not (pling or plang or plong))}'

def choose(val, condition):
    return val if condition else ''
