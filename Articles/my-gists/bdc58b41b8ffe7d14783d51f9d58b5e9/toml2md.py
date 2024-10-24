import sys
import toml
import argparse
import gradio as gr

def convert_toml_to_markdown(input_data=None, output_file=None):
    result = ""
    result_end = []

    for key, obj in input_data["docs"].items():
        result += f"1. <details open><summary>{key}</summary>\n\n"
        if isinstance(obj, list):
            for item in obj:
                name = item.get("name", "")
                desc = item.get("desc", "")
                path = item.get("path", "")
                # category = item.get("category", "")
                result += f"    1. [**{name}**](docs/{path}) : {desc}\n\n"
                result_end.append('</details>\n')
        else:
            result += convert_toml_to_markdown({"docs": obj})
            result += "</details>\n"

    result += ''.join(result_end)

    if output_file:
        with open(output_file, 'w') as out_file:
            out_file.write(result)

    return result


def web_interface():
    def wrapper(input_file, output_file):
        convert_toml_to_markdown(input_file, output_file)
        return f"Conversion completed. Output written to {output_file}"

    iface = gr.Interface(
        fn=wrapper,
        inputs=["text", "text"],
        outputs="text",
        live=True
    )
    iface.launch()

def main():
    parser = argparse.ArgumentParser(description="Convert TOML to Markdown")
    parser.add_argument("input_file", nargs='?', help="Path to the input TOML file")
    parser.add_argument("output_file", nargs='?', help="Path to the output Markdown file")
    parser.add_argument("-i", "--input", dest="input_file_opt", help="Path to the input TOML file (optional)")
    parser.add_argument("-o", "--output", dest="output_file_opt", help="Path to the output Markdown file (optional)")
    parser.add_argument("--webui", action="store_true", help="Launch web interface")

    args = parser.parse_args()

    if args.webui:
        web_interface()
        return

    input_file = args.input_file or args.input_file_opt
    output_file = args.output_file or args.output_file_opt

    if input_file:
        with open(input_file, 'r') as file:
            input_data = toml.load(input_file)
    else:
        print("Waiting for TOML input from stdin...")
        print("Press Ctrl-D (Unix/Linux/macOS) or Ctrl-Z (Windows) to end input.")
        print()
        input_data = toml.load(sys.stdin)

    convert_toml_to_markdown(input_data, output_file)
    print(f"Conversion completed. Output written to {output_file}")

if __name__ == "__main__":
    main()
