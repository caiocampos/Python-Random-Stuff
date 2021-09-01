def two_fer_va(name=None):
    if name is None:
        name = 'you'
    return f'One for {name}, one for me.'

def two_fer_vb(name=None):
    return f'One for {"you" if name is None else name}, one for me.'

def two_fer_vc(name=None):
    return f'One for {name or "you"}, one for me.'

def two_fer_vd(name='you'):
    return f'One for {name}, one for me.'

two_fer = two_fer_vd