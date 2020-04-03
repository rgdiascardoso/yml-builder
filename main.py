import os

def split_by_newline(secret):
    return secret.split('\n')

def save_file(base_path, file_name, expressions):
    with open(base_path + file_name, 'w') as file:
        for expression in expressions:
            file.write(expression)

def main():
    base_path = os.environ["GITHUB_WORKSPACE"]+'/'
    secret = os.environ["CONTENT"]
    file_name = os.environ["FILE_NAME"]

    expressions = split_by_newline(secret)
    save_file(base_path, file_name, expressions)

if __name__ == '__main__':
    main()