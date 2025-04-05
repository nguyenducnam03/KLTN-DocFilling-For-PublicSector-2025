import sys
import os
import random
import re
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Prompts.create_meaningful_form2 import create_residence_identification_form_prompt, residence_indentification_data_generator_prompt, create_study_form_prompt,\
                                            study_data_generator_prompt, create_health_and_medical_form_prompt, health_data_generator_prompt, \
                                            create_vehicle_driver_form_prompt, vehicle_driver_data_generator_prompt, create_job_form_prompt, job_data_generator_prompt

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from Config.LLM import gemini, gemini2


# Folder
label_folder = f"Data/LLM_Data/Gemini/Test/Label"
input_folder = f"Data/LLM_Data/Gemini/Test/Input"
info_folder = f"Data/LLM_Data/Gemini/Test/Info"
# Ensure the folder exists
os.makedirs(label_folder, exist_ok=True)
os.makedirs(input_folder, exist_ok=True)
os.makedirs(info_folder, exist_ok=True)

## Form names

residence_identification_form_names = [
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

study_form_names = [
    # Web
    'Tiếp nhận du học sinh học bổng ngân sách nhà nước tốt nghiệp về nước',
    'Tuyển sinh công dân Việt Nam ra nước ngoài học tập bằng học bổng ngân sách nhà nước',
    'Cử đi học nước ngoài',
    'Gia hạn thời gian học tập ở nước ngoài',
    'Cấp chính sách nội trú cho học sinh, sinh viên tham gia chương trình đào tạo trình độ cao đẳng',
    'Cấp bản sao văn bằng, chứng chỉ gốc',
    'Công nhân bằng cử nhân bằng trình độ tương đương do cơ sở giao dục nước ngoài cấp để sử dụng tại Việt Nam',
    'Công nhân bằng thạc sĩ bằng trình độ tương đương do cơ sở giao dục nước ngoài cấp để sử dụng tại Việt Nam',
    'Công nhân bằng tiến sĩ bằng trình độ tương đương do cơ sở giao dục nước ngoài cấp để sử dụng tại Việt Nam',
    'Công nhân bằng tốt nghiệp THCS bằng trình độ tương đương do cơ sở giao dục nước ngoài cấp để sử dụng tại Việt Nam',
    'Công nhân bằng tốt nghiệp THPT bằng trình độ tương đương do cơ sở giao dục nước ngoài cấp để sử dụng tại Việt Nam',
    'Xét đặc cách tốt nghiệp THPT',
    'Xét tốt nghiệp và cấp bằng thạc sĩ',
    'Phúc khảo bài thi tốt nghiệp trung học phổ thổng',
    'Chỉnh sửa nội dung văn bằng',
    'Xét cấp bằng tiếng sĩ',
    'Đề nghị miễn giảm học phí, hộ trợ tiền đóng học phí',
    'Cấp học bổng và hỗ trợ kinh phí cho người khuyết tật',
    'Xét cấp học bổng chính sách',
    'Hỗ trợ học tập với dân tộc thiểu số ít người',
    'Chuyển trường',
    'Đăng ký dự thi tốt nghiệp THPT',
    'Đăng ký xét trình độ đại học',
    'Xét tuyển sinh vào trường phổ thông dân tộc nội trú',
    'Đăng ký dự thi cấp chứng chỉ ứng dụng công nghệ thông tin',
    # LLM
    'Đăng ký chương trình trao đổi sinh viên quốc tế',
    'Xác nhận sinh viên đang theo học',
    'Xác nhận hoàn thành chương trình đào tạo',
    'Xin cấp học bổng du học tự túc',
    'Đề nghị hỗ trợ chi phí nghiên cứu khoa học cho sinh viên',
    'Đăng ký bảo lưu kết quả học tập',
    'Đề nghị chuyển ngành học trong cùng trường',
    'Đăng ký thực tập tốt nghiệp',
    'Xác nhận thời gian học tập để hoãn nghĩa vụ quân sự',
    'Đăng ký thi lại/mở lớp học lại',
    'Xin cấp bảng điểm học tập',
    'Đề nghị miễn học phí cho sinh viên diện chính sách',
    'Đề nghị hỗ trợ tài chính cho sinh viên gặp khó khăn đột xuất',
    'Đăng ký thi năng lực ngoại ngữ chuẩn quốc tế',
    'Đề nghị xác nhận sinh viên'
]

health_and_medical_form_names = [
    # Web
    "Cấp lại, đổi, điều chỉnh thông tin trên số BHXH, thẻ BHYT",
    "Đăng ký đóng, cấp thẻ BHYT đối với người chỉ tham gia BHYT",
    "Cấp lại thể bảo hiểm y tế",
    "Cấp lại thẻ bảo hiểm y tế cho trẻ em dưới 6 tuổi",
    "Cấp lại thẻ bảo hiểm y tế cho người cao tuổi", 
    "Giải quyết chế độ thừa hưởng thai sản",
    "Thủ tục khám bệnh, chữa bệnh bao hiểm y tế",
    "Cấp thẻ bảo hiểm y tế",
    "Giải quyết hưởng chế độ ốm đau",
    "Đối thẻ BHYT",
    "Khám giám định để hưởng BHXH",
    "Khám giám định lần đầu do bệnh nghề nghiệp",
    # ChatGPT
    "Cấp lại thẻ BHYT cho người lao động",
    "Đăng ký và cấp thẻ bảo hiểm y tế cho học sinh, sinh viên",
    "Điều chỉnh thông tin cá nhân trên thẻ BHXH",
    "Cấp lại thẻ bảo hiểm y tế cho người bị mất",
    "Đổi thông tin trên thẻ BHXH do thay đổi tên, địa chỉ",
    "Cấp lại thẻ bảo hiểm y tế cho người thuộc diện hộ nghèo",
    "Giải quyết chế độ bảo hiểm xã hội",
    "Cấp thẻ bảo hiểm y tế cho người tham gia BHYT tự nguyện",
    "Giải quyết chế độ tử tuất",
    "Cấp thẻ bảo hiểm y tế cho người có công với cách mạng",
    "Cấp lại thẻ BHYT cho người thuộc diện bảo vệ sức khỏe",
    "Cập nhật thông tin trên thẻ BHXH khi thay đổi tình trạng hôn nhân",
    "Giải quyết chế độ bảo hiểm xã hội cho người lao động nghỉ hưu",
    "Cấp lại thẻ BHYT cho người bị mất thẻ do thiên tai",
    "Cấp thẻ bảo hiểm y tế cho người tham gia BHYT theo hộ gia đình"
]

vehicle_driver_form_names = [
    # LLM
    "Tờ khai đăng ký xe",
    "Đơn xin cấp giấy phép lái xe",
    "Tờ khai thay đổi thông tin xe",
    "Đơn xin cấp lại giấy phép lái xe",
    "Tờ khai đăng kiểm phương tiện",
    "Đơn xin chuyển nhượng quyền sở hữu xe",
    "Tờ khai bảo hiểm xe cơ giới",
    "Đơn xin cấp biển số xe",
    "Tờ khai cấp lại biển số xe",
    "Đơn xin miễn thuế phương tiện",
    "Tờ khai xử lý vi phạm giao thông",
    "Đơn xin cấp giấy phép lái xe quốc tế",
    "Tờ khai gia hạn giấy phép lái xe",
    "Đơn xin cấp lại giấy phép lái xe do mất",
    "Tờ khai đăng ký xe cho tổ chức",
    "Đơn xin đổi giấy phép lái xe sang mẫu mới"
]

job_form_names = [
    "Tờ khai cấp giấy phép lao động cho người nước ngoài",
    "Đơn xin cấp giấy phép lao động cho người nước ngoài",
    "Tờ khai thuế thu nhập cá nhân",
    "Đơn xin miễn thuế thu nhập cá nhân",
    "Tờ khai nộp thuế thu nhập doanh nghiệp",
    "Tờ khai đề nghị nâng ngạch công chức, viên chức",
    "Đơn xin nâng ngạch công chức, viên chức",
    "Tờ khai cấp chứng chỉ hành nghề",
    "Đơn xin cấp chứng chỉ hành nghề",
    "Tờ khai hưởng trợ cấp thất nghiệp",
    "Đơn xin trợ cấp thất nghiệp",
    "Tờ khai đăng ký tham gia bảo hiểm thất nghiệp",
    "Đơn xin thôi việc và hưởng trợ cấp thất nghiệp",
    "Đơn xin tuyển dụng lao động",
    "Tờ khai đăng ký hỗ trợ và giới thiệu việc làm",
    "Đơn xin hỗ trợ giới thiệu việc làm",
    "Tờ khai xin hưởng trợ cấp thất nghiệp theo tháng",
    "Đơn xin trợ cấp do mất việc làm",
    "Tờ khai cấp giấy phép lao động cho chuyên gia nước ngoài",
    "Đơn xin cấp giấy phép lao động cho lao động nước ngoài tại doanh nghiệp",
    "Tờ khai đăng ký thuế thu nhập cá nhân cho người nước ngoài",
    "Tờ khai đăng ký thuế thu nhập cho lao động trong nước",
    "Tờ khai yêu cầu hoàn thuế thu nhập cá nhân",
    "Tờ khai hoàn thuế thu nhập cá nhân cho người lao động nước ngoài",
    "Đơn xin miễn thuế thu nhập doanh nghiệp",
    "Đơn xin gia hạn giấy phép lao động cho người nước ngoài",
    "Tờ khai nộp thuế thu nhập cá nhân từ hoạt động kinh doanh",
    "Đơn xin cấp chứng chỉ hành nghề y tế",
    "Đơn xin cấp chứng chỉ hành nghề dược",
    "Tờ khai chứng nhận hành nghề y dược",
    "Đơn xin cấp chứng chỉ hành nghề tại các tổ chức đào tạo quốc tế",
    "Đơn xin trợ cấp thất nghiệp cho lao động tự do",
    "Đơn xin nhận trợ cấp thất nghiệp từ doanh nghiệp đã giải thể",
    "Tờ khai xin cấp giấy phép lao động cho lao động tạm thời",
    "Đơn xin cấp chứng chỉ hành nghề cho các ngành nghề đặc thù",
    "Tờ khai đăng ký cấp thẻ bảo hiểm thất nghiệp cho người lao động nước ngoài",
    "Đơn xin hỗ trợ đăng ký việc làm cho người có nhu cầu tìm việc",
    "Đơn xin tăng lương, thăng chức và nâng ngạch công chức",
    "Tờ khai cấp giấy phép lao động cho lao động nước ngoài tại các doanh nghiệp đầu tư nước ngoài",
    "Tờ khai cấp giấy phép lao động cho lao động trong các ngành công nghiệp đặc biệt",
    "Đơn xin hưởng trợ cấp từ chương trình tái tạo nghề cho lao động thất nghiệp",
    "Đơn xin thẻ công nhận lao động có tay nghề cao",
    "Đơn xin cấp giấy phép lao động cho lao động Việt Nam ở nước ngoài",
    "Đơn xin hỗ trợ giới thiệu việc làm cho người lao động trong các khu công nghiệp",
    "Tờ khai đăng ký tìm việc và hỗ trợ tư vấn nghề nghiệp cho người lao động thất nghiệp",
    "Tờ khai xin nâng ngạch và thăng tiến nghề nghiệp",
    "Đơn xin trợ cấp thất nghiệp cho lao động không có bảo hiểm thất nghiệp",
    "Tờ khai điều chỉnh thông tin cấp giấy phép lao động cho người nước ngoài",
    "Tờ khai đăng ký hỗ trợ bảo hiểm thất nghiệp cho lao động có hợp đồng ngắn hạn",
    "Tờ khai gia hạn thời gian hưởng trợ cấp thất nghiệp",
    "Đơn xin nhận trợ cấp thất nghiệp do gián đoạn công việc hoặc giảm thời gian làm việc",
    "Tờ khai tham gia khóa đào tạo nghề cho lao động thất nghiệp",
    "Đơn xin cấp phép hành nghề cho chuyên gia lao động nước ngoài",
    "Tờ khai đăng ký lao động tại các công ty tuyển dụng quốc tế",
    "Đơn xin chứng nhận lao động tự do hoặc làm việc theo hợp đồng ngắn hạn",
    "Đơn xin miễn giảm thuế thu nhập doanh nghiệp đối với công ty nước ngoài",
    "Tờ khai hỗ trợ chi phí đào tạo và phát triển nghề nghiệp cho lao động trong ngành nghề cần thiết",
    "Đơn xin hỗ trợ và giới thiệu việc làm cho các đối tượng đặc biệt"
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
    ],
    'Thông tin liên hệ': [
        "Số điện thoại (di động hoặc cố định)",
        "Số điện thoại (chỉ lấy số điện thoại di động)",
        "Email (cần phải có email hợp lệ)",
        "Số điện thoại liên lạc khẩn cấp (nếu có)",
    ],
}

