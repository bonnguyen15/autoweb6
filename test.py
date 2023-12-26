import string, random
import numpy as np
# input_info = np.array([[''],['']], dtype=object)
def findSecretCDN(cdn_file):
        with open(cdn_file,'r') as f:
                for line in f:
                if 'CDN_URL_INTERNAL' in line:
                        a = line.split('"')[3]
                        return a
                if 'CDN_URL_PUBLIC' in line:
                        b = line.split('"')[3]
                        return b
                if 'CDN_SECRET' in line:
                        c = line.split('"')[3]
                        return c
                
file_cdn = 'D:\web\cdn-api\process.json'
cdn_private, cdn_public, secret_cdn = findSecretCDN(file_cdn)
    

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