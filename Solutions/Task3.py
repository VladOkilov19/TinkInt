def find_min_lcm_pair(num: int):
    response = num

    for simple in range(1, num // 2)[::-1]:
        if ((num % simple == 0) or (num % (num - simple) == 0)) and (response > num // simple):
            response = num // simple
            break
    return num // response, num - num // response

n = int(input())
print(find_min_lcm_pair(n))
