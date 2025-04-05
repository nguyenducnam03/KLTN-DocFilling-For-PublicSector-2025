create_residence_identification_form_prompt = """
# **Hướng dẫn tạo biểu mẫu cư trú và giấy tờ tùy thân**

Hãy tạo một biểu mẫu hành chính công (như tờ khai, giấy đăng ký, biên bản, đơn từ,...) trong đó mỗi trường dữ liệu phải rõ ràng, chính xác và dễ hiểu cho người dùng.

## I. Yêu cầu chung

1. Mỗi trường trong biểu mẫu phải gán với tagnames dưới dạng `userX_fieldname`, trong đó X là số thứ tự của người trong biểu mẫu (vd: `user1_full_name`, `user2_id_number`).

2. Nội dung của form phải liên kết chặt chẽ, các trường dữ liệu phải logic và phù hợp với nhau.

3. Form có thể áp dụng cho nhiều người, và nếu như vậy thì thông tin của các người trong form phải liên quan chặt chẽ (vd: thành viên gia đình, đồng nghiệp, ...).

## II. Cách tạo form

### II.1. Loại biểu mẫu

- Loại biểu mẫu (form_name): Loại biểu mẫu cần tạo (ví dụ: "Tờ khai Căn cước công dân", "Đơn xin tạm trú", "Giấy đăng ký xe", ...).

- Mục đích biểu mẫu (form_purpose): Mục đích của biểu mẫu (ví dụ: "Cấp mới", "Cấp lại", "Gia hạn", "Thay đổi thông tin", ...).

### II.2. Đối tượng sử dụng form

- Số lượng người (num_users): Số lượng người trong biểu mẫu (1, 2, hoặc nhiều người).

- Quan hệ giữa các người trong biểu mẫu (relationship_between_users): Quan hệ giữa các người trong biểu mẫu (ví dụ: "Thành viên gia đình", "Cùng công ty", "Bạn bè", ...).

### II.3. Thông tin thường có trong form (form_info)

**Thông tin cá nhân:** Mô tả thông tin cá nhân mà bạn cần có trong biểu mẫu, dưới đây sẽ la một số thông tin thường xuất hiện trong biểu mẫu:

- Họ và tên (userX_full_name): Họ và tên đầy đủ như trên giấy tờ tùy thân. Ví dụ: Nguyễn Văn A.

- Ngày tháng năm sinh (userX_dob_day, userX_dob_month, userX_dob_year hoặc userX_dob): Ví dụ: 15/08/1995.

- Giới tính (userX_gender): Chọn Nam, Nữ hoặc Khác.

- Quốc tịch (userX_nationality): Ví dụ: Việt Nam, Hoa Kỳ.

**Giấy tờ tùy thân:** Mô tả thông tin giấy tờ tùy thân mà bạn cần có trong biểu mẫu, dưới đây sẽ là một số thông tin thường xuất hiện trong biểu mẫu:

- Số CMND/CCCD (userX_id_number): Ví dụ: 001203456789.

- Ngày cấp CMND/CCCD (userX_id_issue_date): Có thể tách riêng userX_id_issue_day, userX_id_issue_month, userX_id_issue_year.

- Nơi cấp CMND/CCCD (userX_id_issue_place): Ví dụ: Cục Cảnh sát Quản lý Hành chính về Trật tự Xã hội.

- Số hộ chiếu (userX_passport_number): Ví dụ: C1234567.

- Ngày hết hạn hộ chiếu (userX_passport_expiry_date).

- Số thị thực (userX_visa_number): Ví dụ: V987654321.

- Ngày hết hạn thị thực (userX_visa_expiry_date).

**Địa chỉ cư trú (include_address):** Mô tả thông tin địa chỉ cư trú mà bạn cần có trong biểu mẫu, dưới đây sẽ là một số thông tin thường xuất hiện trong biểu mẫu:

- Địa chỉ thường trú (userX_permanent_address): Ví dụ: 456 Lê Lợi, TP Hà Nội.

- Địa chỉ hiện tại (userX_current_address): Ví dụ: 123 Nguyễn Trãi, Quận 1, TP Hồ Chí Minh.

**Thông tin liên hệ (include_contact):** Mô tả thông tin liên hệ mà bạn cần có trong biểu mẫu, dưới đây sẽ là một số thông tin thường xuất hiện trong biểu mẫu:

- Số điện thoại (userX_phone): Ví dụ: 0901234567.

- Email (userX_email): Ví dụ: nguyenvana@example.com.

**Thông tin bổ sung (include_additional_info):** Tùy theo nhu cầu, có thể thêm các thông tin khác nếu cần.

### II.4. Định dạng và phong cách biểu mẫu(form_format)

- Kiểu trình bày: Kiểu trình bày biểu mẫu (ví dụ: "Ngắn gọn", "Chi tiết", "Đơn giản", "Chuẩn theo quy định nhà nước").

- Giọng văn: Giọng văn (ví dụ: "Trang trọng", "Hành chính", "Dễ hiểu cho mọi đối tượng").

- Đánh số thứ tự: Có đánh số thứ tự các mục không? (Yes/No).

**Lưu ý:** Không trình bày biểu mẫu ở dạng bảng.

### II.5. Quy tắc logic giữa các trường

Liên kết thông tin giữa các người dùng : Các thông tin giữa các user có liên quan với nhau.


## Ví dụ:

### Ví dụ 1:
Input:
```
Hãy tạo một biểu mẫu hành chính công với các yêu cầu sau:
- **Tên biểu mẫu**: Đơn xin tạm trú
- **Mục đích**: Đăng ký tạm trú cho hộ gia đình
- **Số lượng người**: 4 người
- **Quan hệ giữa các người trong biểu mẫu**: Thành viên gia đình
- **Bao gồm các mục**: Thông tin cá nhân, Giấy tờ tùy thân(Chỉ có thông tin về căn cước công dân), 
                        Địa chỉ cư trú(chỉ lấy địa chỉ tạm trú)
- **Định dạng và phong cách biểu mẫu**: Chi tiết, Trang trọng, Không đánh số thứ tự
```
Output:
```
ĐƠN XIN TẠM TRÚ CHO HỘ GIA ĐÌNH

Kính gửi: [receiver]

Tôi tên là: [user1_full_name]
Ngày sinh: [user1_dob_day]/[user1_dob_month]/[user1_dob_year]
Giới tính: [user1_gender]Quốc tịch: [user1_nationality]
CMND/CCCD số: [user1_id_number]
Ngày cấp: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]
Nơi cấp: [user1_id_issue_place]
Địa chỉ tạm trú: [user1_current_address]
Lý do tạm trú: [user1_residence_reason]
Thời gian tạm trú: Từ ngày [user1_residence_start_day]/[user1_residence_start_month]/[user1_residence_start_year] đến ngày [user1_residence_end_day]/[user1_residence_end_month]/[user1_residence_end_year]

Thông tin các thành viên trong gia đình đi cùng:

Họ và tên: [user2_full_name], Ngày sinh: [user2_dob_day]/[user2_dob_month]/[user2_dob_year], CMND/CCCD số: [user2_id_number], Quan hệ: [user2_relationship]

Họ và tên: [user3_full_name], Ngày sinh: [user3_dob_day]/[user3_dob_month]/[user3_dob_year], CMND/CCCD số: [user3_id_number], Quan hệ: [user3_relationship]

Họ và tên: [user4_full_name], Ngày sinh: [user4_dob_day]/[user4_dob_month]/[user4_dob_year], CMND/CCCD số: [user4_id_number], Quan hệ: [user4_relationship]

Tôi cam kết chấp hành đúng các quy định của pháp luật về cư trú và hoàn toàn chịu trách nhiệm về nội dung kê khai.

Ngày [submission_day] tháng [submission_month] năm [submission_year]

Người làm đơn(Ký và ghi rõ họ tên)

[user1_full_name]
```

### Ví dụ 2:
Input:
```
Hãy tạo một biểu mẫu hành chính công với các yêu cầu sau:
- **Tên biểu mẫu**: Cấp đổi thẻ căn cước
- **Mục đích**: Cấp đổi CCCD do hư hỏng
- **Số lượng người**: 1 người
- **Quan hệ giữa các người trong biểu mẫu**: Không áp dụng
- **Bao gồm các mục**: Thông tin cá nhân(Ngày sinh lấy theo định dạng dob), Giấy tờ tùy thân (CMND/CCCD cũ và mới), Địa chỉ cư trú
- **Định dạng và phong cách biểu mẫu**: Chi tiết, Trang trọng, Đánh số thứ tự
```
Output:
```
ĐƠN ĐỀ NGHỊ CẤP ĐỔI THẺ CĂN CƯỚC CÔNG DÂN

Kính gửi: [receiver]

1. Họ và tên: [user1_full_name]
2. Ngày sinh: [user1_dob]
3. Giới tính: [user1_gender]
4. Quốc tịch: [user1_nationality]
5. CMND/CCCD cũ số: [user1_old_id_number]
6. Ngày cấp: [user1_old_id_issue_day]/[user1_old_id_issue_month]/[user1_old_id_issue_year]
7. Nơi cấp: [user1_old_id_issue_place]
8. Địa chỉ thường trú: [user1_permanent_address]
9. Địa chỉ hiện tại: [user1_current_address]
10. Lý do cấp đổi: [user1_id_change_reason]

Tôi cam kết các thông tin trên là đúng sự thật và chịu trách nhiệm trước pháp luật về nội dung kê khai. Kính đề nghị cơ quan có thẩm quyền xem xét và cấp đổi thẻ căn cước công dân cho tôi.

Ngày [submission_day] tháng [submission_month] năm [submission_year]

Người làm đơn(Ký và ghi rõ họ tên)

[user1_full_name]
```

## Input của tôi:
```
Hãy tạo một biểu mẫu hành chính công với các yêu cầu sau:
- **Tên biểu mẫu**: {form_name}
- **Mục đích**: {form_purpose}
- **Số lượng người**: {num_users} người
- **Quan hệ giữa các người trong biểu mẫu**: {relationship_between_users}
- **Bao gồm các mục**: {form_info}
- **Định dạng và phong cách biểu mẫu**: {form_format}
```

### Output mong muốn:
```
Tôi sẽ tạo biểu mẫu phù hợp dựa trên input của bạn. Chỉ tạo biểu mẫu, không kèm theo giải thích, hướng dẫn hoặc ghi chú.
```
"""

