def minimum_number(numbers):
    numbers = [8, 3, 5, 1, 9, 12]
    lowestnumber = numbers[0]
    
    for value in numbers:
        if value < lowestnumber:
            lowestnumber = value
            
    return numbers


print(minimum_number)






