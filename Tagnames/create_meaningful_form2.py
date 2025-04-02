import sys
import os
import random
import re
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Prompts.create_meaningful_form2 import create_residence_identification_form_prompt, create_study_form_prompt, create_health_and_medical_form_prompt,\
                                            create_vehicle_driver_form_prompt, create_job_form_prompt, residence_indentification_data_generator_prompt

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from Config.LLM import gemini, gemini2
from Config.config import Index


# Folder
label_folder = f"DataX/Test/Label{Index}"
input_folder = f"DataX/Test/Input{Index}"
info_folder = f"DataX/Test/Info{Index}"
# Ensure the folder exists
os.makedirs(label_folder, exist_ok=True)
os.makedirs(input_folder, exist_ok=True)
os.makedirs(info_folder, exist_ok=True)

## Form cư trú và giấy tờ tùy thân

residence_identification_form_name = [
    #### Lấy từ website
    'Khai báo tạm vắng',
    'Cấp hộ chiếu phổ thông',
    'Trình báo mất hộ chiếu phổ thông',
    'Khôi phục giá trị sử dụng hộ chiếu phổ thông',
    'Cấp đổi thẻ căn cước',
    'Cấp lại thẻ căn cước',
    'Cấp xác nhận số chứng minh nhân dân 9 số',
    'Cấp xác nhận số định danh cá nhân',
    'Thông báo lưu trú',
    'Đăng ký tạm trú',
    'Gia hạn tạm trú',
    'Xóa đăng ký tạm trú',
    'Đăng ký thường trú',
    'Đăng ký tạm trú cho hộ gia đình',
    ####### LLM sinh
    'Cấp đổi hộ chiếu phổ thông',  # Khác với cấp mới hộ chiếu
    'Cấp hộ chiếu phổ thông lần đầu cho trẻ em dưới 14 tuổi',
    'Cấp hộ chiếu phổ thông theo thủ tục rút gọn',  # Trường hợp đặc biệt
    'Xác nhận thông tin về cư trú',  # Bao gồm lịch sử cư trú, thường trú, tạm trú
    'Điều chỉnh thông tin cư trú',  # Thay đổi thông tin hộ khẩu, nhân khẩu
    'Tách hộ khẩu',  # Tách hộ khẩu khỏi sổ hộ khẩu chung
    'Xác nhận về việc đã đăng ký thường trú/tạm trú',
    'Xác nhận di chuyển hộ khẩu',  # Khi công dân thay đổi nơi thường trú
    'Hủy bỏ đăng ký thường trú',  # Khi định cư nước ngoài hoặc theo quyết định cơ quan
    'Cấp giấy xác nhận không có quốc tịch Việt Nam',  # Khi xin nhập quốc tịch nước ngoài
    'Cấp lại sổ hộ khẩu'  # Trường hợp đặc thù còn cần sổ hộ khẩu
]

form_info_request_options = {
    'Ngày tháng': [
        "Ngày sinh (định dạng `userX_dob`)",
        "Ngày sinh (tách `userX_dob_day`, `userX_dob_month`, `userX_dob_year`)",
        "Ngày cấp (định dạng `userX_id_issue_day/userX_id_issue_month/userX_id_issue_year`)",
    ],
    'Địa chỉ': [
        "Địa chỉ (chỉ lấy thường trú)",
        "Địa chỉ (chỉ lấy tạm trú)",
        "Địa chỉ (bao gồm cả thường trú và tạm trú)",
        "Địa chỉ (yêu cầu cung cấp chứng minh chỗ ở hợp pháp)",
    ],
    'Giấy tờ tùy thân': [
        "CCCD (không cần nơi cấp)",
        "CCCD (có cả nơi cấp và ngày cấp)",
        "Hộ chiếu (nếu có hộ chiếu cũ, cần bổ sung thông tin hộ chiếu cũ)",
        "Hộ chiếu (chỉ cần số hộ chiếu, không cần ngày cấp)",
        "Visa (chỉ cần số visa, không cần nơi cấp)",
    ]
}

form_format_options = [
    # Định dạng biểu mẫu
    "Chi tiết, Trang trọng, Đánh số thứ tự",
    "Chi tiết, Trang trọng, Không đánh số thứ tự",
]

def random_request(form_info_request_options, form_format_options):
    chosen_format = random.choice(form_format_options)
    selected_categories = random.sample(list(form_info_request_options.keys()), random.randint(0, 3))
    chosen_info = [random.choice(form_info_request_options[category]) for category in selected_categories]
    chosen_format = random.choice(form_format_options)
    return " - ".join(chosen_info) + f" - {chosen_format}" if chosen_info else chosen_format

