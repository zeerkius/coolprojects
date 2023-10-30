import pprint
def is_triangle(times):
    if times == 10 :
        return
    else:
         times = 1
         hash = "#"
         for i in range(times):
             print(hash * times)
             return is_triangle(times)


pprint.pprint(is_triangle(5))