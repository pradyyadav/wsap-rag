import logging
import sys
import os

import qdrant_client
from IPython.display import Markdown, display
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core import Settings
from qdrant_client import QdrantClient
import os
import dotenv
dotenv.load_dotenv()

Settings.embed_model = FastEmbedEmbedding(model_name="BAAI/bge-base-en-v1.5")


qdrant_key = os.getenv("QDRANT_API_KEY")


client = QdrantClient(
    url="https://401c0bdd-577d-4cc2-90c7-b9e39047201a.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key=qdrant_key,
)

# vector_store = QdrantVectorStore(client=client,
#                                  collection_name="wsapbot-fastemb")
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
# index = VectorStoreIndex.from_vector_store(vector_store, 
#                                            storage_context=storage_context)
# retriever = VectorIndexRetriever(index=index, similarity_top_k=10)

# # query_engine = index.as_query_engine(logging=True)
# # response = query_engine.query("Gym ayega?")
# response = retriever.retrieve("Gym ayega?")

# print(response)


embed_model = FastEmbedEmbedding(model_name="")



service_context = ServiceContext.from_defaults(chunk_size_limit=1024, embed_model=embed_model)


# retriever = VectorIndexRetriever(index=index, similarity_top_k=10)


query_engine = index.as_query_engine()
query = "gym ayega?"
response = query_engine.query("What is the meaning of life?")
print(response)




def retrieve_similar(client, user_query):
    text_list = []
    query_vector = embed_model.get_query_embedding(user_query)
    response = client.search(collection_name="wsapbot-fastemb", 
                             query_vector=query_vector, limit=10)
    for scored_point in response:
        text = scored_point.payload['chat']
        text_list.append(text)

    return text_list

if __name__=="__main__":
    query = "Testing"
    fetched_text = retrieve_similar(client, query)
    print(fetched_text)
