import os

def make_dockerfile(target):
    with open(os.path.join(target, 'Dockerfile.in'), 'r') as in_file, open(os.path.join(target, 'Dockerfile'), 'w') as out_file:
        for in_line in in_file.readlines():
            if in_line.startswith('include'):
                with open(in_line.split()[1], 'r') as include_file:
                    for include_line in include_file.readlines():
                        print>>out_file,include_line.strip()
            else:
                print>>out_file,in_line.strip()
