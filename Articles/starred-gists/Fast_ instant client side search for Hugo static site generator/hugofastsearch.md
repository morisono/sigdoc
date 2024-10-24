# Super fast, keyboard-optimized, client side Hugo search

This is a fork of and builds upon the work of [Eddie Webb's search](https://gist.github.com/eddiewebb/735feb48f50f0ddd65ae5606a1cb41ae) and [Matthew Daly's search explorations](https://matthewdaly.co.uk/blog/2019/02/20/searching-content-with-fuse-dot-js/). 

It's built for the [Hugo](https://gohugo.io/) static site generator, but could be adopted to function with any json index compatible with [Fuse](https://fusejs.io) fuzzy search library. 

To see it in action, go to [craigmod.com](https://craigmod.com) and press `CMD-/` and start typing. 

![Fast Search](https://craigmod.com/images/misc/fastsearch.gif)

----

- [Why](#why-client-side-why-fast)
- [Sample](#example-craigmodcom)
- [Setup](#setup)
- [Files](#files)
  * [layouts/_default/baseof.html addition](#layouts_defaultbaseofhtml-addition)
  * [static/js/fastsearch.js](#staticjsfastsearchjs)
  * [CSS styling](#css-styling)
  * [layouts/\_default/index.json](#layouts_defaultindexjson)
  * [config.toml](#configtoml)
  * [License](#license)

----

## Why client side, why fast?
I believe [Fast Software is the Best Software](https://craigmod.com/essays/fast_software/) and wanted keyboard-based, super fast search for my [homepage](https://craigmod.com/) / online collection of essays. This method was highly inspired by Sublime Text's CMD-P/CMD-shift-P method of opening files / using functions. 

The core precepts of this exploration were:
- Minimal / zero external dependencies (no jQuery)
- Smallest possible size added to each page 
- json index only delivered when needed (further minimizing overall impact on page speed / user experience)
- Keyboard friendly, instant navigation (ala Alfred / macOS Spotlight) 

As [Eddie Webb points out](https://gist.github.com/eddiewebb/735feb48f50f0ddd65ae5606a1cb41ae), this method has the additional benefits of: 
- No NPM, grunt, etc
- No additional build time steps, just `hugo` as you would normally
- Easy to swap out choice of client side search tools, anything that can use a json index


## Example: craigmod.com
This search is live on my site, [craigmod.com](https://craigmod.com) on every page. How to use: 
- Press `CMD-/` to invoke search 
- start typing 
- use `tab` / `arrow keys` to select result 
- press `enter` to navigate to that page


## Setup
1. Add `index.json` file to `layouts/_default`
1. Add JSON as additional output format in `config.toml`
1. Add `search.js` and `fuse.js` (downloaded from [fusejs.io](https://fusejs.io/)) to `static/js`
1. Add `searchbox` html to bottom of `layouts/_default/baseof.html` 
1. Add `css` styles to your site's main css file or top of `baseof.html`
1. `hugo`
1. Visit `localhost:1313/`
1. Press CMD-/ to invoke search

You can check the json index by visiting `localhost:1313/index.json`


## Files

### layouts/_default/baseof.html addition
Add this block to the bottom of your `baseof.html` file, just before the footer

```html
 <div id="fastSearch">
   <input id="searchInput" tabindex="0">
   <ul id="searchResults">
   </ul>
 </div>
 <script src="/js/fuse.js"></script> <!-- download and copy over fuse.js file from fusejs.io -->
 <script src="/js/fastsearch.js"></script>
```


### static/js/fastsearch.js
This "makes" the search engine based on the index.json file, and wires up all keyboard handling

```js
var fuse; // holds our search engine
var searchVisible = false; 
var firstRun = true; // allow us to delay loading json data unless search activated
var list = document.getElementById('searchResults'); // targets the <ul>
var first = list.firstChild; // first child of search list
var last = list.lastChild; // last child of search list
var maininput = document.getElementById('searchInput'); // input box for search
var resultsAvailable = false; // Did we get any search results?

// ==========================================
// The main keyboard event listener running the show
//
document.addEventListener('keydown', function(event) {
  
  // CMD-/ to show / hide Search
  if (event.metaKey && event.key === '/') {
      // Load json search index if first time invoking search
      // Means we don't load json unless searches are going to happen; keep user payload small unless needed
      if(firstRun) {
        loadSearch(); // loads our json data and builds fuse.js search index
        firstRun = false; // let's never do this again
      }
      
      // Toggle visibility of search box
      if (!searchVisible) {
        document.getElementById("fastSearch").style.visibility = "visible"; // show search box
        document.getElementById("searchInput").focus(); // put focus in input box so you can just start typing
        searchVisible = true; // search visible
      }
      else {
        document.getElementById("fastSearch").style.visibility = "hidden"; // hide search box
        document.activeElement.blur(); // remove focus from search box 
        searchVisible = false; // search not visible
      }
  }

  // Allow ESC (27) to close search box
  if (event.key == 'Escape') {
    if (searchVisible) {
      document.getElementById("fastSearch").style.visibility = "hidden";
      document.activeElement.blur();
      searchVisible = false;
    }
  }

  // DOWN (40) arrow
  if (event.key == 'ArrowDown') {
    if (searchVisible && resultsAvailable) {
      // console.log("down");
      event.preventDefault(); // stop window from scrolling
      if ( document.activeElement == maininput) { first.focus(); } // if the currently focused element is the main input --> focus the first <li>
      else if ( document.activeElement == last ) { last.focus(); } // if we're at the bottom, stay there
      else { document.activeElement.parentElement.nextSibling.firstElementChild.focus(); } // otherwise select the next search result
    }
  }

  // UP (38) arrow
  if (event.key == 'ArrowUp') {
    if (searchVisible && resultsAvailable) {
      event.preventDefault(); // stop window from scrolling
      if ( document.activeElement == maininput) { maininput.focus(); } // If we're in the input box, do nothing
      else if ( document.activeElement == first) { maininput.focus(); } // If we're at the first item, go to input box
      else { document.activeElement.parentElement.previousSibling.firstElementChild.focus(); } // Otherwise, select the search result above the current active one
    }
  }
});


// ==========================================
// execute search as each character is typed
//
document.getElementById("searchInput").onkeyup = function(e) { 
  executeSearch(this.value);
}


// ==========================================
// fetch some json without jquery
//
function fetchJSONFile(path, callback) {
  var httpRequest = new XMLHttpRequest();
  httpRequest.onreadystatechange = function() {
      if (httpRequest.readyState === 4) {
          if (httpRequest.status === 200) {
              var data = JSON.parse(httpRequest.responseText);
              if (callback) callback(data);
          }
      }
  };
  httpRequest.open('GET', path);
  httpRequest.send(); 
}


// ==========================================
// load our search index, only executed once
// on first call of search box (CMD-/)
//
function loadSearch() { 
  fetchJSONFile('/index.json', function(data){

      var options = { // fuse.js options; check fuse.js website for details
        shouldSort: true,
        location: 0,
        distance: 100,
        threshold: 0.4,
        minMatchCharLength: 2,
        keys: [
          'title',
          'permalink',
          'summary'
          ]
      };

      fuse = new Fuse(data, options); // build the index from the json file
      
  });
}


// ==========================================
// using the index we loaded on CMD-/, run 
// a search query (for "term") every time a letter is typed
// in the search box
//
function executeSearch(term) {
  let results = fuse.search(term); // the actual query being run using fuse.js
  let searchitems = ''; // our results bucket

  if (results.length === 0) { // no results based on what was typed into the input box
    resultsAvailable = false;
    searchitems = '';
  } else { // build our html 
    for (let item in results.slice(0,5)) { // only show first 5 results
      searchitems = searchitems + '<li><a href="' + results[item].permalink + '" tabindex="0">' + '<span class="title">' + results[item].title + '</span><br /> <span class="sc">'+ results[item].section +'</span> — ' + results[item].date + ' — <em>' + results[item].desc + '</em></a></li>';
    }
    resultsAvailable = true;
  }
  
  document.getElementById("searchResults").innerHTML = searchitems;
  if (results.length > 0) {
    first = list.firstChild.firstElementChild; // first result container — used for checking against keyboard up/down location
    last = list.lastChild.firstElementChild; // last result container — used for checking against keyboard up/down location
  }
}
```

### CSS Styling

```css
#fastSearch { 
  visibility: hidden;
  position: absolute;
  right: 0px;
  top: 0px;
  display: inline-block;
  width: 300px;
}      

#fastSearch input { 
  padding: 4px 10px;
  width: 100%;
  height: 31px;
  font-size: 1.6em;
  color: #aaa;
  font-weight: bold;
  background-color: #000;
  border-radius: 3px 3px 0px 0px;
  border: none;
  outline: none;
  text-align: left;
  display: inline-block;
}

#searchResults li { 
  list-style: none; 
  margin-left: 0em;
  background-color: #333; 
  border-bottom: 1px dotted #000;
}
  #searchResults li .title { font-size: 1.1em; margin-bottom: 10px; display: inline-block;}

#searchResults { visibility: inherit; display: inline-block; width: 320px; }
#searchResults a { text-decoration: none !important; padding: 10px; display: inline-block; }
  #searchResults a:hover, a:focus { outline: 0; background-color: #666; color: #fff; }
  

```


### layouts/_default/index.json
Hugo already builds indexes of all pages, we can cherry-pick which aspects should be searchable.
The result is a newly created JSON index at `/index.json`
```
{{- $.Scratch.Add "index" slice -}}
{{- range .Site.RegularPages -}}
    {{- $.Scratch.Add "index" (dict "title" .Title "tags" .Params.tags "categories" .Params.categories "contents" .Plain "permalink" .Permalink) -}}
{{- end -}}
{{- $.Scratch.Get "index" | jsonify -}}

```

### Config.toml
Add this snippet to your config file to instruct Hugo to create the index file in JSON format. (RSS and HTML are default outputs, what's important is to add JSON.
```
...
[outputs]
  home = ["HTML", "RSS", "JSON"]
```

Alternately if using a custom _index.md for home page, you can just add the output formats to front matter.
```
outputs:
- html
- rss
- json
```

See https://gohugo.io/templates/output-formats#output-formats-for-pages

### License 

The above cobbled together bits are provided as is under the so-called MIT License. Do whatever ya want with it all. 

Copyright 2020 Craig Mod

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.