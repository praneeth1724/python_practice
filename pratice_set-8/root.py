def sum_digits(number):
    n = number % 10
    numb = number // 10
    if numb != 0 or numb > 0:
         return n + sum_digits(numb)
    else:
        return n


print(sum_digits(125))


