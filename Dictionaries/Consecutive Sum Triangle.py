def convert_str_to_int(lista):
    b = []
    for i in lista:
        b += [int(i)]
    return b
def get_con_sum_list(listb):
    c = len(listb)
    d = []
    for i in range(c-1):
        d += [listb[i] + listb[i+1]]
    return d
        
def print_sum_triangle(int_list):
  while len(int_list) > 1:
    con_sum_list = get_con_sum_list(int_list)
    print(con_sum_list)
    int_list = con_sum_list
    
a = input().split(",")
d = convert_str_to_int(a)
print(d)
print_sum_triangle(d)

    