residence_indentification_data_generator_prompt = """
# **Prompt tạo dữ liệu đầu vào tự động**

Hãy tạo ra kết quả chứa các thông tin sau để tạo biểu mẫu hành chính công. Dữ liệu phải đa dạng và hợp lý theo từng loại biểu mẫu, dựa trên giá trị của biến **`form_name`** mà người dùng cung cấp.  

## **Thông tin cần có**  

### 1. **Loại biểu mẫu** (`form_name`)  
- Nhận giá trị từ input `{form_name}` do người dùng cung cấp.  

### 2. **Mục đích biểu mẫu** (`form_purpose`)  
- Các mục đích hợp lý theo loại biểu mẫu:  
  - **Hộ chiếu**: "Cấp mới", "Cấp lại", "Gia hạn", "Thay đổi thông tin".  
  - **Căn cước công dân**: "Cấp mới", "Cấp đổi", "Cấp lại do mất".  
  - **Tạm trú**: "Đăng ký mới", "Gia hạn tạm trú".  
- Nếu không có yêu cầu cụ thể, chọn mục đích phổ biến nhất cho loại biểu mẫu.  

### 3. **Số lượng người trong biểu mẫu** (`num_users`)  
Xác định số lượng user dựa vào {form_name}.
- **1 người** nếu biểu mẫu chỉ áp dụng cho cá nhân (ví dụ: Cấp hộ chiếu, căn cước công dân, tạm trú cá nhân).  
- **2 người** nếu biểu mẫu liên quan đến cả người nộp đơn và người giám hộ (ví dụ: Cấp hộ chiếu cho trẻ em dưới 14 tuổi).  
- **Nhiều người** nếu biểu mẫu áp dụng cho nhóm hoặc hộ gia đình (ví dụ: Đăng ký tạm trú cho cả hộ). 

### 4. **Quan hệ giữa các người trong biểu mẫu** (`relationship_between_users`)  
- Nếu `num_users = 1`, ghi là `"Không áp dụng"`.  
- Nếu `num_users > 1`, xác định quan hệ hợp lý:  
  - "Thành viên gia đình" (hộ gia đình).  
  - "Cùng công ty" (nhóm lao động).  
  - "Bạn bè", "Đồng nghiệp",... nếu phù hợp.  

### 5. **Thông tin thường xuất hiện trong biểu mẫu** (`form_info`)  
Xác định các trường thông tin hợp lý theo từng loại biểu mẫu:  
- **Thông tin cá nhân** (họ tên, ngày sinh, giới tính, quốc tịch).  
- **Giấy tờ tùy thân** (CMND/CCCD, hộ chiếu, thị thực nếu có).  
- **Địa chỉ cư trú** (thường trú, tạm trú).  
- **Thông tin liên hệ** (số điện thoại, email nếu cần).  
- **Thông tin bổ sung** (lý do xin cấp đổi, thời gian hiệu lực,...).  
- Nếu người dùng có yêu cầu riêng ({request}), phải phản ánh điều đó vào `form_info`.  

#### **Cách ghi dữ liệu**
- Nếu muốn sinh tất cả tagname trong một nhóm, chỉ cần ghi tên nhóm:  
  - `"Thông tin cá nhân"` (bao gồm họ tên, ngày sinh, giới tính,...).  
  - `"Giấy tờ tùy thân (chỉ CMND/CCCD)"` nếu chỉ muốn một phần.  
- Nếu `request` yêu cầu cụ thể (ví dụ: ngày sinh theo `userX_dob`), phải phản ánh vào output.  

### 6. **Định dạng biểu mẫu** (`form_format`)  
- Cách trình bày, giọng văn, cấu trúc:  
  - "Ngắn gọn", "Chi tiết".  
  - "Trang trọng", "Dễ hiểu".  
  - "Đánh số thứ tự", "Không đánh số thứ tự".  

---
## **Ví dụ đầu ra mong muốn**  
```
- 'form_name': 'Cấp hộ chiếu phổ thông cho trẻ dưới 14 tuôie',
- 'form_purpose': 'Cấp mới hộ chiếu',
- 'num_users': 1,
- 'relationship_between_users': 'Không áp dụng',
- 'form_info': 'Thông tin cá nhân(ngày sinh viết theo định dạng `userX_dob`), giấy tờ tùy thân (CMND/CCCD), địa chỉ cư trú(chỉ lấy địa chỉ thường trú), thông tin hộ chiếu cũ (nếu có)',
- 'form_format': 'Chi tiết, Trang trọng, Đánh số thứ tự'
```

---
## Input của tôi:
```
Tên form: {form_name}
Yêu cầu thêm về thông tin có trong form: {request}
```
## Output mong muốn:
```
Tôi sẽ tạo form phù hợp dựa trên input của bạn. Chỉ tạo biểu mẫu, không kèm theo giải thích, hướng dẫn hoặc ghi chú.
```
"""

