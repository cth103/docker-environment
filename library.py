import os
import pwd

def preprocess(line):
    variables = {
            'USER_NAME': pwd.getpwuid(os.getuid()).pw_name,
            'USER_ID': str(os.getuid())
            }
    variables['JENKINS_USER_ID'] = None
    try:
        variables['JENKINS_USER_ID'] = str(pwd.getpwnam('jenkins').pw_uid)
    except KeyError:
        # Maybe no jenkins user on this system
        pass

    if len(line) > 0 and line[0] == '?':
        # ?variable - only do the line if variable is defined
        parts = line.split(' ')
        check_variable = parts[0][1:]
        if variables[check_variable] is None:
            line = ""
        else:
            line = line[len(check_variable) + 2:]

    for k, v in variables.items():
        if v:
            line = line.replace('$%s' % k, v)

    return line


def make_dockerfile(target):
    with open(os.path.join(target, 'Dockerfile.in'), 'r') as in_file, open(os.path.join(target, 'Dockerfile'), 'w') as out_file:
        for in_line in in_file.readlines():
            if in_line.startswith('include'):
                with open(in_line.split()[1], 'r') as include_file:
                    for include_line in include_file.readlines():
                        print(preprocess(include_line.strip()), file=out_file)
            else:
                print(preprocess(in_line.strip()), file=out_file)
