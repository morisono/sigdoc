import uuid
import random
import gradio as gr
from typing import Tuple

class StateModel:
    def __init__(self):
        self.text = ""
        self.number = 0

    def init(self):
        self.text = uuid.uuid4()
        self.number = random.randint(0, 9999)
        print("--initialize--")
        self.show()

    def show(self) -> str:
        text = {"text": self.text, "number": self.number}
        print(text)
        return text

def click_button(state: StateModel) -> Tuple[StateModel, str]:
    if state.number == 0:
        state.init()
    else:
        state.number += 1
    return state, state.show()

with gr.Blocks() as demo:
    state = gr.State(StateModel())
    button = gr.Button(value="click")
    textbox = gr.Textbox()

    button.click(click_button, state, [state, textbox])

if __name__ == "__main__":
    demo.launch()