create_study_form_prompt = """
# **Hướng dẫn tạo biểu mẫu học tập**

Hãy tạo một biểu mẫu hành chính trong lĩnh vực học tập (như đơn xin nhập học, biên bản học vụ, giấy xác nhận sinh viên,...) trong đó mỗi trường dữ liệu phải rõ ràng, chính xác và dễ hiểu cho người dùng.

## I. Yêu cầu chung

1. Mỗi trường trong biểu mẫu phải gán với tagnames dưới dạng `userX_fieldname`, trong đó X là số thứ tự của người trong biểu mẫu (vd: `user1_full_name`, `user2_student_id_number`).

2. Nội dung của form phải liên kết chặt chẽ, các trường dữ liệu phải logic và phù hợp với nhau.

3. Form có thể áp dụng cho nhiều người, và nếu như vậy thì thông tin của các người trong form phải liên quan chặt chẽ (vd: sinh viên cùng lớp, giáo viên và học sinh, ...).

## II. Cách tạo form

### II.1. Loại biểu mẫu

- **Loại biểu mẫu (form_name):** Loại biểu mẫu cần tạo (ví dụ: "Đơn xin nhập học", "Giấy xác nhận sinh viên", "Đơn xin hủy học phí", ...).

- **Mục đích biểu mẫu (form_purpose):** Mục đích của biểu mẫu (ví dụ: "Xác nhận thông tin sinh viên", "Đăng ký khóa học", "Xin hoàn trả học phí", ...).

### II.2. Đối tượng sử dụng form

- **Số lượng người (num_users):** Số lượng người trong biểu mẫu (1, 2, hoặc nhiều người).

- **Quan hệ giữa các người trong biểu mẫu (relationship_between_users):** Quan hệ giữa các người trong biểu mẫu (ví dụ: "Sinh viên cùng lớp", "Giáo viên - Học sinh", ...).

### II.3. Thông tin thường có trong form (form_info)

#### **Thông tin cá nhân:**
- Họ và tên (userX_full_name): Họ và tên đầy đủ như trên giấy tờ tùy thân. Ví dụ: Nguyễn Văn A.

- Ngày tháng năm sinh (userX_dob_day, userX_dob_month, userX_dob_year hoặc userX_dob): Ví dụ: 15/08/1995.

- Giới tính (userX_gender): Chọn Nam, Nữ hoặc Khác.

- Số CMND/CCCD (userX_id_number): Ví dụ: 001203456789.

- Ngày cấp CMND/CCCD (userX_id_issue_date): Có thể tách riêng userX_id_issue_day, userX_id_issue_month, userX_id_issue_year.

- Nơi cấp CMND/CCCD (userX_id_issue_place): Ví dụ: Cục Cảnh sát Quản lý Hành chính về Trật tự Xã hội.

- Số hộ chiếu (userX_passport_number): Ví dụ: C1234567.

- Ngày hết hạn hộ chiếu (userX_passport_expiry_date).

- Số thị thực (userX_visa_number): Ví dụ: V987654321.

- Ngày hết hạn thị thực (userX_visa_expiry_date).


#### **Thông tin học tập:**
- Tên trường (`userX_school`)
- Lớp (`userX_class`)
- Khóa học (`userX_course`)
- Mã số sinh viên (`userX_student_id_number`)
- Trình độ học vấn (`userX_education_level`)
- Năm học (`userX_school_year`)
- Học kỳ (`userX_semester`)
- Hiệu trưởng (`userX_school_principal`)
- Địa chỉ trường (`userX_school_address`)

#### **Thông tin bổ sung:**
- Quyết định liên quan (đi học, khen thưởng,...) (`userX_decision_number`, `userX_decision_day`, `userX_decision_month`, `userX_decision_year`)
- Cơ quan quản lý trực tiếp (`userX_organization`)
- Nội dung đề nghị (`userX_request_content`, `userX_reason`, `userX_suggestion`)

### II.4. Định dạng và phong cách biểu mẫu (form_format)

- Kiểu trình bày: "Ngắn gọn", "Chi tiết", "Chuẩn theo quy định nhà nước".
- Giọng văn: "Trang trọng", "Hành chính", "Dễ hiểu".
- Đánh số thứ tự các mục? (Yes/No).

Lưu ý:** Không trình bày biểu mẫu ở dạng bảng.

### II.5. Quy tắc logic giữa các trường

- Các thông tin của user phải liên quan và đồng bộ với nhau.



## Ví dụ:

### Ví dụ 1:
Input:
```
- **Loại biểu mẫu**: Thời gian học tập nước ngoài  
- **Mục đích**: Xác nhận thời gian học tập tại trường đại học ở nước ngoài  
- **Số lượng người**: 1 người  
- **Quan hệ giữa các người trong biểu mẫu**: Không áp dụng  
- **Bao gồm các mục**: Họ và tên, Ngày sinh, Giới tính, Quốc tịch, Số hộ chiếu, Trường đại học, Khóa học, Mã số sinh viên, Thời gian khóa học, Ngày tốt nghiệp, Kết quả xếp loại, Quyết định cử đi học, Cơ quan quản lý  
- **Định dạng và phong cách biểu mẫu**: Trang trọng, chuẩn theo quy định nhà nước  
```
Output:
```
XÁC NHẬN THỜI GIAN HỌC TẬP NƯỚC NGOÀI  

Kính gửi: [receiver]  

Tôi tên là: [user1_full_name]  
Ngày sinh: [user1_dob_day]/[user1_dob_month]/[user1_dob_year]  
Giới tính: [user1_gender]  
Quốc tịch: [user1_nationality]  
Số hộ chiếu: [user1_passport_number]  
Tên trường đại học: [user1_school]  
Khóa học: [user1_course]  
Mã số sinh viên: [user1_student_id_number]  
Thời gian khóa học: Từ ngày [user1_course_start_day]/[user1_course_start_month]/[user1_course_start_year]  
                       đến ngày [user1_course_end_day]/[user1_course_end_month]/[user1_course_end_year]  
Ngày tốt nghiệp: [user1_graduation_date]  
Kết quả xếp loại: [user1_study_result_rating]  

Quyết định cử đi học: Số [user1_study_decision_number], ngày [user1_study_decision_day]/[user1_study_decision_month]/[user1_study_decision_year]  
Cơ quan quản lý trực tiếp: [user1_organization]  

Tôi cam kết rằng thông tin kê khai trên là đúng sự thật và chịu trách nhiệm trước pháp luật.  

Ngày [submission_day] tháng [submission_month] năm [submission_year]  

Người làm đơn (Ký và ghi rõ họ tên)  

[user1_full_name]  

```

### Ví dụ 2:
Input:
```
Hãy tạo một biểu mẫu liên quan tới học tập với các yêu cầu sau:
- **Loại biểu mẫu**: Xin cấp học bổng chính sách
- **Mục đích**: Đề nghị cấp học bổng hỗ trợ sinh viên theo chính sách  
- **Số lượng người**: 1 người  
- **Quan hệ giữa các người trong biểu mẫu**: Không áp dụng  
- **Bao gồm các mục**: Thông tin cá nhân(Không cần nơi cấp CCCD), Thông tin học tập (Trường, khoa, khóa học, mã số sinh viên, kết quả học tập) , Quyết định cấp học bổng (Số quyết định, ngày ban hành, đơn vị cấp), Cam kết chấp hành quy định về học bổng  
- **Định dạng và phong cách biểu mẫu**: Trang trọng, chuẩn theo quy định nhà nước   
```
Output:
```
ĐƠN XIN CẤP HỌC BỔNG CHÍNH SÁCH  

Kính gửi: [receiver]  

Tôi tên là: [user1_full_name]  
Ngày sinh: [user1_dob_day]/[user1_dob_month]/[user1_dob_year]  
Giới tính: [user1_gender]  
Quốc tịch: [user1_nationality]  
CMND/CCCD số: [user1_id_number]  
Ngày cấp: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]  
Hiện đang là sinh viên tại: [user1_school]  
Khoa: [user1_faculty]  
Khóa học: [user1_course]  
Mã số sinh viên: [user1_student_id_number]  
Kết quả học tập: [user1_study_result_rating]  

Tôi làm đơn này để đề nghị cấp học bổng chính sách theo quyết định số [user1_study_decision_number], ban hành ngày [user1_study_decision_day]/[user1_study_decision_month]/[user1_study_decision_year] do [decision_issuer] cấp.  

Tôi cam kết sử dụng học bổng đúng mục đích, chấp hành các quy định của nhà trường và cơ quan cấp học bổng.  

Ngày [submission_day] tháng [submission_month] năm [submission_year]  

Người làm đơn (Ký và ghi rõ họ tên)  

[user1_full_name]  

```

## Input của tôi:
```
Hãy tạo một biểu mẫu liên quan tới học tập với các yêu cầu sau:
- **Loại biểu mẫu**: {form_name}
- **Mục đích**: {form_purpose}
- **Số lượng người**: {num_users} người
- **Quan hệ giữa các người trong biểu mẫu**: {relationship_between_users}
- **Bao gồm các mục**: {form_info}
- **Định dạng và phong cách biểu mẫu**: {form_format}
```

### Output mong muốn:
```
Tôi sẽ tạo biểu mẫu phù hợp dựa trên input của bạn. Chỉ tạo biểu mẫu, không kèm theo giải thích, hướng dẫn hoặc ghi chú.
```
"""

study_data_generator_prompt = """
# Prompt tạo dữ liệu đầu vào tự động  

Hãy tạo ra kết quả chứa các thông tin sau để tạo biểu mẫu liên quan đến học tập. Dữ liệu phải đa dạng và hợp lý theo từng loại biểu mẫu, dựa trên giá trị của biến **`form_name`** mà người dùng cung cấp.  

## Thông tin cần có  

### 1. Loại biểu mẫu (`form_name`)  
- Nhận giá trị từ input `{form_name}` do người dùng cung cấp.  

### 2. Mục đích biểu mẫu (`form_purpose`)  
- Các mục đích hợp lý theo loại biểu mẫu:  
  - **Xác nhận sinh viên**: "Xác nhận đang theo học", "Xác nhận tốt nghiệp", "Xác nhận miễn giảm học phí".  
  - **Học bổng**: "Xin cấp học bổng", "Gia hạn học bổng".  
  - **Chuyển trường**: "Xin chuyển trường", "Chuyển ngành học".  
  - **Hỗ trợ tài chính**: "Xin vay vốn sinh viên", "Xin miễn giảm học phí".  
- Nếu không có yêu cầu cụ thể, chọn mục đích phổ biến nhất cho loại biểu mẫu.  

### 3. Số lượng người trong biểu mẫu (`num_users`)  
Xác định số lượng user dựa vào `{form_name}`.  
- **1 người** nếu biểu mẫu chỉ áp dụng cho cá nhân (ví dụ: Xin học bổng, xác nhận sinh viên, xin vay vốn).  
- **2 người** nếu biểu mẫu liên quan đến cả sinh viên và người bảo hộ/người xác nhận (ví dụ: Đơn xin hỗ trợ tài chính có xác nhận của phụ huynh).  
- **Nhiều người** nếu biểu mẫu áp dụng cho nhóm sinh viên (ví dụ: Đăng ký lớp học nhóm).  

### 4. Quan hệ giữa các người trong biểu mẫu (`relationship_between_users`)  
- Nếu `num_users = 1`, ghi là `"Không áp dụng"`.  
- Nếu `num_users > 1`, xác định quan hệ hợp lý:  
  - "Phụ huynh - Sinh viên" (đối với đơn hỗ trợ tài chính).  
  - "Cùng lớp", "Cùng khóa học" (đối với đơn xin nhóm).  
  - "Giảng viên - Sinh viên" (đối với đơn xin xác nhận, hướng dẫn khóa luận).  

### 5. Thông tin thường xuất hiện trong biểu mẫu (`form_info`)  
Xác định các trường thông tin hợp lý theo từng loại biểu mẫu:  
- **Thông tin cá nhân** (họ tên, ngày sinh, giới tính, mã số sinh viên).  
- **Thông tin học tập** (trường, khoa, khóa học, kết quả học tập, năm học).  
- **Thông tin học bổng** (loại học bổng, quyết định cấp học bổng).  
- **Thông tin tài chính** (lý do xin miễn giảm học phí, số tiền hỗ trợ).  
- **Xác nhận của tổ chức liên quan** (hiệu trưởng, giảng viên hướng dẫn, cơ quan tài trợ).  
- Nếu người dùng có yêu cầu riêng ({request}), phải phản ánh điều đó vào `form_info`.  

#### Cách ghi dữ liệu  
- Nếu muốn sinh tất cả tagname trong một nhóm, chỉ cần ghi tên nhóm:  
  - `"Thông tin cá nhân"` (bao gồm họ tên, ngày sinh, giới tính, mã số sinh viên).  
  - `"Thông tin học bổng (chỉ loại học bổng và quyết định cấp)"` nếu chỉ cần một phần.  
- Nếu `request` yêu cầu cụ thể (ví dụ: mã số sinh viên phải hiển thị dưới dạng `userX_student_id_number`), phải phản ánh vào output.  

### 6. Định dạng biểu mẫu (`form_format`)  
- Cách trình bày, giọng văn, cấu trúc:  
  - "Ngắn gọn", "Chi tiết".  
  - "Trang trọng", "Dễ hiểu".  
  - "Đánh số thứ tự", "Không đánh số thứ tự".  

---  
## Ví dụ đầu ra mong muốn
'''
- 'form_name': 'Xin cấp học bổng chính sách',
- 'form_purpose': 'Xin học bổng hỗ trợ tài chính',
- 'num_users': 1,
- 'relationship_between_users': 'Không áp dụng',
- 'form_info': 'Thông tin cá nhân, thông tin học tập (trường, khoa, mã số sinh viên, kết quả học tập), thông tin học bổng (loại học bổng, quyết định cấp)',
- 'form_format': 'Chi tiết, Trang trọng, Đánh số thứ tự'
'''

---
## Input của tôi:
```
Tên form: {form_name}
Yêu cầu thêm về thông tin có trong form: {request}
```
## Output mong muốn:
```
Tôi sẽ tạo form phù hợp dựa trên input của bạn. Chỉ tạo biểu mẫu, không kèm theo giải thích, hướng dẫn hoặc ghi chú.
```
"""

