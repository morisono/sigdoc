# 正規表現パターンまとめ

## kutoten
- `[]+`
- `[\u3000-\u303F]+`
- `ﾞﾟ`

## hira
- `[ぁ-ん]+`
- `[\u3040-\u309F]+`

## kata
- `[ァ-ヶ]+`
- `[\u30A0-\u30FF]+`

## cjk shift jis
- `[亜-熙]`

## cjk integrated kanji
- `[一-龠]+`
- `\u4E00-\u9FA0`
- `\u4E00-\u9FFF`
- `\u3005 々`  # 同上記号・同の字点
- `\u3006 〆`  # 締め
- `\u3007 〇`  # 漢数字のゼロ
- `[\u4E00-\u9FFF\u3005-\u3007\uFF61-\uFF9F]+`

## cjk compatible kanji

## kata han
- `[ｦ-ﾝ]+`
- `[\uFF61-\uFF9F]+`

## ancient chinese
- `\u4e00-\u9fa5`

## japanese
- `[\u3000-\u303F\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\u3005-\u3007\uFF61-\uFF9F]+`

## CJK et all in perl
- `[\p{Block=CJK_Compatibility}\p{Block=CJK_Compatibility_Forms}\p{Block=CJK_Compatibility_Ideographs}\p{Block=CJK_Compatibility_Ideographs_Supplement}\p{Block=CJK_Radicals_Supplement}\p{Block=CJK_Strokes}\p{Block=CJK_Symbols_And_Punctuation}\p{Block=CJK_Unified_Ideographs}\p{Block=CJK_Unified_Ideographs_Extension_A}\p{Block=CJK_Unified_Ideographs_Extension_B}\p{Block=CJK_Unified_Ideographs_Extension_C}\p{Block=CJK_Unified_Ideographs_Extension_D}\p{Block=CJK_Unified_Ideographs_Extension_E}\p{Block=CJK_Unified_Ideographs_Extension_F}\p{Block=Enclosed_CJK_Letters_And_Months}]`
- `(?<= [\p{L}\p{N}] )`
- `(?<! \p{General_Category=Unassigned} )`

## Unicode props
- ひらがな: `\p{Hiragana}`
- カタカナ: `\p{Katakana}`
- 漢字: `\p{Han}`

## ascii
- `[0x21-0x7e\s]+`
- `[0x20-0x7e]`
- `[\x00-\x7F]`

## posix char class
- `[:alpha:]` 英字 (Letter | Mark)
- `[:ascii:]` ASCIIに含まれる文字 (0000 - 007F)
- `[:blank:]` スペースとタブ (Space_Separator | 0009)
