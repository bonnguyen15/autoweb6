import string, random
import numpy as np
# input_info = np.array([[''],['']], dtype=object)
numarr = [1, 2, 3, 4, 5, 6, 7, '8', 9, 10, 12, 13, 14, 15, 16]
num = '8'
if num.isdecimal() and num in numarr:
    print('co')
else:
    print('khong')
    

# def replaceFile(self, replace_file, search_str, old_str, new_str):
#     with open(replace_file, 'r') as f:
#         lines = f.readlines()
#     new_lines = []
#     for line in lines:
#         if search_str in line:
#             new_line = line.replace(old_str, new_str)
#             new_lines.append(new_line)
#         else:
#             new_lines.append(line)
#     with open(replace_file, 'w') as f:
#         f.writelines(new_lines)