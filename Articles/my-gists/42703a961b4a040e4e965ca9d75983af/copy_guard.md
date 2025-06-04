# セキュアなウェブサイトの構築

```html
<body onCopy="return false;">サイト全体をコピーさせたくない。</body>
```

```html
<h2 onCopy="return false;">特定のコンテンツをコピーさせたくない。</h2>
```

```html
<div style="-webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none;">DO NOT COPY </div>
```

```js
document.body.oncopy = function(event) { 
  event.preventDefault(); 
}
```

```html
<div onCopy="alert('DO NOT COPY'); return false;">DO NOT COPY</div>
```

```html
<body onContextmenu="return false;">右クリックしちゃだめ。</body>
```


```html
<body onMouseDown="return false;" onSelectStart="return false">
```

```html
<script>
/*<![CDATA[*/
  document.ondragstart = function(){return false;};
/*]]>*/
</script>
```

```css
img {
  pointer-events: none;
}
```

```css
.protect{
  position:relative;
  disply:block;
    &:before{
      position:absolute;
      left:0;
      top:0;
      right:0;
      bottom:0;
      background:url('画像のURL/mask.png');
      z-index:1;
     }
}
```

```html
<div class="protect"><img src="画像のURL" alt=""></div>
```

```css
.protect{
  pointer-events:none;
  -webkit-touch-callout:none;
  -webkit-user-select:none;
  -moz-touch-callout:none;
  -moz-user-select:none;
  touch-callout:none;
  user-select:none;
}
```

```html
<div class="protect"><img src="画像のURL" alt=""></div>
```

```html
<meta http-equiv="imagetoolbar" content="no" />
```
**Ref.**: 
- [WEBサイトのテキスト・画像のコピー・キャプチャ防止策まとめ | 何もないけどヨロシク。](https://nanimonaikedo.jp/coding/406/)
