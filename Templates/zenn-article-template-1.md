---
published: false
cssclass: zenn
type: "<% await tp.system.suggester(['tech', 'idea'], ['tech', 'idea'], false, '?????????') %>"
emoji: "<% await tp.system.prompt('????1???', '??') %>"
<%*
const title = await tp.system.prompt('?????????')
%>
title: "<%* tR += title  %>"
topics: []
date: <% tp.date.now("YYYY-MM-DD") %>
AutoNoteMover: disable
url: "https://zenn.dev/estra/articles/<% tp.file.title %>"
tags: [" #type/zenn "]
aliases: ???<% await tp.frontmatter.title %>?
---

