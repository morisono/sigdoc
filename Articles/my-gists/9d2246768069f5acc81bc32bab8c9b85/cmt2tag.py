import argparse
import toml

def add_tags_from_comments(input_file, output_file, additional_keys):
    # 入力ファイルを読み取ります
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # TOMLデータを構築します
    data = {}
    current_tags = None
    current_key = None
    current_entry = None

    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            # 新しいコメントをタグとして保存します
            current_tags = line[1:].strip().split(', ')
            if len(current_tags) == 1:
                current_tags = current_tags[0]
        elif line.startswith("[["):
            keys = line[2:-2].split('.')
            pre_key, curr_key = keys[0], keys[1]
            current_key = f'{pre_key}.{curr_key}'
            for entry in data[pre_key][curr_key]:
                entry['tag'] = current_tags if current_tags else []
                entry.update(additional_keys)
        elif current_key and "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"')
            current_entry[-1][key] = value

    # 出力ファイルに新しい内容を書き込みます
    with open(output_file, 'w') as file:
        for key, entries in data.items():
            for entry in entries:
                file.write(f'[[{key}]]\n')
                for k, v in entry.items():
                    if k == 'tag':
                        tags_str = ', '.join([f'"{tag}"' for tag in v])
                        file.write(f'{k} = [{tags_str}]\n')
                    else:
                        file.write(f'{k} = "{v}"\n')

def add_tags_from_comments(input_file, output_file, additional_keys):
    # 入力ファイルを読み取ります
    with open(input_file, 'r') as file:
        content = file.read()

    # TOMLとして解析します
    data = toml.loads(content)

    # コメントをタグとして保存します
    current_tags = None
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("#"):
            current_tags = line[1:].strip().split(', ')
        elif line.startswith("[["):
            keys = line[2:-2].split('.')
            pre_key, curr_key = keys[0], keys[1]
            current_key = f'{pre_key}.{curr_key}'
            for entry in data[pre_key][curr_key]:
                entry['tag'] = current_tags if current_tags else []
                entry.update(additional_keys)  # 追加のキーと値をエントリに追加します

    # 出力ファイルに新しい内容を書き込みます
    with open(output_file, 'w') as file:
        toml.dump(data, file)

def main():
    parser = argparse.ArgumentParser(description='Add tags and additional keys to TOML entries.')
    parser.add_argument('input_file', help='Path to the input TOML file.')
    parser.add_argument('output_file', help='Path to the output TOML file.')
    parser.add_argument('--add', nargs='*', action='store', help='Additional key-value pairs to add to each entry. Format: key=value')

    args = parser.parse_args()

    additional_keys = {}
    if args.add is not None:
        if args.add:
            for pair in args.add:
                key, value = pair.split('=')
                additional_keys[key] = value
        else:
            additional_keys = {
                'auth': ['admin'],
                'version': '0.1.0',
                'last_updated': '0000-00-00',
                'status': True
            }
            print("Please enter additional key-value pairs to add to each entry. Format: key=value")
            print("Press Enter without typing anything to finish.")
            while True:
                pair = input("> ")
                if not pair:
                    break
                key, value = pair.split('=')
                additional_keys[key] = value

    add_tags_from_comments(args.input_file, args.output_file, additional_keys)

if __name__ == "__main__":
    main()