create_health_and_medical_form_prompt = """" 
# **Hướng dẫn tạo biểu mẫu y tế**

Hãy tạo một biểu mẫu y tế (như tờ khai sức khỏe, đơn xin khám chữa bệnh, hồ sơ bệnh án, giấy chứng nhận sức khỏe,...) trong đó mỗi trường dữ liệu phải rõ ràng, chính xác và dễ hiểu cho người dùng.

## I. Yêu cầu chung

1. Mỗi trường trong biểu mẫu phải gán với tagnames dưới dạng `userX_fieldname`, trong đó X là số thứ tự của người trong biểu mẫu (vd: `user1_full_name`, `user2_id_number`).

2. Nội dung của form phải liên kết chặt chẽ, các trường dữ liệu phải logic và phù hợp với nhau.

3. Form có thể áp dụng cho nhiều người, và nếu như vậy thì thông tin của các người trong form phải liên quan chặt chẽ (vd: thành viên gia đình, đồng nghiệp, ...).

## II. Cách tạo form

### II.1. Loại biểu mẫu

- **Loại biểu mẫu (`form_name`)**: Loại biểu mẫu cần tạo (ví dụ: "Tờ khai y tế", "Giấy chứng nhận sức khỏe", "Đơn xin khám bệnh", ...).

- **Mục đích biểu mẫu (`form_purpose`)**: Mục đích của biểu mẫu (ví dụ: "Khám chữa bệnh", "Cấp giấy chứng nhận sức khỏe", "Bảo hiểm y tế", ...).

### II.2. Đối tượng sử dụng form

- **Số lượng người (`num_users`)**: Số lượng người trong biểu mẫu (1, 2, hoặc nhiều người).

- **Quan hệ giữa các người trong biểu mẫu (`relationship_between_users`)**: Quan hệ giữa các người trong biểu mẫu (ví dụ: "Thành viên gia đình", "Cùng công ty", "Bạn bè", ...).

### II.3. Thông tin thường có trong form (`form_info`)

#### **Thông tin cá nhân**
- **Họ và tên (`userX_full_name`)**: Họ và tên đầy đủ. Ví dụ: Nguyễn Văn A.
- **Ngày tháng năm sinh (`userX_dob_day`, `userX_dob_month`, `userX_dob_year` hoặc `userX_dob`)**: Ví dụ: 15/08/1995.
- **Giới tính (`userX_gender`)**: Chọn Nam, Nữ hoặc Khác.
- **Quốc tịch (`userX_nationality`)**: Ví dụ: Việt Nam, Hoa Kỳ.

#### **Thông tin giấy tờ**
- **Số CMND/CCCD (`userX_id_number`)**: Ví dụ: 001203456789.
- **Ngày cấp CMND/CCCD (`userX_id_issue_date`)**: Có thể tách riêng `userX_id_issue_day`, `userX_id_issue_month`, `userX_id_issue_year`.
- **Nơi cấp CMND/CCCD (`userX_id_issue_place`)**: Ví dụ: Cục Cảnh sát Quản lý Hành chính về Trật tự Xã hội.
- **Số bảo hiểm xã hội (`userX_social_insurance_number`)**.
- **Số thẻ bảo hiểm y tế (`userX_health_insurance_card_number`)**.
- **Nơi đăng ký bảo hiểm y tế (`userX_health_insurance_registration_place`)**.

#### **Địa chỉ cư trú (`include_address`)**
- **Địa chỉ thường trú (`userX_permanent_address`)**: Ví dụ: 456 Lê Lợi, TP Hà Nội.
- **Địa chỉ hiện tại (`userX_current_address`)**: Ví dụ: 123 Nguyễn Trãi, Quận 1, TP Hồ Chí Minh.

#### **Thông tin liên hệ (`include_contact`)**
- **Số điện thoại (`userX_phone`)**: Ví dụ: 0901234567.
- **Email (`userX_email`)**: Ví dụ: nguyenvana@example.com.

#### **Thông tin y tế**
- **Chiều cao (`userX_height`)**: Đơn vị cm. Ví dụ: 170 cm.
- **Cân nặng (`userX_weight`)**: Đơn vị kg. Ví dụ: 65 kg.
- **Nhóm máu (`userX_blood_type`)**: Ví dụ: A, B, AB, O.
- **Tiền sử bệnh lý (`userX_medical_history`)**: Ví dụ: "Tiểu đường, Cao huyết áp".
- **Dị ứng (`userX_allergy`)**: Ghi rõ loại dị ứng (nếu có).
- **Loại thuốc đang sử dụng (`userX_medication`)**: Danh sách các loại thuốc người dùng đang uống.
- **Bệnh viện/Phòng khám đăng ký (`userX_registered_hospital`)**.

#### **Thông tin bổ sung (`include_additional_info`)**
- **Tên phụ huynh/người bảo hộ (`userX_parent_name`)**: Áp dụng cho trẻ em.
- **Nghề nghiệp (`userX_occupation`)**: Nghề nghiệp hiện tại của người dùng.
- **Lý do khám bệnh (`userX_reason`)**: Ví dụ: "Đau đầu kéo dài", "Khám sức khỏe định kỳ".
- **Yêu cầu cụ thể (`userX_request_content`)**: Nội dung yêu cầu, nếu có.

### II.4. Định dạng và phong cách biểu mẫu (`form_format`)

- **Kiểu trình bày**: Kiểu trình bày biểu mẫu (ví dụ: "Ngắn gọn", "Chi tiết", "Đơn giản", "Chuẩn theo quy định nhà nước").
- **Giọng văn**: Giọng văn (ví dụ: "Trang trọng", "Hành chính", "Dễ hiểu cho mọi đối tượng").
- **Đánh số thứ tự**: Có đánh số thứ tự các mục không? (Yes/No).

**Lưu ý:** Không trình bày biểu mẫu ở dạng bảng.

### II.5. Quy tắc logic giữa các trường

- **Liên kết thông tin giữa các người dùng**: Các thông tin giữa các user có liên quan với nhau (vd: cùng hộ khẩu, cùng công ty,...).
- **Thông tin giấy tờ phải hợp lệ**: CMND/CCCD phải có đủ 12 chữ số, ngày tháng hợp lệ.
- **Thông tin bảo hiểm phải phù hợp**: Nếu có số bảo hiểm xã hội thì cũng phải có nơi đăng ký bảo hiểm y tế.


-----
## Ví dụ:

Ví dụ 1:
Input:
```
- **Loại biểu mẫu**: Tờ khai bảo hiểm y tế  
- **Mục đích**: Đăng ký bảo hiểm y tế  
- **Số lượng người**: 1 người  
- **Quan hệ giữa các người trong biểu mẫu**: Không áp dụng
- **Bao gồm các mục**: Thông tin cá nhân, Giấy tờ tùy thân(CCCD), địa chỉ thường trú, thông tin bảo hiểm y tế, thông tin liên hệ
- **Định dạng và phong cách biểu mẫu**:  Chi tiết, trang trọng, Không đánh số thứ tự
```
Output:
```
TỜ KHAI BẢO HIỂM Y TẾ  

Kính gửi: [receiver]  

Tôi tên là: [user1_full_name]  
Ngày sinh: [user1_dob_day]/[user1_dob_month]/[user1_dob_year]  
Giới tính: [user1_gender]  
Quốc tịch: [user1_nationality]  
Số CCCD: [user1_id_number]  
Ngày cấp: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]  
Nơi cấp: [user1_id_issue_place]  
Số bảo hiểm xã hội: [user1_social_insurance_number]  
Số thẻ bảo hiểm y tế: [user1_health_insurance_card_number]  
Nơi đăng ký bảo hiểm y tế: [user1_health_insurance_registration_place]  
Địa chỉ thường trú: [user1_permanent_address]  
Số điện thoại: [user1_phone]  
Email: [user1_email]  
Tiền sử bệnh lý: [user1_medical_history]  
Dị ứng: [user1_allergy]  
Bệnh viện/Phòng khám đăng ký: [user1_registered_hospital]  

Yêu cầu cụ thể: [user1_request_content]  

Tôi cam kết rằng thông tin kê khai trên là đúng sự thật và chịu trách nhiệm trước pháp luật.  

Ngày [submission_day] tháng [submission_month] năm [submission_year]  

Người khai (Ký và ghi rõ họ tên)  

[user1_full_name]  

```

Ví dụ 2:
Input:
```
- **Loại biểu mẫu**: Khám giám định để được hưởng BHXH một lần  
- **Mục đích**: Xác nhận tình trạng sức khỏe để hưởng BHXH một lần  
- **Số lượng người**: 1 người  
- **Quan hệ giữa các người trong biểu mẫu**: Không áp dụng  
- **Bao gồm các mục**: Thông tin cá nhân(Ngày sinh viết dưới dạng dob), Giấy tờ tùy thân (CCCD), địa chỉ thường trú, thông tin bảo hiểm y tế, thông tin liên hệ, lý do khám giám định  
- **Định dạng và phong cách biểu mẫu**: Chi tiết, trang trọng, Không đánh số thứ tự  
```
Output:
```
KHÁM GIÁM ĐỊNH ĐỂ ĐƯỢC HƯỞNG BHXH MỘT LẦN  

Kính gửi: [receiver]  

Tôi tên là: [user1_full_name]  
Ngày sinh: [user1_dob]
Giới tính: [user1_gender]  
Quốc tịch: [user1_nationality]  
Số CCCD: [user1_id_number]  
Ngày cấp: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]  
Nơi cấp: [user1_id_issue_place]  
Số bảo hiểm xã hội: [user1_social_insurance_number]  
Nơi đăng ký bảo hiểm y tế: [user1_health_insurance_registration_place]  
Địa chỉ tạm trú: [user1_current_address]  
Số điện thoại: [user1_phone]  
Email: [user1_email]  
Bệnh viện/Phòng khám đăng ký: [user1_registered_hospital]  

Lý do khám giám định: [user1_medical_assessment_reason]  
Yêu cầu cụ thể: [user1_request_content]  

Tôi cam kết rằng thông tin kê khai trên là đúng sự thật và chịu trách nhiệm trước pháp luật.  

Ngày [submission_day] tháng [submission_month] năm [submission_year]  

Người khai (Ký và ghi rõ họ tên)  

[user1_full_name]  

```

## Input của tôi:
```
Hãy tạo một biểu mẫu liên quan tới học tập với các yêu cầu sau:
- **Loại biểu mẫu**: {form_name}
- **Mục đích**: {form_purpose}
- **Số lượng người**: {num_users} người
- **Quan hệ giữa các người trong biểu mẫu**: {relationship_between_users}
- **Bao gồm các mục**: {form_info}
- **Định dạng và phong cách biểu mẫu**: {form_format}
```

### Output mong muốn:
```
Tôi sẽ tạo biểu mẫu phù hợp dựa trên input của bạn. Chỉ tạo biểu mẫu, không kèm theo giải thích, hướng dẫn hoặc ghi chú.
```

"""

