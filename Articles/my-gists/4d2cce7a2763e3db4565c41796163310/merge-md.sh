#!/bin/bash

# 検索するディレクトリを指定
search_dir="."

# 出力ファイル名を指定
output_file="merged.md"

# 一時ファイルを作成
temp_file=$(mktemp)

# Markdownファイルを検索し、ソートして処理
fd -e md "$search_dir" | sort | while read -r file; do
  # ファイル名をコメントとして追加
  echo "<!-- $file -->" >> "$temp_file"
  # ファイル内容を追加
  cat "$file" >> "$temp_file"
  # ファイル内容の後に改行を追加
  echo -e "\n" >> "$temp_file"
done

# 一時ファイルを最終出力ファイルに移動
mv "$temp_file" "$output_file"

echo "Markdown files have been merged into $output_file"
