from functools import reduce
fibonacci_series = reduce(lambda acc, _: acc + [acc[-1] + acc[-2]],range(2, 50),[1, 1])
print(fibonacci_series)
