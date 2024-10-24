```js
<%*
const uid = tp.date.now("YYYYMMDD_HHmmss");

const extractByHeader = async (path, header) => {
    let content = await tp.file.include(`[[${path}#${header}]]`);
    if (!content.startsWith(`# ${header}`)) {
        return undefined;
    }

    content = content.replace(new RegExp(`^# ${header}\n+`), "");
    return content.trim();
};

// select template

const templateName = await tp.system.suggester((item) => item, [
    "plain",
    "idea",
    "person",
    "review book",
    "review movie",
]);

const templateDir = "_plugin/templater/type";
const templateFile = tp.file.find_tfile(`${templateDir}/${templateName}`);

// extract template frontmatter

let templateFM = {};
await app.fileManager.processFrontMatter(templateFile, (fm) => {
    templateFM = Object.assign(fm, templateFM);
});

// extract template parts

const templateTitle = await extractByHeader(templateFile.path, "%title%");
const templateContent = await extractByHeader(templateFile.path, "%content%");

// set title

let title = tp.file.title;
if (templateTitle !== undefined) {
    title = templateTitle;
}
else if (title.startsWith("Untitled")) {
    title = await tp.system.prompt("Title");
}
-%>
---
uid: "<% uid %>"
title: "<% title %>"
aliases: []
created_at: <% tp.date.now("YYYY-MM-DD HH:mm:ss") %>
archived_at: null
<%*
for (const [key, value] of Object.entries(templateFM)) {
    tR += `${key}: ${JSON.stringify(value)}\n`;
}
-%>
---
<% templateContent || "" %>
<%*
// rename
await tp.file.move(`${tp.date.now("YYYY/MM")}/${uid}`);
-%>
```