form_format_options = [
    # Định dạng biểu mẫu
    "Chi tiết, Trang trọng, Đánh số thứ tự",
    "Chi tiết, Trang trọng, Không đánh số thứ tự",
]

def random_request(form_info_request_options, form_format_options):
    chosen_format = random.choice(form_format_options)
    selected_categories = random.sample(list(form_info_request_options.keys()), random.randint(0, 4))
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

def create_data(llm, form_name, data_generator_prompt):
    '''
    Tạo dữ liệu đầu vào cho bước tạo form.
    '''
    prompt = PromptTemplate.from_template(data_generator_prompt)
    chain = prompt | llm | StrOutputParser()
    request = random_request(form_info_request_options, form_format_options)
    response = chain.invoke({'form_name': form_name, 'request': request})
    data = convert_to_dict(response)
    return response, data
    

def create_meaningful_form(llm, data, create_form_prompt):
    '''
    Tạo form với những thông tin sau: Tên biểu  mẫu, mục đích biểu mẫu, số lượng người dùng, mối quan hệ giữa người dùng, nội dung form,\
    phong cách và định dạng form.
    '''
    prompt = PromptTemplate.from_template(create_form_prompt)
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({'form_name': data['form_name'],
                             'form_purpose': data['form_purpose'],
                             'num_users': data['num_users'],
                             'relationship_between_users': data['relationship_between_users'], 
                             'form_info': data['form_info'],
                             'form_format': data['form_format']})
    return response


