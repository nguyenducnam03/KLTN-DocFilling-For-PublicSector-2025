import sys
import os
import re
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Prompts.convert_random_form_to_meaningful import convert_random_form_to_meaningful_template
from Config.LLM import embeddings, gemini


# Đọc form
def create_retrieve(data_dir):
    original_forms = []
    paths = os.listdir(data_dir)
    for path in paths:
        with open(os.path.join(data_dir, path), "r", encoding="utf-8") as f:
            original_forms.append(f.read())
    return original_forms

def convert_random_form_to_meaningful_form(llm, form, original_forms):
    # Tạo retriever
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    splits = text_splitter.create_documents(original_forms)
    vectostore = FAISS.from_documents(splits, embeddings)
    retriever = vectostore.as_retriever()
    prompt = PromptTemplate.from_template(convert_random_form_to_meaningful_template)
    chain = (
        ({"context": retriever, "random_form": RunnablePassthrough()})
        | prompt
        | llm
        | StrOutputParser()
    )
    meaningful_form = chain.invoke(form)
    return meaningful_form

def generate_data_type_5(llm, data_dir, orginal_form_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    original_forms = create_retrieve(data_dir)
    paths = os.listdir(orginal_form_dir)
    
    for idx, path in enumerate(paths, start=1):
        
        
        with open(os.path.join(orginal_form_dir, path), "r", encoding="utf-8") as f:
            form = f.read()
        
        meaningful_form = convert_random_form_to_meaningful_form(llm, form, original_forms)

        # Sử dụng regex để trích xuất nội dung bên trong dấu ```
        match = re.search(r'```(.*?)```', meaningful_form, re.DOTALL)

        if match:
            meaningful_form = match.group(1).strip()

        with open(os.path.join(output_dir, path), "w", encoding="utf-8") as f:
            f.write(meaningful_form)

        print(f"{idx}. Processing file: {path}")

generate_data_type_5(gemini, "Data\LLM_filled", "Data_5", "Data_5/meaningful_form/")