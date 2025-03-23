import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Prompts.create_meaningful_form2 import create_residence_identification_form_prompt, create_study_form_prompt, create_health_and_medical_form_prompt,\
                                            create_vehicle_driver_form_prompt, create_job_form_prompt


from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from Config.LLM import gemini


def create_meaningful_form(llm, data):
    prompt = PromptTemplate.from_template(create_residence_identification_form_prompt)
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({'form_type': data['form_type'],
                             'form_purpose': data['form_purpose'],
                             'num_users': data['num_users'],
                             'relationship_between_users': data['relationship_between_users'], 
                             'form_info': data['form_info'],
                             'form_format': data['form_format']})
    return response

data = {
    'form_type': 'Cấp hộ chiếu phổ thông',
    'form_purpose': 'Cấp mới hộ chiếu',
    'num_users': 1,
    'relationship_between_users': 'Không áp dụng',
    'form_info': 'Thông tin cá nhân(ngày sinh viết theo định dạng `user1_dob`), giấy tờ tùy thân (CMND/CCCD), địa chỉ cư trú(chỉ lấy địa chỉ thường trú), '
                    'thông tin hộ chiếu cũ (nếu có)',
    'form_format': 'Chi tiết, Trang trọng, Đánh số thứ tự'
}

response = create_meaningful_form(gemini, data)
print(response)