> [!NOTE]  
> Highlights information that users should take into account, even when skimming.

> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.


> **Note**
> This is a note

> **Warning**<br>
> This is a warning


```
{
    "Note": {
        "prefix": "note",
        "body": [
            "> [!NOTE]",
            "> $1"
        ],
        "description": "GFM Note block"
    },
    "Important": {
        "prefix": "important",
        "body": [
            "> [!IMPORTANT]",
            "> $1"
        ],
        "description": "GFM Important block"
    },
    "Warning": {
        "prefix": "warning",
        "body": [
            "> [!WARNING]",
            "> $1"
        ],
        "description": "GFM Warning block"
    }
}
```