# def generate_form(llm, number):
#     expected_keys = {'form_name', 'form_purpose', 'num_users', 
#                      'relationship_between_users', 'form_info', 'form_format'}
    
#     for i in range(0, number):
#         file_name = f"data_{i}.txt"
#         input_path = f"{input_folder}/{file_name}"
#         label_path = f"{label_folder}/{file_name}"
#         info_path = f"{info_folder}/{file_name}"
        
#         print(f"Processing file: {file_name}")
#         form_name = random.choice(residence_identification_form_name)

#         while True:
#             try:
#                 response, data = create_data(llm, form_name)
#                 if set(data.keys()) == expected_keys:
#                     break
#             except Exception as e:
#                 print(f"Error encountered: {e}. Retrying in 5 seconds...")
#                 time.sleep(5)
        
#         try:
#             label_form = create_meaningful_form(llm, data)
#             # Sinh lại dữ liệu nếu nó gặp những trường hợp đặc biệt. 
#             while has_table(label_form) or has_invalid_full_name_placeholder(label_form):
#                 label_form = create_meaningful_form(llm, data)
#             # Post processing
#             label_form = remove_empty_brackets(label_form)
#             label_form = remove_optional_text(label_form)
#             ## Replace tagname to '........' to create input data
#             input_form = re.sub(r'\[([^\]]+)\]', '..........', label_form)

