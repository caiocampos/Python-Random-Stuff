SOUND_FACTORS = [(3, "Pling"), (5, "Plang"), (7, "Plong")]

def convert(number):
  sounds = [el[1] for el in SOUND_FACTORS if number % el[0] == 0]
  return str(number) if not sounds else ''.join(sounds)

