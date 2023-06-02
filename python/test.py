""" ko dùng builtin function
    - cho 1 list các list:
        a = [[1,2],[4,6, 9],[9],[5,34,89, 12],[20,28, 29, 30, 90],[19,26]]
        - tính tổng từng phần tử của list a, rồi tính tổng chung
        - tính giá trị trung bình của list a
"""
a = [[1,2],[4,6, 9],[9],[5,34,89, 12],[20,28, 29, 30, 90],[19,26]]

def total_def(a: list) -> float: # anotation
    total = 0
    for i in a:
        total += i
    avg = total / len(a)
    return avg

# 3/2

total_list = 0
for i in a:
    total_list += total_def(i)
avg = total_list / len(a)
print(avg)


