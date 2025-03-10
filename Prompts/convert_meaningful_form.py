create_multi_user_prompt = """
# TẠO FORM CÓ NHIỀU USER VỚI BỐI CẢNH LIÊN KẾT

## Mô tả yêu cầu
Tôi cần bạn tạo form có nhiều user, trong đó các user có mối quan hệ và sự liên kết với nhau chứ không chỉ đơn thuần là liệt kê thông tin. Tôi sẽ cung cấp danh sách các user cùng với các tagname tương ứng, và bạn cần:

### Yêu cầu chính:
1. Tạo bối cảnh hợp lý để giải thích mối quan hệ giữa các user trong biểu mẫu (ví dụ: Chủ xe - Người làm thủ tục).
2. Sắp xếp thứ tự hợp lý, đảm bảo tính logic (ví dụ: Chủ xe đứng trước, Người làm thủ tục đứng sau).
3. Đưa ra tiêu đề và phần mô tả phù hợp để giúp biểu mẫu có tính liên kết, tránh chỉ đơn thuần liệt kê thông tin.
4. Giữ nguyên tagname mà tôi cung cấp trong nội dung (tagname không được thay đổi).
5. Nội dung phải mang tính nghiệp vụ, hành chính, phù hợp với các loại giấy tờ khai báo, đăng ký.
6. Diễn giải mối quan hệ giữa các user thành câu đầy đủ, không chỉ liệt kê đơn thuần.
7. Không có quá nhiều khoảng cách giữa các dòng trong form.  

### Xử lý các trường hợp đặc biệt:
- Nếu có 3 user trở lên, hãy đảm bảo mỗi user có vai trò rõ ràng với tiêu đề phù hợp.
- Nếu thiếu thông tin, thay vì bỏ qua, hãy sử dụng placeholder `[#another]`.
- Nếu có thông tin bổ sung hoặc không xác định, hãy đưa vào phần ghi chú cuối biểu mẫu.

---------------------
## Ví dụ:
Input:
```
1. Chủ xe:
Họ và tên: [use1_full_name]
năm sinh: [user1_dob_year]
địa chỉ: [user1_current_address]
số CCCD: [user1_id_number]
ngày cấp của CCCD: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]

2. Người làm thủ tục
Họ và tên: [user2_full_name]
Số CCCD: [user2_id_number]
Nơi cấp: [user2_id_issue_place]
Điện thoại: [#another]
```
Output:
```
GIẤY KHAI ĐĂNG KÝ XE (Vehicle registation declaration)
A. PHẦN CHỦ XE TỰ KÊ KHAI (self declaration vehicle owner’s)
Tên chủ xe : [use1_full_name]
Năm sinh: [user1_dob_year]
Địa chỉ :  [user1_current_address]
Số CCCD của chủ xe: [user1_id_number]
cấp ngày [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]
Tên người làm thủ tục: [user2_full_name]
Số CCCD/CMND/Hộ chiếu của người làm thủ tục [user2_id_number]
Nơi cấp: [user2_id_issue_place]
Điện thoại của người làm thủ tục : [#another]
```

## Ví dụ:
Input:
```
1. Chủ hộ  
Họ và tên: [user1_full_name]  
Năm sinh: [user1_dob_year]  
Địa chỉ thường trú: [user1_address]  
Số CCCD: [user1_id_number]  

2. Người ủy quyền  
Họ và tên: [user2_full_name]  
Số CCCD: [user2_id_number]  
Quan hệ với chủ hộ: [#another]
Nội dung ủy quyền: [#another]
```
Output:
```
GIẤY ỦY QUYỀN  
Hôm nay, ngày [day]/[month]/[year], tại [#location], chúng tôi gồm:  

1. Bên ủy quyền (Chủ hộ):  
Họ và tên: [user1_full_name]  
Năm sinh: [user1_dob_year]  
Địa chỉ thường trú: [user1_address]  
Số CCCD: [user1_id_number]  

2. Bên được ủy quyền:  
Họ và tên: [user2_full_name]  
Số CCCD: [user2_id_number]  
Quan hệ với bên ủy quyền: [user2_relation]  

Nội dung ủy quyền: [user2_authorize_content]  

Giấy ủy quyền này được lập thành 02 bản có giá trị như nhau, mỗi bên giữ một bản để thực hiện.  
```

## Ví dụ:
Input:
```
1. Người bán
Họ và tên: [user1_full_name]  
Năm sinh: [user1_dob_year]  
Địa chỉ thường trú: [user1_address]  
Số CCCD: [user1_id_number]  
Ngày cấp: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]  
Nơi cấp: [user1_id_issue_place]  

2. Người mua  
Họ và tên: [user2_full_name]  
Năm sinh: [user2_dob_year]  
Địa chỉ thường trú: [user2_address]  
Số CCCD: [user2_id_number]  
Ngày cấp: [user2_id_issue_day]/[user2_id_issue_month]/[user2_id_issue_year]  
Nơi cấp: [user2_id_issue_place]  

3. Người làm chứng  
Họ và tên: [user3_full_name]  
Số CCCD: [user3_id_number]  
Quan hệ với các bên: [#another]  
```
Output:
```
HỢP ĐỒNG MUA BÁN TÀI SẢN  

Hôm nay, ngày [day]/[month]/[year], tại [#location], chúng tôi gồm:  

**BÊN BÁN (Bên A):**  
Họ và tên: [user1_full_name]  
Năm sinh: [user1_dob_year]  
Địa chỉ thường trú: [user1_address]  
Số CCCD: [user1_id_number]  
Cấp ngày: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]  
Nơi cấp: [user1_id_issue_place]  

**BÊN MUA (Bên B):**  
Họ và tên: [user2_full_name]  
Năm sinh: [user2_dob_year]  
Địa chỉ thường trú: [user2_address]  
Số CCCD: [user2_id_number]  
Cấp ngày: [user2_id_issue_day]/[user2_id_issue_month]/[user2_id_issue_year]  
Nơi cấp: [user2_id_issue_place]  

**NGƯỜI LÀM CHỨNG:**  
Họ và tên: [user3_full_name]  
Số CCCD: [user3_id_number]  
Quan hệ với các bên: [#another]  

Hai bên đồng ý thực hiện việc mua bán tài sản theo các điều khoản sau:  
1. Loại tài sản: [#property_type]  
2. Giá trị tài sản: [#property_value]  
3. Hình thức thanh toán: [#payment_method]  

Hợp đồng này được lập thành 03 bản, mỗi bên giữ một bản, có giá trị pháp lý như nhau.  
```

## Ví dụ:
Input:
```
1. Cha/Mẹ
Họ và tên: [user1_full_name]
Dân tộc: [user1_ethnicity]
Ngày sinh: [user1_dob]
Nơi cư trú: [user1_address]
Quan hệ với người được khai sinh: [#another]
Giấy tờ tùy thân: [user1_id_number]
Quốc tịch: [user1_nationality]

2. Người chết
Nơi cư trú cuối cùng: [#another]
Giấy tờ tùy thân: [user2_id_number]
Nguyên nhân chết: [#another]
Quốc tịch: [user2_nationality]
Họ và tên: [user2_full_name]
Dân tộc: [user2_ethnicity]
Ngày mất: [user2_death_day]/[user2_death_month]/[user2_death_year]
Ngày sinh: [user2_dob]
Giới tính: [user2_gender]
```
Output:
```
TRÍCH LỤC KHAI TỬ

Số: …/TLKT

Hôm nay, ngày [day]/[month]/[year], tại [#place], chúng tôi tiến hành trích lục khai tử như sau:

**I. THÔNG TIN NGƯỜI KHAI TỬ (Cha/Mẹ hoặc người thân thích):**

Họ và tên: [user1_full_name]
Dân tộc: [user1_ethnicity]
Ngày sinh: [user1_dob]
Nơi cư trú: [user1_address]
Quan hệ với người chết: [user1_relation]
Giấy tờ tùy thân: [user1_id_number]
Quốc tịch: [user1_nationality]

**II. THÔNG TIN NGƯỜI CHẾT:**

Họ và tên: [user2_full_name]
Dân tộc: [user2_ethnicity]
Ngày sinh: [user2_dob]
Giới tính: [user2_gender]
Nơi cư trú cuối cùng: [user2_last_address]
Quốc tịch: [user2_nationality]
Giấy tờ tùy thân: [user2_id_number]
Ngày mất: [user2_death_day]/[user2_death_month]/[user2_death_year]
Nguyên nhân chết: [user2_death_reason]

**III. GHI CHÚ:**

*   Thông tin về nơi cư trú cuối cùng của người chết có thể cần xác minh thêm.
*   Nguyên nhân chết cần được xác nhận bởi cơ quan y tế có thẩm quyền.

Trích lục này được lập thành 02 bản, một bản lưu tại cơ quan đăng ký hộ tịch, một bản giao cho người khai tử.
```
## Ví dụ:
Input:
```
1. Người bị tố cáo
Họ và tên: [user1_full_name]
Giấy tờ tùy thân: [user1_id_number]
Quốc tịch: [user1_nationality]
Ngày sinh: [user1_dob]

2. Người làm đơn
Dân tộc: [user2_ethnicity]
Nơi cư trú: [user2_address]
Họ và tên: [user2_full_name]
Ngày sinh: [user2_dob]
Quốc tịch: [user2_nationality]
Email: [#another]
Quan hệ với người liên quan: [#another]

3. Người được khai sinh
Họ và tên: [user3_full_name]
Giấy khai sinh: [user3_birth_certificate]
Nơi cư trú: [user3_address]
Giới tính: [user3_gender]
```
Output:
```
ĐƠN TỐ CÁO

Kính gửi:  [#receiving_authority]

Hôm nay, ngày [day]/[month]/[year], tôi/chúng tôi là:

**I. NGƯỜI LÀM ĐƠN TỐ CÁO:**

Họ và tên: [user1_full_name]
Ngày sinh: [user1_dob]
Dân tộc: [user1_ethnicity]
Quốc tịch: [user1_nationality]
Nơi cư trú: [user1_address]
Email: [#another]
Quan hệ với người liên quan: [user1_relation]

Tôi/Chúng tôi làm đơn này để tố cáo hành vi vi phạm pháp luật của:

**II. NGƯỜI BỊ TỐ CÁO:**

Họ và tên: [user2_full_name]
Ngày sinh: [user2_dob]
Quốc tịch: [user2_nationality]
Giấy tờ tùy thân: [user2_id_number]

Liên quan đến:

**III. NGƯỜI ĐƯỢC KHAI SINH (Nếu có liên quan):**

Họ và tên: [user3_full_name]
Giới tính: [user3_gender]
Nơi cư trú: [user3_address]
Giấy khai sinh (nếu có): [user3_birth_certificate]

**IV. NỘI DUNG TỐ CÁO:**

[#complaint_content] (Mô tả chi tiết hành vi vi phạm pháp luật bị tố cáo, thời gian, địa điểm xảy ra sự việc, hậu quả gây ra, các bằng chứng kèm theo (nếu có)).

**V. ĐỀ NGHỊ:**

[#complaint_request] (Đề nghị cơ quan có thẩm quyền xem xét, giải quyết theo quy định của pháp luật).

Tôi/Chúng tôi xin cam đoan những nội dung tố cáo trên là đúng sự thật và chịu trách nhiệm trước pháp luật về những gì đã trình bày.

Kính mong nhận được sự quan tâm và giải quyết của Quý cơ quan.

                                                                        Người làm đơn
                                                                        (Ký và ghi rõ họ tên)
```

-----------------

## CÁCH SỬ DỤNG:
Bạn chỉ cần thay thế `{input}` bằng danh sách user và tagname, tôi sẽ tự động tạo form với nội dung liên kết phù hợp.

### Input của bạn:
```
{input}
```

### Output mong muốn:
```
(Tôi sẽ tạo form phù hợp dựa trên input của bạn)
```
"""