import os
from llama_hub.confluence.base import ConfluenceReader
from llama_index import VectorStoreIndex

os.environ["CONFLUENCE_API_TOKEN"] = "YWJoaS5idWdzQGdtYWlsLmNvbTpBVEFUVDN4RmZHRjBoX2Y1dnNUNUtwOUQ2SVFURnlUaGNfWnB4V3ZGeFpHcl95S0RRRHN4VjZrVUdrN0dLOVhvZEc3dmh5QUQ3Y2xER0RsbG43cU11cEd3RjNORF9ZNl9iLTZ1cmhGV3Q4bTYxRW5US3hJM2RRa2ZsWFFUOXlhblYzR3VtdW5VcDRPTnVaWGtERWVRMVlZNVJ5OTdhTUdyM2QtRHVCMkZxeW5CVXBvQVF0X3VCcGs9NDNEQjY0RjQ="
os.environ['OPENAI_API_KEY'] = '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'
#os.environ['OPENAI_API_KEY'] = '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'
base_url = "https://gen8iveai.atlassian.net/wiki/"
space_key = 'DE'

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


