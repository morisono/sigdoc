---

title: Learn Jq
name: learn-jq
description: 
status: pending
categories: education
tags: 
  - #json

lang: en
private: true
weight: 1
image: 
video: 
id: 4db517
uid: 4ff16534-4562-44c1-873b-c5d858191742
link: https://username.github.io/repo/posts/2024/08/19/0/1/learn-jq-
path: Notes/pending/learn-jq.md
slug: learn-jq
date: 2024-08-19T17:47:48
created_at: 1724057268
updated_at: 1724057268

---

# Learn Jq

## Abstract

を学ぶ。

## Introduction

Jq とは、


## Objectives

- [jq]()
- [gron]()
- [fx]()

Jqpgのデモに数多くの例が記載されています。

## Methodologies

### 基本

リファレンスの読み方

- `/n` のような表記は、n番目の用法 を意味します。(例: del/2 .. delの2番目の用法)

- `/empty` のような実際にスラッシュを書く記法と混同しないように注意しましょう。

1. aaa
   ```bash

   ```

### 選択


1. aaa
   ```bash

   ```


### 変更


1. aaa
   ```bash

   ```


### 削除

1. aaa
   ```bash
   jq '
      def when(p;q):
         if p? // false then q else . end;

      def delNull(p):
         walk(when(p == null; del(p)));

      delNull(.parent)
   '
   test.json
   ```

### カスタム関数定義 def

1. aaa
   ```bash

   ```



### Scriptingと読み込み

1. aaa
   ```bash

   ```


### Piping

1. aaa
   ```bash

   ```

### 活用例

1. ディレクトリ構造をCytoscapeJSONへ変換する

   powershellの `tree` コマンドで出力されるテキストを、可視化ツールCytoscapeで読み込める形式へ変換する。
   ```bash
   jq -c '
      [(.. | objects | select(.name) | {
         nodes:[{data:{id:.name,label:.name}}| reduce .[] as $d (null; .+$d)],
         edges:[{data:{source:.name, target:.contents[]?.name}} | reduce .[] as $d (null; .+$d)]
      })]
   '
   tree2cy-src.json

   jq -c '
   {nodes:[{data:.[].nodes[]}],edges:[{data:.[].edges[]}]}'
   tree2cy-dst.json
   ```

   ```

   ```


1. CSV を JSON へ変換する。
   ```bash
   def objectify(headers):
      def tonumberq: tonumber? // .;
      . as $in
      | reduce range(0; headers|length) as $i ({};
            if $in[$i] == "null" then
            .
            else
            .[headers[$i]] = ($in[$i] | tonumberq)
            end
         );

   def csv2table:
      # For jq 1.4, replace the following line by:  def trim: .;
      def trim: sub("^ +";"") |  sub(" +$";"");
      split("\n") | map( split(",") | map(trim) );

   def csv2json:
      csv2table
      | .[0] as $headers
      | reduce (.[1:][] | select(length > 0) ) as $row
            ( []; . + [ $row|objectify($headers) ]);

   csv2json

   ```

   ```

   ```


1. JSONを並び替える
   ```bash
   def reorder(a; n):
      def order(a; n):
         a as $a |
         n as $n |
         index($a) as $i |
         if $i == null then .
         else
               if $i<$n then .[:$i] + .[$i+1:$n+1] + [$a] + .[$n+1:]
               elif $n<$i then .[:$n] + [$a] + .[$n:]
               else .
               end
         end;

      . as $in
   | if type == "object" then
         reduce (keys_unsorted|order(a;n))[] as $key(
         {}; . + { ($key):  ($in[$key] | reorder(a; n)) }
         )
      elif type == "array" then map( reorder(a; n) )
      else .
      end;

   [.[]  | reorder("id"; 0)| reorder("W"; 5) | reorder("name"; 1)]
   ```

   ```

   ```

1. IDを連番で生成する・
   ```bash
   # 1 gen id for indexing
   jq '
   def genObjectId:
      with_entries(.key += "_" * length);

   def genArrayId:
      with_entries(.key |= "n" +(.|tostring) );
   '

   ```

   ```

   ```

1. ゼロパッドされたIDを配列に追加する
   ```bash
   .nodes | reduce range(0,length) as $i (.;.[$i].data.id = "#\($i)")

   def pad_left(s;n;c):
      s |tostring |(length |
      if . >= n then "" else c*(n-.) end) as $padding |
      "\($padding)\(.)"
      ;
   {
      nodes:(.nodes | reduce range(0,length) as $i (.;.[$i].data.id = "#"+ pad_left($i;4;0))),
      edges:.edges |{label:"team"}
   }
   ```

   ```

   ```


1. 再帰的にnullを削除する。
   ```bash
   jq '
      def when(p;q):
         if p? // false then q else . end;

      def delNull(p):
         walk(when(p == null; del(p)));

      delNull(.parent)
   '
   test.json
   ```

   ```

   ```

