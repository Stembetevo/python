def results(numbers):
    if not numbers:
        return 0
    
    even_indexed_sum = sum(numbers[::2])
    return even_indexed_sum * numbers[-1]

""" numbers = [23,45,55,66,3,2]
print(results) """