health_data_generator_prompt = """
# Prompt tạo dữ liệu đầu vào tự động

Hãy tạo ra kết quả chứa các thông tin sau để tạo **biểu mẫu y tế và sức khỏe**. Dữ liệu phải đa dạng và hợp lý theo từng loại biểu mẫu, dựa trên giá trị của biến **`form_name`** mà người dùng cung cấp.

---

## Thông tin cần có

### 1. Loại biểu mẫu (`form_name`)
- Nhận giá trị từ input `{form_name}` do người dùng cung cấp.

### 2. Mục đích biểu mẫu (`form_purpose`)
- Các mục đích hợp lý theo loại biểu mẫu:
  - **Khám sức khỏe định kỳ**: "Xác nhận tình trạng sức khỏe", "Theo dõi sức khỏe học sinh".
  - **Xin nghỉ học do bệnh**: "Xin phép nghỉ học có lý do sức khỏe", "Báo cáo điều trị ngoại trú".
  - **Yêu cầu hỗ trợ y tế**: "Xin hỗ trợ y tế đặc biệt", "Đăng ký dịch vụ y tế học đường".
  - **Tự khai y tế**: "Khai báo y tế định kỳ", "Bổ sung thông tin dịch tễ".
- Nếu không có yêu cầu cụ thể, chọn mục đích phổ biến nhất cho loại biểu mẫu.

### 3. Số lượng người trong biểu mẫu (`num_users`)
Xác định số lượng user dựa vào `{form_name}`.
- **1 người** nếu biểu mẫu chỉ áp dụng cho cá nhân (ví dụ: xin nghỉ học, khám sức khỏe).
- **2 người** nếu biểu mẫu cần xác nhận từ phụ huynh hoặc bác sĩ (ví dụ: đơn xin nghỉ có xác nhận y tế).
- **Nhiều người** nếu biểu mẫu dùng trong nhóm, tập thể (ví dụ: khảo sát y tế lớp học).

### 4. Quan hệ giữa các người trong biểu mẫu (`relationship_between_users`)
- Nếu `num_users = 1`, ghi là `"Không áp dụng"`.
- Nếu `num_users > 1`, xác định quan hệ hợp lý:
  - "Phụ huynh - Học sinh" (đơn nghỉ học do bệnh, đơn xin hỗ trợ y tế).
  - "Bác sĩ - Học sinh" (giấy xác nhận tình trạng sức khỏe).
  - "Cùng lớp", "Cùng ký túc xá" (trong các biểu mẫu kiểm tra dịch tễ, y tế cộng đồng).

### 5. Thông tin thường xuất hiện trong biểu mẫu (`form_info`)
Xác định các trường thông tin hợp lý theo từng loại biểu mẫu:
- **Thông tin cá nhân** (họ tên, ngày sinh, giới tính, mã số sinh viên/học sinh).
- **Thông tin y tế** (tiền sử bệnh, triệu chứng, chẩn đoán, thời gian điều trị, loại hỗ trợ y tế).
- **Thông tin xác nhận** (ý kiến phụ huynh, xác nhận của bác sĩ, xác nhận từ nhà trường).
- **Thông tin dịch tễ** (lịch sử tiếp xúc, khai báo vùng dịch, thời gian cách ly).
- Nếu người dùng có yêu cầu riêng (`{request}`), phải phản ánh điều đó vào `form_info`.

> **Cách ghi dữ liệu**
> - Nếu muốn sinh tất cả tagname trong một nhóm, chỉ cần ghi tên nhóm:
>   - `"Thông tin cá nhân"` (bao gồm họ tên, ngày sinh, giới tính, mã số sinh viên).
>   - `"Thông tin y tế (triệu chứng và chẩn đoán)"` nếu chỉ cần một phần.

### 6. Định dạng biểu mẫu (`form_format`)
- Cách trình bày, giọng văn, cấu trúc:
  - "Ngắn gọn", "Chi tiết".
  - "Trang trọng", "Dễ hiểu".
  - "Đánh số thứ tự", "Không đánh số thứ tự".

---

## Ví dụ đầu ra mong muốn
```
- 'form_name': 'Giấy xác nhận tình trạng sức khỏe',
- 'form_purpose': 'Xác nhận tình trạng sức khỏe',
- 'num_users': 2,
- 'relationship_between_users': 'Bác sĩ - Học sinh',
- 'form_info': 'Thông tin cá nhân, thông tin y tế (triệu chứng, chẩn đoán, thời gian điều trị), thông tin xác nhận (ý kiến bác sĩ)',
- 'form_format': 'Chi tiết, Trang trọng, Đánh số thứ tự'

---
## Input của tôi:
```
Tên form: {form_name}
Yêu cầu thêm về thông tin có trong form: {request}
```
## Output mong muốn:
```
Tôi sẽ tạo form phù hợp dựa trên input của bạn. Chỉ tạo biểu mẫu, không kèm theo giải thích, hướng dẫn hoặc ghi chú.
```
"""

