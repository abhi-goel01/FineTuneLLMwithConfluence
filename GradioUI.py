import os
import gradio as gr
from llama_hub.confluence.base import ConfluenceReader
from llama_index import VectorStoreIndex
from llama_index import StorageContext, load_index_from_storage

class GPTProcessing(object):
    def __init__(self, ui_obj):
        self.name = "Custom Data Processing with GPT"
        self.description = "Perform Custom Data Processing with GPT"
        self.config_status = "Error: Required config not set"
        self.index_status = "Error: Index not set"
        self.ui_obj = ui_obj
        self.api_key = None
        self.api_token = None
        self.base_url = None
        self.space_key = None

    def create_ui(self):
        with self.ui_obj:
            gr.Markdown("Custom Fine-tuning with Large Language Model")
            with gr.Tabs():
                with gr.TabItem("Setup the required Configuration for your App"):
                    with gr.Row():
                        openai_api_key = gr.Textbox(label="OpenAI API Key",
                                                    placeholder="Place your OpenAI API key here..",
                                                    type='password')
                    with gr.Row():
                        confluence_api_token = gr.Textbox(label="Confluence API Token",
                                                    placeholder="Place your Confluence API token here..",
                                                    type='password')
                        confluence_base_url = gr.Textbox(label="Confluence Base URL",
                                                         placeholder="Provide confluence base URL ending with /wiki")
                        confluence_space_key = gr.Textbox(label="Confluence Space Key",
                                                         placeholder="Provide confluence space key to read documents from")
                    with gr.Row():
                        set_config_action = gr.Button("Setup the required config parameters")
                    with gr.Row():
                        set_config_status = gr.Label(self.config_status)
                with gr.TabItem("Training/Fine-tuning with Custom Data"):
                    with gr.Row():
                        set_index_action = gr.Button("Create Index")
                    with gr.Row():
                        set_index_status = gr.Label(self.index_status)
                with gr.TabItem("Query Custom Data"):
                    with gr.Row():
                        query_question = gr.Textbox(label="Enter your question:", lines=5)
                        set_query_action = gr.Button("Get Answer")
                    with gr.Row():
                        query_result_text = gr.Textbox(label="Query Result:", lines=10)

            set_config_action.click(
                self.update_config_status,
                [
                    openai_api_key, confluence_api_token, confluence_base_url, confluence_space_key
                ],
                [
                    set_config_status
                ]
            )
            set_index_action.click(
                self.update_index_status,
                [
                ],
                [
                    set_index_status
                ]
            )
            set_query_action.click(
                self.get_answer_from_index,
                [
                    query_question
                ],
                [
                    query_result_text
                ]
            )

    def update_config_status(self, api_key, api_token, base_url, space_key):
        if (api_key is not None and len(api_key) > 0 and
            api_token is not None and len(api_token) > 0 and
            base_url is not None and len(base_url) > 0 and
            space_key is not None and len(space_key) > 0):
            self.api_key = str(api_key)
            self.api_token = str(api_token)
            self.base_url = str(base_url)
            self.space_key = str(space_key)
            self.config_status = str("Success: Required config all set")
            os.environ["OPENAI_API_KEY"] = self.api_key
            os.environ["CONFLUENCE_API_TOKEN"] = self.api_token
            return self.config_status
        else:
            self.config_status = str("Error: Required config not set, please enter values")
            return self.config_status

    def update_index_status(self):
        reader = ConfluenceReader(base_url=self.base_url)
        documents = reader.load_data(space_key=self.space_key, include_attachments=True, page_status="current")
        output_index = VectorStoreIndex.from_documents(documents)
        output_index.storage_context.persist('IndexDataNew/Index.json')
        self.index_status = str("Success: Required index created")
        return self.index_status

    def get_answer_from_index(self, query_question):
        query_result = "Error: Unable to get answer to your question"
        if query_question is not None and len(query_question) > 0:
            storage_context = StorageContext.from_defaults(persist_dir='IndexDataNew/Index.json')
            output_index = load_index_from_storage(storage_context)
            query_engine = output_index.as_query_engine()
            query_result = query_engine.query(query_question)
            return query_result

    def launch_ui(self):
        self.ui_obj.launch()
