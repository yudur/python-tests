"""
1 - receive an integer
2 - know if the number is a multiple of 3 and 5: bacon and eggs
3 - know if the number is multiple only 3: bacon
4 - know if the number is multiple only 5: eggs
4 - know if a number is not multiple of 3 and 5: starving
"""

def bacon_with_eggs(n):
    assert isinstance(n, int), '(n) deve ser um int'

    if n % 3 == 0 and n % 5 == 0:
        return 'bacon and eggs'

    if n % 3 == 0:
        return 'bacon'

    if n % 5 == 0:
        return 'eggs'

    return 'starving'
