n = int(input())
for x in range(n):
    same = True
    the_list = input().split(' ')
    the_list = res = [eval(i) for i in the_list]
    for y in range(len(the_list)-1):
        if the_list[y] != the_list[y+1]:
            same = False
    sorted_list = sorted(the_list)
    reverse_sorted_list = []
    for y in range(len(sorted_list)):
        a = len(sorted_list) - y - 1
        element = sorted_list[a]
        reverse_sorted_list.append(element)
    if same != False:
        print('The list has all equal elements.')
    elif the_list == sorted(the_list):
        print('The list is sorted in ascending order.')
    elif the_list == reverse_sorted_list:
        print('The list is sorted in descending order.')
    else:
        print('The list is not sorted.')