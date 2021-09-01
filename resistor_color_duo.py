__COLORS = ['black', 'brown', 'red', 'orange', 'yellow',
            'green', 'blue', 'violet', 'grey', 'white']


def value(colors):
    return __COLORS.index(colors[0]) * 10 + __COLORS.index(colors[1])
