def is_prime(char_f):
    if char_f == 0 or char_f == 1:
        return False
    for i in range(2, char_f):
        if char_f % i == 0:
            return False
    return True


def crypto(object):
    return [object[i] for i, val in enumerate(object) if is_prime(i)]
