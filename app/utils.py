# app/utils.py
# #import openai
# # import os

# # import dotenv
# import replicate
# import requests
# from bs4 import BeautifulSoup
# from openai import OpenAI
# # import pinecone
# from pinecone import Pinecone, ServerlessSpec

# pc = Pinecone(api_key='b48026df-1663-47bc-b9e2-c3a92067af2e')
# # pc = pinecone(
# #         api_key=os.environ.get('eb4e664e-7a14-4f09-997e-2dbd4a4c1ff1')
# #     )
# #pc = pinecone.init(api_key='eb4e664e-7a14-4f09-997e-2dbd4a4c1ff1')
# # index_name = 'website-content'
# # if index_name not in pc.list_indexes():
# #     pc.create_index(index_name, dimension=384)
# # index = pc.Index(index_name)
# index_name = "docs-quickstart-index"

# if index_name not in pc.list_indexes().names():
#     pc.create_index(
#         name=index_name,
#         dimension=2,
#         metric="cosine",
#         spec=ServerlessSpec(
#             cloud='aws', 
#             region='us-east-1'
#         ) 
#     ) 
# index = pc.Index(index_name)

# def text_to_vector(text):
#     # Implement your text vectorization logic here
#     import torch
#     from transformers import AutoModel, AutoTokenizer

#     tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
#     model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

#     inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
#     with torch.no_grad():
#         outputs = model(**inputs)
#     return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

# def scrape_website(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     text = soup.get_text()
#     # Convert text to vector (this is a placeholder; you need a real implementation)
#     vector = text_to_vector(text)
#     index.upsert([(url, vector)])

# scrape_website("https://u.ae/en/information-and-services")
# #openai.api_key = 'sk-proj-Gt7CD780ADXR4hlRfQcaT3BlbkFJtPeTF94qwsxtULuTkgFy'
# #replicate_api_key = 'YOUR_REPLICATE_API_KEY'
# #OPENAI_API_KEY="sk-proj-Gt7CD780ADXR4hlRfQcaT3BlbkFJtPeTF94qwsxtULuTkgFy"
# client = OpenAI(api_key="sk-proj-Gt7CD780ADXR4hlRfQcaT3BlbkFJtPeTF94qwsxtULuTkgFy")





# def query_vector_database(prompt):
#     # Implement querying logic here
#     return "mock search results"  # Placeholder

# def query_llms(prompt):
#     search_results = query_vector_database(prompt)
#     combined_prompt = f"{search_results}\n\n{prompt}"

#     responses = {}
#     models = {
#         "gpt-3.5-turbo": client.chat.completions.create,
#         "gpt-4": client.chat.completions.create,
#         "llama-2-70b-chat": replicate.run,
#         "falcon-40b-instruct": replicate.run,
#     }

#     for model, method in models.items():
#         response = method(
#             model=model,
#             prompt=combined_prompt,
#             max_tokens=100
#         )
#         responses[model] = response

#     return responses
from langchain.embeddings import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key='b48026df-1663-47bc-b9e2-c3a92067af2e')
index = pc.Index("pages1")
def query_llms(input):
    return getChatGPTAnswer(input)

def getChatGPTAnswer(input):
    embeddings_model = OpenAIEmbeddings(api_key="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")
    embedded_query = embeddings_model.embed_query(input)
    answer=index.query(
        vector=embedded_query,
        namespace="NewSpace",
        top_k=2,
        include_metadata=True,
        )
    return answer