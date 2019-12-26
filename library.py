import os
import pwd

def insert_magic(line):
    return line.replace('$USER_NAME', pwd.getpwuid(os.getuid()).pw_name).replace('$USER_ID', str(os.getuid()))

def make_dockerfile(target):
    with open(os.path.join(target, 'Dockerfile.in'), 'r') as in_file, open(os.path.join(target, 'Dockerfile'), 'w') as out_file:
        for in_line in in_file.readlines():
            if in_line.startswith('include'):
                with open(in_line.split()[1], 'r') as include_file:
                    for include_line in include_file.readlines():
                        print>>out_file,insert_magic(include_line.strip())
            else:
                print>>out_file,insert_magic(in_line.strip())
