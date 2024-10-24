# Custom FontをSVGのような可変寸法で使いたい

1. SVGFontをつくり、pathとして埋め込む


これは不可

```svg
<foreignObject>
```

svg2png(SVGFont,fontforge) でFont x, y がリセットされる
```css
  @font-face {
  font-family:          myfont;
  font-style:           normal;
  font-weight:          bold;
  src:                  url("../../fonts/Sevenfold.otf");
  }
```

- SVGFont
```
  <text x="50" y="200" font-family="YourFontName" font-size="40" fill="#9498d0">N8CH</text>
```

- glyph, units-per-em, horiz-adv-x

```
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <font id="customFont" horiz-adv-x="1000"> <!-- Set horiz-adv-x to the desired width of your characters -->
      <font-face font-family="YourFontName" units-per-em="1000" />
      <glyph unicode="N" d="M100 500l100-500h200l100 500h-50l-20-100h-160l-20 100h-50zm80-280h160l20 100h-200zm80 280v-200h40v200z"/>
      <!-- Add more glyph elements for other characters -->
    </font>
  </defs>

  <!-- Example usage of the custom font -->
  <text x="50" y="200" font-family="YourFontName" font-size="40" fill="#9498d0">N8CH</text>
</svg>

```