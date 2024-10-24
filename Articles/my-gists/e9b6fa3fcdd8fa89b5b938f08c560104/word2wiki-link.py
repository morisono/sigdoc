import gradio as gr
from janome.tokenizer import Tokenizer
import wikipediaapi

def analyze_text(text, lang):
    # Use Janome to tokenize the text
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)

    # Create an instance of Wikipedia based on the selected language
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='MyProjectName (example@example.com)',
        language=lang,
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    # Convert each word to a Markdown link by searching on Wikipedia and obtaining the URL
    markdown_links = []
    for token in tokens:
        word = token.surface
        part_of_speech = token.part_of_speech.split(',')[0]
        if part_of_speech == 'noun':  # Check if it's a noun
            page = wiki_wiki.page(word)
            if page.exists():
                url = page.fullurl
                markdown_link = f"[{word}]({url})"
                markdown_links.append(markdown_link)
            else:
                markdown_links.append(word)
        else:
            markdown_links.append(word)

    # Return the text converted to Markdown links
    return ' '.join(markdown_links)

iface = gr.Interface(
    fn=analyze_text,
    inputs=["text", gr.Dropdown(["ja", "en"], label="language")],
    outputs="text",
    title="Generate Text with Wikipedia Links",
    description="Tokenizes the input text and converts nouns into Markdown links pointing to relevant Wikipedia articles."
)
iface.launch()