#             # Write info file
#             with open(info_path, 'w', encoding="utf-8") as f:
#                 f.write(response)

#             # Write input file
#             with open(input_path, 'w', encoding='utf-8') as f:
#                 f.write(input_form)

#             # Write label file
#             with open(label_path, 'w', encoding='utf-8') as f:
#                 f.write(label_form)
#         except Exception as e:
#             print(f"Error writing files for {file_name}: {e}. Retrying in 5 seconds...")
#             time.sleep(5)

def generate_form(llm, form_names, data_generator_prompt, create_form_prompt):
    expected_keys = {'form_name', 'form_purpose', 'num_users', 
                     'relationship_between_users', 'form_info', 'form_format'}
    
    for i, form_name in enumerate(form_names):
        file_name = f"data{i+65}.txt"
        input_path = f"{input_folder}/{file_name}"
        label_path = f"{label_folder}/{file_name}"
        info_path = f"{info_folder}/{file_name}"
        
        print(f"Processing file: {file_name}")

        while True:
            try:
                print(000000000)
                response, data = create_data(llm, form_name, data_generator_prompt)
                if set(data.keys()) == expected_keys:
                    break
            except Exception as e:
                print(f"Error encountered: {e}. Retrying in 5 seconds...")
                time.sleep(5)
        
        while True:
            try:
                print(11111)
                label_form = create_meaningful_form(llm, data, create_form_prompt)
                print(label_form)
                # Sinh lại dữ liệu nếu nó gặp những trường hợp đặc biệt. 
                while has_table(label_form) or has_invalid_full_name_placeholder(label_form):
                    print(222)
                    label_form = create_meaningful_form(llm, data, create_form_prompt)
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
                break
            except Exception as e:
                print(f"Error writing files for {file_name}: {e}. Retrying in 5 seconds...")
                time.sleep(5)



generate_form(gemini2, health_and_medical_form_names, health_data_generator_prompt, create_health_and_medical_form_prompt)

# response, data = create_data(gemini2,"Báo cáo tốt nghiệp" , study_data_generator_prompt)



