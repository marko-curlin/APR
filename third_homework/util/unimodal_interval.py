from typing import Tuple


def find_unimodal_interval(h: float, start_point: float, function) -> Tuple[float, float]:
    l = start_point - h
    r = start_point + h
    m = start_point

    step = 1

    fm = function(m)
    fl = function(l)
    fr = function(r)

    if fm < fr and fm < fl:
        return l, r

    if fm > fr and fm > fl:
        raise ValueError('Function is not unimodal!')

    if fm > fr:
        while True:
            l = m
            m = r
            fm = fr

            step *= 2

            r = start_point + h * step
            fr = function(r)

            if fm <= fr:
                return l, r

    else:
        while True:
            r = m
            m = l
            fm = fl

            step *= 2

            l = start_point - h * step
            fl = function(l)

            if fm <= fl:
                return l, r
