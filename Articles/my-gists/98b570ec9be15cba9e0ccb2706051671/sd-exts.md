# Stable DiffusionWebUI 拡張について

- **ControlNet v1.1**
  - [ControlNet-v1-1](https://github.com/Mikubill/sd-webui-controlnet)
  - [ControlNet-v1-1 nightly](https://github.com/lllyasviel/ControlNet-v1-1-nightly)
- https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/tree/main
- 
- **ControlNet Reference**
  - [ControlNet Reference](https://www.youtube.com/results?search_query=ControlNet+Reference)

- **ControlNet IP-Adapter**
  - [IPAdapter-ComfyUI NOTE](- https://note.com/kurayu_ai/n/n9d8aecd7410e)
  - [IPAdapter-ComfyUI Plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus)
  - [sd_control_collection](https://huggingface.co/lllyasviel/sd_control_collection/tree/main)

- **LCM**
  - [LCM](https://wikiwiki.jp/sd_toshiaki/LCM)

- **LyCORIS**
  - [LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS)
  - [a1111-sd-webui-lycoris](https://github.com/KohakuBlueleaf/a1111-sd-webui-lycoris)
  - [LyCORISのノート](https://note.com/kurayu_ai/n/nd3ed149ae368#14eb9472-0c86-4983-be88-edad4c28ca26)

- **Mov2Mov**
  - [Mov2Movの検索結果](https://twitter.com/search?q=Mov2Mov&src=typed_query&f=media)
  - [sd-webui-mov2mov](https://github.com/Scholar01/sd-webui-mov2mov)

- **ComfyUI AnimateDiff**
  - [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
  - [ComfyUI AnimateDiffに関するノート1](https://note.com/kurayu_ai/n/n02db54746629#a07059f7-5b15-42a2-af8b-935f0d70f454)
  - [ComfyUI AnimateDiffに関するノート2](https://note.com/kurayu_ai/n/n28ac74be4cc8)
  - [comfyui-workflow](https://github.com/hylarucoder/comfyui-workflow)

- **Magic Animate | 字節跳動(ByteDance)**
  - [magic-animate](https://github.com/magic-research/magic-animate)

- **Magic Animate デモ**
  - [Magic Animate デモ](https://huggingface.co/spaces/zcxu-eric/magicanimate)
    (Note: 無料ですがエラーになることが多いです)

- **Stable Diffusion FaceSwap**
  - https://romptn.com/article/22892
  - [sd-webui-faceswap](https://github.com/IntellectzProductions/sd-webui-faceswap.git)
  - https://github.com/haofanwang/inswapper
  - https://huggingface.co/ezioruan/inswapper_128.onnx
  - https://visualstudio.microsoft.com/ja/downloads/

- **懸念点**
  - アジア人特に男性は苦手です

```sh
❯ git clone --branch v1.7.0-RC https://github.com/AUTOMATIC1111/stable-diffusion-webui.git stable-diffusion-webui-v1.7.0
rc
❯ cd stable-diffusion-webui-v1.7.0rc/tmp

stable-diffusion-webui-v1.7.0rc/tmp (48fae7c)
❯ mkdir -p extensions/sd-webui-controlnet/models/
❯ cd extensions/sd-webui-controlnet/models/

extensions/sd-webui-controlnet/models (48fae7c)
❯ git clone https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors
❯ cp ControlNet-v1-1_fp16_safetensors/* ../../../../extensions/sd-webui-controlnet/models/

❯ git clone https://huggingface.co/ezioruan/inswapper_128.onnx
❯ cp inswapper_128.onnx/* ../../../../extensions/sd-webui-controlnet/models/

❯ git clone https://huggingface.co/lllyasviel/sd_control_collection
❯ cp sd_control_collection/* ../../../../extensions/sd-webui-controlnet/models/
```