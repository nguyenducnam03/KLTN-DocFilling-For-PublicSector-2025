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

llm = GoogleGenerativeAI(model = 'gemini-1.5-flash', timeout= None, max_tokens = 1000, temperature = 0, top_k = 1, top_p = 1,  google_api_key = gemini_key)

type_form_feature = """
## Thông tin phân loại:

### **1. Cư trú và giấy tờ tùy thân**  
**Mẫu đơn thường gặp:**  
- Tờ khai căn cước công dân, hộ chiếu, chứng minh nhân dân.  
- Đơn đề nghị khôi phục, điều chỉnh thông tin liên quan đến cư trú hoặc giấy tờ tùy thân.

**Từ khóa đặc trưng:**
- "TỜ KHAI CĂN CƯỚC CÔNG DÂN"
- "TỜ KHAI"
- "GIẤY XÁC NHẬN"
- "ĐƠN ĐỀ NGHỊ"
- "CMND", "CCCD", "Chứng minh nhân dân", "Căn cước công dân"
- "Hộ chiếu", "passport", "số hộ chiếu"
- "Nơi cấp", "Ngày cấp", "Tháng cấp", "Năm cấp"
- "Quốc tịch", "Quê quán", "Địa chỉ thường trú", "Địa chỉ hiện tại"
- "Nghề nghiệp", "Nơi đăng ký khai sinh"
- "Phường", "Xã", "Quận", "Huyện", "Tỉnh"
- "Số thị thực (visa)", "Ngày hết hạn thị thực"
- "Lý do thay đổi", "Điều chỉnh thông tin cư trú", "Khôi phục hộ chiếu"

**Thông tin bổ sung đặc trưng:**
- Thông tin cá nhân như: tên, họ, chữ đệm, ngày/tháng/năm sinh.
- Số chứng minh nhân dân hoặc căn cước công dân.
- Các thông tin liên quan đến địa chỉ và nơi cư trú của người dùng.

### **2. Giáo dục**  
**Mẫu đơn thường gặp:**  
- Đơn đề nghị hỗ trợ học tập, xin học bổng, chuyển trường  
- Báo cáo tốt nghiệp, đơn đề nghị cấp chính sách nội trú.  
- Các mẫu đơn có liên quan đến trường học, học sinh, sinh viên và các vấn đề giáo dục.

**Thông tin đặc trưng:**  
- Tên trường, lớp, khóa học  
- Hiệu trưởng, giáo viên, người hướng dẫn  
- Bằng cấp đạt được  
- Mã số sinh viên  
- Các thuật ngữ liên quan như **học tập, học phí, học bổng, giáo dục, chuyển trường**  
- Số quyết định cử đi học  
- Thời gian của khóa học, điểm đạt được, kết quả xếp loại.  
- Các thông tin liên quan đến học kỳ, năm học.

### **3. Y tế và sức khỏe**  
**Mẫu đơn thường gặp:**  
- Đơn đăng ký bảo hiểm y tế, bảo hiểm xã hội  
- Đơn khiếu nại bảo hiểm, báo cáo tình hình sức khỏe  
- Mẫu đơn liên quan đến các quyền lợi và chi phí y tế.  

**Thông tin đặc trưng:**  
- Mã số bảo hiểm xã hội, bảo hiểm y tế  
- Tên ngân hàng, số tài khoản  
- Nghề nghiệp  
- Nơi đăng ký bảo hiểm y tế  
- Thông tin về cha/mẹ/giám hộ  
- Số thẻ bảo hiểm y tế  
- Các từ khóa như: **bảo hiểm y tế, bảo hiểm xã hội, bệnh nghề nghiệp**  
- Tên cơ quan bảo hiểm xã hội  
- Các mục liên quan đến thanh toán y tế, chăm sóc sức khỏe.  

### **4. Phương tiện và lái xe**  
**Mẫu đơn thường gặp:**  
- Giấy phép lái xe, đăng ký xe, các loại giấy tờ liên quan đến phương tiện giao thông và hoạt động vận tải.  
- Đơn đăng ký cấp giấy phép lái xe quốc tế, đơn xin cấp đổi giấy phép lái xe.  

**Thông tin đặc trưng:**  
- Số giấy phép lái xe  
- Cơ quan cấp giấy phép lái xe  
- Ngày cấp, nơi cấp  
- Hạng giấy phép lái xe  
- Thông tin về số máy, số khung xe  
- Mã hồ sơ khai lệ phí trước bạ, số hóa đơn điện tử  
- Số tờ khai hải quan điện tử  
- Các thuật ngữ liên quan như: **GPLX, giấy phép lái xe quốc tế, sở giao thông vận tải**  
- Các mục liên quan đến vận hành, điều khiển phương tiện, giấy phép kinh doanh vận tải.  

### **5. Việc làm**  
**Mẫu đơn thường gặp:**  
- Đơn xin việc, đơn xin nghỉ việc  
- Mẫu đơn hưởng trợ cấp thất nghiệp  
- Các biểu mẫu liên quan đến quyền lợi và trách nhiệm của người lao động.  

**Thông tin đặc trưng:**  
- Trung tâm dịch vụ việc làm  
- Ngày nộp đơn hưởng trợ cấp  
- Các thuật ngữ như: **thất nghiệp, trợ cấp, hỗ trợ học nghề**  
- Số quyết định liên quan đến quyền lợi lao động  
- Tổng số tháng đóng bảo hiểm thất nghiệp  
- Các mẫu đơn liên quan đến thuế thu nhập cá nhân, hợp đồng lao động, quyết định hưởng trợ cấp thất nghiệp.  

### **6. Khác**  
**Mẫu đơn thường gặp:**  
- Đơn từ không thuộc các danh mục trên hoặc có mục đích sử dụng khác biệt.  

**Thông tin đặc trưng:**  
- Không có từ khóa cụ thể cho các danh mục trên  
- Nội dung không liên quan đến cư trú, giáo dục, y tế, phương tiện hoặc việc làm. 
"""

