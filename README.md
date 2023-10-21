# FineTuneLLMwithConfluence

Fine tune the GPT Large Language Model with custom data to utilize Q&A, summarization and many other ChatGPT like functionalities

We will use llama-hub to read custom data from our confluence pages and then llama-index to convert the loaded content into a vector index. Then we will load the vector index as a query engine and use it to query custom data from the LLM. We will also create a Gradio based UI to use the project in a more user friendly way.

# Pre-requisites

1. Base URL: URL for a Confluence instance to initialize the ConfluenceReader - base URL needs to end with /wiki
2. Space Key: The confluence space from where all the pages will be read
3. Confluence API token: Generate the token from confluence - The token should be a combination of userid:<confluence token>
4. open AI key: Generate a key from openai in order to integrate with the GPT Large Language Model

Note: Confluence API's only support basic auth so change bearer token to basic in rest_api.py file


# References

1. https://github.com/run-llama/llama-hub/tree/main/llama_hub/confluence
2. https://github.com/run-llama/llama_index
3. https://www.gradio.app/guides/quickstart
4. https://github.com/prodramp/DeepWorks/tree/main/ChatGPT/finetunellm
