def summ(*args):
    summ_obj = 0
    for el in args:
        if isinstance(el, list) or isinstance(el, set):
            for i in el:
                summ_obj += summ(i)
        elif isinstance(el, dict):
            for i in el:
                summ_obj += summ(el[i])
        else:
            summ_obj += el
    return summ_obj