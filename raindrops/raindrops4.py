SOUND_FACTORS = [(3, "Pling"), (5, "Plang"), (7, "Plong")]

def convert(number):
  sounds = [sound for factor, sound in SOUND_FACTORS if number % factor == 0]
  return str(number) if not sounds else ''.join(sounds)

