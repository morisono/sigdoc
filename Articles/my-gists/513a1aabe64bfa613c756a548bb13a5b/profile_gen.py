import uuid
import random
import gradio as gr

from modules.utils import Interface, Converter
from modules.providers import MyProviders

# TODO: implement keyword weight
# TODO: visualise keyword weight using gr.HighlightedText() or Interpretation
# TODO:

# def gen_data(el, locale, preview, num, rate, seed, choiced):
def gen_data(el, locale, preview, num, rate, seed, *choiced):
    if el:
        el = Interface.read_file(el.name)

    gs = {}
    for cs in choiced:
        for c in cs:
            for k, v in el.items():
                if c in v:
                    gs.setdefault(k, []).append(c)
    # print(gs)
    result = {}
    rows = []
    header = []

    for i in range(num):
        dt = {}
        for g in gs.keys():
            fakes = gen_fake(seed + i, el, locale)
            if g not in dt:
                dt[g] = {}
            for field in gs[g]:
                if field in fakes.get(g, {}):
                    value = fakes[g][field]
                    if field not in dt[g]:
                        dt[g][field] = []
                    dt[g][field].append(value)

        result[f'No. {i:04d}'] = dt

    for i in range(num):
        row = []
        for g in gs.keys():
            for field in gs[g]:
                if field in result[f'No. {i:04d}'][g]:
                    row.append(result[f'No. {i:04d}'][g][field][0])
        rows.append(row)

    for g in gs.keys():
        for field in gs[g]:
            header.append(f'{g}.{field}')

    print(rows)

    ts, tmp_dir = Interface.get_tempdir()
    tmp_file = f'{tmp_dir}/{ts}'
    csv_file = tmp_file + '.csv'
    json_file = tmp_file + '.json'
    toml_file = tmp_file + '.toml'
    yaml_file = tmp_file + '.yaml'

    Interface.write_csv(rows, header, csv_file)
    Interface.write_json(result, json_file)
    Interface.write_toml(result, toml_file)
    Interface.write_yaml(result, yaml_file)

    fake_prev = Interface.write_yaml(result)

    print(fake_prev)

    if 'table' in preview and 'tree' in preview:
        Interface.create_zip([csv_file, json_file, toml_file, yaml_file], tmp_file)
        return None, fake_prev, csv_file
    elif 'table' in preview:
        return csv_file, None, csv_file
    elif 'tree' in preview:
        return json_file, fake_prev, None
    else:
        Interface.create_zip([csv_file, json_file, toml_file, yaml_file], tmp_file)
        return tmp_file, None, None

def read_jp_post(jp_post, header, encoding):
    jp_post = Interface.read_csv(jp_post, fieldnames=header, encoding=encoding)['items']

    return jp_post

def gen_fake(seed, el, locale):
    flattened_el = Converter.flatten_obj(el)
    # print(flattened_el)
    # header = ['gov_code', 'postcode_old', 'postcode', 'prefecture_kana', 'city_kana', 'area_kana', 'prefecture', 'city', 'area', 'city_has_multi_code', 'num_per_village', 'street', 'multi_city_in_one_code', 'renew', 'misc']
    header = [ 'jis_code', 'kana_name', 'kanji_name', 'prefecture', 'city', 'area', 'street', 'office_number', 'postcode_old', 'handling_office', 'office_number_type', 'multiple_numbers', 'modification_code' ]

    fake = MyProviders(seed, locale, flattened_el, read_jp_post(jp_post='data/jigyosho.csv', header=header, encoding='cp932'))
    # fake.add_provider(MyProviders)
    fields = fake.fields()
    # flattened_data = Converter.flatten_obj(fields)

    return fields

def create_choices(data):
    choiced = []
    for label, choices in data.items():
        choices_list = list(choices.keys())
        checkbox_group = gr.CheckboxGroup(choices=choices_list, value=choices_list[:1], label=label, elem_id=uuid.uuid4())
        choiced.append(checkbox_group)
        # choiced.update({label: checkbox_group})
    # print(choiced)
    return choiced

