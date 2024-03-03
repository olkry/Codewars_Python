# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.
#
# Вы получаете массив чисел, возвращаете сумму всех положительных чисел.
# Пример [1,-4,7,12] => 1 + 7 + 12 = 20
# Примечание. Если суммировать нечего, сумма по умолчанию равна 0.

def positive_sum(arr):
    sum_positive = 0
    if len(arr) > 0:
        for digit in arr:
            if digit > 0:
                sum_positive += digit
        return sum_positive
    return 0

def positive_sum(arr):
    return sum(x for x in arr if x > 0)
