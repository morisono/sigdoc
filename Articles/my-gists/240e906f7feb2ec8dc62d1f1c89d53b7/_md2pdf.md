# Markdown to PDF with VSCode Extension

### Prerequisites

- [yzane/vscode-markdown-pdf](https://github.com/yzane/vscode-markdown-pdf)
- `settings.json` or `*.code-workspace`
```json
{
    "settings": {
        "markdown-pdf.styles": ["./style.css"],
        "markdown-pdf.displayHeaderFooter": true,
        "markdown-pdf.headerTemplate": "<div style=\"font-size: 9px; margin-left: 1cm;\"></div> <div style=\"font-size: 9px; margin-left: auto; margin-right: 1cm; \"></div>",
        "markdown-pdf.footerTemplate": "<div style=\"font-size: 9px; margin: 0 auto;\"> <span class='pageNumber'></span></div>",
        "markdown-pdf.breaks": true,
        "markdown-pdf.format": "A5",
        "markdown-pdf.margin.top": "20mm",
        "markdown-pdf.margin.bottom": "20mm",
        "markdown-pdf.margin.right": "20mm",
        "markdown-pdf.margin.left": "20mm",
        "markdown-pdf.mermaidServer": "https://unpkg.com/mermaid@10.0.3-alpha.1/dist/mermaid.min.js",
        "markdown-pdf.plantumlOpenMarker": "```plantuml",
        "markdown-pdf.plantumlCloseMarker": "```"
    }
}
```

- styling : 
    - Win: `%USERPROFILE%\.vscode\extensions\yzane.markdown-pdf-1.5.0\styles\`
    - WSL2: `~/.vscode-server/extensions/yzane.markdown-pdf-1.5.0/styles/`

### css priority

1. style.css
1. markdown-pdf.css
1. markdown.css
