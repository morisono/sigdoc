# 背景

[Gist外部埋め込みHTMLをJSONPで受け取る](http://qiita.com/zaneli@github/items/8515089e2a786eed181e)にてGistをJSONPで
取得できることを知った。

# JSONPで取得できるJSONは微妙

JSONPで取得したJSONはサイトに貼り付けるには便利なのだが、コードとして取り出すにはちょっと面倒

```html
<div class="file-data">
    <table cellpadding="0" cellspacing="0" class="lines highlight">
        <tr>
            <td class="line-numbers">
                <span class="line-number" id="file-index-html-L1" rel="file-index-html-L1">1</span>
                <span class="line-number" id="file-index-html-L2" rel="file-index-html-L2">2</span>
                <span class="line-number" id="file-index-html-L3" rel="file-index-html-L3">3</span>
            </td>
            <td class="line-data">
                <pre class="line-pre">
                  <div class="line" id="file-index-html-LC1"><span class="cp">&lt;!DOCTYPE html&gt;</span></div>
                  <div class="line" id="file-index-html-LC2"><span class="nt">&lt;h2&gt;</span>Road to videoconverter.js<span class="nt">&lt;/h2&gt;</span></div>
                  <div class="line" id="file-index-html-LC3"><span class="nt">&lt;script </span><span class="na">src=</span><span class="s">&quot;http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js&quot;</span><span class="nt">&gt;&lt;/script&gt;</span></div>
				</pre>
            </td>
         </tr>
      </table>
</div>
```
このように、行番号のデータが埋めこまれ、ちょっと扱うのが面倒臭そうでした。


# HTMLやJavaScriptのコードを取り出したい

よくよく上の例を見るとコード本体は&lt;pre class="line-pre"&gt;、preタグでかつclass属性がline-preのタグの中身を取り出せば良さそう。

## XPath登場

正規表現でも行けそうでしたが、今回は自分が数日前に覚えたXPathで取り出します。

```js
var codes = document.evaluate("//pre[@class='line-pre']",dom,null, XPathResult.ANY_TYPE, null );
```

### HTMLやコードの取出し、

```js
var codes = document.evaluate("//pre[@class='line-pre']",dom,null, XPathResult.ANY_TYPE, null );
for(var i = 0; i < codes.length; i++) {
  
}
```

## Chromeで動かしたら。。

最近はiOSの事もあり、Chromeで開発する方が多い感じですが、私はMosaic自体から細々とFirefox使っている縁もあり、
Firefoxで開発してます。

が、そんな昨今のChrome人気があり、Chromeで動かしたら、まさかのエラー！

ちょっと調べて解決しそうになかったので、XPathでの実装は諦め、正規表現で実装することになりました。

# コード

バカの一つ覚えでjQueryでAjaxとかヘドがでるので自前でAjaxな中二病が通りますよ。

```js
function getGist(gistUrl) {
        //"https://gist.github.com/<ユーザー名>/<Gist ID>.json?calback=<コールバック関数名>"
        //var gistUrl = "https://gist.github.com/mbostock/6dcc9a177065881b1bc4";
        gistUrl += ".json?callback=cb";
        var s = document.createElement('script');
        s.charset = 'utf-8';
        s.type = "text/javascript";
        s.src = gistUrl;
        document.body.appendChild(s);
}

/**
 * JSONPのコールバック
 */
function cb(gistJson) {
    // JSONPで返されるJSONのdivにサイトに貼り付け用のHTMLが文字列で格納されている。
    console.dir(parse(text2Dom(gistJson.div)));
}

/**
 * 文字列からDOMに変換する
 */
function text2Dom(htmlPart) {
    var dummyDiv = document.createElement("div");
    dummyDiv.innerHTML = htmlPart;
    return dummyDiv;
}

/**
 * DOMから扱いやすいJSONを返す
 */
function parse(dom) {
    // 取りたいもの
    // <pre class="line-pre">！このの部分！</pre>
    var codes = getCode4Chrome(dom);
    var gistCode = [];
    for(var i=0; i<codes.length; i++) {
        var res = codes[i];
        var obj = {};

        // gistのファイル名をもとにつけられるIDを元に、ファイル種別、ファイル名を取得する。
        // file-index-html-LCNな形式なので、
        // kind:html,id:indexという形で取り出す。
        var tmp = (res.firstChild.attributes.id.value).split("-");
        obj.kind = tmp[tmp.length - 2];
        obj.id = tmp.slice(1, tmp.length - 1).join("-");

        // 行番号の装飾情報を削除する。
        tmp = res.innerHTML;
        // 行番号のタグの直前に改行コードを埋め込んでおく。
        // これやらないと、取り出したjsが一行になり、//コメントで即死。
        res.innerHTML = tmp.replace(/<div class=\"line\"/g,"\n<div class=\"line\"" );

        // preタグ要素はtextContentで不要な装飾情報タグを取り除ける模様。
        obj.code = res.textContent;
        gistCode.push(obj);
    }
    return gistCode;
}

/**
 * コードの中身の取出し
 */
function getCode4Chrome(dom) {
    var codes = [];
    var regex = /<pre class=\"line-pre\".*?>(.*?)<\/pre>/g;
    var match = regex.exec(dom.innerHTML);
    // matchの2番目の要素から括弧の中にマッチした文字列が格納されている模様。
    for(var i=1; i <match.length; i++) {
        // DOM形式で保持しておく。
        codes.push(text2Dom(match[i]));
    }
    return codes;
}
```
