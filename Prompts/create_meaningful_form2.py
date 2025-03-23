create_residence_identification_form_prompt = """
# **Hướng dẫn tạo biểu mẫu cư trú và giấy tờ tùy thân**

Hãy tạo một biểu mẫu hành chính công (như tờ khai, giấy đăng ký, biên bản, đơn từ,...) trong đó mỗi trường dữ liệu phải rõ ràng, chính xác và dễ hiểu cho người dùng.

## I. Yêu cầu chung

1. Mỗi trường trong biểu mẫu phải gán với tagnames dưới dạng `userX_fieldname`, trong đó X là số thứ tự của người trong biểu mẫu (vd: `user1_full_name`, `user2_id_number`).

2. Nội dung của form phải liên kết chặt chẽ, các trường dữ liệu phải logic và phù hợp với nhau.

3. Form có thể áp dụng cho nhiều người, và nếu như vậy thì thông tin của các người trong form phải liên quan chặt chẽ (vd: thành viên gia đình, đồng nghiệp, ...).

## II. Cách tạo form

### II.1. Loại biểu mẫu

- Loại biểu mẫu (form_type): Loại biểu mẫu cần tạo (ví dụ: "Tờ khai Căn cước công dân", "Đơn xin tạm trú", "Giấy đăng ký xe", ...).

- Mục đích biểu mẫu (form_purpose): Mục đích của biểu mẫu (ví dụ: "Cấp mới", "Cấp lại", "Gia hạn", "Thay đổi thông tin", ...).

### II.2. Đối tượng sử dụng form

- Số lượng người (num_users): Số lượng người trong biểu mẫu (1, 2, hoặc nhiều người).

- Quan hệ giữa các người trong biểu mẫu (relationship_between_users): Quan hệ giữa các người trong biểu mẫu (ví dụ: "Thành viên gia đình", "Cùng công ty", "Bạn bè", ...).

### II.3. Thông tin cần có trong form (form_info)

**Thông tin cá nhân:** Mô tả thông tin cá nhân mà bạn cần có trong biểu mẫu, dưới đây sẽ la một số thông tin thường xuất hiện trong biểu mẫu:

- Họ và tên (userX_full_name): Họ và tên đầy đủ như trên giấy tờ tùy thân. Ví dụ: Nguyễn Văn A.

- Ngày tháng năm sinh (userX_dob_day, userX_dob_month, userX_dob_year): Ví dụ: 15/08/1995.

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

### II.5. Quy tắc logic giữa các trường

Liên kết thông tin giữa các người dùng : Các thông tin giữa các user có liên quan với nhau.

## Ví dụ:

### Ví dụ 1:
Input:
```
Hãy tạo một biểu mẫu hành chính công với các yêu cầu sau:
- **Loại biểu mẫu**: Đơn xin tạm trú
- **Mục đích**: Đăng ký tạm trú cho hộ gia đình
- **Số lượng người**: 4 người
- **Quan hệ giữa các người trong biểu mẫu**: Thành viên gia đình
- **Bao gồm các mục**: Thông tin cá nhân, Giấy tờ tùy thân(Chỉ có thông tin về căn cước công dân), Địa chỉ cư trú(chỉ lấy địa chỉ tạm trú)
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
- **Loại biểu mẫu**: Cấp đổi thẻ căn cước
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
- **Loại biểu mẫu**: {form_type}
- **Mục đích**: {form_purpose}
- **Số lượng người**: {num_users} người
- **Quan hệ giữa các người trong biểu mẫu**: {relationship_between_users}
- **Bao gồm các mục**: {form_info}
- **Định dạng và phong cách biểu mẫu**: {form_format}
```

### Output mong muốn:
```
(Tôi sẽ tạo form phù hợp dựa trên input của bạn)
```
"""

