# import os

# def traverse(path, level=0):
#     dirs = os.listdir(path)
    
#     if not dirs:
#         return  

#     for dir in dirs:
#         dir_path = os.path.join(path, dir)
#         print(dir)
#         if dir == '.git' or not os.path.isdir(dir_path):
#             continue
#         if 'solution.md' in os.listdir(dir_path):
#             challenge_name = open(dir_path + "/solution.md").readline().replace("#", '').lstrip().rstrip()
#             indent = ' ' * level
#             print(f'{indent}- [{challenge_name}]({dir_path}/solution.md)')

#         traverse(dir_path, level + 1)

# traverse('.')