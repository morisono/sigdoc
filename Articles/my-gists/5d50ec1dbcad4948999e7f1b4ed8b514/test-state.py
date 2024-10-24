import gradio as gr

import glob
import tempfile
import zipfile
import pandas as pd

class Interface:

    def get_tempdir():
        timestamp = int(time.time())
        temp_dir = tempfile.mkdtemp()
        return timestamp, temp_dir

    def create_zip(filelist, tmp_fname):
        if not filelist:
            return
        else:
            tmp_dir = os.path.dirname(filelist[0])
            zip_name = os.path.join(tmp_dir, tmp_fname)
            with zipfile.ZipFile(zip_name, "w") as f:
                for file in filelist:
                    f.write(file, os.path.basename(file))
            return zip_name

    def read_file(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

def process_input(state, inputs):
    if state is None:
        state = {'items': [], 'index_counter': 0}
    text = inputs
    idx = state['index_counter']
    state['index_counter'] += 1
    state['items'].append({
        'Index': idx,
        'Text': text})  # Add the new item without 'total' key
    state_df = pd.DataFrame(state['items'])
    state_df = state_df.astype(str)
    state_df = state_df.fillna('')
    return state, state_df


def update_tbox(input_text):
    return '\n---\n\n'.join(Interface.read_file(txt) for txt in input_text)

def remove_item(state, row_index):
    if 'items' in state:
        items = state['items']
    else:
        items = []

    if 0 <= row_index < len(items):
        del items[row_index]
        state['items'] = items

        items_df = pd.DataFrame(items)
        items_df = items_df.astype(str)
        items_df = items_df.fillna('')

        return state, items_df
    else:
        raise gr.Error("Invalid row index.")

def find_item(state, regex):
    if 'items' in state:
        items = state['items']
    else:
        items = []

    matched_items = [item for item in items for value in item.values() if re.search(regex, str(value))]

    df = pd.DataFrame(matched_items)

    return state, df

with gr.Blocks() as demo:
    state = gr.State()

    with gr.Row():
        with gr.Column():
            files_in = gr.Files(label="Enter text and optionally upload an image or video")
            tbox_in = gr.TextArea(label="Merged Text")
            with gr.Row():
                with gr.Row():
                    row_idx_out = gr.Number(minimum=0, step=1, label="Index to out")
                    submit_rm = gr.Button("Remove")
                with gr.Row():
                    submit_button_clear = gr.ClearButton(tbox_in)
                    submit_button = gr.Button("Submit", variant='primary')

            example_files = glob.glob('src/md/demo/*.md')
            gr.Examples([[example_files]], files_in)

        with gr.Column():
            output = gr.DataFrame(label="State Output")

    files_in.change(update_tbox, files_in, tbox_in)

    submit_rm.click(
        remove_item,
        inputs=[state, row_idx_out],
        outputs=[state, output]
    )
    submit_button.click(
        process_input,
        inputs=[state, tbox_in],
        outputs=[state, output]
    )

demo.launch()
