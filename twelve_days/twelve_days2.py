
FIRST_GIFT = 'a Partridge in a Pear Tree'

GIFTS = [
    f'and {FIRST_GIFT}',
    'two Turtle Doves',
    'three French Hens',
    'four Calling Birds',
    'five Gold Rings',
    'six Geese-a-Laying',
    'seven Swans-a-Swimming',
    'eight Maids-a-Milking',
    'nine Ladies Dancing',
    'ten Lords-a-Leaping',
    'eleven Pipers Piping',
    'twelve Drummers Drumming'
]

DAYS = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
]


def recite(start_verse, end_verse):
    return [recite_day(i) for i in range(start_verse - 1, end_verse)]


def recite_day(day):
    return f'On the {DAYS[day]} day of Christmas my true love gave to me: {gifts(day)}.'


def gifts(day):
    return FIRST_GIFT if not day else ', '.join(GIFTS[0:day+1][::-1])
