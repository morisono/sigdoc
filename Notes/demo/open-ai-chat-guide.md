---
id: 1721940031585
name: Untitled 6
path: Notes/Untitled 6.md
link: https://example.com/articles/undefined
title: OpenAI Chat Migration Guide
lang: en
type: note
categories: idea
tags: 
author: me
status: pending
created_at: 2024-07-26T05-40-31 +09:00
updated_at: NaN
img: 
alias: 
keywords: 
topics: 
emoji: 
toc: false
private: true
---

|               uid                |               name               |                                                                  categories                                                                   |        tags        | author | status |                      created_at                      | updated_at                                                 |
| :------------------------------: | :------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------: | :----------------: | :----: | :----: | :--------------------------------------------------: | ---------------------------------------------------------- |
| 1721940031585 | 1721940031585 | idea |  |        |        | 2024-07-26T05-40-31 +09:00 | NaN |

![80](logo.png)

![%|200](noimage.png)

# OpenAI Chat Migration Guide


## Abstract

- デフォルトでは、チャット履歴データは会話の最後の更新から 90 日間保存されます。.
[Copilot in Windows: Your data and privacy - Microsoft Support](https://support.microsoft.com/en-us/windows/copilot-in-windows-your-data-and-privacy-3e265e82-fc76-4d0a-afc0-4a0de528b73a)
## Summary

## Delete History

- [How to delete all chats in ChatGPT | Digital Trends](https://www.digitaltrends.com/computing/how-to-delete-chat-history-chatgpt/)
- [GitHub - ac1982/claude-chats-cleaner: Chrome extension to effortlessly clean all conversation history in Claude AI. One-click solution for a tidy, privacy-focused Claude experience.](https://github.com/ac1982/claude-chats-cleaner)
- [How To Delete Claude 3 AI History? - Claude AI](https://claude-ai.uk/how-to-delete-claude-3-ai-history/)
- [How To Access Claude AI: A Step-by-Step Guide \[2023\] - Claude AI](https://claude-ai.uk/how-to-access-claude-ai-a-step-by-step-guide-2023/)
- [Script to delete Claude AI conversations history without any dependency or using external tool. · GitHub](https://gist.github.com/Jalalx/6b99f5ff4a0aef17b4e4eff37b0ad235)
- [Manage & delete your Gemini Apps activity - Android - Gemini Apps Help](https://support.google.com/gemini/answer/13278892?hl=en&co=GENIE.Platform%3DAndroid)
- [git - how to delete all commit history in github? - Stack Overflow](https://stackoverflow.com/questions/13716658/how-to-delete-all-commit-history-in-github)
- [Google Bard: How to Clear or Turn Off History](https://nerdschalk.com/clear-bard-history/)
- [Edge Copilot Now Lets You Delete Entire Chat History with One Click](https://geekermag.com/edge-copilot-now-lets-you-delete-entire-chat-history-with-one-click/)
- [Search and delete Copilot data in Microsoft 365 – 4sysops](https://4sysops.com/archives/search-and-delete-copilot-data-in-microsoft-365/)
## Download History


#### GitHub
```bash
gh auth login
```

```bash
gh repo list myorgname --limit 4000 | while read -r repo _; do
  gh repo clone "$repo" "$repo"
done
```
- The default limit is 30.
  
[git - How to clone all repos at once from GitHub? - Stack Overflow](https://stackoverflow.com/questions/19576742/how-to-clone-all-repos-at-once-from-github)



## ChatGPT by OpenAI

- Download ChatGPT-Exporter (Userscript)
- Install Tampermonkey (or Adguard)  

 - 1m for appx.10 files, 1h for apx.1000 files waiting time require.

- [GitHub - ryanschiang/chatgpt-export: Browser script to share and export ChatGPT chat logs to Markdown, JSON, or as Image (PNG)](https://github.com/ryanschiang/chatgpt-export)
## Claude.ai by Anthropic
- [GitHub - ryanschiang/claude-export: Browser script to share and export Anthropic Claude chat logs to Markdown, JSON, or as Image (PNG)](https://github.com/ryanschiang/claude-export)

## Gemini by Google

### Bard by Google
- Google Takeout
```bash
wl-paste > orig.html
pandoc -f html -t html4 orig.html -o result.html
sed -iE -e '/<(div|img)(.*")?$/,/.*>/d' -e '/^<.?(div|img)( [^>]*)?>$/d' result.html
```

```bash
alias hatediv='pandoc -f html -t html4 | sed -E -e '\''/<(div|img)(.*")?$/,/.*>/d'\'' -e '\''/^<.?(div|img)( [^>]*)?>$/d'\'
function undiv {
 wl-paste | hatediv > $1
}
```
## Copilot by Microsoft


## Phi-3 by Microsoft


## All at once
- [GitHub - lencx/Noi: 🚀 Power Your World with AI - Explore, Extend, Empower.](https://github.com/lencx/Noi)

## Copilot Chat by GitHub

- [How to export the chat history of GitHub Copilot Chat? · community · Discussion #57190 · GitHub](https://github.com/orgs/community/discussions/57190)
## References

- [Manual export from Bard, ChatGPT, MS Copilot - DEV Community](https://dev.to/mkf/manual-export-from-bard-chatgpt-ms-copilot-g23)
- [Userscripts | AdGuard Knowledge Base](https://adguard.com/kb/general/userscripts/)
- [Tampermonkey - Chrome Web Store](https://chromewebstore.google.com/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)
- [GitHub - AdguardTeam/AdGuardExtra: AdGuard Extra is designed to solve complicated cases when regular ad blocking rules aren't enough.](https://github.com/AdguardTeam/AdGuardExtra)
- [GitHub - pionxzh/chatgpt-exporter: Export and Share your ChatGPT conversation history](https://github.com/pionxzh/chatgpt-exporter)
- [AI Prompt Genius - Chrome Web Store](https://chrome.google.com/webstore/detail/chatgpt-prompt-genius/jjdnakkfjnnbbckhifcfchagnpofjffo)
- [Enhanced ChatGPT - Chrome Web Store](https://chrome.google.com/webstore/detail/enhanced-chatgpt/mcbhhiafbiafmggccdcpgfldcaeipopg)
- [Export ChatGPT Conversation - Chrome Web Store](https://chrome.google.com/webstore/detail/export-chatgpt-conversati/clgidpflecgaaabfcmdmkcgebpbadgoc)
- [ShareGPT: Share your ChatGPT conversations - Chrome Web Store](https://chrome.google.com/webstore/detail/sharegpt-share-your-chatg/daiacboceoaocpibfodeljbdfacokfjb)