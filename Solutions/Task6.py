def get_max_xor(s: list, b:int):
    max = (s[0] ^ b)
    for num in s:
        if num ^ b > max:
            max = num ^ b

    return max


q = int(input("Введите количество запросов:"))
num_list = []

for i in range(0, q):
    b = int(input("Введите запрос:"))
    if not (b in num_list):
        num_list.append(b)
    print(get_max_xor(num_list, b))


