ls = ['1', '10', '4', '6', '100']

ls.sort(key=lambda x : int(x.split('.')[0]))

print(ls)