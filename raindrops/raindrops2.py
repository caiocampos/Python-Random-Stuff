SOUNDS = ["Pling", "Plang", "Plong"]
FACTORS = [3, 5, 7]

def convert(number):
  sounds = [SOUNDS[i] for i in range(3) if number % FACTORS[i] == 0]
  return str(number) if len(sounds) == 0 else ''.join(sounds)

