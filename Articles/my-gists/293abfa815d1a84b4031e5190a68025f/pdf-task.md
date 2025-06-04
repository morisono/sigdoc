
# PDFTkを活用する

1. 結合やページの並べ替え
   
```bash
pdftk A=input1.pdf B=input2.pdf cat A B output output.pdf
```

1. 分割
   
```bash
pdftk input.pdf burst
```

1. ページの回転
   
```bash
pdftk input.pdf cat 1-endeast output output.pdf
```

1. 暗号化と復号化
   
```bash
pdftk input.pdf output output.pdf user_pw YOURPASSWORD
```

1. フォームの入力とフラット化
   
```bash
pdftk input.pdf fill_form data.fdf output output.pdf flatten
```

1. ウォーターマークの追加
   
```bash
pdftk input.pdf background watermark.pdf output output.pdf
```

1. メタデータの追加と更新
   
```bash
pdftk input.pdf update_info metadata.txt output output.pdf
```

1. ファイルの添付
   
```bash
pdftk input.pdf attach_files file.txt output output.pdf
```

1. ファイルの取り出し
   
```bash
pdftk input.pdf unpack_files output output_directory
```

1. PDFの複合化

```bash
pdftk secured.pdf input_pw foopass output unsecured.pdf
```

1. AES-128で暗号化（デフォルト）、すべての権限を保持（デフォルト）

```bash
pdftk 1.pdf output 1.128.pdf owner_pw foopass
```

1. 出力PDFを開くためにはパスワード 'baz' も使用する必要があります

```bash
pdftk 1.pdf output 1.128.pdf owner_pw foo user_pw baz
```

1. 印刷許可（PDFが開いた後）

```bash
pdftk 1.pdf output 1.128.pdf owner_pw foo user_pw baz allow printing
```

1. 出力にRCA 40ビットの暗号化を適用し、すべての権限を取り消します（デフォルト）。オーナーPWを 'foopass' に設定します

```bash
pdftk 1.pdf 2.pdf cat output 3.pdf encrypt_40bit owner_pw foopass
```

1. 2つのファイルを結合します。そのうち1つはパスワード 'foopass' が必要です。出力は暗号化されません。

```bash
pdftk A=secured.pdf 2.pdf input_pw A=foopass cat output 3.pdf
```

1. in1.pdfとin2.pdfを新しいPDFのout1.pdfに結合します

```bash
pdftk in1.pdf in2.pdf cat output out1.pdf
```

   または（ハンドルを使用する場合）：

```bash
pdftk A=in1.pdf B=in2.pdf cat A B output out1.pdf
```

   または（ワイルドカードを使用する場合）：

```bash
pdftk *.pdf cat output combined.pdf
```

1. in1.pdfからページ13を削除してout1.pdfを作成します

```bash
pdftk in.pdf cat 1-12 14-end output out1.pdf
```

   または：

```bash
pdftk A=in1.pdf cat A1-12 A14-end output out1.pdf
```

1. PDFページストリームを解凍して、PDFをテキストエディタ（たとえばvim、emacs）で編集できるようにします

```bash
pdftk doc.pdf output doc.unc.pdf uncompress
```

1. PDFの破損したXREFテーブルとストリームの長さを修復します

```bash
pdftk broken.pdf output fixed.pdf
```

1. 単一のPDFドキュメントをページに分割し、データをdoc_data.txtにダンプします

```bash
pdftk in.pdf burst
```

1. 単一のPDFドキュメントを暗号化されたページに分割します。低品質の印刷を許可します

```bash
pdftk in.pdf burst owner_pw foopass allow DegradedPrinting
```

1. PDFドキュメントのメタデータとブックマークに関するレポートをreport.txtに書き込みます

```bash
pdftk in.pdf dump_data output report.txt
```

1. 最初のPDFページを時計回りに90度回転させる

```bash
pdftk in.pdf cat 1east 2-end output out.pdf
```

1. PDFドキュメント全体を180度回転させる

```bash
pdftk in.pdf cat 1-endsouth output out.pdf
```

