seen_tagnames = [
    "[full_name]",
    "[alias_name]",
    "[dob_text]",
    "[dob]",
    "[dob_date]",
    "[dob_day]",
    "[dob_month]",
    "[dob_year]",
    "[gender]",
    "[id_number]",
    "[id_issue_date]",
    "[id_issue_day]",
    "[id_issue_month]",
    "[id_issue_year]",
    "[id_issue_place]",
    "[occupation]",
    "[ethnicity]",
    "[religion]",
    "[nationality]",
    "[marital_status]",
    "[blood_type]",
    "[birthplace]",
    "[birthplace_ward]",
    "[birthplace_district]",
    "[birthplace_province]",
    "[birth_registration_place]",
    "[birth_registration_place_ward]",
    "[birth_registration_place_district]",
    "[birth_registration_place_province]",
    "[hometown]",
    "[hometown_ward]",
    "[hometown_district]",
    "[hometown_province]",
    "[permanent_address]",
    "[current_address]",
    "[current_address_ward]",
    "[current_address_district]",
    "[current_address_province]",
    "[passport_number]",
    "[passport_issue_date]",
    "[passport_issue_day]",
    "[passport_issue_month]",
    "[passport_issue_year]",
    "[passport_issue_place]",
]

create_multi_user_prompt = """
# TẠO FORM CÓ NHIỀU USER VỚI BỐI CẢNH LIÊN KẾT

## Mô tả yêu cầu
Tôi cần bạn tạo một form có thể áp dụng cho một hoặc nhiều user, trong đó thông tin không chỉ đơn thuần được liệt kê mà cần có ngữ cảnh rõ ràng. Tôi sẽ cung cấp danh sách
thông tin của từng user cùng với các tagname tương ứng, và bạn cần:

### Yêu cầu chính:
1. Tạo phần mở đầu phù hợp, đảm bảo có bối cảnh rõ ràng.
2. Nếu có nhiều user, xác định mối quan hệ giữa họ và sắp xếp thứ tự hợp lý (ví dụ: Chủ xe trước, Người làm thủ tục sau).
3. Nếu chỉ có một user, form vẫn phải có tính liên kết và diễn giải hợp lý.
4. Đưa ra tiêu đề và phần mô tả phù hợp giúp form có tính liên kết, tránh liệt kê đơn thuần.
5. Giữ nguyên tagname mà tôi cung cấp trong nội dung (tagname không được thay đổi).
6. Nội dung phải mang tính nghiệp vụ, hành chính, phù hợp với các loại giấy tờ khai báo, đăng ký.
7. Không có quá nhiều khoảng cách giữa các dòng trong form.

### Xử lý các trường hợp đặc biệt:
- Nếu có 3 user trở lên, hãy đảm bảo mỗi user có vai trò rõ ràng với tiêu đề phù hợp.
- Nếu thiếu thông tin, thay vì bỏ qua, hãy sử dụng placeholder `[#another]`.
- Nếu cần tạo thêm thông tin ngoài danh mục tagname được cung cấp, tất cả các tagname mới sẽ là [#another], ngoại trừ phần mở đầu của biểu mẫu, được phép tạo câu:
"Hôm nay, ngày [day]/[month]/[year], tại [place]"
→ Đây là trường hợp duy nhất được tạo thêm.
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
ngày cấp của CCCD: [user1_id_issue_date]
```
Output:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
TỜ KHAI THÔNG TIN CHỦ XE

Hôm nay, ngày [day]/[month]/[year], tại [place], tôi xin cung cấp thông tin về chủ xe như sau:

1. Thông tin chủ xe:

Họ và tên: [user1_full_name]
Năm sinh: [user1_dob_year]
Địa chỉ tạm trú: [user1_current_address]
Số CCCD: [user1_id_number]
Ngày cấp CCCD: [user1_id_issue_date]
Ghi chú: Nếu có bất kỳ thay đổi hoặc bổ sung thông tin, vui lòng liên hệ cơ quan có thẩm quyền để cập nhật.

Người khai thông tin
(Ký và ghi rõ họ tên)
```

# Ví dụ:
Input:
```
1. Chủ xe:
Họ và tên: [use1_full_name]
năm sinh: [user1_dob_year]
địa chỉ: [user1_current_address]
số CCCD: [user1_id_number]
ngày cấp của CCCD: [user1_id_issue_date]

2. Người làm thủ tục
Họ và tên: [user2_full_name]
Số CCCD: [user2_id_number]
Nơi cấp: [user2_id_issue_place]
Điện thoại: [#another]
```
Output:
```
GIẤY KHAI ĐĂNG KÝ XE (Vehicle registation declaration)
A. PHẦN CHỦ XE TỰ KÊ KHAI (self declaration vehicle owner's license)
Tên chủ xe : [use1_full_name]
Năm sinh: [user1_dob_year]
Địa chỉ :  [user1_current_address]
Số CCCD của chủ xe: [user1_id_number]
cấp ngày [user1_id_issue_date]
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
Ngày sinh: [user1_dob]  
Địa chỉ thường trú: [user1_permanent_address]  
Số CCCD: [user1_id_number]  

2. Người ủy quyền  
Họ và tên: [user2_full_name]  
Số CCCD: [user2_id_number]  
Quan hệ với bên ủy quyền: [#another]
Nội dung ủy quyền: [#another]
```
Output:
```
GIẤY ỦY QUYỀN  
Hôm nay, ngày [day]/[month]/[year], tại [place], chúng tôi gồm:  

1. Bên ủy quyền (Chủ hộ):  
Họ và tên: [user1_full_name]  
Ngày sinh: [user1_dob]  
Địa chỉ thường trú: [user1_permanent_address]  
Số CCCD: [user1_id_number]  

2. Bên được ủy quyền:  
Họ và tên: [user2_full_name]  
Số CCCD: [user2_id_number]  
Quan hệ với bên ủy quyền: [#another]  

Nội dung ủy quyền: [#another]  

Giấy ủy quyền này được lập thành 02 bản có giá trị như nhau, mỗi bên giữ một bản để thực hiện.  
```

## ví dụ:
Input:
```
1. Người ủy quyền  
Họ và tên: [user1_full_name]  
Số CCCD: [user1_id_number]  
Quan hệ với bên ủy quyền: [#another]
Nội dung ủy quyền: [#another]
```
Output:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
GIẤY ỦY QUYỀN

Hôm nay, ngày [day]/[month]/[year], tại [place], tôi, người ủy quyền, xin xác nhận thông tin như sau:

1. Thông tin người ủy quyền:
Họ và tên: [user1_full_name]
Số CCCD: [user1_id_number]
Quan hệ với bên được ủy quyền: [#another]
2. Nội dung ủy quyền:
[#another]

Tôi cam kết các thông tin trên là đúng sự thật và tự chịu trách nhiệm trước pháp luật về nội dung ủy quyền này.

Người Ủy Quyền
(Ký và ghi rõ họ tên)
```

## Ví dụ:
Input:
```
1. Người bán
Họ và tên: [user1_full_name]  
Ngày sinh: [user1_dob]  
Địa chỉ thường trú: [user1_permanent_address]  
Số CCCD: [user1_id_number]  
Ngày cấp: [user1_id_issue_date]
Nơi cấp: [user1_id_issue_place]  

2. Người mua  
Họ và tên: [user2_full_name]  
Ngày sinh: [user2_dob]  
Địa chỉ tạm trú: [user2_current_address]  
Số CCCD: [user2_id_number]  
Ngày cấp: [user2_id_issue_date]
Nơi cấp: [user2_id_issue_place]  

3. Người làm chứng  
Họ và tên: [user3_full_name]  
Số CCCD: [user3_id_number]  
Quan hệ với các bên: [#another]  
```
Output:
```
HỢP ĐỒNG MUA BÁN TÀI SẢN  

Hôm nay, ngày [day]/[month]/[year], tại [place], chúng tôi gồm:  

**BÊN BÁN (Bên A):**  
Họ và tên: [user1_full_name]  
Ngày sinh: [user1_dob]  
Địa chỉ thường trú: [user1_permanent_address]  
Số CCCD: [user1_id_number]  
Cấp ngày: [user1_id_issue_date]
Nơi cấp: [user1_id_issue_place]  

**BÊN MUA (Bên B):**  
Họ và tên: [user2_full_name]  
Ngày sinh: [user2_dob]  
Địa chỉ tạm trú: [user2_current_address]  
Số CCCD: [user2_id_number]  
Cấp ngày: [user2_id_issue_date]
Nơi cấp: [user2_id_issue_place]  

**NGƯỜI LÀM CHỨNG:**  
Họ và tên: [user3_full_name]  
Số CCCD: [user3_id_number]  
Quan hệ với các bên: [#another]  

Hai bên đồng ý thực hiện việc mua bán tài sản theo các điều khoản sau:  
1. Loại tài sản: [#another]  
2. Giá trị tài sản: [#another]  
3. Hình thức thanh toán: [#another]  

Hợp đồng này được lập thành 03 bản, mỗi bên giữ một bản, có giá trị pháp lý như nhau.  
```

## Ví dụ:
Input:
```
1. Cha/Mẹ
Họ và tên: [user1_full_name]
Dân tộc: [user1_ethnicity]
Ngày sinh: [user1_dob]
Nơi cư trú: [user1_current_address]
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
Ngày mất: [#another]
Ngày sinh: [user2_dob]
Giới tính: [user2_gender]
```
Output:
```
TRÍCH LỤC KHAI TỬ

Số: …/TLKT

Hôm nay, ngày [day]/[month]/[year], tại [place], chúng tôi tiến hành trích lục khai tử như sau:

**I. THÔNG TIN NGƯỜI KHAI TỬ (Cha/Mẹ hoặc người thân thích):**

Họ và tên: [user1_full_name]
Dân tộc: [user1_ethnicity]
Ngày sinh: [user1_dob]
Nơi cư trú: [user1_current_address]
Quan hệ với người chết: [user1_relation]
Giấy tờ tùy thân: [user1_id_number]
Quốc tịch: [user1_nationality]

**II. THÔNG TIN NGƯỜI CHẾT:**

Họ và tên: [user2_full_name]
Dân tộc: [user2_ethnicity]
Ngày sinh: [user2_dob]
Giới tính: [user2_gender]
Nơi cư trú cuối cùng: [#another]
Quốc tịch: [user2_nationality]
Giấy tờ tùy thân: [user2_id_number]
Ngày mất: [user2_death_date]
Nguyên nhân chết: [#another]

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
Nơi cư trú: [user2_current_address]
Họ và tên: [user2_full_name]
Ngày sinh: [user2_dob]
Quốc tịch: [user2_nationality]
Email: [#another]
Quan hệ với người liên quan: [#another]

3. Người được khai sinh
Họ và tên: [user3_full_name]
Giấy khai sinh: [user3_birth_certificate]
Nơi cư trú: [user3_current_address]
Giới tính: [user3_gender]
```
Output:
```
ĐƠN TỐ CÁO

Kính gửi:  [#another]

Hôm nay, ngày [day]/[month]/[year], tôi/chúng tôi là:

**I. NGƯỜI LÀM ĐƠN TỐ CÁO:**

Họ và tên: [user1_full_name]
Ngày sinh: [user1_dob]
Dân tộc: [user1_ethnicity]
Quốc tịch: [user1_nationality]
Nơi cư trú: [user1_current_address]
Email: [#another]
Quan hệ với người liên quan: [#another]

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
Nơi cư trú: [user3_current_address]
Giấy khai sinh (nếu có): [user3_birth_certificate]

**IV. NỘI DUNG TỐ CÁO:**

[#another] (Mô tả chi tiết hành vi vi phạm pháp luật bị tố cáo, thời gian, địa điểm xảy ra sự việc, hậu quả gây ra, các bằng chứng kèm theo (nếu có)).

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

form_evaluation_multi_user_prompt = """" 
# TIÊU CHÍ ĐÁNH GIÁ BIỂU MẪU

