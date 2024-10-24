import gradio as gr

with gr.Blocks() as app:
    with gr.Accordion('devtoys', open=False):
        with gr.Accordion('Essentials', open=False):

            with gr.Accordion('base64', open=False):
                in_base64 = gr.Textbox('in_base64')
                out_base64 = gr.Textbox('out_base64')

                def run_base64(in_base64):
                    result = str(in_base64)
                    return gr.Textbox.update(result)
                in_base64.change(run_base64, in_base64, out_base64)

            with gr.Accordion('html', open=False):
                in_html = gr.Textbox('<html>Hi!</html>', label='in_html')
                out_html = gr.Textbox('out_html')
                chk_deci = gr.Textbox('decimal')
                chk_nameref = gr.Textbox('use name ref')
                chk_encode = gr.Textbox('encode all')

                def run_html(in_html):
                    result = str(in_html)
                    return gr.Textbox.update(result)
                in_html.change(run_html, in_html, out_html)

            with gr.Accordion('url', open=False):
                in_url = gr.Textbox('in_url')
                out_url = gr.Textbox('out_url')

                def run_url(in_url):
                    result = str(in_url)
                    return gr.Textbox.update(result)
                in_url.change(run_url, in_url, out_url)

            with gr.Accordion('jwt', open=False):
                in_jwt = gr.Textbox('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c', label='in_jwt')
                out_jwt = gr.Textbox('out_jwt')
                out_jwt_header = gr.Textbox('out_jwt_header')
                out_jwt_payload = gr.Textbox('out_jwt_payload')
                out_jwt_secret = gr.Textbox('out_jwt_secret')
                drp_jwt_algo = gr.Textbox('drp_jwt_algo')

                def run_jwt(in_jwt):
                    result = str(in_jwt)
                    return gr.Textbox.update(result)
                in_jwt.change(run_jwt, in_jwt, out_jwt)

            with gr.Accordion('json2yaml', open=False):
                in_json2yaml = gr.Textbox('in_json2yaml')
                out_json2yaml = gr.Textbox('out_json2yaml')

                def run_json2yaml(in_json2yaml):
                    result = str(in_json2yaml)
                    return gr.Textbox.update(result)
                in_json2yaml.change(run_json2yaml, in_json2yaml, out_json2yaml)

            with gr.Accordion('num_base', open=False):
                in_num_base = gr.Textbox('1101', label='in_num_base')
                out_num_base_bin = gr.Textbox('out_num_base_bin')
                out_num_base_oct = gr.Textbox('out_num_base_oct')
                out_num_base_deci = gr.Textbox('out_num_base_deci')
                out_num_base_hex = gr.Textbox('out_num_base_hex')
                out_num_base_base32 = gr.Textbox('out_num_base_base32')
                out_num_base_base64 = gr.Textbox('out_num_base_base64')

                def run_num_base(in_num_base):
                    result = str(in_num_base)
                    return gr.Textbox.update(result)
                in_num_base.change(run_num_base, in_num_base, out_num_base_bin)

            with gr.Accordion('timestamp', open=False):
                in_timestamp = gr.Textbox('1691959765829', label='in_timestamp')
                out_timestamp = gr.Textbox('out_timestamp unix')
                out_timestamp_datetime = gr.Textbox('out_timestamp_datetime')
                out_timestamp_cunix = gr.Textbox('out_timestamp_cunix')
                btn_stop = gr.Button('stop')
                def run_timestamp(in_timestamp):
                    result = str(in_timestamp)
                    return gr.Textbox.update(result)
                in_timestamp.change(run_timestamp, in_timestamp, out_timestamp)

            with gr.Accordion('curl2code', open=False):
                in_curl = gr.Textbox('curl example.com', label='in_curl')
                out_curl = gr.Textbox('out_curl')
                drp_lang = gr.Dropdown(choices=['Python'], label='out_curl_lang')

                def run_curl(in_curl):
                    result = str(in_curl)
                    return gr.Textbox.update(result)
                in_curl.change(run_curl, in_curl, out_curl)

            with gr.Accordion('uuid', open=False):
                chk_hyphen = gr.Checkbox(label='chk_hyphen')
                chk_case = gr.Checkbox(label='chk_case')
                rad_ver_v1 = gr.Radio(label='rad_ver_v1')
                rad_ver_v4 = gr.Radio(label='rad_ver_v4')
                in_uuid = gr.Textbox('Counnt')
                out_uuid = gr.Textbox('uuid')

                def run_uuid(in_uuid):
                    result = str(in_uuid)
                    return gr.Textbox.update(result)
                in_uuid.change(run_uuid, in_uuid, out_uuid)

            with gr.Accordion('hash', open=False):
                drp_type = gr.Dropdown(choices=['MD5'], label='out_curl_lang')
                in_hash = gr.Textbox('in_hash')
                out_hash = gr.Textbox('out_hash')

                def run_hash(in_hash):
                    result = str(in_hash)
                    return gr.Textbox.update(result)
                in_hash.change(run_hash, in_hash, out_hash)

            with gr.Accordion('regex', open=False):
                chk_global_match = gr.Checkbox(label='chk_global_match')
                chk_ignore_case = gr.Checkbox(label='chk_ignore_case')
                chk_multiline = gr.Checkbox(label='chk_multiline')
                chk_dot_all = gr.Checkbox(label='chk_dot_all')
                chk_unicode = gr.Checkbox(label='chk_unicode')
                chk_sticky = gr.Checkbox(label='chk_sticky')
                in_regex = gr.Textbox('^[a-z0-9]+(?:-[a-z0-9]+)*$', label='in_regex')
                out_regex = gr.Textbox('out_regex')

                def run_regex(in_regex):
                    result = str(in_regex)
                    return gr.Textbox.update(result)
                in_regex.change(run_regex, in_regex, out_regex)

            with gr.Accordion('color', open=False):
                rad_protanopia = gr.Radio(label='rad_protanopia')
                rad_deuternopia = gr.Radio(label='rad_deuternopia')
                rad_tritanopia = gr.Radio(label='rad_tritanopia')
                rad_achromatopsia = gr.Radio(label='rad_achromatopsia')
                rad_original = gr.Radio(label='rad_original')
                in_color = gr.File(label='in_color')
                out_color = gr.ColorPicker('out_color')
                out_color_simulated = gr.ColorPicker('out_color_simulated')

                def run_color(in_color):
                    result = str(in_color)
                    return gr.Textbox.update(result)
                in_color.change(run_color, in_color, out_color)

            with gr.Accordion('qr', open=False):
                rad_image = gr.Radio(label='rad_image')
                rad_svg = gr.Radio(label='rad_svg')
                rad_canvas = gr.Radio(label='rad_canvas')
                in_qr_version = gr.Textbox('in_qr_version')
                in_qr = gr.Textbox('in_qr')
                rad_error_correction = gr.CheckboxGroup(['Low','Mid','Quartile','High'], label='error_correction')
                out_qr = gr.Textbox('out_qr')

                def run_qr(in_qr):
                    result = str(in_qr)
                    return gr.Textbox.update(result)
                in_qr.change(run_qr, in_qr, out_qr)

            with gr.Accordion('cron', open=False):
                in_cron = gr.Textbox('0 */12 * * * *', label='in_cron')
                out_cron = gr.Textbox('out_cron')
                out_cron_last = gr.Textbox('out_cron_last')

                def run_cron(in_cron):
                    result = str(in_cron)
                    return gr.Textbox.update(result)
                in_cron.change(run_cron, in_cron, out_cron)

            with gr.Accordion('useragent', open=False):
                in_useragent = gr.Textbox('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Code/1.81.0 Chrome/108.0.5359.215 Electron/22.3.18 Safari/537.36', label='in_useragent')
                out_useragent = gr.Textbox('out_useragent')

                def run_useragent(in_useragent):
                    result = str(in_useragent)
                    return gr.Textbox.update(result)
                in_useragent.change(run_useragent, in_useragent, out_useragent)

app.launch()