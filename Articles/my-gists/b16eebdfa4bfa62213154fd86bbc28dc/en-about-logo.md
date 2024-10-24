# Logo Creation Procedure

1. **Extend Background and Whiten**

    ```bash
    convert input_logo.jpg \
        -background white -extent 1200x1200 \
        -colors 3 -fuzz 10% -fill white -opaque '#b7271e' \
        output_logo_step1.jpg
    ```

    - `-background white -extent 1200x1200`: Set white background and extend canvas to 1200x1200 pixels.
    - `-colors 3`: Limit the image to 3 colors. This option performs color reduction.
    - `-fuzz 10%`: Consider colors within 10% similarity for color comparison, used in subsequent `-fill white -opaque '#b7271e'`.
    - `-fill white -opaque '#b7271e'`: Replace colors close to `#b7271e` with white.

2. **Add Text**

    ```bash
    convert output_logo_step1.jpg \
        -fill black -font 'Sevenfold' -pointsize 120 -gravity center \
        -annotate +0+400 'N8CH' \
        final_logo.jpg
    ```

    - `-fill black`: Set fill color of text to black.
    - `-font 'Sevenfold'`: Set font to 'Sevenfold'. Specify appropriate font if unavailable.
    - `-pointsize 120`: Set text size to 120 points.
    - `-gravity center`: Set text position to center.
    - `-annotate +0+400 'N8CH'`: Add text 'N8CH' at center.

3. **Convert to SVG**
    Open `final_logo.jpg` in SD VectorStudio and save it as an SVG file.

    **Cleaning:** Remove unnecessary elements.

    **Coloring:** Fill in colors. If elements are not properly separated, edit the code and split the `path` as needed.


4. **Variation Expansion**

    - Generate required variations of files according to naming convention.

    #### Naming Convention

    Basic Format:
    `<Name/Timestamp>-<Type>-<Color>-<Shape>-<Variant>-<Size>.<Ext>`

    Extended Expressions:

    ```yaml
    - Prefixes: 
       - Position: (t, b, l, r, tl, tr, bl, br)
       - Size: (s, m, l, xl)
    - Suffixes: 
       - Serial: (1, 1a, 2, ..)
       - Revision: (r1, r2, ..) 
    ```

    Example:
    `MyLogo-2024-02-15-sTXT-CL1-RR-QR-1500x500.svg`

    - Each element is in uppercase and separated by hyphens. However, extended expressions and file formats are in lowercase.
    - Elements are kept concise for character limit and readability.

    ```yaml
    - `<Name/Timestamp>`: Name or timestamp of the logo.
       - Name in CamelCase (e.g., `MyLogo`), words separated by underscores `_`.
       - Timestamp in ISO 8601 format (e.g., `2024-02-15`)
    - `<Type>`: Type of the logo.
       - `TXT`: Text
       - `IMG`: Image
    - `<Color>`: Color of the logo.
       - `BW`: Black background and white foreground.
       - `WB`: White background and black foreground.
       - `CL1`, `CL2`, ...: Color schemes (`CL1`, `CL2`, etc., added as needed)
    - `<Shape>`: Shape of the logo.
       - `C`: Circle
       - `R`: Rectangle
       - `RR`: Rounded rectangle
       - `FR`: Frame
    - `<Variant>`: Variant of the logo, marked with * where applicable.
       - `QR`: QR code
       - `BAR`: Bar code
       - `SN`: Serial number
       - `DATE`: Date
       - `TABLE`: Table
       - `URL`: URL
    - `<Size>`: Logo size (WxH px)
    - `<Ext>`: File extension.
       - `SVG`
       - `PNG`
       - `JPG`
       - `WEBP`
    - Additional as needed
    ```


- [Beta releases](https://beta.rclone.org/) are generated from each commit to master. Note these are named like

```
{Version Tag}.beta.{Commit Number}.{Git Commit Hash}
```

e.g.
```
v1.53.0-beta.4677.b657a2204
```
- Some beta releases may have a branch name also:
```
{Version Tag}-beta.{Commit Number}.{Git Commit Hash}.{Branch Name}
```
e.g.
```
v1.53.0-beta.4677.b657a2204.semver
```

