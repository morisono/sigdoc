---
uid: <% tp.file.creation_date("x") %>
name: <% tp.file.title %>
<%*
const title = await tp.system.prompt('Title')
%>
title: <%* tR += title  %>
link: https://example.com/articles/<% tp.frontmatter.uid %>
lang: <% await tp.system.prompt('Language', 'en', false, false) %>
type: <% await tp.system.suggester**((**item) => item, ['article', 'note', 'daily', 'project-doc', 'about', 'howto', 'cheatsheet', 'intro', 'manual', 'catalog'], false, 'Type') %>
categories: <% await tp.system.suggester((item) => item, ['tech', 'idea', 'crypto', 'finance', 'sports', 'car', 'marketing', ''], false, 'Categories') %>
tags: <% await tp.system.suggester(item => item, Object.keys(app.metadataCache.getTags()).map(x => x.replace("#", "")), false, 'Tags') %>
author: <% await tp.system.prompt('Author', 'me') %>
status: <% await tp.system.suggester((item) => item, ['pending', 'in progress', 'complete', 'reviewed', 'fixed', 'updated', 'accepted', 'rejected', 'published', 'deprecated'], false, 'Status') %>
created: <% tp.file.creation_date("YYYY-MM-DDThh-mm-ss Z") %>
updated: <%+ tp.file.last_modified_date("YYYY-MM-DDThh-mm-ss Z") %>
---

# <%* tR += title %>

