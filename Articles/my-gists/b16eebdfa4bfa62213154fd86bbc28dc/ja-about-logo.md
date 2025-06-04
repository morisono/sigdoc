# ロゴの制作

## 手順

### 生成

#### Illustratorを用いる方法

#### Canvaを用いる方法

#### ImageMagickを用いる方法

1. **背景の拡張と白色化**

```bash
convert input_logo.jpg \
   -background white -extent 1200x1200 \
   -colors 3 -fuzz 10% -fill white -opaque '#b7271e' \
   output_logo_step1.jpg
```

- `-background white -extent 1200x1200`: 白色の背景を設定し、キャンバスを1200x1200ピクセルに拡張します。
- `-colors 3`: 画像の色数を3色に制限します。このオプションは減色処理を行います。
- `-fuzz 10%`: このオプションは色の比較において、指定された割合（ここでは10%）以内の色を同じ色と見なします。以降の `-fill white -opaque '#b7271e'` で使用されます。
- `-fill white -opaque '#b7271e'`: `#b7271e`に近い色を白色に置き換えます。

2. **テキストの追加**

```bash
convert output_logo_step1.jpg \
   -fill black -font 'Sevenfold' -pointsize 120 -gravity center \
   -annotate +0+400 'N8CH' \
   final_logo.jpg
```

- `-fill black`: テキストの塗りつぶし色を黒に設定します。
- `-font 'Sevenfold'`: 使用するフォントを 'Sevenfold' に設定します。フォントが存在しない場合は、適切なフォントを指定してください。
- `-pointsize 120`: テキストのサイズを120ポイントに設定します。
- `-gravity center`: テキストの位置を中央に設定します。
- `-annotate +0+400 'N8CH'`: テキスト 'N8CH' を中央に配置します.


### 変換

1. **SVGへのデータ形式変換**
SD VectorStudioで `final_logo.jpg` を開き、SVGファイルに保存します。

**クリーニング:** 余計な要素を除去します。

**カラーリング:** 色を塗りつぶします。
要素が適切に分かれていない場合は、コードを編集し、`path`を分割するなどの調整を行います。

**トリミング:** 余計な空白を除去します。全要素をGroupにまとめる。Alignツールで左上に寄せ、コードを編集し、viewBoxサイズを変更します。


2. **サイズ変換・展開処理**

ファイル名の規則に従って、必要なバリエーションのファイルを生成します。

#### 命名規則

基本形式:
`<Name/Timestamp>-<Type>-<Color>-<Shape>-<Variant>-<Size>.<Ext>`

拡張表現:

```yaml
- プレフィックス: 
   - 位置: （t, b, l, r, tl, tr, bl, br）
   - サイズ: （s, m, l, xl）
- サフィックス: 
   - 連番: (1, 1a, 2, ..)
   - 改訂: (r1, r2, ..) 
```

　例:
`MyLogo-2024-02-15-sTXT-CL1-RR-QR-1500x500.svg`

- 各要素は大文字で表記され、要素間にはハイフンが使用されます。ただし拡張表現・ファイルフォーマットは小文字で表記します。
- 文字数制限や可読性を考慮し、各要素の表記は簡潔に保たれています。

```yaml
- `<Name/Timestamp>`: ロゴの名前またはタイムスタンプ。
   - 名前はキャメルケース（例: `MyLogo`）で、単語間はアンダースコア `_` で区切ります。
   - タイムスタンプはISO 8601形式（例: `2024-02-15`）
- `<Type>`: ロゴの種類。
   - `TXT`: テキスト
   - `IMG`: 画像
- `<Color>`: ロゴの色。
   - `BW`: 黒地に白字
   - `WB`: 白地に黒字
   - `CL1`, `CL2`, ...: カラースキーム（`CL1`、`CL2`など、必要に応じて追加）
- `<Shape>`: ロゴの形状。
   - `C`: 円形
   - `R`: 長方形
   - `RR`: 角丸長方形
   - `FR`: フレーム
- `<Variant>`: ロゴのバリエーション。適用可能なものには*が付きます。
   - `QR`: QRコード
   - `BAR`: バーコード
   - `SN`: シリアルナンバー 
   - `DATE`: 日付
   - `TABLE`: テーブル
   - `URL`: URL
- `<Size>`: ロゴのサイズ（WxH px）
- `<Ext>`: ファイルの拡張子。
   - `SVG`
   - `PNG`
   - `JPG`
   - `WEBP`
- その他、必要に応じて追加
```