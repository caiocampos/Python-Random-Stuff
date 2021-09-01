def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("strands must be of equal length")
    distance = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            distance += 1
    return distance
