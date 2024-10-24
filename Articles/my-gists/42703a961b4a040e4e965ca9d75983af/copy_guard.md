```
<body onCopy="return false;">サイト全体をコピーさせたくない。</body>
```

```
<h2 onCopy="return false;">特定のコンテンツをコピーさせたくない。</h2>
```

```
<div style="-webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none;">コピーさせたくないコンテンツを記述 </div>
```

```
document.body.oncopy = function(event) { 
  event.preventDefault(); 
}
```

```
<div onCopy="alert('ここだけコピーしちゃだめ。'); return false;">コピーさせたくないコンテンツ。</div>
```

```
<body onContextmenu="return false;">右クリックしちゃだめ。</body>
```


```
<body onMouseDown="return false;" onSelectStart="return false">
```

```
<script>
/*<![CDATA[*/
  document.ondragstart = function(){return false;};
/*]]>*/
</script>
```

```
img {
  pointer-events: none;
}
```

```
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

```
<div class="protect"><img src="画像のURL" alt=""></div>
```

```
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

```
<div class="protect"><img src="画像のURL" alt=""></div>
```

```
<meta http-equiv="imagetoolbar" content="no" />
```

- https://nanimonaikedo.jp/coding/406/