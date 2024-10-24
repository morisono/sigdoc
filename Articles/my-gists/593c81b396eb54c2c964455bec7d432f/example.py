import gradio as gr

def login(username, state):
    # ユーザー名をstateオブジェクトに保存
    state["username"] = username
    return f"{username}さんがログインしました！", state

def greet(state):
    # stateオブジェクトからユーザー名を取得
    return f"{state['username']}さん、こんにちは！", state

with gr.Blocks() as demo:
    # Stateオブジェクトを初期化
    state = gr.State({"username": None})

    with gr.Row():
        with gr.Column():
            tb_username = gr.Textbox(label="Input your name")
            button_login = gr.Button(value="Login")
        with gr.Column():
            message = gr.Markdown()
            button_greet = gr.Button(value="Greet")

    # ボタンがクリックされたときの動作を定義
    button_login.click(login, [tb_username, state], [message, state])
    button_greet.click(greet, state, [message, state])

if __name__ == "__main__":
    demo.launch()
