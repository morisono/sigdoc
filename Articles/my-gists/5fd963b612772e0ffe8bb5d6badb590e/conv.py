import sys
import os
from datetime import datetime

def convert_to_gradio_lite(python_files, requirements_file):
    # gradio-requirements.txt からの依存関係の取得
    dependencies = []
    if requirements_file:
        with open(requirements_file, "r") as file:
            dependencies = [line.strip() for line in file]

    # Gradio Lite の HTML テンプレートを作成
    html_template = """
<html>
    <head>
        <script type="module" crossorigin src="https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.js"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.css" />
    </head>
    <body>
        <gradio-lite theme="light">
            <gradio-requirements>
{}
            </gradio-requirements>

{}
        </gradio-lite>
    </body>
</html>
    """

    # 依存関係を Gradio Lite の HTML に挿入
    requirements = "\n".join(dependencies)

    # 各 Python ファイルを処理し、<gradio-file> タグを作成
    gradio_files = []
    for python_file in python_files:
        with open(python_file, "r") as file:
            python_code = file.read()

        entrypoint = "entrypoint" if python_file == python_files[0] else ""
        gradio_file = f"""
            <gradio-file name="{os.path.basename(python_file)}" {entrypoint}>
{python_code}
            </gradio-file>
        """
        gradio_files.append(gradio_file)

    # 完成した HTML を返す
    return html_template.format(requirements, "\n".join(gradio_files))

# コマンドライン引数からファイルパスを取得
python_files = sys.argv[1:-1]
requirements_file = sys.argv[-1] if len(sys.argv) > 1 else None

# Gradio Lite への変換
gradio_lite_html = convert_to_gradio_lite(python_files, requirements_file)

# タイムスタンプ付きのファイル名を生成
timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
output_file = f"index_{timestamp}.html"

# 結果をファイルに出力
with open(output_file, "w") as file:
    file.write(gradio_lite_html)

print(f"Gradio Lite HTML has been generated and saved as {output_file}")