residence_indentification_data_generator_prompt = """
# **Prompt tạo dữ liệu đầu vào tự động**

Hãy tạo một cấu trúc dữ liệu dạng dictionary chứa các thông tin sau để tạo biểu mẫu hành chính công. Dữ liệu phải đa dạng và hợp lý theo từng loại biểu mẫu.  

## **Thông tin cần có**  

### 1. **Loại biểu mẫu** (`form_type`)  
- Nhận giá trị từ input do người dùng cung cấp.  

### 2. **Mục đích biểu mẫu** (`form_purpose`)  
- Các mục đích phù hợp với loại biểu mẫu, ví dụ:  
  - **Hộ chiếu**: "Cấp mới", "Cấp lại", "Gia hạn", "Thay đổi thông tin".  
  - **Căn cước công dân**: "Cấp mới", "Cấp đổi", "Cấp lại do mất".  
  - **Tạm trú**: "Đăng ký mới", "Gia hạn tạm trú".  

### 3. **Số lượng người trong biểu mẫu** (`num_users`)  
- Tùy vào loại biểu mẫu, có thể là 1 người hoặc nhiều người.  
- Ví dụ:  
  - "Đơn xin cấp hộ chiếu" thường là 1 người.  
  - "Đăng ký tạm trú hộ gia đình" có thể nhiều người.  

### 4. **Quan hệ giữa các người trong biểu mẫu** (`relationship_between_users`)  
- Chỉ có giá trị nếu `num_users > 1`.  
- Ví dụ: "Thành viên gia đình", "Cùng công ty", "Bạn bè", ...  

### 5. **Thông tin cần có trong biểu mẫu** (`form_info`)  
Xác định các mục thông tin có trong biểu mẫu, đảm bảo đa dạng theo từng loại:  
- **Thông tin cá nhân** (họ tên, ngày sinh, giới tính, quốc tịch).  
- **Giấy tờ tùy thân** (CMND/CCCD, hộ chiếu cũ nếu có).  
- **Địa chỉ cư trú** (thường trú, tạm trú).  
- **Thông tin liên hệ** (số điện thoại, email nếu cần).  
- **Thông tin bổ sung** (lý do xin cấp đổi, thời gian hiệu lực, ...).  

#### **Quy tắc ghi dữ liệu**  
- **Ngày sinh**:  
  - Dạng `userX_dob_day/userX_dob_month/userX_dob_year` hoặc `userX_dob`.  
- **Địa chỉ**:  
  - Chỉ lấy thường trú hoặc cả thường trú + tạm trú tùy loại biểu mẫu.  
- **Giấy tờ tùy thân**:  
  - Nếu có hộ chiếu cũ thì bổ sung mục thông tin hộ chiếu cũ.  

### 6. **Định dạng biểu mẫu** (`form_format`)  
- Quy định cách trình bày, giọng văn, và cấu trúc:  
  - "Ngắn gọn", "Chi tiết".  
  - "Trang trọng", "Dễ hiểu".  
  - "Đánh số thứ tự", "Có checkbox", ...  

---

## **Ví dụ đầu ra mong muốn**  

```python
{
    'form_type': 'Cấp hộ chiếu phổ thông',
    'form_purpose': 'Cấp mới hộ chiếu',
    'num_users': 1,
    'relationship_between_users': 'Không áp dụng',
    'form_info': 'Thông tin cá nhân(ngày sinh viết theo định dạng `user1_dob`), giấy tờ tùy thân (CMND/CCCD), địa chỉ cư trú(chỉ lấy địa chỉ thường trú), thông tin hộ chiếu cũ (nếu có)',
    'form_format': 'Chi tiết, Trang trọng, Đánh số thứ tự'
}

---
## Input của tôi:
```
{form_type}
```
## Output mong muốn:
```
(Tôi sẽ tạo form phù hợp dựa trên input của bạn)
```
"""

