import os
import shutil
import argparse
import zipfile
from datetime import datetime
import hashlib
from rich.progress import Progress
from rich.console import Console

def copy_to_src(target_dir, files):
    try:
        for file in files:
            shutil.copy(file, os.path.join(target_dir, "src", os.path.basename(file)))
    except Exception as e:
        console.print(f"[red]Error in copy_to_src: {e}[/red]")

def compress_src_to_pkg(target_dir):
    try:
        with zipfile.ZipFile(os.path.join(target_dir, "pkg", f"download.zip"), "w") as zipf:
            for root, _, files in os.walk(os.path.join(target_dir, "src")):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(target_dir, "src")))
    except Exception as e:
        console.print(f"[red]Error in compress_src_to_pkg: {e}[/red]")

def create_download_file(target_dir, input_file):
    yaml_formatter = f'''---
title: {os.path.basename(input_file)}
path: {os.path.join(target_dir, 'pkg', f'download.zip')}
link: https://mega.nz/example
    ---
    '''
    txt_file = os.path.join(target_dir, "src", f"{os.path.splitext(os.path.basename(input_file))[0]}.txt")
    with open(os.path.join(target_dir, "download.txt"), "w") as download_file:
        download_file.write(yaml_formatter)
        with open(txt_file, "r") as txt_content:
            download_file.write(txt_content.read())

def create_readme_file(target_dir, input_file):
    yaml_formatter = f'''---
category: {os.path.dirname(target_dir)}
title: {os.path.basename(input_file)}
rev: 1.0
tag: [""]
lastmod: {datetime.now().strftime('%Y-%m-%d')}
license: Your License Here
passcode: Your Passcode Here
path: {os.path.join(target_dir, 'pkg', f'download.zip')}
link: https://mega.nz/example
vouchers:
md5: {get_hash(input_file, 'md5')}
sha256: {get_hash(input_file, 'sha256')}
virus_total: https://www.virustotal.com/example
---

![alt](../img/thumbnail.png)

    '''
    try:
        txt_file = os.path.join(target_dir, "src", f"{os.path.splitext(os.path.basename(input_file))[0]}.txt")
        with open(os.path.join(target_dir, "readme.txt"), "w") as readme_file:
            readme_file.write(yaml_formatter)
            with open(txt_file, "r") as txt_content:
                readme_file.write(txt_content.read())
    except Exception as e:
        console.print(f"[red]Error in create_readme_file: {e}[/red]")

def get_hash(file_path, hash_algorithm):
    try:
        block_size = 65536
        hash_function = hashlib.new(hash_algorithm)
        with open(file_path, 'rb') as file_to_hash:
            for block in iter(lambda: file_to_hash.read(block_size), b''):
                hash_function.update(block)
        return hash_function.hexdigest()
    except Exception as e:
        console.print(f"[red]Error in get_hash: {e}[/red]")
        return None

def find_input_files(source_dir):
    try:
        input_files = []
        for root, _, files in os.walk(source_dir):
            input_files.extend([os.path.join(root, file) for file in files if file.endswith('.pdf')])
        return input_files
    except Exception as e:
        console.print(f"[red]Error in get_hash: {e}[/red]")
        return None


def main():
    parser = argparse.ArgumentParser(description="Process PDF files and create corresponding ZIP and README files.")
    parser.add_argument("--base-dir", default="categories/EBooks+Methods/", help="Base directory")
    parser.add_argument("--template-dir", default="__TMP__", help="Template directory")
    parser.add_argument("--source-dir", default="files", help="Source directory")
    parser.add_argument("--target-prefix", default="demo", help="Target prefix")

    parser.add_argument("--init", store_true, help="Initialize the package")
    parser.add_argument("--build", store_true, help="Build the package")

    args = parser.parse_args()

    console = Console()

    content_files = find_input_files(args.source_dir)
    console.print(f"[cyan]Processing {len(content_files)} files...")

    if args.init:
        console.print(f"[cyan]Initializing {len(content_files)} files...")

        with Progress() as progress:
            task = progress.add_task("[cyan]Processing...", total=len(content_files))

            for idx, input_file in enumerate(content_files):
                target_dir = os.path.join(args.base_dir, f"{args.target_prefix}{idx}")
                shutil.copytree(os.path.join(args.base_dir, args.template_dir), target_dir)

                base_filename = os.path.splitext(os.path.basename(input_file))[0]
                content_files_all = [input_file]

                for file_type in ["txt", "png"]:
                    file_path = os.path.join(target_dir, f"src/{base_filename}.{file_type}")
                    if os.path.exists(file_path):
                        content_files_all.append(file_path)

                copy_to_src(target_dir, content_files_all)

                progress.update(task, advance=1, description=f"[cyan]Processing {idx}/{len(content_files)} files")

    if args.build:
        console.print(f"[cyan]Building {len(content_files)} files...")

        with Progress() as progress:
            task = progress.add_task("[cyan]Processing...", total=len(content_files))

            for idx, input_file in enumerate(content_files):
                target_dir = os.path.join(args.base_dir, f"{args.target_prefix}{idx}")
                compress_src_to_pkg(target_dir)

                # create_download_file(target_dir, input_file) # TODO:
                # create_readme_file(target_dir, input_file) # TODO:

                progress.update(task, advance=1, description=f"[cyan]Processing {idx}/{len(content_files)} files")

        console.print("\n[green]Processing completed successfully!")

if __name__ == "__main__":
    main()

