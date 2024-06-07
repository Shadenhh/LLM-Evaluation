from langchain.embeddings import OpenAIEmbeddings
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key='b48026df-1663-47bc-b9e2-c3a92067af2e')
index = pc.Index("pages1")


def query_llms(input):
    answer = getChatGPTAnswer(input)
    return answer

def getChatGPTAnswer(input):
    embeddings_model = OpenAIEmbeddings(api_key="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")
    embedded_query = embeddings_model.embed_query(input)
    data= index.query(
        vector=embedded_query,
        namespace="NewSpace",
        top_k=2,
        include_metadata=True,
        )
    texts = [match['metadata']['text'] for match in data['matches']]
    gatheredData=""
    for i, text in enumerate(texts, 1):
      gatheredData=gatheredData+"\n"+text
    answer=ask_question("Using only the following information " +gatheredData+", answer the next question.\n"+input+"\nMake sure that the answer is short and includes only the specific answer that the user asked about, DO NOT Just rephrase the provided information unless the users question requires that.\nPlease note that in case the provided data is not enough to answer the question, just say that No answer found")
    return answer


import openai

client = OpenAI(api_key = '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')
def ask_question(question):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": question}
        ]
        
    )
    
    return response.choices[0].message.content

# answer =query_llms("what is the police number")
# print(answer)