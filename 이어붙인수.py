def solution(num_list):
    odd_num = []
    even_num = []
    for num in num_list:
        if num % 2 == 1:
            odd_num.append(num)
        else:
            even_num.append(num)
    a = int(''.join(map(str, odd_num)))
    b = int(''.join(map(str, even_num)))
    return a+b