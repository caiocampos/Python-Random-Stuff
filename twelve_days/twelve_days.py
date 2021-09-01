
FIRST_GIFT = 'a Partridge in a Pear Tree'

DAYS = [
    ('first', 'twelve Drummers Drumming'),
    ('second', 'eleven Pipers Piping'),
    ('third', 'ten Lords-a-Leaping'),
    ('fourth', 'nine Ladies Dancing'),
    ('fifth', 'eight Maids-a-Milking'),
    ('sixth', 'seven Swans-a-Swimming'),
    ('seventh', 'six Geese-a-Laying'),
    ('eighth', 'five Gold Rings'),
    ('ninth', 'four Calling Birds'),
    ('tenth', 'three French Hens'),
    ('eleventh', 'two Turtle Doves'),
    ('twelfth', f'and {FIRST_GIFT}')
]


def recite(start_verse, end_verse=None):
    return [recite_day(i) for i in range(start_verse - 1, end_verse)]


def recite_day(day):
    th, _ = DAYS[day]
    return f'On the {th} day of Christmas my true love gave to me: {gifts(day)}.'


def gifts(day):
    return FIRST_GIFT if not day else ', '.join([gift for _, gift in DAYS[11 - day: 12]])
