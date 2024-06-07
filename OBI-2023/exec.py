import timeit

# Código como uma string
datal = """
data = [(3, 'c'), (1, 'a'), (2, 'b')]
data.sort(key= lambda i: i[1], reverse=1)
"""

datad = """
data = {'b': 3, 'a': 1, 'c': 2}
sorted(data.items(), key=lambda x: x[1])
"""

# Medir o tempo de execução
execution_time_list = timeit.timeit(datal, number=1)
execution_time_dict = timeit.timeit(datad, number=1)

print(f"Tempo de execução: {execution_time_list} segundos")
print(f"Tempo de execução: {execution_time_dict} segundos")

