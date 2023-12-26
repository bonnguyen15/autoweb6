import string, random
import numpy as np
# input_info = np.array([[''],['']], dtype=object)
a = 'ERP-API'

if 'API' in a:
    print('là api')
else:
    print('không phải api')
    

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