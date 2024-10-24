'''
Usage: ❯ python scripts/api_viewer_e-stat.py --api_key $API_KEY_1
'''

import argparse
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os
import time
import tempfile

class Interface:

    def get_tempdir():
        timestamp = int(time.time())
        temp_dir = tempfile.mkdtemp()
        return timestamp, temp_dir

def download_datasheet(api_key, params, output_format):
    try:
        if output_format == 'csv':
            endpoint = 'http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData'
        else:
            endpoint = 'http://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsData'
        url = f"{endpoint}?{params}&appId={api_key}"

        res = requests.get(url)
        print(f' --> {res}')
        return res
    except Exception as e:
        print(e)
        return

def replace_col(col_origin, col_rep):
    output = list(col_origin.copy())

    if len(col_origin) < len(col_rep):
        raise ValueError('交換元の列のデータ数が不足しています')

    for idx, col in enumerate(col_rep):
        output[idx] = col
    return output

def save_datasheet(output_path, res_csv, output_format):
    if output_format != 'json':
        with open(f'{output_path}.csv', 'w', encoding='utf8') as f:
            f.write(res_csv.text)
            print(f'   --> {output_path}.csv')

def save_plot_image(output_path):
    plt.savefig(f'{output_path}.png')
    print(f'   --> {output_path}.png')
def analyze_data(res):
    main_data = res.json()['GET_STATS_DATA']['STATISTICAL_DATA']

    df_data = pd.DataFrame(main_data['DATA_INF']['VALUE'])
    df_class = pd.DataFrame(main_data['CLASS_INF']['CLASS_OBJ'])
    cols = replace_col(df_data.columns, df_class['@name'])
    df_data.columns = cols
    code2name_dict = {}
    for key, data_class in zip(df_class['@name'], df_class['CLASS']):

        code2name = {data['@code']:data['@name'] for data in data_class}
        code2name_dict[key] = code2name

    for key in df_class['@name']:
        df_data[key] = df_data[key].map(code2name_dict[key])
    df_data2018 = df_data[df_data['時間軸(年次)']=='2018年']
    query_men = '''
            性別=="男性" and
            表章項目=="平均値" and
            身長体重=="身長(cm)" and
            "総数" not in 年齢階級 and
            "（再掲）" not in 年齢階級
            '''
    df_data2018_men = df_data2018.query(query_men.replace('\n      ',''))
    mask = [True if not '（再掲）' in x else False for x in df_data2018_men['年齢階級']]
    df_data2018_men = df_data2018_men[mask]
    query_women = '''
            性別=="女性" and
            表章項目=="平均値" and
            身長体重=="身長(cm)" and
            "総数" not in 年齢階級 and
            "（再掲）" not in 年齢階級
            '''
    df_data2018_women = df_data2018.query(query_women.replace('\n      ',''))
    mask = [True if not '（再掲）' in x else False for x in df_data2018_women['年齢階級']]
    df_data2018_women = df_data2018_women[mask]
    df_data2018_men['$'] = df_data2018_men['$'].astype(float)
    df_data2018_women['$'] = df_data2018_women['$'].astype(float)

    mean_men, mean_women = df_data2018_men['$'].mean(), df_data2018_women['$'].mean()
    plt.figure(figsize=(10, 5))
    plt.bar(df_data2018_men['年齢階級'], df_data2018_men['$'], label='男性',
            align='edge', width=-0.5, color='royalblue')
    plt.bar(df_data2018_women['年齢階級'], df_data2018_women['$'], label='女性',
            align='edge', width=0.5, color='tomato')

    plt.plot(df_data2018_men['年齢階級'], np.ones(len(df_data2018_men))*mean_men, label='男性平均',
             color='blue', linestyle='--')
    plt.plot(df_data2018_women['年齢階級'], np.ones(len(df_data2018_women))*mean_women, label='女性平均',
             color='red', linestyle='--')

    plt.xticks(rotation=90)
    plt.grid()
    plt.legend()
    save_plot_image(output_path)

def main(api_key, params, output_format='csv'):
    ts, tempd = Interface.get_tempdir()
    output_path = f'{tempd}/{ts}'

    res = download_datasheet(api_key, params, output_format)
    if res is None:
        print("Failed to download data.")
        return
    else:
        save_datasheet(output_path, res, output_format)

    try:
        analyze_data(res)
        return
    except KeyError as e:
        print(f"Error: {e}")
        print("Failed to retrieve 'STATISTICAL_DATA' from the response. Check if the API response structure has changed.")
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="API Viewer for e-stat")
    parser.add_argument("--api_key", required=True, default='', help="Your e-stat API key")
    parser.add_argument("--sid", required=False, default='0003224177', help="statsDataId parameter")
    parser.add_argument("--appId", required=False, default='', help="appId parameter")
    parser.add_argument("--lang", required=False, default='J', help="lang parameter")
    parser.add_argument("--endpoints", required=False, default='J', help="endpoints parameter")
    parser.add_argument("--metaGetFlg", required=False, default='Y', help="metaGetFlg parameter")
    parser.add_argument("--cntGetFlg", required=False, default='N', help="cntGetFlg parameter")
    parser.add_argument("--explanationGetFlg", required=False, default='Y', help="explanationGetFlg parameter")
    parser.add_argument("--annotationGetFlg", required=False, default='Y', help="annotationGetFlg parameter")
    parser.add_argument("--sectionHeaderFlg", required=False, default=1, help="sectionHeaderFlg parameter")
    parser.add_argument("--replaceSpChars", required=False, default=0, help="replaceSpChars parameter")
    parser.add_argument("--output", required=False, default='csv', help="Use output format endpoint")

    args = parser.parse_args()
    params = {
        "sid": args.sid,
        "appId": args.appId,
        "lang": args.lang,
        "metaGetFlg": args.metaGetFlg,
        "cntGetFlg": args.cntGetFlg,
        "explanationGetFlg": args.explanationGetFlg,
        "annotationGetFlg": args.annotationGetFlg,
        "sectionHeaderFlg": args.sectionHeaderFlg,
        "replaceSpChars": args.replaceSpChars,

    }
    print(f'[~] Processing: https://www.e-stat.go.jp/dbview?sid={args.sid}', end='\n\n')

    params = "&".join(f"{key}={value}" for key, value in params.items())

    main(args.api_key, params, args.output)

