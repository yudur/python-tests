from src.calculator import soma

# print(soma(10, 50))
# print(soma(-10, 50))
# print(soma(1.5, 5.5))
# print(soma(15, 15))

try:
    print(soma('14', 12))
except AssertionError as error:
    print('conta inválida')
    print(error)
