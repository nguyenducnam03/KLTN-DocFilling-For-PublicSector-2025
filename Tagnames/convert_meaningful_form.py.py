import sys
import os
import re
import random
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Prompts.convert_meaningful_form import create_multi_user_prompt
from Config.LLM import gemini
from Config.config import Index


# Folder
label_folder = f"DataX/Test/Label{Index}"
input_folder = f"DataX/Test/Info{Index}"
# Ensure the folder exists
os.makedirs(label_folder, exist_ok=True)
os.makedirs(input_folder, exist_ok=True)

user_dict = {
    "Người làm đơn": {
        "Họ và tên": "[user0_full_name]",
        "Ngày sinh": "[user0_dob_year]",
        "Giới tính": "[user0_gender]",
        "Dân tộc": "[user0_ethnicity]",
        "Quốc tịch": "[user0_nationality]",
        "Nơi cư trú": "[user0_address]",
        "Giấy tờ tùy thân": "[user0_id_number]",
        "Quan hệ với người liên quan": "[#another]",
        "Số điện thoại": "[#another]",
        "Email": "[#another]"
    },
    "Người giám hộ": {
        "Họ và tên": "[user0_full_name]",
        "Ngày sinh": "[user0_dob_year]",
        "Giới tính": "[user0_gender]",
        "Dân tộc": "[user0_ethnicity]",
        "Quốc tịch": "[user0_nationality]",
        "Nơi cư trú": "[user0_address]",
        "Giấy tờ tùy thân": "[user0_id_number]",
        "Quan hệ với người được giám hộ": "[#another]"
    },
    "Người được khai sinh": {
        "Họ và tên": "[user0_full_name]",
        "Ngày sinh": "[user0_dob_year]",
        "Giới tính": "[user0_gender]",
        "Dân tộc": "[user0_ethnicity]",
        "Quốc tịch": "[user0_nationality]",
        "Nơi cư trú": "[user0_address]",
        "Giấy khai sinh": "[user0_birth_certificate]"
    },
    "Cha/Mẹ": {
        "Họ và tên": "[user0_full_name]",
        "Ngày sinh": "[user0_dob_year]",
        "Dân tộc": "[user0_ethnicity]",
        "Quốc tịch": "[user0_nationality]",
        "Nơi cư trú": "[user0_address]",
        "Giấy tờ tùy thân": "[user0_id_number]",
        "Quan hệ với người được khai sinh": "[#another]"
    },
    "Người bị tố cáo": {
        "Họ và tên": "[user0_full_name]",
        "Ngày sinh": "[user0_dob_year]",
        "Giới tính": "[user0_gender]",
        "Dân tộc": "[user0_ethnicity]",
        "Quốc tịch": "[user0_nationality]",
        "Nơi cư trú": "[user0_address]",
        "Giấy tờ tùy thân": "[user0_id_number]"
    },
    "Người chết": {
        "Họ và tên": "[user0_full_name]",
        "Ngày sinh": "[user0_dob_year]",
        "Giới tính": "[user0_gender]",
        "Dân tộc": "[user0_ethnicity]",
        "Quốc tịch": "[user0_nationality]",
        "Nơi cư trú cuối cùng": "[#another]",
        "Giấy tờ tùy thân": "[user0_id_number]",
        "Ngày mất": "[user0_death_day]/[user0_death_month]/[user0_death_year]",
        "Nguyên nhân chết": "[#another]"
    },
    "Người ủy quyền": {
        "Họ và tên": "[user0_full_name]",
        "Ngày sinh": "[user0_dob_year]",
        "Giới tính": "[user0_gender]",
        "Dân tộc": "[user0_ethnicity]",
        "Quốc tịch": "[user0_nationality]",
        "Nơi cư trú": "[user0_address]",
        "Giấy tờ tùy thân": "[user0_id_number]",
        "Nội dung ủy quyền": "[#another]"
    },
    "Người đại diện hợp pháp": {
        "Họ và tên": "[user0_full_name]",
        "Chức vụ": "[#another]",
        "Cơ quan/tổ chức": "[#another]",
        "Giấy tờ tùy thân": "[user0_id_number]",
        "Địa chỉ": "[user0_current_address]"
    },
    "Chủ hộ": {
        "Họ và tên": "[user0_full_name]",
        "Số định danh cá nhân": "[user0_id_number]",
        "Nơi cư trú": "[user0_address]",
        "Giấy tờ tùy thân": "[user0_id_number]",
        "Quan hệ với người khai báo": "[#another]"
    },
    "Người thân": {
        "Họ và tên": "[user0_full_name]",
        "Ngày sinh": "[user0_dob_year]",
        "Quan hệ với người khai báo": "[#another]",
        "Giấy tờ tùy thân": "[user0_id_number]",
        "Nơi cư trú": "[user0_current_address]"
    }
}


def get_random_users(user_dict, min_users=2, max_users=3):
    selected_users = random.sample(list(user_dict.keys()), random.randint(min_users, max_users))
    result = []
    
    for idx, user in enumerate(selected_users, start=1):
        user_data = user_dict[user]
        selected_tagnames = random.sample(list(user_data.keys()), random.randint(2, len(user_data)))
        
        if 'Họ và tên' not in selected_tagnames:
            selected_tagnames.insert(0, 'Họ và tên')
        
        user_str = f"{idx}. {user}"  # User type with increasing index
        for tag in selected_tagnames:
            tagname = re.sub('user0', f'user{idx}', user_data[tag])
            user_str += f"\n{tag}: {tagname}"
        
        result.append(user_str)
    
    return '\n\n'.join(result)
    

def create_meaningful_form(llm, data):
    prompt = PromptTemplate.from_template(create_multi_user_prompt)
    chain = prompt | gemini | StrOutputParser()
    response = chain.invoke({"input": data})
    return response

def generate_data_type_II(llm, number):
    
    for i in range(number):
        file_name = f"data_{i}.txt"
        input_path = f"{input_folder}/{file_name}"
        label_path = f"{label_folder}/{file_name}"
        print(f"Processing file: {file_name}")
        
        data = get_random_users(user_dict)
        meaningful_form = create_meaningful_form(llm, data)
        
        input_form = re.sub(r'\[([^\]]+)\]', '..........', meaningful_form)
        
        # Write input file
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write(input_form)
        
        # Write label file
        with open(label_path, 'w', encoding='utf-8') as f:
            f.write(meaningful_form)
    


generate_data_type_II(gemini, 5)