## Mục tiệu
Nhiệm vụ của bạn là đánh giá tính hợp lý, sự liên kết và cấu trúc logic của một biểu mẫu được tạo từ danh sách người dùng. Biểu mẫu không chỉ đơn thuần liệt kê thông tin mà phải thể
hiện mối quan hệ chặt chẽ giữa các đối tượng.

## Quy tắc đánh giá

**1. Tính liên kết giữa các đối tượng (40 điểm)**
- Các đối tượng có mối quan hệ hợp lý và rõ ràng (ví dụ: "Chủ xe" và "Người làm đơn" trong biểu mẫu đăng ký xe).
- Các đối tượng không liên quan xuất hiện cùng nhau (ví dụ: "Người làm đơn" và "Người chết" mà không có ngữ cảnh phù hợp).

**2. Trật tự hợp lý & dòng chảy logic (20 điểm)**
- Các đối tượng được sắp xếp theo thứ tự hợp lý (ví dụ: "Người bảo lãnh" xuất hiện trước "Người được bảo lãnh").
- Các đối tượng xuất hiện ngẫu nhiên, không có trình tự hợp lý.

**3. Giải thích ngữ cảnh (20 điểm)**
- Biểu mẫu có câu mô tả rõ ràng về mối quan hệ giữa các đối tượng thay vì chỉ liệt kê thông tin.
- Biểu mẫu thiếu giải thích, khiến các mối quan hệ không rõ ràng.