create_vehicle_driver_form_prompt = """`
# **Hướng dẫn tạo biểu mẫu Phương tiện và Người lái**

Hãy tạo một biểu mẫu liên quan đến phương tiện và người lái (ví dụ: đơn xin cấp lại giấy phép lái xe, hồ sơ đăng ký phương tiện, xác nhận thông tin xe,...) với các trường dữ liệu rõ ràng, hợp lệ và phù hợp với thực tiễn.

## I. Yêu cầu chung

1. Mỗi trường dữ liệu phải gắn tagname theo định dạng `userX_fieldname`, trong đó X là số thứ tự của người trong biểu mẫu (vd: `user1_full_name`, `user1_driving_license_number`).

2. Nội dung biểu mẫu cần logic, có liên kết giữa người dùng và thông tin phương tiện (vd: người đứng tên đăng ký xe, người điều khiển xe...).

3. Nếu biểu mẫu có nhiều người thì thông tin giữa họ phải có mối quan hệ hợp lý như: chủ xe – người được ủy quyền, đồng sở hữu, thành viên gia đình,...

---

## II. Cách tạo form

### II.1. Loại biểu mẫu

- **Loại biểu mẫu (`form_name`)**: Ví dụ: "Đơn xin cấp lại giấy phép lái xe", "Tờ khai đăng ký xe ô tô", "Đơn xác nhận thông tin phương tiện", ...

- **Mục đích biểu mẫu (`form_purpose`)**: Ví dụ: "Cấp lại giấy phép do mất", "Đăng ký phương tiện mới", "Xác nhận thông tin phương tiện cho giao dịch dân sự",...

---

### II.2. Đối tượng sử dụng form

- **Số lượng người (`num_users`)**: Số người tham gia trong biểu mẫu (1, 2 hoặc nhiều).
  - 1 người: chủ phương tiện.
  - 2 người: chủ xe và người được ủy quyền.
  - Nhiều người: đồng sở hữu, công ty giao xe cho nhiều lái xe,…

- **Quan hệ giữa các người trong biểu mẫu (`relationship_between_users`)**: Ví dụ: "Chủ xe - Người điều khiển", "Cùng hộ gia đình", "Đồng nghiệp", "Người ủy quyền - Người được ủy quyền".

---

### II.3. Thông tin thường có trong form (`form_info`)

#### **Thông tin cá nhân**
- `userX_full_name`
- `userX_dob_day`, `userX_dob_month`, `userX_dob_year`
- `userX_gender`
- `userX_nationality`
- `userX_id_number`
- `userX_id_issue_day`, `userX_id_issue_month`, `userX_id_issue_year`
- `userX_id_issue_place`

#### **Thông tin hộ chiếu (nếu có)**
- `userX_passport_number`
- `userX_passport_issue_day`, `userX_passport_issue_month`, `userX_passport_issue_year`
- `userX_passport_issue_place`

#### **Thông tin giấy phép lái xe**
- `userX_driving_license_number`
- `userX_driving_license_category`
- `userX_driving_license_issue_day`, `userX_driving_license_issue_month`, `userX_driving_license_issue_year`
- `userX_driving_license_issuer`

#### **Thông tin liên hệ**
- `userX_permanent_address`
- `userX_current_address`
- `userX_phone`
- `userX_email`

#### **Thông tin phương tiện**
- `userX_vehicle_chassis_number`
- `userX_vehicle_engine_number1`, `userX_vehicle_engine_number2`
- `userX_vehicle_brand`
- `userX_vehicle_color`
- `userX_vehicle_registration_number`

#### **Thông tin thuế và hải quan**
- `userX_tax_invoice_number`
- `userX_tax_declaration_code_issuing_agency`
- `userX_electronic_customs_declaration_number_issuing_agency`

#### **Giấy phép kinh doanh vận tải (nếu là phương tiện kinh doanh)**
- `userX_transport_license_issue_day`, `userX_transport_license_issue_month`, `userX_transport_license_issue_year`
- `userX_transport_license_issue_place`

#### **Thông tin yêu cầu**
- `userX_request_content`
- `userX_reason`

---

### II.4. Định dạng và phong cách biểu mẫu (`form_format`)

- **Kiểu trình bày**: Ví dụ: "Chi tiết", "Ngắn gọn", "Theo mẫu cơ quan giao thông",...
- **Giọng văn**: Ví dụ: "Trang trọng", "Hành chính", "Phù hợp quy chuẩn Nhà nước".
- **Đánh số thứ tự**: Có hoặc Không (Yes/No).

---

### II.5. Quy tắc logic giữa các trường

- **Tính hợp lệ của thông tin giấy tờ**: Số CMND/CCCD phải đủ độ dài, ngày tháng hợp lệ.
- **Phù hợp giữa giấy phép lái xe và mục đích**: Nếu xin cấp lại bằng hạng B2 thì thông tin phải phản ánh đúng loại phương tiện liên quan.
- **Thông tin phương tiện phải khớp nhau**: Số khung – số máy – biển số không được mâu thuẫn.
- **Liên kết giữa người và xe**: Người điều khiển phải có GPLX hợp lệ cho phương tiện tương ứng.

---

**Lưu ý:** Không trình bày biểu mẫu ở dạng bảng.

---

## Ví dụ:

Ví dụ 1:
Input:
```
- **Loại biểu mẫu**: Tờ khai đăng ký xe ô tô  
- **Mục đích**: Đăng ký xe ô tô cá nhân mới  
- **Số lượng người**: 1 người  
- **Quan hệ giữa các người trong biểu mẫu**: Không áp dụng  
- **Bao gồm các mục**: Thông tin cá nhân, Giấy tờ tùy thân(CCCD), địa chỉ thường trú, thông tin phương tiện, thông tin liên hệ  
- **Định dạng và phong cách biểu mẫu**: Chi tiết, trang trọng, Không đánh số thứ tự  
```
Ouput:
```
TỜ KHAI ĐĂNG KÝ XE Ô TÔ  

Kính gửi: [receiver]  

Tôi tên là: [user1_full_name]  
Ngày sinh: [user1_dob_day]/[user1_dob_month]/[user1_dob_year]  
Giới tính: [user1_gender]  
Quốc tịch: [user1_nationality]  
Số CCCD: [user1_id_number]  
Ngày cấp: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]  
Nơi cấp: [user1_id_issue_place]  
Địa chỉ thường trú: [user1_permanent_address]  
Số điện thoại: [user1_phone]  
Email: [user1_email]  

Thông tin phương tiện:  
- Loại xe: [user1_vehicle_type]  
- Nhãn hiệu: [user1_vehicle_brand]  
- Số loại: [user1_vehicle_model]  
- Màu sơn: [user1_vehicle_color]  
- Số máy: [user1_engine_number]  
- Số khung: [user1_chassis_number]  
- Năm sản xuất: [user1_vehicle_year]  
- Nơi sản xuất: [user1_vehicle_origin]  

Yêu cầu cụ thể: [user1_request_content]  

Tôi cam kết rằng thông tin kê khai trên là đúng sự thật và chịu trách nhiệm trước pháp luật.  

Ngày [submission_day] tháng [submission_month] năm [submission_year]  

Người khai (Ký và ghi rõ họ tên)  

[user1_full_name]  

```

Ví dụ 2:
Input:
```
- **Loại biểu mẫu**: Đơn đề nghị cấp lại giấy phép lái xe  
- **Mục đích**: Cấp lại GPLX do mất  
- **Số lượng người**: 1 người  
- **Quan hệ giữa các người trong biểu mẫu**: Không áp dụng  
- **Bao gồm các mục**: Thông tin cá nhân, CCCD, địa chỉ cư trú, thông tin giấy phép lái xe cũ, lý do cấp lại, thông tin liên hệ  
- **Định dạng và phong cách biểu mẫu**: Chi tiết, trang trọng, Không đánh số thứ tự  
```
Ouput:
```
ĐƠN ĐỀ NGHỊ CẤP LẠI GIẤY PHÉP LÁI XE  

Kính gửi: [receiver]  

Tôi tên là: [user1_full_name]  
Ngày sinh: [user1_dob_day]/[user1_dob_month]/[user1_dob_year]  
Giới tính: [user1_gender]  
Quốc tịch: [user1_nationality]  
Số CCCD: [user1_id_number]  
Ngày cấp: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]  
Nơi cấp: [user1_id_issue_place]  
Địa chỉ thường trú: [user1_permanent_address]  
Địa chỉ hiện tại: [user1_current_address]  
Số điện thoại: [user1_phone]  
Email: [user1_email]  

Thông tin giấy phép lái xe cũ:  
- Số GPLX: [user1_old_license_number]  
- Hạng bằng lái: [user1_license_class]  
- Ngày cấp: [user1_old_license_issue_day]/[user1_old_license_issue_month]/[user1_old_license_issue_year]  
- Cơ quan cấp: [user1_old_license_issuer]  

Lý do đề nghị cấp lại: [user1_license_reissue_reason]  
Yêu cầu cụ thể: [user1_request_content]  

Tôi cam kết rằng thông tin kê khai trên là đúng sự thật và chịu trách nhiệm trước pháp luật.  

Ngày [submission_day] tháng [submission_month] năm [submission_year]  

Người khai (Ký và ghi rõ họ tên)  

[user1_full_name]  

```

## Input của tôi:
```
Hãy tạo một biểu mẫu liên quan tới học tập với các yêu cầu sau:
- **Loại biểu mẫu**: {form_name}
- **Mục đích**: {form_purpose}
- **Số lượng người**: {num_users} người
- **Quan hệ giữa các người trong biểu mẫu**: {relationship_between_users}
- **Bao gồm các mục**: {form_info}
- **Định dạng và phong cách biểu mẫu**: {form_format}
```

### Output mong muốn:
```
Tôi sẽ tạo biểu mẫu phù hợp dựa trên input của bạn. Chỉ tạo biểu mẫu, không kèm theo giải thích, hướng dẫn hoặc ghi chú.
```
"""

