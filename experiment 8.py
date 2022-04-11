#  1. input two lists :alist and blist，
#  members of each list are of integer decimals and no more than 10；

# alist = list(map(int,input().split()))
# blist = list(map(int,input().split()))
# clist = list(set(alist + blist))
# print(sorted((clist)))


# 2. input one list, its members are integer decimalssort list members according to their absolute values，
# if two members have the same absolute values, their originalsequential order keep stable，output the sorted
# list（the absolute values are the base of sorting, output members keep their original values）。

alist = list(map(int,input().split()))
print(sorted(alist,key = abs))