create_study_form_prompt = """
# **Hướng dẫn tạo biểu mẫu học tập**

Hãy tạo một **biểu mẫu liên quan đến học tập**, trong đó mỗi trường dữ liệu phải **rõ ràng, chính xác** và đảm bảo **dễ hiểu** cho người dùng.  
Mỗi trường phải được mô tả cụ thể với hướng dẫn điền thông tin để đảm bảo dữ liệu nhập vào **phù hợp với thực tế**.

## **1. Thông tin cá nhân**
- **Họ và tên** (`[full_name]`):  
  - Họ và tên đầy đủ như trên giấy tờ tùy thân.  
  - Còn gọi là: **Tên đầy đủ**, **Họ tên chính thức**.  
  - **Ví dụ**: Trần Thanh Bình.  
- **Tên gọi khác (nếu có)** (`[alias_name]`):  
  - Tên thường gọi, biệt danh hoặc tên khác ngoài tên chính thức.  
  - **Ví dụ**: Bin, Tý.  
- **Ngày tháng năm sinh** (`[dob]`):  
  - Gồm `[dob_day]`, `[dob_month]`, `[dob_year]`.  
  - Còn gọi là: **Ngày sinh nhật**, **Ngày chào đời**.  
  - **Ví dụ**: 10/05/2002.  
- **Giới tính** (`[gender]`):  
  - Chọn Nam, Nữ hoặc Khác nếu có quy định pháp lý.  
  - Còn gọi là: **Phái**, **Giới tính sinh học**.  
- **Số CMND/CCCD** (`[id_number]`):  
  - Còn gọi là: **Mã định danh cá nhân**, **Số thẻ căn cước**.  
  - **Ví dụ**: 0123456789.  
- **Ngày cấp CMND/CCCD** (`[id_issue_date]`):  
  - Gồm `[id_issue_day]`, `[id_issue_month]`, `[id_issue_year]`.  
  - Còn gọi là: **Thời điểm cấp**, **Ngày phát hành thẻ**.  
- **Nơi cấp CMND/CCCD** (`[id_issue_place]`):  
  - **Ví dụ**: Công an TP Hà Nội.  
- **Số điện thoại** (`[phone]`):  
  - Ghi số di động chính xác để liên hệ.  
  - **Ví dụ**: 0987654321.  
- **Số điện thoại nhà (nếu có)** (`[phone_home]`):  
  - **Ví dụ**: 024-3824-xxxx.  
- **Email** (`[email]`):  
  - Ghi email cá nhân hoặc trường cung cấp.  
  - **Ví dụ**: sinhvienA@gmail.com.  

## **2. Thông tin học tập**
- **Tên lớp** (`[class]`):  
  - Còn gọi là: **Lớp học**, **Lớp hiện tại**.  
  - **Ví dụ**: 12A1, CNTT-K65.  
- **Tên trường** (`[school]`):  
  - Trường đang theo học.  
  - **Ví dụ**: Đại học Bách Khoa Hà Nội.  
- **Hiệu trưởng** (`[school_principal]`):  
  - Người đứng đầu nhà trường.  
  - **Ví dụ**: PGS.TS Nguyễn Văn B.  
- **Khóa học** (`[course]`):  
  - Ghi tên khóa học chính thức.  
  - **Ví dụ**: Công nghệ thông tin K65.  
- **Khoa** (`[faculty]`):  
  - Khoa trực thuộc trường.  
  - **Ví dụ**: Khoa Khoa học Máy tính.  
- **Mã số sinh viên** (`[student_id_number]`):  
  - Còn gọi là: **MSSV**, **ID Sinh viên**.  
  - **Ví dụ**: 20201234.  
- **Trình độ học vấn** (`[education_level]`):  
  - Ghi rõ bậc học hiện tại.  
  - **Ví dụ**: Đại học, Cao đẳng, Thạc sĩ.  
- **Thời gian khóa học** (`[duration_of_course]`):  
  - Số năm theo học theo chương trình đào tạo.  
  - **Ví dụ**: 4 năm.  
- **Ngày tốt nghiệp** (`[graduation_date]`):  
  - Dự kiến hoặc ngày tốt nghiệp chính thức.  
  - **Ví dụ**: 30/06/2026.  
- **Bằng cấp đạt được** (`[degree]`):  
  - Còn gọi là: **Văn bằng**, **Chứng chỉ tốt nghiệp**.  
  - **Ví dụ**: Cử nhân Công nghệ thông tin.  
- **Điểm trung bình (GPA)** (`[grade]`):  
  - Điểm trung bình tích lũy theo thang điểm của trường.  
  - **Ví dụ**: 3.8/4.0 hoặc 8.5/10.  
- **Xếp loại học tập** (`[study_result_rating]`):  
  - Còn gọi là: **Xếp hạng thành tích**, **Loại tốt nghiệp**.  
  - **Ví dụ**: Giỏi, Xuất sắc.  
- **Học kỳ** (`[semester]`):  
  - Ghi rõ học kỳ đang theo học.  
  - **Ví dụ**: Học kỳ 1, Năm 2.  
- **Năm học** (`[school_year]`):  
  - Ghi rõ niên khóa.  
  - **Ví dụ**: 2023-2024.  
- **Tên người hướng dẫn** (`[supervisor_name]`):  
  - Dành cho sinh viên làm đồ án, nghiên cứu khoa học.  
  - **Ví dụ**: TS. Lê Quang H.  
- **Địa chỉ trường** (`[school_address]`):  
  - Địa chỉ trụ sở chính của trường.  
  - **Ví dụ**: Số 1 Đại Cồ Việt, Hai Bà Trưng, Hà Nội.  
- **Số điện thoại trường** (`[school_phone]`):  
  - **Ví dụ**: 024-3623-xxxx.  

## **3. Thông tin quyết định học tập**
- **Cơ quan quản lý trực tiếp** (`[organization]`):  
  - Đơn vị quản lý sinh viên/học sinh.  
  - **Ví dụ**: Bộ Giáo dục và Đào tạo.  
- **Số quyết định liên quan** (`[decision_number]`):  
  - Còn gọi là: **Số văn bản quyết định**.  
  - **Ví dụ**: QĐ-1234/2024.  
- **Ngày quyết định** (`[decision_day]`, `[decision_month]`, `[decision_year]`):  
  - Ngày văn bản có hiệu lực.  
  - **Ví dụ**: 15/07/2023.  
- **Số quyết định cử đi học** (`[study_decision_number]`):  
  - **Ví dụ**: QĐ-5678/2023.  
- **Người ban hành quyết định** (`[decision_issuer]`):  
  - Cá nhân/tổ chức đưa ra quyết định.  
  - **Ví dụ**: Hiệu trưởng Đại học Quốc gia.  

## **4. Thông tin bổ sung**
- **Nội dung yêu cầu** (`[request_content]`):  
  - Lý do nộp đơn, đề xuất hoặc yêu cầu.  
  - **Ví dụ**: Xin cấp lại thẻ sinh viên.  
- **Lý do** (`[reason]`):  
  - Giải thích nguyên nhân cụ thể.  
  - **Ví dụ**: Thẻ sinh viên bị mất.  
- **Kiến nghị, đề xuất** (`[suggestion]`):  
  - Gửi đến cơ quan quản lý để xem xét.  
  - **Ví dụ**: Đề xuất hỗ trợ cấp lại trong vòng 3 ngày.  
"""

