# def divisors(num):
#     divisors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisors.append(i)
#     return divisors

def divisor(num):
    try:
        if num < 0:
            raise ValueError("ingresa un número positvo")
        divisors =[i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisor(num))
        print("Termino mi programa")
    except ValueError:
        print("Debes ingresar un número")

if __name__ == "__main__":
    run()