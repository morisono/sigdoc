

## Tools

- Jq  ( CLI )
	- https://github.com/jqlang/jq
- Fx - Explorer ( CLI )
	- https://github.com/antonmedv/fx
	- gron https://github.com/tomnomnom/gron
	- jid
	- jo
   - https://github.com/jpmens/jo
	- jless (Fastest CLI)
- jp - parser
	- https://github.com/jmespath/jp
- [jnv](https://github.com/ynqa/jnv)
	- jaq
- https://github.com/trailofbits/graphtage
- https://github.com/gpanders/ijq


- Jqpg  ( Web / VSCode )
	- 
- Json Hero - Explore Json ( Web / Desktop / VSCode )
	- https://github.com/triggerdotdev/jsonhero-web

- https://github.com/paolosimone/virtual-json-viewer

- [JSON Diff - The semantic JSON compare tool](https://jsondiff.com/)
- https://github.com/zgrossbart/jdd

''
## Methodologies

- Pure JSON
- Json-Per-Line ([JSONL](https://jsonlines.org/))
- JSON5 (Commentable)



- Chrome Devtools > Networks > Preview

```bash
# Search json
cat demo.json | gron | fzf

# Search yaml
cat in.yaml | yj | gron | fzf

# Search toml
hcl | gron | fzf

# Search file path
rg 'bbs' -g "*.json" -null | parallel --dry-run gron {} '>\t' {.}.gron
rg 'bbs' -g "*.json" -null | parallel gron | fzf -m
rg 'bbs' -g "*.html" | pup -p 'a attr{href}' json{} | gron | fzf -m
rg 'github' -g "*.html" -0 -l | parallel -0 -k 'cat {}' | pup -p json{} | gron | fzf -m
rg 'github' -g "*.html" -0 -l | parallel -0 -k -j9 'cat {}' | pup -p a json{} | jq '[.[]|.href]' | gron | fzf -m


# Convert to JSON
curl --head www.example.com | jc --curl-head
cat file.csv | jc --csv

# Convert from xlsx
csvtk xlsx2csv demo.xlsx -o demo.csv | jc --csv

```

## PCRE2

### 量指定子 (Qualifier)

|メタキャラクタ|説明|
|-|-|
|*|0回以上の繰り返しにマッチ|
|+|1回以上の繰り返しにマッチ|
|?|0回または1回の出現にマッチ|
|{n}|指定した回数（ここではn回）の繰り返しにマッチ|
|{n,}|指定した回数（ここではn回）以上の繰り返しにマッチ|
|{n,m}|指定した回数の範囲（ここではn回以上m回以下）の繰り返しにマッチ|

### 特殊文字 (Special Character)

|[]|文字クラス|
|-|-|
|()|キャプチャ|
|^|アンカー|
|$|アンカー|
|\A|文字列先頭|
|\Z|文字列の末尾|
|\b|単語境界|
|\B|単語の境界以外|
|\d|数字全体|
|\w|単語文字全体|

キャプチャしたパターンは、`$1,$2,..$0`などとして置換文字列の構成に利用できます。

### 最短/最長一致

|パターン|説明|
|-|-|
|*|0回以上の繰り返しにマッチ|
|+|1回以上の繰り返しにマッチ|
|?|0回または1回の出現にマッチ|
|{n}|指定した回数（ここではn回）の繰り返しにマッチ|
|{n,}|指定した回数（ここではn回）以上の繰り返しにマッチ|
|{n,m}|指定した回数の範囲（ここではn回以上m回以下）の繰り返しにマッチ|


|パターン|説明|
|-|-|
|*?|0回以上の繰り返しにマッチ|
|+?|1回以上の繰り返しにマッチ|
|??|0回または1回の出現にマッチ|
|{n}?|指定した回数（ここではn回）の繰り返しにマッチ|
|{n,}?|指定した回数（ここではn回）以上の繰り返しにマッチ|
|{n,m}?|指定した回数の範囲（ここではn回以上m回以下）の繰り返しにマッチ|

### Lookaround (肯定/否定/先読み/後読み)

それぞれのパターンに名称がついており、総称してLookAroundといいます。
|パターン|名称|説明|
|-|-|-|
|X(?=Y)|肯定先読み(Positive lookahead)|X(Y が後に続く場合)|
|X(?!Y)|否定先読み(Negative lookahead)|X(Y が後に続かない場合)|
|(?<=Y)X|肯定後読み(Positive lookbehind)|X(Y の後の場合)|
|(?<!Y)X|否定後読み(Negative lookbehind)|X(Y の後でない場合)|

表にすると、さらに簡潔に表せます。
||LookAhead|LookBehind|
|-|-|-|
|Positive|(?=...)|(?<=...)|
|Negative|(?!...)|(?<!...)|


正規表現の LookAround (Lookahead, Lookbehind) に関して、さまざまなパターンを学習するための例題を、文字列 `pompompurin pompurinpom pompompom` を使っていくつか紹介します。LookAround には **先読み (Lookahead)** と **後読み (Lookbehind)** があり、条件に基づいて特定の部分にマッチさせることができます。

- `pom(?=purin)`: `pom` にマッチするが、続けて `purin` という文字列が続く場合のみマッチさせる。これにより、最初の `pom` にだけマッチする。

- `pom(?!purin)`: `pom` の後に `purin` が続かない場合にだけ `pom` をマッチします。

- `(?<=pom)pom`: 前に `pom` が存在する場合のみマッチする。

- `(?<!purin)pom`: `pom` の前に `purin` がない場合にのみ `purin` をマッチさせます。

- `(?<=purin)pom(?= )`: `purin` の後にあり、その後ろにスペース（半角空白）がある`pom`にのみマッチさせる。


### 正規表現のパフォーマンスについて

同じ文字列処理をするにしても、複数の表現が可能な場合があります。大規模な処理を行うような場面では、必要十分な検索が完了した時点で打ち切りにするような表現をつくると、処理全体のパフォーマンスが向上します。


### Search and Paste


- fx: 

   - search by regex: `/t(ue|hur)sday/i`
   - string wrapping: ``
   - JSON transformation
   - and JSON digging
   - streaming


   - Save
      ```bash
      cat demo.json | fx
      <select value or path or >
      <q to quit>
      # need to yank path; press y p then paste.
      ```


### Other format
#### YAML
- https://github.com/kislyuk/yq
- https://github.com/mikefarah/yq
- https://github.com/mikefarah/yq
- https://github.com/sclevine/yj

#### TOML
- https://github.com/TomWright/dasel

#### CSV
- https://github.com/BurntSushi/xsv
- https://github.com/jqnatividad/qsv
- http://johnkerl.org/miller/doc/

#### XLSX
- https://github.com/shenwei356/csvtk

#### HTML
- https://github.com/ericchiang/pup
- https://github.com/mgdm/htmlq

#### XML
- https://github.com/sibprogrammer/xq

#### Multiple
- http://augeas.net/
- https://github.com/saulpw/visidata

#### GUI
- https://www.tadviewer.com/


## Howto


### [JMESPath](https://jmespath.org/)

### XPath



- [GitHub - JoinMarket-Org/joinmarket-clientserver: Bitcoin CoinJoin implementation with incentive structure to convince people to take part](https://github.com/JoinMarket-Org/joinmarket-clientserver)

- [16 Best Free and Open Source JSON Tools - LinuxLinks](https://www.linuxlinks.com/best-free-open-source-json-tools/)




### Seealso

https://github.com/dbohdan/structured-text-tools