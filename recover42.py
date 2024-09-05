# numbers = ['20240903_13', '20240903_12', '20240903_11']
# sorted_numbers_desc = sorted(numbers, reverse=False)
# print(f"정렬 : {sorted_numbers_desc}")


import os
folderName = os.listdir('test')
# sorted_numbers_desc = sorted(folderName, reverse=False)
sorted_numbers_desc = sorted(folderName, key=lambda x: tuple(map(int, x.split('_'))))
print(sorted_numbers_desc)