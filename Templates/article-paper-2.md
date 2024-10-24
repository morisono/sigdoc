
---
tags: in/paper state/process
aliases:
    - '{{VALUE:title}}'
cssclass: null
abstract: >
    {{VALUE:abstract}}
---

# {{VALUE:title}}

---

Type:: [[&]]
Title:: {{VALUE:title}}
Author:: {{VALUE:authors}}
Year:: {{VALUE:date}}
Tags::
DOI:: {{VALUE:doi}}
Reviewed Date:: ==UPDATE THIS==
Rating:: ==Give a rating==

---

## Abstract

{{VALUE:abstract}}

## Summary of key points

-

## Other Comments

-

## Interesting Cited References

-   

---

{{VALUE:formattedAnnotations}}



---

```js quickadd
const note = this.variables.note;
let quote = this.variables.quote;

if (this.variables.annotationType === "image") {
    return "==Images not supported yet.=="
}

const headingMatch = note.match(/\.h(\d+)/);

if (headingMatch) {
    const headingLevel = Number.parseInt(headingMatch[1], 10) + 2;
    const hashtags = '#'.repeat(headingLevel);
    quote = `${hashtags} ${quote}`;
}

if (quote.trim().startsWith("#")) return quote;
return `> ${quote}`
```

{{VALUE:note}}
