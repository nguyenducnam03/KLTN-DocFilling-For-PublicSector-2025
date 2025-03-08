create_multi_user_prompt = """
# Tạo form có nhiều user với bối cảnh liên kết

Tôi cần bạn tạo form có nhiều user, trong đó các user có mối quan hệ và sự liên kết với nhau chứ không chỉ đơn thuần là liệt kê thông tin. Tôi sẽ cung cấp danh sách các user cùng với các tagname tương ứng, và bạn cần:

1. Tạo bối cảnh hợp lý để giải thích mối quan hệ giữa các user trong form (ví dụ: Chủ xe – Người làm thủ tục).
2. Sắp xếp các user theo thứ tự logic (ví dụ: Chủ xe trước, Người làm thủ tục sau).
3. Đưa ra tiêu đề hoặc phần mô tả nếu cần để giúp biểu mẫu có tính liên kết, tránh chỉ đơn thuần liệt kê.
4. Giữ nguyên tagname tôi cung cấp trong nội dung (tagname không được thay đổi).
5. Nội dung phải mang tính nghiệp vụ, hành chính phù hợp với các loại giấy tờ khai báo, đăng ký.

# Ví dụ:
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

Input:
```
{input}
```
Output:
"""