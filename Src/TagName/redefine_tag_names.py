import sys
import os
import re
import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from Prompt import *
from dotenv import load_dotenv

load_dotenv()
gemini_key = os.getenv("GEMINI_KEY")

llm = GoogleGenerativeAI(model = 'gemini-2.0-flash-exp', timeout= None, max_tokens = 1000, temperature = 0, top_k = 1, top_p = 1,  google_api_key = gemini_key)

def read_file(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    
def write_file(file_path, text):
    os.makedirs(os.path.dirname(file_path),exist_ok=True)
    # Write content to the file
    try:
        with open(file_path, 'w',encoding='utf-8') as file:
            file.write(text)
        print(f"File written successfully to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

def redefined_tag_names(llm = llm, folder_dir = "Forms/Text/Input_test/Input/TagName", start = 0): # Phải có start và end chứ nếu không nó sẽ lỗi gemini
    for index, filename in enumerate(os.listdir(folder_dir)):
        template_prompt = None
        tagnames = None
        name = None
        if filename.endswith(".txt"):
            print("Start with: ", filename)
            file_dir = folder_dir + '/' + filename
            response_dir = "Forms/Text/Input_test/Input/TagName2/" + filename 
            text = read_file(file_dir)
            prompt = PromptTemplate.from_template(redefine_full_name_template_prompt)
            chain = prompt | llm | StrOutputParser()
            try:
                response = chain.invoke({"form": text})
                write_file(response_dir, response)
            except Exception as e:
                print(e)
            print("End with: ", filename)

redefined_tag_names()