1. nullの代わりに空文字列を充填する。
   ```bash

   ```

   ```

   ```


1. ツリー構造をつくる。
   ```bash
   jq '
   def parsePathname:
      split("/") | {path: .[0:length-1], file: .[-1]};

   # skip over lines that only specify directories
   def pathnames:
      foreach inputs as $x (null;
         if . == null
         then if ($x|length) == 0 then 0 else . end
         else .+1
         end;
         select(. and . > 0)|$x)
         | parsePathname ;
      reduce pathnames as $pn ({};
         getpath($pn.path + ["children"]) as $children
         | setpath($pn.path + ["children"]; $children + [$pn.file]) );

   .| pathnames'
   dir.json

   ```

   ```

   ```

1. ツリー構造をフラット化する
   ```bash
   # _3 flatten
   jq '
      def flatten_obj(p):
         walk(when(p|(type == "object") and has(p); p|=p ));
   '

   # 3 flatten to raw
   jq '
      def flatten_obj:
         reduce (
               tostream |
               select(length==2) |
               .[0] |= [join(".")]
         ) as [$p,$v] ({}; setpath($p; $v));

      flatten_obj
   '
   test.json
   # walk(if select(has("children")|not) then flatten_obj else . end)


   # _3 Recursive select node & flatten
   jq '
      (.. | objects |  {
         nodes:[{data:{id:.name}}],
         edges:[{data:{source:.name, target:.contents[]?.name}}]
      }) | group_by(.nodes)
   '
   _jimaku.json

   # walk(if select(has("children")|not) then flatten_obj else . end)

   # Another plan for flatten
   jq -R --slurp -s '[
      split("\n\n") as $list

      | $list
      | .[0]
      | split("\n")
      | .  + [  .[0] | split("\\") | .[0:-1] | join("\\")  ] # add root folder
      | sort
      | . as $folders

      | $list
      | .[1]
      | split("\n") as $files

      | $folders [] as $parent


      | {
         path: $parent,
         children: (
               $files
               | map({
                  path: select(
                     . | (split("\\") | .[0:-1] | join("\\")) as $fileParent # get parent path
                        | $fileParent == $parent
                  )
               })
         )
      }



   ] as $flatTree
   | $flatTree'
   dirtree.txt

   ```

   ```

   ```

1. グループを作成する・重複をまとめる（内部結合）・非連結頂点の処理
   ```bash
   # group by .group propeties
   jq '[group_by(.group)[]|{(.[0].group): .}]'
   output.json

   # junction dups
   jq ' .[0]*.[1] | { nodes:.nodes, edges:.edges} '
   _out.json

   ## pick up specific properties
   jq '.[0]*.[1] | { nodes:[.nodes[]|{data,position}], edges:[.edges[].data]}'
   _out.json

   ## if no edges
   jq '.[] | { nodes:[.nodes[]|{data,position}], edges:[.edges[]?.data?]}'
   _out.json

   # del .position at edges
   jq 'del(.edges[]|.position)'
   outputss.json
   ```

   ```

   ```

1. 探索してマッチした場合に、要素を追加する。
   ```bash
   # 1 Add id or parent indexing
   jq '
   def traverse:
      if type == "object" and has("name") and has("type") then
         .name as $p |
         if .type == "directory" then
               {id:.name, parent} +(
                  if has("contents") then
                  {children:(.contents[]|.+{parent:$p})}+{classes:"compound"}
                  | map_values(traverse)
                  else null
                  end )
         elif .type == "file" then
            {id:.name}
         else null
         end
      elif type == "array" then
         map(traverse)
      else
         .
      end;

   .  | traverse'
   test.json
   ```

   ```

   ```

## Results



## Discussions

### Modules from RossetaCode.org

assert.jq - module to support assertions アサーションをサポートするモジュール
bitwise.jq - bit streams, bit arrays, and integers ビットストリーム、ビット配列、整数
fibonacci.jq - Fibonacci sequence and Fibonacci coding フィボナッチシーケンスとフィボナッチコーディング
peg.jq - Parsing Expression Grammar foundations 表現文法の基礎を解析
polynomials.jq - polynomials as JSON arrays JSON配列としての多項式
rational.jq - rational numbers 有理数
Date.jq - Gregorian calendar from the year 1 1年目のグレゴリオ暦
MRG32k3a.jq - MRG32k3a Combined Recursive Pseudo-Random Number Generator MRG32k3a複合再帰的疑似乱数ジェネレーター
RealSet.jq - Union of finite real intervals 有限の実際の間隔の連合


## Conclusion



## Summary



## Declarations




## References

1. https://github.com/fiatjaf/awesome-jq
1. https://github.com/wader/fq
1. https://github.com/xo/usql
1. https://github.com/neilotoole/sq
1. https://github.com/kellyjonbrazil/jc


[^1]: 
[^2]: 
[^3]: 
