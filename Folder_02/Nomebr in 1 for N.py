# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

N = int(input('Введите число: '))
def get_factorial_list(n):
    fact = 1
    facts = []
    for i in range(1, n+1):
        fact *= i
        facts.append(fact)
    return facts

print(get_factorial_list(N))