def convert_to_dict(text):
    # Xóa dấu `-` ở đầu mỗi dòng
    text = re.sub(r"^\s*-\s*", "", text, flags=re.MULTILINE)
    
    # Tìm các cặp key-value chính xác hơn
    matches = re.findall(r"'(.*?)':\s*(\d+|'.*?')", text, re.DOTALL)

    # Xây dựng dictionary
    data_dict = {}
    for key, value in matches:
        # Loại bỏ dấu nháy đơn trong value nếu có
        if value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        
        # Chuyển thành số nếu cần
        if value.isdigit():
            value = int(value)
        
        data_dict[key] = value

    return data_dict


def remove_empty_brackets(text):
    """
    Loại bỏ tất cả các dấu [] xuất hiện trong văn bản nhưng giữ nguyên placeholders.
    
    :param text: Chuỗi văn bản đầu vào
    :return: Văn bản đã được xử lý
    """
    pattern = re.compile(r'\[\s*\]')
    return pattern.sub('', text)


def has_table(text):
    """
    Kiểm tra xem văn bản có chứa bảng hay không (dựa trên ký hiệu markdown của bảng: '|---|').
    
    :param text: Chuỗi văn bản đầu vào
    :return: True nếu có bảng, False nếu không
    """
    pattern = re.compile(r'\|\s*-+\s*\|')
    return bool(pattern.search(text))

def remove_optional_text(text):
    """
    Loại bỏ các đoạn văn bản trong placeholders chứa phần tùy chọn (*...*).
    
    :param text: Chuỗi văn bản đầu vào
    :return: Văn bản đã được xử lý
    """
    pattern = re.compile(r'\[([^\]]+?) - \*[^\]]+?\*\]')
    return pattern.sub(r'[\1]', text)


def has_invalid_full_name_placeholder(text):
    """
    Kiểm tra xem có placeholder full_name nào không đúng dạng [userX_full_name].
    
    :param text: Chuỗi văn bản đầu vào
    :return: True nếu có placeholder không hợp lệ, False nếu tất cả hợp lệ
    """
    pattern = re.compile(r'\[(?!user\d+_full_name)\w+_full_name\]')
    return bool(pattern.search(text))

def create_data(llm, form_name):
    '''
    Tạo dữ liệu đầu vào cho bước tạo form.
    '''
    prompt = PromptTemplate.from_template(residence_indentification_data_generator_prompt)
    chain = prompt | llm | StrOutputParser()
    request = random_request(form_info_request_options, form_format_options)
    response = chain.invoke({'form_name': form_name, 'request': request})
    data = convert_to_dict(response)
    return response, data
    

def create_meaningful_form(llm, data):
    '''
    Tạo form với những thông tin sau: Tên biểu  mẫu, mục đích biểu mẫu, số lượng người dùng, mối quan hệ giữa người dùng, nội dung form,\
    phong cách và định dạng form.
    '''
    prompt = PromptTemplate.from_template(create_residence_identification_form_prompt)
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({'form_name': data['form_name'],
                             'form_purpose': data['form_purpose'],
                             'num_users': data['num_users'],
                             'relationship_between_users': data['relationship_between_users'], 
                             'form_info': data['form_info'],
                             'form_format': data['form_format']})
    return response


def generate_form(llm, number):
    expected_keys = {'form_name', 'form_purpose', 'num_users', 
                     'relationship_between_users', 'form_info', 'form_format'}
    
    for i in range(86, number):
        file_name = f"data_{i}.txt"
        input_path = f"{input_folder}/{file_name}"
        label_path = f"{label_folder}/{file_name}"
        info_path = f"{info_folder}/{file_name}"
        
        print(f"Processing file: {file_name}")
        form_name = random.choice(residence_identification_form_name)

        while True:
            try:
                response, data = create_data(llm, form_name)
                if set(data.keys()) == expected_keys:
                    break
            except Exception as e:
                print(f"Error encountered: {e}. Retrying in 5 seconds...")
                time.sleep(5)
        
        try:
            label_form = create_meaningful_form(llm, data)
            # Sinh lại dữ liệu nếu nó gặp những trường hợp đặc biệt. 
            while has_table(label_form) or has_invalid_full_name_placeholder(label_form):
                label_form = create_meaningful_form(llm, data)
            # Post processing
            label_form = remove_empty_brackets(label_form)
            label_form = remove_optional_text(label_form)
            ## Replace tagname to '........' to create input data
            input_form = re.sub(r'\[([^\]]+)\]', '..........', label_form)

            # Write info file
            with open(info_path, 'w', encoding="utf-8") as f:
                f.write(response)

            # Write input file
            with open(input_path, 'w', encoding='utf-8') as f:
                f.write(input_form)

            # Write label file
            with open(label_path, 'w', encoding='utf-8') as f:
                f.write(label_form)
        except Exception as e:
            print(f"Error writing files for {file_name}: {e}. Retrying in 5 seconds...")
            time.sleep(5)


generate_form(gemini2, 200)



