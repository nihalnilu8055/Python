numbers = [2, 3, 4, 5, 6]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        num1 = numbers[i]
        num2 = numbers[j]
        
        product = num1 * num2
        total_sum = num1 + num2
        
        if product % 2 == 0 and total_sum % 2 != 0:
            print(f"Pair: ({num1}, {num2}), Product: {product}, Sum: {total_sum}")
