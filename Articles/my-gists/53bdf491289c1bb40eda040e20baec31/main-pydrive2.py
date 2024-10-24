import gradio as gr
from gdrive_api import GoogleDriveAPI
import uuid

class StateModel:
    def __init__(self):
        self.folder_name = ""
        self.file_name = ""
        self.target_dir = ""
        self.folder_id = ""
        self.upload_status = ""

class GDriveHandler():
    def __init__(self):
        self.drive_api = GoogleDriveAPI()

    def list_all_files(self, folder_name):
        file_df = self.drive_api.get_file_df(folder_name=folder_name)
        return file_df

    def search_files_by_name(self, folder_name, file_name):
        file_id = self.drive_api.get_file_id(
            folder_name=folder_name,
            file_name=file_name
        )
        if file_id:
            return file_id
        else:
            print("File not found.")

    def download_file(self, folder_name, target_dir, file_name):
        file_id = self.drive_api.get_file_id(folder_name=folder_name)
        if file_id:
            self.drive_api.gdrive_download(
                file_id=file_id,
                target_dir=target_dir)
            return f"File {file_name} downloaded successfully from folder {folder_name}."
        else:
            print("No files found in the specified folder.")

    def download_all_files(self, folder_name, target_dir, file_name):
        file_ids = self.get_all_file_id(folder_name)
        if file_ids:
            for file_id in file_ids:
                file_name = self.get_file_name(file_id)
                self.gdrive_download(file_id=file_id, output_name=file_name, target_dir=target_dir)
            return f"All files downloaded successfully from folder {folder_name}."
        else:
            return f"No files found in folder {folder_name}."

    def download_newest_file(self, folder_name, target_dir, file_name):
        file_id = self.get_file_id(folder_name=folder_name) # TODO try: async?
        if file_id:
            file_name = self.get_file_name(file_id)
            self.gdrive_download(file_id=file_id, output_name=file_name, target_dir=target_dir)
            return f"Newest file {file_name} downloaded successfully from folder {folder_name}."
        else:
            return f"No files found in folder {folder_name}."

    def upload_file(self, folder_id, content_file, file_name):
        self.gdrive_upload(folder_id, content_file, file_name=file_name)
        return f"File {file_name} uploaded successfully to folder with ID {folder_id}."

    def show_folder_info(self, folder_name):
        file_df = self.get_file_df(folder_name)
        created_at = self.get_created_at(folder_name)
        info = {
            "files": file_df.to_dict(),
            "created_at": created_at
        }
        return json.dumps(info, indent=4)

