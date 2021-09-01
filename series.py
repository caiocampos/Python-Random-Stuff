def slices(series, length):
    if length < 1 or len(series) < length:
        raise ValueError("Invalid length")
    s = []
    for i in range(len(series) - length + 1):
        s.append(series[i:i+length])
    return s
