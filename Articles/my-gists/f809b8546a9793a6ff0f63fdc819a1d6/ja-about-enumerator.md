# Enumeratorについて

Enumeratorは、情報収集やセキュリティテストなどの目的で使用されるツールの一つです。主にGeneration機能とValidation機能の二つの側面があります。

## Generation

Generation機能は、情報やデータを生成するための機能です。
Generator機能は生成方法によって2種類に分類することができます。

- **buster**
   - bruteforceやDictionary Attackを行うツール
   - 代表的なツールとしてgobusterがあります。
   ```sh
   $ gobuster -u <URL> -w <wordlist>mggyuugy 
   ```

- **sitemap-scanner**
   - sitemap.xmlのハイパーリンクをたどるか、root pageからのHyperlink treeを再帰的に探索するツール
   - 代表的なツールとして[dirhunt](https://github.com/Nekmo/dirhunt)があります。
   ```sh
   $ dirhunt $url --to-file report.json
   ```

生成対象によってもう一層細かく分類することができ、以下の2つに分けられます。

- dns
- sub directory/file search

## Validation

Validation機能は生成された情報やURLなどが有効であるかを検証する機能です。これにより、セキュリティテストやネットワーク診断の信頼性が向上します。検証の対象としては、URLの有効性が挙げられます。

- **port-scanner**
   - ポートスキャンを行うツール
   - 具体的なツールはここに記載がありませんが、一般的にはネットワークセキュリティの評価や脆弱性診断に使用されます。
   ```sh
   $ nmap <target>
   ```

## 総括
Generation・Validation どちらかに特化したツールや、複数のモードを有するツール、両方を同時に行うツールなど、様々存在します。