def web_ui():
    gdrive = GDriveHandler()
    readme = f'''
    This is a demo of Google Drive API. You can upload, download, and list files in Google Drive. Before using this demo, you need to create a Google Drive API project and enable the [Google Cloud Console](https://cloud.google.com/console). For more information, please refer to [Google Drive API](https://developers.google.com/drive/api/quickstart/python?hl=ja).
    '''
    with gr.Blocks() as demo:
        state = gr.State(StateModel())
        gr.Markdown(f'# Google Drive API Demo')
        gr.Markdown(f'{readme}')

        with gr.Tab('List_All_Files'):
            with gr.Row():
                with gr.Column():
                    folder_name_input = gr.Textbox(label="Folder Name")
                    file_name_input = gr.Textbox(label="File Name")
                    target_dir_input = gr.Textbox(label="Target Directory")
                    with gr.Row():
                        submit_button_clear = gr.ClearButton(folder_name_input)
                        submit_button = gr.Button("Submit", variant='primary')

                    gr.Examples([
                        ['Documents', 'demo.txt', '/'],
                        ['Downloads', 'demo.txt', '/'],
                    ], folder_name_input)

                with gr.Column():
                    pass
            table_out = gr.Dataframe(label="Files List")

            submit_button.click(
                gdrive.list_all_files,
                folder_name_input,
                table_out
            )

        with gr.Tab('Search_Files_By_Name'):
            with gr.Row():
                with gr.Column():
                    folder_name_input = gr.Textbox(label="Folder Name")
                    file_name_input = gr.Textbox(label="File Name")
                    with gr.Row():
                        submit_button_clear = gr.ClearButton(folder_name_input)
                        submit_button = gr.Button("Search", variant='primary')

                    gr.Examples([
                        ['Documents/Manuals', '*.pdf', '/'], # TODO
                        ['Downloads', 'demo.txt', '/'],
                    ], [folder_name_input, file_name_input])

                with gr.Column():
                    pass

            search_result = gr.Textbox(label="Search Result")
            submit_button.click(
                gdrive.search_files_by_name,
                [folder_name_input, file_name_input],
                [search_result]
            )

        with gr.Tab('Download_File'):
            with gr.Row():
                with gr.Column():
                    folder_name_input = gr.Textbox(label="Folder Name")
                    target_dir_input = gr.Textbox(label="Target Directory")
                    with gr.Row():
                        submit_button_clear = gr.ClearButton(folder_name_input)
                        submit_button = gr.Button("Download", variant='primary')
                        file_name_input = gr.Textbox(label="File Name")

                    gr.Examples([
                        ['Documents/Manuals', '.', '*.pdf'],
                        ['Downloads', '.', 'demo.txt'],
                    ], [folder_name_input, target_dir_input, file_name_input])

                with gr.Column():
                    pass

            download_status = gr.Textbox(label="Download Status")
            submit_button.click(
                gdrive.download_file,
                [folder_name_input, target_dir_input, file_name_input],
                [download_status]
            )

        with gr.Tab('Download_All_Files'):
            with gr.Row():
                with gr.Column():
                    folder_name_input = gr.Textbox(label="Folder Name")
                    target_dir_input = gr.Textbox(label="Target Directory")
                    with gr.Row():
                        submit_button_clear = gr.ClearButton(folder_name_input)
                        submit_button = gr.Button("Download All", variant='primary')
                        file_name_input = gr.Textbox(label="File Name")
                    gr.Examples([
                        ['Documents/Manuals', '.', '*.pdf'],
                        ['Downloads', '.', 'demo.txt'],
                    ], [folder_name_input, target_dir_input, file_name_input])

                with gr.Column():
                    pass

            download_status = gr.Textbox(label="Download Status")
            submit_button.click(
                gdrive.download_all_files,
                [folder_name_input, target_dir_input, file_name_input],
                [download_status]
            )

        with gr.Tab('Download_Newest_File'):
            with gr.Row():
                with gr.Column():
                    folder_name_input = gr.Textbox(label="Folder Name")
                    target_dir_input = gr.Textbox(label="Target Directory")
                    file_name_input = gr.Textbox(label="File Name")
                    with gr.Row():
                        submit_button_clear = gr.ClearButton(folder_name_input)
                        submit_button = gr.Button("Download Newest", variant='primary')

                    gr.Examples([
                        ['Documents/Manuals', '.', '*.pdf'],
                        ['Downloads', '.', 'demo.txt'],
                    ], [folder_name_input, target_dir_input, file_name_input])

                with gr.Column():
                    pass


            download_status = gr.Textbox(label="Download Status")
            submit_button.click(
                gdrive.download_newest_file,
                [folder_name_input, target_dir_input, file_name_input],
                [download_status]
            )

        with gr.Tab('Upload_File'):
            with gr.Row():
                with gr.Column():
                    folder_id_input = gr.Textbox(label="Folder ID")
                    content_file_input = gr.File(label="Upload File")
                    file_name_input = gr.Textbox(label="File Name")
                    with gr.Row():
                        submit_button_clear = gr.ClearButton(folder_id_input)
                        submit_button = gr.Button("Submit", variant='primary')

                        gr.Examples([
                            ['Documents/Manuals', '*.pdf', '/'],
                            ['Downloads', 'demo.txt', '/'],
                        ], folder_id_input)

                with gr.Column():
                    pass


                with gr.Column():
                    status_ = gr.TextArea(label="Upload Status")

                inputs = [folder_id_input, content_file_input, file_name_input]
                outputs = status_

                submit_button.click(
                    gdrive.upload_file,
                    inputs,
                    outputs
                )

    demo.launch()

web_ui()
