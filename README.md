# FineTuneLLMwithConfluence

Fine tune the GPT Large Language Model to utilize Q&A, summarization and many other ChatGPT like functionalities on your **organization data**

We will use llama-hub to read custom data from our confluence pages and then llama-index to convert the loaded content into a vector index. The vector index will be then loaded as a query engine and used to query custom data from the LLM. We will also create a Gradio based UI to use the functionalities in a more user friendly way.

# Pre-requisites

1. Base URL: URL for a Confluence instance to initialize the ConfluenceReader, it must end with /wiki
2. Space Key: The confluence space from where all the pages will be read
3. Confluence API token: Combination of user ID:token generated from confluence
4. open AI key: Key generated from openai in order to integrate with the GPT Large Language Model

Note: Confluence API's only support basic auth so change bearer token to basic in rest_api.py file


# References

1. https://github.com/run-llama/llama-hub/tree/main/llama_hub/confluence
2. https://github.com/run-llama/llama_index
3. https://www.gradio.app/guides/quickstart
4. https://github.com/prodramp/DeepWorks/tree/main/ChatGPT/finetunellm
