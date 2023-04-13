sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
def find_duplicates(lst):
    return set([x for x in lst if lst.count(x) > 1])
print(list(find_duplicates(sample_list)))