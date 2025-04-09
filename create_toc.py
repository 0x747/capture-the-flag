import os
import re

markdown = ''
tab = '    '

def traverse(path, level=0):
    files = os.listdir(path)
    global markdown

    if 'solution.md' in files:
        markdown += create_md_link('', path, level, True)
        return
            
    if not files:
        return  

    for dir in files:
        dir_path = os.path.join(path, dir)

        if dir == '.git' or not os.path.isdir(dir_path):
            continue

        markdown += create_md_link(dir, dir_path, level)
        traverse(dir_path, level + 1)

def create_md_link(dir, dir_path, level, is_md=False):

    if level == 0:
        return f'[{dir}]({dir_path})\n'

    if is_md:
        challenge_name = open(dir_path + "/solution.md").readline()
        sanitized_challenge_name = re.sub(r"^#\s*|\s+$", '', challenge_name)
        return f'{tab * level}- [{sanitized_challenge_name}]({dir_path}/solution.md) - write up\n'

    return f'{tab * level}- [{dir}]({dir_path})\n'

traverse('.')
print(markdown)