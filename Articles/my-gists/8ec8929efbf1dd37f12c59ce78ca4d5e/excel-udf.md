# Excelでのユーザー定義関数（UDF）の作成

Excelには便利なビルトイン関数がたくさんありますが、特定の要件に合わない場合、ユーザー独自の関数を作成することができます。これがユーザー定義関数（UDF）です。UDFを使うことで、特定の処理をカスタマイズして自分のニーズに合わせることができます。

## UDFの基本

ExcelでUDFを作成するには、VBA（Visual Basic for Applications）を使用します。以下は、簡単なUDFを作成する基本的なステップです。

```vba
Function MyCustomFunction(arg1 As Double, arg2 As Double) As Double
    ' ここに関数の処理を記述
    MyCustomFunction = arg1 + arg2
End Function
```
この例では、2つの引数を受け取り、それらを加算して結果を返す簡単な関数が定義されています。

- GetHyperlink : ハイパーリンクのURLを取得

```vba
Function GetHyperlink(セル As Range) As String
　　　　Dim sp As Shape
　　　　If セル.Hyperlinks.Count > 0 Then
　　　　　　　　GetHyperlink = セル.Hyperlinks(1).Address
　　　　End If
　　　　For Each sp In ActiveSheet.Shapes
　　　　　　　　If セル.Address = sp.TopLeftCell.Address Then
　　　　　　　　　　　　GetHyperlink = GetHyperlink & vbLf & sp.Hyperlink.Address
　　　　　　　　End If
　　　　Next
End Function
```
## UDFの使い方
UDFを使用するには、まずVBAエディタを開き、コードを挿入して保存します。保存した後、Excelのセルで以下のように関数を呼び出すことができます。
```
=MyCustomFunction(A1, B1)
```
ここでは、A1とB1のセルの値を引数として関数を呼び出しています。


- GetHyperlink : 

```
=GetHyperlink(A1)
```

## 注意事項
UDFを使用する場合は、マクロが有効になっていることを確認してください。
コードは慎重に検討し、エラーハンドリングを実装するなど、堅牢なコードを書くよう心がけましょう。
UDFはExcelの機能を拡張し、特定のタスクを簡素化するために非常に強力なツールです。自分の作業を効率的に行うために、ぜひUDFを活用してみてください。