create_health_and_medical_form_prompt = """" 
# **Hướng dẫn tạo biểu mẫu sức khỏe và y tế**

Hãy tạo một **biểu mẫu liên quan đến sức khỏe và y tế**, trong đó mỗi trường dữ liệu phải **rõ ràng, chính xác** và đảm bảo **dễ hiểu** cho người dùng.  
Mỗi trường phải được mô tả cụ thể với hướng dẫn điền thông tin để đảm bảo dữ liệu nhập vào **phù hợp với thực tế**.

## **1. Thông tin cá nhân**
- **Họ và tên** (`[full_name]`):  
  - Họ và tên đầy đủ như trên giấy tờ tùy thân.  
  - Còn gọi là: **Tên đầy đủ**, **Họ tên chính thức**.  
  - **Ví dụ**: Nguyễn Văn A.  
- **Ngày tháng năm sinh** (`[dob_day]`, `[dob_month]`, `[dob_year]`):  
  - Gồm đầy đủ ngày, tháng, năm sinh.  
  - Còn gọi là: **Ngày chào đời**, **Sinh nhật**.  
  - **Ví dụ**: 15/08/1995.  
- **Số CMND/CCCD** (`[id_number]`):  
  - Còn gọi là: **Mã định danh cá nhân**, **Số thẻ căn cước**.  
  - **Ví dụ**: 079203004567.  
- **Ngày cấp CMND/CCCD** (`[id_issue_date]`):  
  - Gồm `[id_issue_day]`, `[id_issue_month]`, `[id_issue_year]`.  
  - Còn gọi là: **Thời điểm cấp**, **Ngày phát hành thẻ**.  
  - **Ví dụ**: 20/06/2015.  
- **Nơi cấp CMND/CCCD** (`[id_issue_place]`):  
  - Cơ quan cấp giấy tờ.  
  - **Ví dụ**: Công an TP Hồ Chí Minh.  

## **2. Thông tin địa chỉ**
- **Nơi đăng ký khai sinh** (`[birth_registration_place]`):  
  - Địa chỉ nơi đăng ký khai sinh của người dùng.  
  - **Ví dụ**: UBND phường Đống Đa, Hà Nội.  
- **Địa chỉ thường trú** (`[current_address]`):  
  - Địa chỉ nơi ở hiện tại của người dùng.  
  - Gồm `[current_address_ward]`, `[current_address_district]`, `[current_address_province]`.  
  - **Ví dụ**: Số 12, đường Nguyễn Trãi, phường 5, quận 10, TP Hồ Chí Minh.  

## **3. Thông tin bảo hiểm và y tế**
- **Số bảo hiểm xã hội** (`[social_insurance_number]`):  
  - Dãy số định danh cá nhân trong hệ thống bảo hiểm xã hội.  
  - **Ví dụ**: 0123456789.  
- **Số thẻ bảo hiểm y tế** (`[health_insurance_card_number]`):  
  - Mã số trên thẻ bảo hiểm y tế.  
  - **Ví dụ**: BHYT-987654321.  
- **Nơi đăng ký bảo hiểm y tế** (`[health_insurance_registration_place]`):  
  - Cơ sở y tế nơi đăng ký khám chữa bệnh ban đầu.  
  - **Ví dụ**: Bệnh viện Bạch Mai.  

## **4. Thông tin liên hệ**
- **Số điện thoại** (`[phone]`):  
  - Ghi số điện thoại chính xác để liên hệ.  
  - **Ví dụ**: 0987654321.  
- **Email** (`[email]`):  
  - Ghi email cá nhân hoặc email liên hệ công việc.  
  - **Ví dụ**: nguoidung@email.com.  

## **5. Thông tin nghề nghiệp & tài chính**
- **Nghề nghiệp** (`[occupation]`):  
  - Công việc hiện tại của người dùng.  
  - **Ví dụ**: Bác sĩ, Kỹ sư phần mềm.  
- **Số tài khoản ngân hàng** (`[bank_account]`):  
  - Cần nhập số tài khoản ngân hàng chính xác.  
  - **Ví dụ**: 123456789012.  
- **Tên ngân hàng** (`[bank_name]`):  
  - Ghi rõ tên ngân hàng sử dụng.  
  - **Ví dụ**: Vietcombank.  

## **6. Thông tin người thân**
- **Tên phụ huynh/người giám hộ** (`[parent_name]`):  
  - Ghi rõ họ và tên của cha/mẹ hoặc người bảo hộ hợp pháp.  
  - **Ví dụ**: Trần Văn B.  

## **7. Thông tin yêu cầu**
- **Nội dung yêu cầu** (`[request_content]`):  
  - Lý do gửi đơn, đề xuất hoặc yêu cầu liên quan đến y tế.  
  - **Ví dụ**: Xin cấp lại thẻ bảo hiểm y tế.  
- **Lý do cụ thể** (`[reason]`):  
  - Giải thích nguyên nhân yêu cầu.  
  - **Ví dụ**: Thẻ bảo hiểm bị mất hoặc hư hỏng.  

---
"""

