def bad_float_compare(n1, n2):
    assert n1 == n2, 'numbers are not equal'
    return True

def good_float_compare(n1, n2):
    tolerance = 1e-05
    assert abs(n1-n2) <= tolerance, 'numbers are not within tolerance'
    return True

number1 = 3.3**2
number2 = 10.89

good = good_float_compare(number1, number2)
print('GOOD TEST RETURNS: ', good)
print('BAD TEST RETURNS: ')
bad = bad_float_compare(number1, number2)
print(bad)
