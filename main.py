import yaml, os, sys

def load_file(input_file):
    with open(input_file) as file: 
        return yaml.load(file, Loader=yaml.FullLoader)

def write_file(output_file, data):
    with open(output_file, 'w') as file:
        yaml.dump(data, file)

def parse_params(params):
    return [param.strip() for param in params.split('--')]

def split_param_action(param):
    buffer = param.split(':', 1)
    return (buffer[0], buffer[1])

def get_parent_object(param, data):
    if '=' in param:
        parsed_param = param.split('=', 1)
    else:
        parsed_param = [param]
    keys = parsed_param[0].split('.')
    if len(parsed_param) == 2:
        value = parsed_param[1]
    else:
        value = None
    for i in range(len(keys)-1):
        data = data[keys[i]]
    return (keys[-1], value, data)

def replace_value(param, data):
    key, value, data = get_parent_object(param, data)
    data[key] = eval(value)

def add_key(param, data):
    key, value, data = get_parent_object(param, data)
    data.update({key: eval(value)})

def append_value(param, data):
    key, value, data = get_parent_object(param, data)
    data[key].append(eval(value))

def delete_value(param, data):
    key, value, data = get_parent_object(param, data)
    data.pop(key, None)

def main():
    base_path = os.environ['GITHUB_WORKSPACE']+'/'
    input_file = base_path + os.environ['INPUT_INPUTFILE']
    output_file = base_path + os.environ['INPUT_OUTPUTFILE']
    params = sys.argv[1]

    data = load_file(input_file)

    for param in parse_params(params):
        if param:
            action, argument = split_param_action(param)
            if action == 'replace':
                replace_value(argument, data)
            elif action == 'add':
                add_key(argument, data)
            elif action == 'append':
                append_value(argument, data)
            elif action == 'remove':
                delete_value(argument, data)
    
    write_file(output_file, data)

if __name__ == '__main__':
    main()