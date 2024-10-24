import gradio as gr
import re

def markdown_to_html_table(markdown_text):
    img_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    title_pattern = re.compile(r'\*\*([^*]+)\*\*')
    link_pattern = re.compile(r'<p align="right"><a href="([^"]+)">([^<]+)</a></p>')
    desc_pattern = re.compile(r'\*\*\:[\s\n]+(.+)', re.DOTALL)

    items = []
    for block in markdown_text['text'].split("\n\n"):
        img_match = img_pattern.search(block)
        title_match = title_pattern.search(block)
        link_match = link_pattern.search(block)
        desc_match = desc_pattern.search(block)

        if img_match and title_match and link_match:
            img_alt = img_match.group(1)
            img_url = img_match.group(2)
            title = title_match.group(1)
            description = desc_match.group(1).strip()
            link_url = link_match.group(1)
            link_text = link_match.group(2)

            items.append({
                'img_url': img_url,
                'img_alt': img_alt,
                'title': title,
                'description': description,
                'link_url': link_url,
                'link_text': link_text
            })

    # HTML Table Generation
    html_table = "<table>\n"
    for i in range(0, len(items), 3):
        html_table += "  <tr>\n"
        for j in range(3):
            if i + j < len(items):
                item = items[i + j]
                html_table += f'    <td align="center" valign="top" width="33.33%">\n'
                html_table += f'      <a href="{item["link_url"]}">\n'
                html_table += f'        <img src="{item["img_url"]}" width="100px;" alt="{item["img_alt"]}"/><br />\n'
                html_table += f'        <sub><b>{item["title"]}</b></sub>\n'
                html_table += f'      </a><br />\n'
                html_table += f'      <p>{item["description"]}</p>\n'
                # html_table += f'      <a href="{item["link_url"]}" title="{item["link_text"]}">{item["link_text"]}</a>\n'
                html_table += f'    </td>\n'
            else:
                html_table += '    <td align="center" valign="top" width="33.33%"></td>\n'
        html_table += "  </tr>\n"
    html_table += "</table>"

    return html_table

def gradio_interface(input_markdown, output_file):
    html_table = markdown_to_html_table(input_markdown)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(html_table)

    return output_file, html_table

examples = '''
## List of Crypto Coins

1. ### ![image](https://user-images.githubusercontent.com/111455900/268934347-6f2fbefa-0f2a-4eca-949f-fd1e7ebd7dff.png) **BTC (Bitcoin/ビットコイン)**:
    BTC（ビットコイン）は、2008年にサトシ・ナカモトによって発表された、最も広く知られた暗号通貨です。ビットコインは、分散型のデジタル通貨で、ブロックチェーン技術を基盤にしています。時価総額ランキングで常にトップの位置にあり、発行上限は2100万枚です。現在の単価は約$50,000です。主要な取引所で取引されています。
    <p align="right"><a href="https://bitcoin.org/">Bitcoin.orgの公式サイト</a></p>

1. ### ![image](https://user-images.githubusercontent.com/111455900/268934291-867b42a5-ee40-48ca-a014-b233362aa3be.png) **ETH (Ethereum/イーサリアム)**:
    ETH（イーサリアム）は、スマートコントラクトと分散アプリケーション（DApps）のプラットフォームとして知られるEthereumのネイティブトークンです。Ethereumはビットコインとは異なるブロックチェーンを使用しており、時価総額ランキングで上位に位置しています。発行上限は設定されていませんが、将来のアップグレードで変更される可能性があります。現在の単価は約$3,000です。ETHは多くの取引所で取引されています。
    <p align="right"><a href="https://en.wikipedia.org/wiki/Ethereum">EthereumのWikipedia</a></p>

1. ### ![image](https://user-images.githubusercontent.com/111455900/268957616-8d48b448-2f37-4f5d-91e3-b9f3442553ce.png) **ETC (Ethereum Classic/イーサリアムクラシック)**:
    ETC（イーサリアムクラシック）は、Ethereumの分岐バージョンで、イーサリアムクラシックとも呼ばれます。これはEthereumのブロックチェーンの過去バージョンを維持し続けており、一部のコミュニティメンバーによって支持されています。
    <p align="right"><a href="https://en.wikipedia.org/wiki/Ethereum_Classic">Ethereum ClassicのWikipedia</a></p>

1. ### ![image](https://user-images.githubusercontent.com/111455900/268956176-1292bafd-d365-4532-95e0-41541f9a849d.png) **LTC (Litecoin/ライトコイン)**:
    LTC（ライトコイン）は、ビットコインに似たオープンソースの暗号通貨で、高速なトランザクション処理を提供することが特徴です。時価総額ランキングでは上位に位置しており、発行上限は8400万枚です。現在の単価は約$150です。ライトコインは多くの取引所で取引されています。
    <p align="right"><a href="https://en.wikipedia.org/wiki/Litecoin">LitecoinのWikipedia</a></p>

1. ### ![image](https://user-images.githubusercontent.com/111455900/268956235-3e36fad1-b177-4254-aaf2-a17050993130.png) **XMR (Monero/モネロ)**:
    XMR（モネロ）は、プライバシーと匿名性に特化した暗号通貨で、トランザクションの完全な秘匿性を提供します。モネロはプライバシー志向のユーザーに支持されており、時価総額ランキングで上位に位置しています。
    <p align="right"><a href="https://www.getmonero.org/">Moneroの公式サイト</a></p>

1. ### ![image](https://user-images.githubusercontent.com/111455900/268956288-8c71341a-ba5f-45eb-a77b-476079a9749c.png) **BCH (Bitcoin Cash/ビットコインキャッシュ)**:
    BCH（ビットコインキャッシュ）は、ビットコインの派生通貨で、高速で低コストのトランザクションを実現しようとしています。ビットコインとは異なるブロックサイズとコンセンサスルールを持ち、一部のユーザーと支持者によって採用されています。
    <p align="right"><a href="https://en.wikipedia.org/wiki/Bitcoin_Cash">Bitcoin CashのWikipedia</a></p>

1. ### ![image](https://user-images.githubusercontent.com/111455900/268956326-9e536c91-aa9a-4879-acdf-c01186692a4f.png) **EOS**:
    EOSは、分散アプリケーション（DApps）の開発をサポートするプラットフォームで、スケーラビリティと使いやすさに焦点を当てています。EOSトークンはEOS.IOプラットフォーム上で使用され、DAppsの開発者とユーザーに利益をもたらします。
    <p align="right"><a href="https://eos.io/">EOS.IOの公式サイト</a></p>
'''

iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.MultimodalTextbox(lines=10, label="Input Markdown", placeholder="Enter Markdown text here..."),
        gr.Textbox(label="Output HTML File Path", placeholder="Enter the output file path here...")
    ],
    outputs=[
        gr.File(label="Output HTML File"),
        gr.HTML(label="Generated HTML Table")
    ],
    examples=[[{'text': examples}, 'out.html']],
    description="Convert Markdown List to HTML Table (3xN) Format"
)

iface.launch()
