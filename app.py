import gradio as gr
from GradioUI import GPTProcessing

if __name__ == "__main__":
    my_app = gr.Blocks()
    gradio_ui = GPTProcessing(my_app)
    gradio_ui.create_ui()
    gradio_ui.launch_ui()