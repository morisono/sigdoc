# RSS

1. `target="_blank" `は現在のタブで開きます。元のページに戻りたい時にブラウザバックで戻らなくて済みます。ユーザーの離脱率が減少します。
```
<a href="example.com" target="_blank" rel="noopener">Link</a>
```

## HTML

```html
<div class="rss_wrapper">
    <div class="rss_item">
	<script type="text/javascript">
        <!--
            var blogroll_channel_id = ○○○○○○;
        // -->
        </script>
        <script type="text/javascript" charset="utf-8" src="https://blogroll.livedoor.net/js/blogroll.js"></script>
    </div>
    <div class="rss_item">
        <script type="text/javascript">
        <!--
            var blogroll_channel_id = ○○○○○○;
        // -->
        </script>
        <script type="text/javascript" charset="utf-8" src="https://blogroll.livedoor.net/js/blogroll.js"></script>
    </div>
</div>
```

## CSS

```css
.rss_wrapper {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-line-pack: stretch;
    align-content: stretch;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -ms-flex-flow: row wrap;
    flex-flow: row wrap;
    width: 100%;
    height: 250px;
    overflow-y: scroll;
}

.rss_item {
    -ms-flex-preferred-size: 50%;
    flex-basis: 50%;
    height: auto;
    padding: 10px;
}

.blogroll-list-wrap {
    list-style: none;
    font-size: 1em;
}

.blogroll-list-wrap a {
    text-decoration: none;
}

.blogroll-list-wrap a:hover {
    color: red;
}

@media screen and (max-width: 600px) {
    .rss_item {
        -ms-flex-preferred-size: 100%;
        flex-basis: 100%;
    }
}
```

https://blogroll.livedoor.com/

https://matometools.com/

https://feed.mikle.com/

https://blogcircle.jp/