create_vehicle_driver_form_prompt = """
# **Hướng dẫn tạo biểu mẫu phương tiện và người lái**

Hãy tạo một **biểu mẫu liên quan đến phương tiện giao thông và người lái**, trong đó mỗi trường dữ liệu phải **rõ ràng, chính xác** và đảm bảo **dễ hiểu** cho người dùng.  
Mỗi trường phải được mô tả cụ thể với hướng dẫn điền thông tin để đảm bảo dữ liệu nhập vào **phù hợp với thực tế**.

## **1. Thông tin cá nhân**
- **Họ và tên** (`[full_name]`):  
  - Họ và tên đầy đủ như trên giấy tờ tùy thân.  
  - Còn gọi là: **Tên đầy đủ**, **Họ tên chính thức**.  
  - **Ví dụ**: Nguyễn Văn A.  
- **Ngày tháng năm sinh** (`[dob_day]`, `[dob_month]`, `[dob_year]`):  
  - Gồm đầy đủ ngày, tháng, năm sinh.  
  - Còn gọi là: **Ngày chào đời**, **Sinh nhật**.  
  - **Ví dụ**: 15/08/1995.  
- **Số CMND/CCCD** (`[id_number]`):  
  - Còn gọi là: **Mã định danh cá nhân**, **Số thẻ căn cước**.  
  - **Ví dụ**: 079203004567.  
- **Ngày cấp CMND/CCCD** (`[id_issue_date]`):  
  - Gồm `[id_issue_day]`, `[id_issue_month]`, `[id_issue_year]`.  
  - Còn gọi là: **Thời điểm cấp**, **Ngày phát hành thẻ**.  
  - **Ví dụ**: 20/06/2015.  
- **Nơi cấp CMND/CCCD** (`[id_issue_place]`):  
  - Cơ quan cấp giấy tờ.  
  - **Ví dụ**: Công an TP Hồ Chí Minh.  

## **2. Thông tin hộ chiếu**
- **Số hộ chiếu** (`[passport_number]`):  
  - Dãy số trên hộ chiếu cá nhân.  
  - **Ví dụ**: C1234567.  
- **Ngày cấp hộ chiếu** (`[passport_issue_date]`):  
  - Gồm `[passport_issue_day]`, `[passport_issue_month]`, `[passport_issue_year]`.  
  - **Ví dụ**: 10/02/2020.  
- **Nơi cấp hộ chiếu** (`[passport_issue_place]`):  
  - Cơ quan cấp hộ chiếu.  
  - **Ví dụ**: Cục Quản lý Xuất nhập cảnh, Hà Nội.  

## **3. Thông tin giấy phép lái xe**
- **Số giấy phép lái xe** (`[driving_license_number]`):  
  - Số hiệu của giấy phép lái xe.  
  - **Ví dụ**: 123456789.  
- **Cơ quan cấp giấy phép** (`[driving_license_issuer]`):  
  - Tên cơ quan cấp GPLX.  
  - **Ví dụ**: Sở Giao thông Vận tải TP Hồ Chí Minh.  
- **Ngày cấp giấy phép** (`[driving_license_issue_date]`):  
  - Gồm `[driving_license_issue_day]`, `[driving_license_issue_month]`, `[driving_license_issue_year]`.  
  - **Ví dụ**: 05/07/2018.  
- **Hạng GPLX** (`[driving_license_category]`):  
  - Phân loại bằng lái theo quy định.  
  - **Ví dụ**: Hạng B2.  

## **4. Thông tin về phương tiện**
- **Số khung xe (Chassis No)** (`[vehicle_chassis_number]`):  
  - Số nhận dạng khung xe.  
  - **Ví dụ**: RL4CR23D9HC012345.  
- **Số máy xe (Engine No)** (`[vehicle_engine_number1]`, `[vehicle_engine_number2]`):  
  - Số nhận dạng động cơ xe.  
  - **Ví dụ**: 3NRX234567.  

## **5. Thông tin thuế và hải quan**
- **Số hóa đơn điện tử** (`[tax_invoice_number]`):  
  - Mã số hóa đơn khi đăng ký phương tiện.  
  - **Ví dụ**: 0123456789.  
- **Mã hồ sơ khai lệ phí trước bạ** (`[tax_declaration_code_issuing_agency]`):  
  - Mã khai báo thuế khi đăng ký xe.  
  - **Ví dụ**: 456789123.  
- **Số tờ khai hải quan điện tử** (`[electronic_customs_declaration_number_issuing_agency]`):  
  - Số hiệu khai báo hải quan khi nhập khẩu phương tiện.  
  - **Ví dụ**: HQ2023123456.  

## **6. Thông tin giấy phép kinh doanh vận tải**
- **Ngày cấp giấy phép** (`[transport_license_issue_date]`):  
  - Ngày giấy phép vận tải có hiệu lực.  
  - **Ví dụ**: 15/09/2022.  
- **Nơi cấp giấy phép** (`[transport_license_issue_place]`):  
  - Đơn vị cấp phép kinh doanh vận tải.  
  - **Ví dụ**: Sở Giao thông Vận tải Hà Nội.  

## **7. Thông tin yêu cầu**
- **Nội dung yêu cầu** (`[request_content]`):  
  - Lý do gửi đơn, đề xuất hoặc yêu cầu liên quan đến phương tiện và người lái.  
  - **Ví dụ**: Xin cấp lại giấy phép lái xe bị mất.  
- **Lý do cụ thể** (`[reason]`):  
  - Giải thích nguyên nhân yêu cầu.  
  - **Ví dụ**: Giấy phép lái xe bị mất trong quá trình di chuyển.  

---
"""

