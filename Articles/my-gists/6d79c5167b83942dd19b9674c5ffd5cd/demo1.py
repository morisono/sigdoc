import os
import gradio as gr
import gensim
from markdown2 import markdown
from gensim.models.doc2vec import Doc2Vec
from gensim.similarities import Similarity

# 事前学習済みのDoc2Vecモデルをロード
pretrained_model_path = "path/to/pretrained/doc2vec/model"
pretrained_model = Doc2Vec.load(pretrained_model_path)

# ドキュメントをトピックに分類するためのルールを定義
topic_rules = {
    'topic1': ['machine learning', 'deep learning', 'artificial intelligence'],
    'topic2': ['data analysis', 'data visualization', 'statistics'],
    'topic3': ['web development', 'frontend', 'backend']
}

# Markdownファイルを読み込んでテキストに変換する関数
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
        text_content = markdown(markdown_content)
        return text_content

# テキストとトピックルールを使用して、文書を分類する関数
def classify_document(text_content, topic_rules):
    inferred_vector = pretrained_model.infer_vector(text_content.split())
    similarities = {}
    for topic, keywords in topic_rules.items():
        similarity = pretrained_model.docvecs.most_similar([inferred_vector], topn=1)[0][1]
        similarities[topic] = similarity
    return similarities

# ドキュメントの類似度を計算する関数
def calculate_similarity(text1, text2):
    vec1 = pretrained_model.infer_vector(text1.split())
    vec2 = pretrained_model.infer_vector(text2.split())
    similarity = Similarity("", [vec1], num_features=pretrained_model.vector_size)
    return similarity[vec2][0]

# インタフェースの定義
def classify_document_interface(text_content):
    similarities = classify_document(text_content, topic_rules)
    return similarities

def calculate_similarity_interface(text1, text2):
    similarity = calculate_similarity(text1, text2)
    return similarity

# インタラクティブなUIを作成
classify_document_interface = gr.Interface(classify_document_interface, 
                                            gr.inputs.Textbox(lines=10, label="Enter document text"), 
                                            gr.outputs.Label(num_top_classes=len(topic_rules), label="Topic Similarities")).launch()

calculate_similarity_interface = gr.Interface(calculate_similarity_interface, 
                                               gr.inputs.Textbox(lines=10, label="Enter text 1"), 
                                               gr.inputs.Textbox(lines=10, label="Enter text 2"), 
                                               gr.outputs.Textbox(label="Similarity")).launch()
