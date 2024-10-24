# Markdown - Resize pictures in GitHub

I found that the "best" way is to use HTML, as it works both in Readme/.md files and also in comments (within Issues, Gist...)

E.g. when adding/editing a comment (within Issues, Gist...) :
* Upload the picture by drag-and-drop in the text field
* replace `![image](https://your-image-url.type)` with `<img src="https://your-image-url.type" width="100" height="100">`

As mentioned by @cbestow (thanks!), it's not mandatory to set both `width` and `height`. If only one is set, the other will be adjusted accordingly to preserve the aspect ratio of the image.