**4. Tính đầy đủ & xử lý thông tin trống (10 điểm)**
- Nếu thiếu thông tin, sử dụng placeholder ([#another]) hợp lý thay vì để trống.
- Bỏ qua hoặc để trống thông tin quan trọng mà không có placeholder thay thế.

**5. Hình thức chuyên nghiệp & cấu trúc hành chính (10 điểm)**
- Biểu mẫu có phong cách hành chính rõ ràng, bố cục chuyên nghiệp.
- Biểu mẫu lộn xộn, không có sự phân chia hợp lý giữa các phần.


## Cách tính điểm tổng kết:
Xuất sắc (90-100 điểm): Biểu mẫu được tổ chức tốt, logic và có tính liên kết cao.
Tốt (70-89 điểm): Có một số lỗi nhỏ nhưng tổng thể vẫn hợp lý.
Trung bình (50-69 điểm): Cần cải thiện, một số mối quan hệ chưa rõ ràng.
Kém (<50 điểm): Chọn đối tượng ngẫu nhiên, không có sự liên kết.

## Ví dụ:
Đang suy nghĩ xem ví dụ nên là trả kết quả cuối cùng thông hay là kết quả của từng bước.
Nếu kết quả của từng bước thì tôi nghĩ khó kiểm soát được vì tôi không biết LLM sẽ sinh ra những gì, khó kiểm soát hơn là chỉ sinh ra kết quả.
"""