def update_choices(el, *choiced): # TODO
    checkbox_groups = []
    for g in choiced:
        li = []
        for l in g:
            li.append(list(gen_fake(0, {'items': l}, 'en_US').keys()))
        checkbox_groups.append(gr.CheckboxGroup.update(choices=li))
    return tuple(checkbox_groups)


is_running = True

if __name__ == '__main__':

    with gr.Blocks(
        css='footer {visibility: hidden}', title='Profile Generator'
        ) as app:
        gr.HTML(f"<div style='max-width:100%; max-height:360px; text-align: center; overflow:auto'><h1>Profile Generator</h1></div>")
        with gr.Row(equal_height=False):
            # with gr.Column(variant='panel'):
                # num_interval = gr.Number(3, precision=1, label='Interval')
            btn_stop = gr.Button('Stop', size='sm')
            btn_start = gr.Button('Start', size='sm')
            btn_run = gr.Button('Run', variant='primary', size='sm')

        with gr.Tab('Processor'):
            with gr.Row():
                with gr.Column(variant='panel'):
                    el = gr.File('el/0000.toml')
                    el_data = Interface.read_file(el.value['name'])
                    locales = Interface.read_file('data/locales.toml')["locales"]
                    locale = gr.Dropdown(choices=locales, value='en_US', multiselect=True, label='Locale')
                    prev_flags = gr.Dropdown(choices=['table', 'tree'], value=['tree'], multiselect=True, label='Preview')
                    size = gr.Number(minimum=1, maximum=100, value=1, precision=0, label='Size')
                    orate = gr.Number(minimum=0.0, maximum=1.0, value=1.0, label='Occurrence Rate')
                    seed = gr.Number(value=-1, precision=0, label='Seed')

                    with gr.Accordion(label='Fields'):
                        targets = gen_fake(0, el_data, 'en_US')
                        # print(targets)
                        choiced = create_choices(targets)

                with gr.Column(variant='panel'):
                    out_files = gr.Files()
                    out_text = gr.Code(language='yaml')
        with gr.Tab('Viewer'):
            with gr.Row():
                with gr.Column(variant='panel'):
                    out_df = gr.Dataframe()
        with gr.Tab('Preferences'):
            with gr.Row():
                with gr.Column(variant='panel'):
                    gr.Markdown('# Preferences')
        with gr.Tab('Help'):
            with gr.Row():
                with gr.Column(variant='panel'):
                    gr.Markdown('# Help')


        inputs = [
            el,
            locale,
            prev_flags,
            size,
            orate,
            seed,
            *choiced
        ]

        outputs=[
            out_files,
            out_text,
            out_df,
        ]

        examples = [
            ['el/en01.toml', ['en_US'], ['tree']],
            ['el/zh01.toml', ['zh_CN'], ['table']],
            ['el/ja01.toml', ['ja_JP'], ['tree']],
            ['el/ko01.toml', ['ko_KR'], ['table']],
        ]
        examples = gr.Examples(examples, inputs[:2], inputs[:2])

        inputs[0].change(fn=update_choices, inputs=[el, *choiced], outputs=choiced)
        btn_run.click(gen_data, inputs, outputs)
        start_repeat = btn_start.click(gen_data, inputs, outputs, every=1)
        stop_repeat = btn_stop.click(None, None, None, cancels=start_repeat)


    app.queue().launch(
        # inline=True,
        inbrowser=False,
        # share=True,
        # debug=True,
        # max_threads=40,
        # auth=('test','pass'),
        # auth_message=auth_message,
        # prevent_thread_lock=False,
        show_error=True,
        server_name=None,
        # server_port=None,
        # show_tips=False,
        # height=,
        # width=,
        # encrypt=,
        # favicon_path="assets/favicon.ico",
        ssl_keyfile=None,
        ssl_certfile=None,
        ssl_keyfile_password=None,
        ssl_verify=True,
        quiet=False,
        # show_api=False,
        # file_directories=False,
        # allowed_paths=False,
        # blocked_paths=False,
        # root_path=False,
        # app_kwargs=False,
        )