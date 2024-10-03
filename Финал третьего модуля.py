data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(numbers):
    if isinstance(numbers, (list, tuple, set)):
      return sum(calculate_structure_sum(item) for item in numbers)
    elif isinstance(numbers, int):
      return numbers
    elif isinstance(numbers, str):
      return len(numbers)
    elif isinstance(numbers, dict):
      return sum(calculate_structure_sum(key) + calculate_structure_sum(volme) for key, volme in numbers.items())


print(calculate_structure_sum(data_structure))