vehicle_driver_data_generator_prompt = """
# Prompt tạo dữ liệu đầu vào tự động

Hãy tạo ra kết quả chứa các thông tin sau để tạo **biểu mẫu phương tiện và người lái**. Dữ liệu phải đa dạng và hợp lý theo từng loại biểu mẫu, dựa trên giá trị của biến **`form_name`** mà người dùng cung cấp.

---

## Thông tin cần có

### 1. Loại biểu mẫu (`form_name`)
- Nhận giá trị từ input `{form_name}` do người dùng cung cấp.

### 2. Mục đích biểu mẫu (`form_purpose`)
- Các mục đích hợp lý theo loại biểu mẫu:
  - **Cấp phép và đăng ký**: "Đăng ký xe mới", "Gia hạn giấy phép lái xe", "Đăng ký biển số tạm thời".
  - **Xác nhận phương tiện**: "Xác nhận quyền sở hữu xe", "Xác nhận thông tin phương tiện".
  - **Đăng ký sử dụng phương tiện**: "Xin sử dụng xe công", "Đăng ký xe đưa đón học sinh".
  - **Bảo hiểm và kiểm định**: "Đăng ký kiểm định an toàn", "Xác nhận tham gia bảo hiểm bắt buộc".
- Nếu không có yêu cầu cụ thể, chọn mục đích phổ biến nhất cho loại biểu mẫu.

### 3. Số lượng người trong biểu mẫu (`num_users`)
Xác định số lượng user dựa vào `{form_name}`:
- **1 người** nếu biểu mẫu chỉ liên quan đến chủ xe hoặc người điều khiển phương tiện.
- **2 người** nếu biểu mẫu có cả chủ xe và người sử dụng (ví dụ: xe cho mượn, xe công ty).
- **Nhiều người** nếu biểu mẫu đăng ký phương tiện cho nhóm hoặc tổ chức (ví dụ: xe đưa đón tập thể).

### 4. Quan hệ giữa các người trong biểu mẫu (`relationship_between_users`)
- Nếu `num_users = 1`, ghi là `"Không áp dụng"`.
- Nếu `num_users > 1`, xác định quan hệ hợp lý:
  - "Chủ xe - Người sử dụng"
  - "Người đại diện - Lái xe"
  - "Thành viên cùng tổ chức"

### 5. Thông tin thường xuất hiện trong biểu mẫu (`form_info`)
Xác định các trường thông tin hợp lý theo từng loại biểu mẫu:
- **Thông tin cá nhân** (họ tên, ngày sinh, số CCCD/CMND, địa chỉ, mã số bằng lái).
- **Thông tin phương tiện** (loại xe, biển số, số khung, số máy, ngày đăng ký).
- **Thông tin lái xe** (hạng giấy phép, thời hạn bằng lái, đơn vị cấp).
- **Thông tin đăng ký/bảo hiểm** (loại hình bảo hiểm, thời hạn bảo hiểm, nơi đăng kiểm).
- **Xác nhận của cơ quan chức năng** (chữ ký xác nhận, con dấu, thông tin kiểm định).
- Nếu người dùng có yêu cầu riêng (`{request}`), phải phản ánh điều đó vào `form_info`.

> **Cách ghi dữ liệu**
> - Nếu muốn sinh tất cả tagname trong một nhóm, chỉ cần ghi tên nhóm:
>   - `"Thông tin phương tiện"`
>   - `"Thông tin lái xe"`
> - Nếu `{request}` yêu cầu cụ thể (ví dụ: biển số xe cần định dạng `XX-123.45`), phải phản ánh vào output.

### 6. Định dạng biểu mẫu (`form_format`)
- Cách trình bày, giọng văn, cấu trúc:
  - "Ngắn gọn", "Chi tiết"
  - "Trang trọng", "Dễ hiểu"
  - "Đánh số thứ tự", "Không đánh số thứ tự"

---

## Ví dụ đầu ra mong muốn

```
- 'form_name': 'Đơn xin đăng ký xe cá nhân',
- 'form_purpose': 'Đăng ký xe mới',
- 'num_users': 1,
- 'relationship_between_users': 'Không áp dụng',
- 'form_info': 'Thông tin cá nhân, thông tin phương tiện (loại xe, số khung, số máy, biển số), thông tin đăng ký/bảo hiểm (loại hình bảo hiểm, thời hạn, nơi đăng kiểm)',
- 'form_format': 'Chi tiết, Trang trọng, Đánh số thứ tự'


---
## Input của tôi:
```
Tên form: {form_name}
Yêu cầu thêm về thông tin có trong form: {request}
```
## Output mong muốn:
```
Tôi sẽ tạo form phù hợp dựa trên input của bạn. Chỉ tạo biểu mẫu, không kèm theo giải thích, hướng dẫn hoặc ghi chú.
```
"""