create_job_form_prompt = """
# **Hướng dẫn tạo biểu mẫu việc làm**

Hãy tạo một **biểu mẫu liên quan đến việc làm**, trong đó mỗi trường dữ liệu phải **rõ ràng, chính xác** và đảm bảo **dễ hiểu** cho người dùng.  
Mỗi trường phải được mô tả cụ thể với hướng dẫn điền thông tin để đảm bảo dữ liệu nhập vào **phù hợp với thực tế**.

## **1. Thông tin cá nhân**
- **Họ và tên** (`[full_name]`):  
  - Họ và tên đầy đủ theo giấy tờ tùy thân.  
  - Còn gọi là: **Tên đầy đủ**, **Họ tên chính thức**.  
  - **Ví dụ**: Nguyễn Văn A.  
- **Ngày tháng năm sinh** (`[dob_day]`, `[dob_month]`, `[dob_year]`):  
  - Gồm đầy đủ ngày, tháng, năm sinh.  
  - Còn gọi là: **Ngày chào đời**, **Sinh nhật**.  
  - **Ví dụ**: 15/08/1995.  
- **Số CMND/CCCD** (`[id_number]`):  
  - Số trên chứng minh nhân dân hoặc căn cước công dân.  
  - **Ví dụ**: 079203004567.  
- **Ngày cấp CMND/CCCD** (`[id_issue_date]`):  
  - Gồm `[id_issue_day]`, `[id_issue_month]`, `[id_issue_year]`.  
  - **Ví dụ**: 20/06/2015.  
- **Nơi cấp CMND/CCCD** (`[id_issue_place]`):  
  - Cơ quan cấp giấy tờ.  
  - **Ví dụ**: Công an TP Hồ Chí Minh.  

## **2. Thông tin hộ chiếu**
- **Số hộ chiếu** (`[passport_number]`):  
  - Số hiệu của hộ chiếu cá nhân.  
  - **Ví dụ**: C1234567.  
- **Ngày cấp hộ chiếu** (`[passport_issue_date]`):  
  - Gồm `[passport_issue_day]`, `[passport_issue_month]`, `[passport_issue_year]`.  
  - **Ví dụ**: 10/02/2020.  
- **Nơi cấp hộ chiếu** (`[passport_issue_place]`):  
  - Cơ quan cấp hộ chiếu.  
  - **Ví dụ**: Cục Quản lý Xuất nhập cảnh, Hà Nội.  
- **Ngày hết hạn hộ chiếu** (`[passport_expiry_date]`):  
  - Ngày hộ chiếu không còn hiệu lực.  
  - **Ví dụ**: 10/02/2030.  

## **3. Địa chỉ cư trú**
- **Địa chỉ hiện tại** (`[current_address]`):  
  - Nơi ở thực tế hiện tại.  
  - **Ví dụ**: 123 Nguyễn Trãi, Quận 1, TP Hồ Chí Minh.  
- **Nơi thường trú** (`[permanent_address]`):  
  - Địa chỉ đăng ký hộ khẩu thường trú.  
  - **Ví dụ**: 456 Lê Lợi, TP Hà Nội.  

## **4. Bảo hiểm xã hội**
- **Số sổ bảo hiểm xã hội** (`[social_insurance_number]`):  
  - Mã số sổ bảo hiểm xã hội cá nhân.  
  - **Ví dụ**: 0123456789.  

## **5. Trợ cấp thất nghiệp**
- **Tổng số tháng đóng bảo hiểm thất nghiệp** (`[unemployment_insurance_months]`):  
  - Tổng số tháng người dùng đã tham gia bảo hiểm thất nghiệp.  
  - **Ví dụ**: 36 tháng.  
- **Thời gian hưởng trợ cấp thất nghiệp** (`[unemployment_duration]`):  
  - Số tháng nhận trợ cấp theo chính sách.  
  - **Ví dụ**: 3 tháng.  
- **Ngày quyết định hưởng trợ cấp thất nghiệp** (`[unemployment_decision_day]`, `[unemployment_decision_month]`, `[unemployment_decision_year]`):  
  - Ngày ban hành quyết định trợ cấp.  
  - **Ví dụ**: 01/03/2024.  
- **Số quyết định hưởng trợ cấp thất nghiệp** (`[unemployment_decision_number]`):  
  - Mã số quyết định hưởng trợ cấp.  
  - **Ví dụ**: 2024/QĐ-TCTN-01.  
- **Ngày nộp đơn hưởng trợ cấp thất nghiệp** (`[unemployment_application_day]`, `[unemployment_application_month]`, `[unemployment_application_year]`):  
  - Ngày gửi hồ sơ đề nghị trợ cấp.  
  - **Ví dụ**: 15/02/2024.  

## **6. Thông tin yêu cầu**
- **Nội dung yêu cầu** (`[request_content]`):  
  - Lý do gửi đơn hoặc đề xuất liên quan đến việc làm, bảo hiểm thất nghiệp.  
  - **Ví dụ**: Xin hưởng trợ cấp thất nghiệp do mất việc làm.  
- **Lý do cụ thể** (`[reason]`):  
  - Giải thích chi tiết về tình trạng việc làm.  
  - **Ví dụ**: Công ty giải thể, không có công việc thay thế.  

---
"""