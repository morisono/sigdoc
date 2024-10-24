# Distortion

ここでは、画像処理における様々な変形手法について説明されています。以下では、それぞれの手法の詳細と適用例を追加して、情報量を増やしました。


## Displacement Mapping
変位マッピング(Displacement Mapping)は、別の画像(マップ画像)のピクセル値に基づいて、元の画像のピクセルを移動させる手法です。イラストに歪みを与えることができます。

オリジナルTシャツの商品プレビューについて考えてみましょう。Tシャツは布で出来ているので、布のしわの状態に応じて、イラスト画像にも微妙なしわを入れてください。

- 変位マップ ( 50グレーより明るい場合、左や上方向, 暗い場合、右や下方向に画像が歪むような)を作成
```sh
# Generate map_h.png and map_v.png from the displacement data (this is an example of how it might be done)
convert grid.png -virtual-pixel Black -displace 10x0 +distort SRT '1,0,10' map_h.png
convert grid.png -virtual-pixel Black -displace 0x10 +distort SRT '1,10,0' map_v.png
```

- テカリを表現する lightingを作成
```sh
# Apply lighting effect to enhance the realism (optional)
composite lighting.png output.png -compose HardLight final_output.png
```

- 適用
```sh
# Apply the displacement maps to the input image
composite map_h.png input.png -displace 210x0 temp_h.png
composite map_v.png temp_h.png -displace 0x40 output.png
```


```sh
composite map_h.png input.png map_v.png -displace 210x40 output.png
```
上記コマンドでは、水平方向のマップ画像(map_h.png)と垂直方向のマップ画像(map_v.png)を使用して、input.pngの各ピクセルを移動させ、output.pngに出力しています。この手法は、3Dレンダリングにおける地形の表現などにも使われます。

- `map_h.png`と`map_v.png`は、ピクセル移動量を示す2つのマップ画像
- `210x40`は、最大移動量のピクセル数(水平210、垂直40)

## UV Mapping 
UVマッピングは、3Dモデルの頂点に2D画像(テクスチャ)を貼り付ける手法です。上記コマンドでは、Blenderを使ってt-shirt.blendモデルのレンダリング画像を rendering.pyスクリプトで生成しています。UVマッピングは3Dモデルにテクスチャを適用する上で重要な処理です。

```sh
blender --background t-shirt.blend --python rendering.py
```

- `t-shirt.blend`は3Dモデルファイル
- `rendering.py`はUVマッピングとレンダリングを行うPythonスクリプト

## Distort SRT
まずはアルゴリズム一覧を確認しましょう。
```sh
magick -list distort | column
```

SRT変換(Scale, Rotation, Translation)は、画像全体に対して拡大・縮小、回転、平行移動を行う手法です。
```sh
magick logo: -distort SRT 200,0,1,45
```
logoを原点(0,0)を中心に拡大率1(等倍)、45度回転、(200,0)に平行移動した画像をoutput.pngに出力しています。


```sh
magick logo: -distort SRT "%[fx:w/2],%[fx:h/2],2,45,200,0" output.jpg
```
中心(w/2,h/2)を原点として、2倍に拡大、45度回転、(200,0)に平行移動した画像を出力します。

アフィン変換では、せいぜい平行四辺形までの変換しか行えません。台形のような射影変換が必要な場合は、`Perspective`ディストーションか`Bilinear`を使用します。

## Perspective

遠近射影変換(Perspective)は、元の四角形を任意の四角形に変換できる手法です。
```sh
magick $input -distort Perspective \
  'topleft(x,y) topleft-2(x,y) topright(x,y) topright-2(x,y) bottomleft(x,y) bottomleft2(x,y) bottomright(x,y) bottomright2(x,y)' $output
```

```sh
magick $input -distort 'Perspective' '0,0 100,100 1024,0 600,100 0,1024 100,600 1024,1024 600,600' $output
```

- 入力画像の4隅と出力画像の対応する4隅の座標を指定

## Bilinear
双線形補間(Bilinear)は、画像の回転や拡大・縮小時に、近傍の画素値から補間して新しい画素値を計算する手法です。
Bilinear変換は、4点対応の射影変換で、簡単に指定できます。
```