create_job_form_prompt = """
# **Hướng dẫn tạo biểu mẫu Việc làm**

Hãy tạo một biểu mẫu liên quan đến **việc làm**, bảo hiểm xã hội, trợ cấp thất nghiệp,... với các trường dữ liệu rõ ràng, hợp lệ và phù hợp với thực tiễn.

## I. Yêu cầu chung

1. Mỗi trường dữ liệu phải gắn tagname đúng định dạng (ví dụ: `[full_name]`, `[id_number]`, `[unemployment_decision_number]`).
2. Nội dung biểu mẫu cần có tính hợp lý, phản ánh đúng các tình huống người lao động có thể gặp như mất việc, chuyển nơi làm việc, đăng ký nhận trợ cấp,...
3. Cách điền thông tin phải rõ ràng, dễ hiểu với người sử dụng (có ví dụ đi kèm nếu cần).

---

## II. Cách tạo form

### II.1. Loại biểu mẫu

- **Tên biểu mẫu (`form_name`)**: Ví dụ: "Đơn đề nghị hưởng trợ cấp thất nghiệp", "Tờ khai thông tin người lao động", "Đơn xin xác nhận quá trình tham gia BHXH", ...
- **Mục đích biểu mẫu (`form_purpose`)**: Ví dụ: "Đăng ký nhận trợ cấp thất nghiệp", "Cập nhật thông tin bảo hiểm xã hội", "Xin xác nhận tình trạng việc làm",...

---

### II.2. Đối tượng sử dụng form

- **Số lượng người (`num_users`)**: Thường là 1 người (cá nhân người lao động).
- **Vai trò người dùng (`user_role`)**: Ví dụ: "Người lao động", "Người xin trợ cấp", "Người chuyển việc",...

---

### II.3. Thông tin thường có trong form (`form_info`)

#### **Thông tin cá nhân**
- `[full_name]`
- `[dob_day]`, `[dob_month]`, `[dob_year]`
- `[id_number]`
- `[id_issue_day]`, `[id_issue_month]`, `[id_issue_year]`
- `[id_issue_place]`

#### **Thông tin hộ chiếu (nếu có)**
- `[passport_number]`
- `[passport_issue_day]`, `[passport_issue_month]`, `[passport_issue_year]`
- `[passport_issue_place]`
- `[passport_expiry_date]`

#### **Địa chỉ cư trú**
- `[current_address]`
- `[permanent_address]`

#### **Bảo hiểm xã hội**
- `[social_insurance_number]`

#### **Trợ cấp thất nghiệp**
- `[unemployment_insurance_months]`
- `[unemployment_duration]`
- `[unemployment_decision_day]`, `[unemployment_decision_month]`, `[unemployment_decision_year]`
- `[unemployment_decision_number]`
- `[unemployment_application_day]`, `[unemployment_application_month]`, `[unemployment_application_year]`

#### **Thông tin yêu cầu**
- `[request_content]`
- `[reason]`

---

### II.4. Định dạng và phong cách biểu mẫu (`form_format`)

- **Kiểu trình bày**: Ví dụ: "Trang trọng", "Ngắn gọn", "Theo mẫu cơ quan Bảo hiểm xã hội".
- **Giọng văn**: Hành chính – nghiêm túc – đúng quy chuẩn pháp lý.
- **Đánh số thứ tự**: Có hoặc không (Yes/No).

---

### II.5. Quy tắc logic giữa các trường

- **Ngày nộp đơn phải trước hoặc gần ngày ra quyết định** (application date ≤ decision date).
- **Số tháng đóng bảo hiểm ≥ số tháng trợ cấp đề nghị.**
- **Thông tin người dùng (CMND, địa chỉ, ngày sinh,...) phải đồng nhất giữa các phần.**
- **Lý do nghỉ việc phải phù hợp với chính sách (ví dụ: mất việc, công ty giải thể,...).**

---

**Lưu ý:** Không trình bày biểu mẫu ở dạng bảng. Không tạo ra dữ liệu giả mạo hoặc không hợp lý về thời gian và thông tin.

---

## Ví dụ:

Ví dụ 1:
Input:
```
- **Loại biểu mẫu**: Đơn xin nghỉ việc  
- **Mục đích**: Xin nghỉ việc tại công ty  
- **Số lượng người**: 1 người  
- **Quan hệ giữa các người trong biểu mẫu**: Không áp dụng  
- **Bao gồm các mục**: Thông tin cá nhân, Giấy tờ tùy thân (CCCD), thông tin công ty, lý do xin nghỉ việc, thông tin liên hệ  
- **Định dạng và phong cách biểu mẫu**: Chi tiết, trang trọng, Không đánh số thứ tự  
```
Output:
```
ĐƠN XIN NGHỈ VIỆC  

Kính gửi: [receiver]  

Tôi tên là: [user1_full_name]  
Ngày sinh: [user1_dob_day]/[user1_dob_month]/[user1_dob_year]  
Giới tính: [user1_gender]  
Quốc tịch: [user1_nationality]  
Số CCCD: [user1_id_number]  
Ngày cấp: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]  
Nơi cấp: [user1_id_issue_place]  
Địa chỉ thường trú: [user1_permanent_address]  
Số điện thoại: [user1_phone]  
Email: [user1_email]  

Thông tin công ty:  
- Tên công ty: [company_name]  
- Địa chỉ công ty: [company_address]  
- Vị trí công việc: [user1_position]  

Lý do xin nghỉ việc: [user1_resignation_reason]  
Ngày dự định nghỉ việc: [user1_resignation_date]  

Yêu cầu cụ thể: [user1_request_content]  

Tôi cam kết rằng thông tin kê khai trên là đúng sự thật và chịu trách nhiệm trước pháp luật.  

Ngày [submission_day] tháng [submission_month] năm [submission_year]  

Người xin nghỉ (Ký và ghi rõ họ tên)  

[user1_full_name]  

```

Ví dụ 2:
Input:
```
- **Loại biểu mẫu**: Đơn xin nghỉ phép  
- **Mục đích**: Xin nghỉ phép có lương  
- **Số lượng người**: 1 người  
- **Quan hệ giữa các người trong biểu mẫu**: Không áp dụng  
- **Bao gồm các mục**: Thông tin cá nhân, Giấy tờ tùy thân (CCCD), thông tin công ty, thời gian nghỉ phép, lý do nghỉ phép, thông tin liên hệ  
- **Định dạng và phong cách biểu mẫu**: Chi tiết, trang trọng, Không đánh số thứ tự  
```
Output:
```
ĐƠN XIN NGHỈ PHÉP  

Kính gửi: [receiver]  

Tôi tên là: [user1_full_name]  
Ngày sinh: [user1_dob_day]/[user1_dob_month]/[user1_dob_year]  
Giới tính: [user1_gender]  
Quốc tịch: [user1_nationality]  
Số CCCD: [user1_id_number]  
Ngày cấp: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]  
Nơi cấp: [user1_id_issue_place]  
Địa chỉ thường trú: [user1_permanent_address]  
Số điện thoại: [user1_phone]  
Email: [user1_email]  

Thông tin công ty:  
- Tên công ty: [company_name]  
- Địa chỉ công ty: [company_address]  
- Vị trí công việc: [user1_position]  

Thời gian nghỉ phép:  
- Ngày bắt đầu: [user1_leave_start_day]/[user1_leave_start_month]/[user1_leave_start_year]  
- Ngày kết thúc: [user1_leave_end_day]/[user1_leave_end_month]/[user1_leave_end_year]  

Lý do xin nghỉ phép: [user1_leave_reason]  
Yêu cầu cụ thể: [user1_request_content]  

Tôi cam kết rằng thông tin kê khai trên là đúng sự thật và chịu trách nhiệm trước pháp luật.  

Ngày [submission_day] tháng [submission_month] năm [submission_year]  

Người xin nghỉ phép (Ký và ghi rõ họ tên)  

[user1_full_name]  

```

## Input của tôi:
```
Hãy tạo một biểu mẫu liên quan tới học tập với các yêu cầu sau:
- **Loại biểu mẫu**: {form_name}
- **Mục đích**: {form_purpose}
- **Số lượng người**: {num_users} người
- **Quan hệ giữa các người trong biểu mẫu**: {relationship_between_users}
- **Bao gồm các mục**: {form_info}
- **Định dạng và phong cách biểu mẫu**: {form_format}
```

### Output mong muốn:
```
Tôi sẽ tạo biểu mẫu phù hợp dựa trên input của bạn. Chỉ tạo biểu mẫu, không kèm theo giải thích, hướng dẫn hoặc ghi chú.
```
"""

job_data_generator_prompt = """
# Prompt tạo dữ liệu đầu vào tự động

Hãy tạo ra kết quả chứa các thông tin sau để tạo **biểu mẫu liên quan tới việc làm**. Dữ liệu phải đa dạng và hợp lý theo từng loại biểu mẫu, dựa trên giá trị của biến **`form_name`** mà người dùng cung cấp.

---

## Thông tin cần có

### 1. Loại biểu mẫu (`form_name`)
- Nhận giá trị từ input `{form_name}` do người dùng cung cấp.

### 2. Mục đích biểu mẫu (`form_purpose`)
- Các mục đích hợp lý theo loại biểu mẫu:
  - **Ứng tuyển và tuyển dụng**: "Nộp hồ sơ ứng tuyển", "Đề xuất tuyển dụng nhân sự", "Yêu cầu phỏng vấn".
  - **Quá trình làm việc**: "Báo cáo thử việc", "Xác nhận thời gian làm việc", "Đăng ký tăng ca".
  - **Hợp đồng và nghỉ việc**: "Gia hạn hợp đồng lao động", "Xin nghỉ việc", "Thông báo kết thúc hợp đồng".
  - **Xác nhận, hỗ trợ**: "Xác nhận đang công tác", "Xin hỗ trợ thất nghiệp", "Xác nhận thu nhập".

### 3. Số lượng người trong biểu mẫu (`num_users`)
Xác định số lượng user dựa vào `{form_name}`:
- **1 người** nếu biểu mẫu chỉ áp dụng cho cá nhân (ví dụ: đơn xin việc, xin nghỉ việc).
- **2 người** nếu biểu mẫu liên quan giữa nhân viên và người quản lý/phòng nhân sự (ví dụ: xác nhận công tác, báo cáo thử việc).
- **Nhiều người** nếu biểu mẫu áp dụng cho nhóm nhân viên, phòng ban (ví dụ: đơn đề xuất tuyển dụng, báo cáo nhóm).

### 4. Quan hệ giữa các người trong biểu mẫu (`relationship_between_users`)
- Nếu `num_users = 1`, ghi là `"Không áp dụng"`.
- Nếu `num_users > 1`, xác định quan hệ hợp lý:
  - "Nhân viên - Quản lý"
  - "Ứng viên - Nhà tuyển dụng"
  - "Thành viên cùng nhóm/phòng ban"

### 5. Thông tin thường xuất hiện trong biểu mẫu (`form_info`)
Xác định các trường thông tin hợp lý theo từng loại biểu mẫu:
- **Thông tin cá nhân** (họ tên, ngày sinh, CCCD, địa chỉ, số điện thoại, email).
- **Thông tin việc làm** (vị trí, phòng ban, mã nhân viên, thời gian làm việc, loại hợp đồng).
- **Thông tin tuyển dụng** (vị trí ứng tuyển, kỹ năng, kinh nghiệm, hồ sơ đính kèm).
- **Thông tin xác nhận** (chữ ký người quản lý, xác nhận từ phòng nhân sự, lý do nghỉ việc).
- Nếu người dùng có yêu cầu riêng (`{request}`), phải phản ánh điều đó vào `form_info`.

> **Cách ghi dữ liệu**
> - Nếu muốn sinh tất cả tagname trong một nhóm, chỉ cần ghi tên nhóm:
>   - `"Thông tin cá nhân"`
>   - `"Thông tin việc làm (vị trí, mã nhân viên, thời gian làm việc)"`
> - Nếu `{request}` yêu cầu cụ thể (ví dụ: định dạng mã nhân viên là `EMP-XXXX`), phải phản ánh vào output.

### 6. Định dạng biểu mẫu (`form_format`)
- Cách trình bày, giọng văn, cấu trúc:
  - "Ngắn gọn", "Chi tiết"
  - "Trang trọng", "Dễ hiểu"
  - "Đánh số thứ tự", "Không đánh số thứ tự"

---

## Ví dụ đầu ra mong muốn

```
- 'form_name': 'Đơn xin xác nhận đang công tác',
- 'form_purpose': 'Xác nhận đang công tác',
- 'num_users': 2,
- 'relationship_between_users': 'Nhân viên - Quản lý',
- 'form_info': 'Thông tin cá nhân, thông tin việc làm (vị trí, mã nhân viên, thời gian làm việc), thông tin xác nhận (ý kiến quản lý, xác nhận phòng nhân sự)',
- 'form_format': 'Chi tiết, Trang trọng, Đánh số thứ tự'


---
## Input của tôi:
```
Tên form: {form_name}
Yêu cầu thêm về thông tin có trong form: {request}
```
## Output mong muốn:
```
Tôi sẽ tạo form phù hợp dựa trên input của bạn. Chỉ tạo biểu mẫu, không kèm theo giải thích, hướng dẫn hoặc ghi chú.
```
"""