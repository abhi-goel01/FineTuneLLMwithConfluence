import os
from llama_hub.confluence.base import ConfluenceReader
from llama_index import VectorStoreIndex

os.environ["CONFLUENCE_API_TOKEN"] = "<your key>"
os.environ['OPENAI_API_KEY'] = "<your-key"
base_url = "<your base URL"
space_key = "<your space key>"

# Read the confluence pages using llama_hub confluence data connector
reader = ConfluenceReader(base_url=base_url)
documents = reader.load_data(space_key=space_key, include_attachments=True, page_status="current")

# Use LLM model to convert the loaded confluence content into a vector index
output_index = VectorStoreIndex.from_documents(documents)

# Save the generated index to disk
output_index.storage_context.persist('IndexDataNew/Index.json')

# Ask your queries related to your custom data to the LLM model
#query_engine = output_index.as_query_engine()
#response = query_engine.query("how does the alpha LLM model help")
#print(response)


