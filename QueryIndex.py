import os
from llama_index import StorageContext, load_index_from_storage

os.environ['OPENAI_API_KEY'] = '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'
#os.environ['OPENAI_API_KEY'] = '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'

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir='IndexData/Index.json')
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
