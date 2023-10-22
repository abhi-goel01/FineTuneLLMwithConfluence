import os
from llama_index import StorageContext, load_index_from_storage

os.environ['OPENAI_API_KEY'] = '<your key>'

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir='IndexDataNew/Index.json')
# load index
output_index = load_index_from_storage(storage_context)

# load the output index to the query engine
query_engine = output_index.as_query_engine()

# Ask your queries related to your custom data to the LLM model
prompt = input("Prompt > ")
while prompt != 'exit':
    response = query_engine.query(prompt)
    print(response)
    prompt = input("Prompt > ")
