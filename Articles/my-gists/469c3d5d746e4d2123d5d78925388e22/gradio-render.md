```diff
def update_df(files):
    image_count = len(files)
    positions = calculate_positions(image_count)
    df = pd.DataFrame(positions, columns=['PosX', 'PosY', 'PosPx', 'PosPy'])
    df.insert(0, 'ImageId', range(1, image_count + 1))
    return df


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            cm_img_input = gr.Files(label='Insert common images')
            idv_img_input = gr.Files(label='Insert individual images')

        with gr.Column():
              pos_df = gr.Dataframe(headers=headers, label="Positions")


    cm_img_input.change(fn=update_df, inputs=cm_img_input, outputs=pos_df)
    idv_img_input.change(fn=update_df, inputs=idv_img_input, outputs=pos_df)
```

```diff
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            cm_img_input = gr.Files(label='Insert common images')
            idv_img_input = gr.Files(label='Insert individual images')

        with gr.Column():
                headers = ['ImageId', 'PosX', 'PosY', 'PosPx', 'PosPy']
+                @gr.render(inputs=[cm_img_input, idv_img_input])
                def update_df(*files):
+                    image_count = sum(len(file) for file in files if file is not None)
                    positions = calculate_positions(image_count)
                    df = pd.DataFrame(positions, columns=['PosX', 'PosY', 'PosPx', 'PosPy'])
                    df.insert(0, 'ImageId', range(1, image_count + 1))
                    return df
                pos_df = gr.Dataframe(headers=headers, label="Positions")

    cm_img_input.change(fn=update_df, inputs=cm_img_input, outputs=pos_df)
    idv_img_input.change(fn=update_df, inputs=idv_img_input, outputs=pos_df)
```