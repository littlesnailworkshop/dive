from examples.base import index_example_data,query_example_data,clear_example_data
from dive.util.configAPIKey import set_pinecone_api_key,set_pinecone_env,set_pinecone_index_dimentions,set_openai_api_key,\
    set_ocr_api_key,set_supabase_auth_token,set_supabase_folder_path
import time
import requests
#Use chromadb and model all-MiniLM-L6-v2 embeddings and llm

index_example_data(256, 20, False, None,None)
# wait 1 min to run query method
print('------------Finish Indexing Data-----------------')
time.sleep(30)
print('------------Start Querying Data-----------------')
question='What is airbnb\'s revenue?'
#query_example_data(question, 4, None, None, None)
#clear_example_data()

#Use pinecone instead of chromadb
#set_pinecone_api_key()
#set_pinecone_env()
#set_pinecone_index_dimentions()