def identify_type_form(llm):
    # Tạo retriever
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key = gemini_key)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 100)
    splits = text_splitter.create_documents([type_form_feature])
    vectostore = FAISS.from_documents(splits, embeddings)
    retriever = vectostore.as_retriever()
    template = """
    Bạn là một chuyên gia phân loại tài liệu vào các danh mục phù hợp. Có sáu loại tài liệu mà bạn cần phân biệt:

    1. Cư trú và giấy tờ tùy thân  
    2. Giáo dục  
    3. Y tế và sức khỏe  
    4. Phương tiện và lái xe  
    5. Việc làm  
    6. Khác

    # Hướng dẫn:  
    - Tôi sẽ cung cấp cho bạn một mẫu đơn được đặt trong ''' '''.  
    - Bạn phải **sử dụng retriever** để trích xuất và đọc các thông tin quan trọng trong mẫu đơn đó.  
    - Sau khi đã có các đặc điểm nổi bật của tài liệu, hãy **so sánh và xác định loại tài liệu phù hợp** nhất với 6 danh mục trên.  

    # Cách sử dụng retriever:  
    - Bạn sẽ tìm kiếm các thông tin như **từ khóa đặc trưng** (ví dụ: "Căn cước công dân", "Bảo hiểm", "Học tập", "Đăng ký xe", "Hợp đồng lao động") để nhận diện danh mục.  
    - Chú ý các **đặc điểm chính** như: tiêu đề, loại thông tin cần điền, và mục đích sử dụng mẫu đơn.

    # Cấu trúc trả lời:  
    - Trả lời của bạn phải theo định dạng: **Số thứ tự và Tên danh mục** như ví dụ bên dưới.

    # Lưu ý:  
    - Câu trả lời phải chính xác theo **một trong sáu** loại danh mục đã cho.  
    - Chỉ chọn một loại phù hợp nhất với thông tin trong mẫu đơn.  
    - Đừng cung cấp giải thích hay bất kỳ thông tin bổ sung nào khác ngoài danh mục và số thứ tự.
    
    ## Example:
    Mẫu đơn:
    '''
                    TỜ KHAI CĂN CƯỚC CÔNG DÂN
        1. Họ, chữ đệm và tên(1): ..........
        2. Họ, chữ đệm và tên gọi khác (nếu có)(1): ..........
        3. Ngày, tháng, năm sinh:........../........../..........; 4. Giới tính (Nam/nữ): ..........
        5. Số CMND/CCCD: ..........
        6. Dân tộc: ..........; 7. Tôn giáo: .......... 8. Quốc tịch: ..........
        9. Tình trạng hôn nhân: .......... 10. Nhóm máu (nếu có): ..........
        11. Nơi đăng ký khai sinh: ..........
        12. Quê quán: ..........
        13. Nơi thường trú: ..........
        14. Nơi ở hiện tại: ..........
        15. Nghề nghiệp: .......... 16. Trình độ học vấn: ..........
    '''
    Kết quả: 1. Cư trú và giấy tờ tùy thân
    
    ## Example:
    Mẫu đơn:
    '''
                                TỜ KHAI THAM GIA, ĐIỀU CHỈNH THÔNG TIN BẢO HIỂM XÃ HỘI, BẢO HIỂM Y TẾ

    I.	Áp dụng đối với người tham gia tra cứu không thấy mã số BHXH do cơ quan BHXH cấp
    [01]. Họ và tên (viết chữ in hoa): ............................................	[02]. Giới tính: ............................................
    [03]. Ngày, tháng, năm sinh: ...../...../......	  [04]. Quốc tịch: ............................................
    [05]. Dân tộc: ........................	[06]. Số CCCD/ĐDCN/Hộ chiếu: .........................................	
    [07]. Điện thoại: ............................	[08]. Email (nếu có): ............................................	
    [09]. Nơi đăng ký khai sinh: [09.1]. Xã: .........................	[09.2]. Huyện: ................................ [09.3]. Tỉnh: ........................
    [10]. Họ tên cha/mẹ/giám hộ (đối với trẻ em dưới 6 tuổi): ..................................................
    [11]. Đăng ký nhận kết quả giải quyết thủ tục hành chính: ............................
    [12]. Số nhà, đường/phố, thôn/xóm: ............................................	
    [13]. Xã: ..........................	[14]	Huyện: .............................	[15]. Tỉnh: ....................................... 	
    [16]. Kê khai Phụ lục Thành viên hộ gia đình (phụ lục kèm theo) đối với người tham gia tra cứu không thấy mã số BHXH và người tham gia BHYT theo hộ gia đình để giảm trừ mức đóng.
    '''
    Kết quả: 3. Y tế và sức khỏe

    ## Example:
    Mẫu đơn:
    '''
        CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
            Độc lập - Tự do - Hạnh phúc

    ĐƠN ĐỀ NGHỊ HỖ TRỢ HỌC TẬP 
    (Dùng cho cha mẹ trẻ mẫu giáo hoặc người chăm sóc trẻ mẫu giáo học tại các cơ sở giáo dục công lập)
    Kính gửi: ..........(Cơ sở giáo dục)
    Họ và tên cha mẹ (hoặc người chăm sóc): ..........
    Hộ khẩu thường trú tại:..........
    Là cha/mẹ (hoặc người chăm sóc) của em:..........
    Sinh ngày:..........
    Dân tộc:..........
    Hiện đang học tại lớp:..........
    Trường:..........
    Tôi làm đơn này đề nghị các cấp quản lý xem xét, giải quyết cấp tiền hỗ trợ học tập theo quy định và chế độ hiện hành.

    XÁC NHẬN CỦA ỦY BAN NHÂN DÂN CẤP XÃ1
    Nơi trẻ mẫu giáo có hộ khẩu thường trú
    (Ký tên, đóng dấu)	..........,ngày..........tháng..........năm..........
    Người làm đơn
    (Ký, ghi rõ họ tên)
    '''
    Kết quả: 2. Giáo dục

    Example:
    Mẫu đơn:
    '''
    {form}
    '''
    Kết quả:
    """

    prompt = PromptTemplate.from_template(template)


    chain = (
        (
            {
                "context" : retriever,
                "form": RunnablePassthrough()
            }
        )
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

form = """
            CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
                Độc lập - Tự do - Hạnh phúc
                
            TỜ KHAI THAY ĐỔI THÔNG TIN CƯ TRÚ

    Kính gửi(1):..........
1. Họ, chữ đệm và tên:	..........
2. Ngày, tháng, năm sinh:........../........../ ..........       3. Giới tính:	..........
4. CCCD: ..........
5. Số điện thoại liên hệ:..........6. Email:..........	
7. Họ, chữ đệm và tên chủ hộ:.......... 8. Mối quan hệ với chủ hộ:..........
9.Số định danh cá nhân của chủ hộ: ..........
10. Nội dung đề nghị(2): ..........	
"""

# chain = identify_type_form(llm)

# print(chain.invoke(form))
# Function to read file contents
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


def extract_dates(text):
    #
    text = text.lower()
    # Các biểu thức regex
    regex = r"(?:ngày sinh|sinh ngày|ngày tháng năm sinh|ngày, tháng, năm sinh|ngày tháng năm sinh|ngày/tháng/năm sinh|ngày cấp|cấp ngày|ngày)\s*:*\s*(?:\(\d+\))?\s*\[([^\d\s][^\]\s]*?_(?:issue_date|dob))\]"
    regex1 = r"(?:ngày sinh|sinh ngày|ngày tháng năm sinh|ngày, tháng, năm sinh|ngày tháng năm sinh|ngày/tháng/năm sinh|ngày cấp|cấp ngày)\s*:*\s*(?:\(\d+\))?\s*\[([^\[\]]+)\]/\[([^\[\]]+)\]/\[([^\[\]]+)\]"
    regex2 = r"(?:ngày sinh|sinh ngày|ngày tháng năm sinh|ngày, tháng, năm sinh|ngày/tháng/năm sinh|ngày cấp|cấp ngày|ngày)\s*:*\s*(?:\(\d+\))?\s*\[([^\s\d][^\]\s]*?(?:issue_day|dob_day))\]"
    regex3 = r"(?:tháng sinh|tháng)\s*:*\s*(?:\(\d+\))?\s*\[([^\s\d][^\]\s]*?(?:issue_month|dob_month))\]"
    regex4 = r"(?:năm sinh|năm)\s*:*\s*(?:\(\d+\))?\s*\[([^\s\d][^\]\s]*?(?:issue_day|dob_year))\]"

    matches = []
    match1 = re.findall(regex1, text, re.DOTALL)
    if match1:
        for m in match1:
            matches.append(f"{m[0]}/{m[1]}/{m[2]}")

    match = re.findall(regex, text, re.DOTALL)
    if match:
        matches.extend([m for m in match])

    match_day = re.findall(regex2, text, re.DOTALL)
    match_month = re.findall(regex3, text, re.DOTALL)
    match_year = re.findall(regex4, text, re.DOTALL)

    # Thêm vào danh sách kết quả nếu chưa có thông tin tương ứng
    if match_day:
        matches += match_day
    if match_month:
        matches += match_month
    if match_year:
        matches += match_year

    # Trả về danh sách các thông tin đã trích xuất được
    return list(set(matches))

def replaced_date_function(form):
  copy_form = copy.deepcopy(form)
  tagnames = extract_dates(copy_form)
  for tagname in tagnames:
    if "day" in tagname and "month" in tagname and "year" in tagname:
      continue
    if "day" in tagname:
      temp1 = f'{tagname[:-3]}month'
      temp2 = f'{tagname[:-3]}year'
      regex1 = rf'{temp1}'
      regex2 = rf'{temp2}'
      regex3 = rf"(?:ngày sinh|sinh ngày|ngày tháng năm sinh|ngày, tháng, năm sinh|ngày tháng năm sinh|ngày/tháng/năm sinh|ngày cấp|cấp ngày|ngày)\s*:*\s*(?:\(\d+\))?\s*\[{tagname}\]\s*tháng"
      _match1 = re.findall(regex1, copy_form.lower(), re.DOTALL)
      _match2 = re.findall(regex2, copy_form.lower(), re.DOTALL)
      _match3 = re.findall(regex3, copy_form.lower(), re.DOTALL)
      if not (_match1 or _match2 or _match3):
        form = form.replace(f"[{tagname}]", f"[{tagname}]/[{temp1}]/[{temp2}]")
    elif tagname[-3:] == "dob":
      form = form.replace(f"[{tagname}]", f"[{tagname}_day]/[{tagname}_month]/[{tagname}_year]")
    elif tagname[-4:] == "date":
      temp = tagname[:-5]
      form = form.replace(f"[{tagname}]", f"[{temp}_day]/[{temp}_month]/[{temp}_year]")
  return form




# "Forms/Text/Input_test"           
# "Forms/Text/Input/Output"
def auto_generate_tag_names(llm = llm, folder_dir = "Forms/Text/Input_test/Input", start = 0): # Phải có start và end chứ nếu không nó sẽ lỗi gemini
    for index, filename in enumerate(os.listdir(folder_dir)):
        chain = identify_type_form(llm)
        template_prompt = None
        tagnames = None
        name = None
        if filename.endswith(".txt"):
            print("Start with: ", filename)
            file_dir = folder_dir + '/' + filename
            response_dir = folder_dir + '/TagName/' + filename
            text = read_file(file_dir)
            type = chain.invoke(text)
            print(type.strip())
            if "1" in type:
                print("111111111111111111111111111")
                template_prompt = residence_identification_template_prompt
                tagnames = residence_identification_tagnames
                name = "residence_identification_tagnames"
            elif "2" in type:
                print("222222222222222222")
                template_prompt = study_template_prompt
                tagnames = study_tagnames
                name = "study_tagnames"
            elif "3" in type:
                print("333333333333333333333")
                template_prompt = health_medical_template_prompt
                tagnames = health_and_medical_tagnames
                name = "health_and_medical_tagnames"
            elif "4" in type:
                print("44444444444444444444")
                template_prompt = vehicle_driver_template_prompt
                tagnames = vehicle_driver_tagnames
                name = "vehicle_driver_tagnames"
            elif "5" in type:
                print("55555555555555555555")
                template_prompt = job_template_prompt
                tagnames = job_tagnames
                name = "job_tagnames"
            else:
                template_prompt = residence_identification_template_prompt
                tagnames = residence_identification_tagnames
                name = "residence_identification_tagnames"
            prompt = PromptTemplate.from_template(template_prompt)
            chain = prompt | llm | StrOutputParser()
            try:
                response = chain.invoke({name: tagnames, "remaining_tag_names": remaining_tag_names, "form": text})
                write_file(response_dir, response)
            except Exception as e:
                print(e)
            print("End with: ", filename)

auto_generate_tag_names()

def replace_date(folder_dir = "Forms/Text/Input_test/Input/TagName"):
   for index, filename in enumerate(os.listdir(folder_dir)):
        if filename.endswith(".txt"):
            file_dir = folder_dir + '/' + filename
            response_dir = f'{folder_dir}1/' + filename
            text = read_file(file_dir)
            form = replaced_date_function(text)
            write_file(response_dir, form)

# replace_date("Forms\Text\Input_test\Label_Output_NDN")

def auto_identify_relationship(llm = llm, folder_dir = "Forms/Text/Input/Output/TagName", save_dir = "Forms/Text/Input/Output/", start = 0, end = 10):
    for index,filename in enumerate(os.listdir(folder_dir)[start:end]):
        if filename.endswith(".txt"):
            print("Start with: ", filename)
            file_dir = folder_dir + '/' + filename
            respones_dir = save_dir + '/Relationship/' + filename
            text = read_file(file_dir)
            prompt_parts2 = template_identify_relationship_prompt.format(form = text)
            response2 = llm.model.generate_content(prompt_parts2)
            write_file(respones_dir, response2.text)

