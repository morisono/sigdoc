```bash
# (1.) complete auth may be needed, interaction will start. 
huggingface-cli repo create   # or huggingface-cli repo create <your_repo> --type space --space_sdk streamlit
git clone https://huggingface.co/spaces/<your_name>/<your_repo> hfco

# then start git managenent
git init 
```

```
.
├── <your_repo>
│   └── README.md
├── hfco
│   ├── app.py
│   ├── README.md
│   └── .gitattributes
└──.git
```

```
# edit readme, requirements.txt, etc
cp hfco/README.md requirements.txt .
```