---
datetime: 2024-07-17 05:58
tags:
  - cloudflare
  - CMS
  - announcements
aliases:
  - <% tp.file.title %>
---
# test


[...](obsidian://advanced-uri?vault=Obsidian2&daily=true&clipboard=true&mode=append)


```
obsidian://advanced-uri?vault=<your-vault>&filepath=<your-file>&commandid=workspace%253Aclose

obsidian://advanced-uri?vault=<your-vault>&filepath=<your-file>&commandid=workspace%253Aclose
```

  
- [[{{fileName}}#test]]

<%*  
	// Set the current timestamp as the filename
	await tp.file.rename(tp.file.creation_date("YYYYMMDDHHmmss"));
	  await title = tp.file.title;

	// Move to the Notes folder
		tp.file.move("Notes/" + title)
%>
```dataviewjs
<%*  
	// Set the current timestamp as the filename
	await tp.file.rename(tp.file.creation_date("YYYYMMDDHHmmss"));
	  await title = tp.file.title;

	// Move to the Notes folder
		tp.file.move("Notes/" + title)
%>
```

<% await tp.file.move("/1on1" + "/" + tp.file.creation_date("YYYY-MMM-DD") + ' - ' + (mytitle = await tp.system.prompt( 'Meeting Name', 'test name', false) ))) %>

```dataviewjs
<% await tp.file.move("/1on1" + "/" + tp.file.creation_date("YYYY-MMM-DD") + ' - ' + (mytitle = await tp.system.prompt( 'Meeting Name', 'test name', false) ))) %>

```


<% tp.file.move( 'People/1on1/' + (mytitle = await tp.system.prompt( '名前:', 'テスト名', false) )) %>


```dataviewjs
<% tp.file.move( 'People/1on1/' + (mytitle = await tp.system.prompt( '名前:', 'テスト名', false) )) %>
```


```dataviewjs
dv.header(3, "Ref. ");
var maxLoop = Math.min(dv.current().file.tags.length, 3);
for(let i=0;i<maxLoop;i++){
dv.span(dv.current().file.tags[i]);
dv.list(dv.pages(dv.current().file.tags[i]).sort(f=>f.file.mtime.ts,"desc").limit(15).file.link);
}

for (let outgo of dv.pages('outgoing([[' + dv.current().file.name + ']])')) {
    dv.header(4, outgo.file.name);
    dv.list(outgo.file.inlinks.sort());
}
```
