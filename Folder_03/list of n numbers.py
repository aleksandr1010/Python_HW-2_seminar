n = int(input('Введите число: '))
num = [round((1+1/i)**i, 3) 
      for i in range(1, n+1)]
print(f'Последовательность: {num}\nСумма: {round(sum(num), 3)}')
