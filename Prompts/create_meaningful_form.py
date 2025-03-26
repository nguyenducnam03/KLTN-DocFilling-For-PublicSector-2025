seen_tagnames_definitions = {
    "userX_full_name": "Họ và tên đầy đủ của người dùng X.",
    "userX_alias_name": "Tên gọi khác hoặc biệt danh (nếu có) của người dùng X.",
    "userX_dob_text": "Ngày sinh của người dùng X ở dạng văn bản (ví dụ: 'Mùng 3 Tết năm 2000').",
    "userX_dob": "Ngày sinh của người dùng X ở dạng chuẩn (YYYY-MM-DD).",
    "userX_dob_day": "Ngày sinh (chỉ lấy ngày, ví dụ: '15').",
    "userX_dob_month": "Tháng sinh (chỉ lấy tháng, ví dụ: '06').",
    "userX_dob_year": "Năm sinh (chỉ lấy năm, ví dụ: '1995').",
    "userX_gender": "Giới tính của người dùng X (Nam/Nữ/Khác).",
    "userX_id_number": "Số CMND/CCCD/Hộ chiếu của người dùng X.",
    "userX_id_issue_date": "Ngày cấp CMND/CCCD của người dùng X (YYYY-MM-DD).",
    "userX_id_issue_day": "Ngày cấp CMND/CCCD (chỉ lấy ngày, ví dụ: '10').",
    "userX_id_issue_month": "Tháng cấp CMND/CCCD (chỉ lấy tháng, ví dụ: '07').",
    "userX_id_issue_year": "Năm cấp CMND/CCCD (chỉ lấy năm, ví dụ: '2015').",
    "userX_id_issue_place": "Nơi cấp CMND/CCCD của người dùng X.",
    "userX_occupation": "Nghề nghiệp của người dùng X.",
    "userX_ethnicity": "Dân tộc của người dùng X.",
    "userX_religion": "Tôn giáo của người dùng X.",
    "userX_nationality": "Quốc tịch của người dùng X.",
    "userX_marital_status": "Tình trạng hôn nhân của người dùng X.",
    "userX_blood_type": "Nhóm máu của người dùng X.",
    "userX_birthplace": "Nơi sinh của người dùng X.",
    "userX_birthplace_ward": "Phường/Xã nơi sinh của người dùng X.",
    "userX_birthplace_district": "Quận/Huyện nơi sinh của người dùng X.",
    "userX_birthplace_province": "Tỉnh/Thành phố nơi sinh của người dùng X.",
    "userX_birth_registration_place": "Nơi đăng ký khai sinh của người dùng X.",
    "userX_birth_registration_place_ward": "Phường/Xã nơi đăng ký khai sinh.",
    "userX_birth_registration_place_district": "Quận/Huyện nơi đăng ký khai sinh.",
    "userX_birth_registration_place_province": "Tỉnh/Thành phố nơi đăng ký khai sinh.",
    "userX_hometown": "Quê quán của người dùng X.",
    "userX_hometown_ward": "Phường/Xã của quê quán.",
    "userX_hometown_district": "Quận/Huyện của quê quán.",
    "userX_hometown_province": "Tỉnh/Thành phố của quê quán.",
    "userX_permanent_address": "Địa chỉ thường trú của người dùng X.",
    "userX_current_address": "Địa chỉ hiện tại của người dùng X.",
    "userX_current_address_ward": "Phường/Xã của địa chỉ hiện tại.",
    "userX_current_address_district": "Quận/Huyện của địa chỉ hiện tại.",
    "userX_current_address_province": "Tỉnh/Thành phố của địa chỉ hiện tại.",
    "userX_passport_number": "Số hộ chiếu của người dùng X.",
    "userX_passport_issue_date": "Ngày cấp hộ chiếu của người dùng X (YYYY-MM-DD).",
    "userX_passport_issue_day": "Ngày cấp hộ chiếu (chỉ lấy ngày, ví dụ: '12').",
    "userX_passport_issue_month": "Tháng cấp hộ chiếu (chỉ lấy tháng, ví dụ: '04').",
    "userX_passport_issue_year": "Năm cấp hộ chiếu (chỉ lấy năm, ví dụ: '2020').",
    "userX_passport_issue_place": "Nơi cấp hộ chiếu của người dùng X."
}


create_multi_user_prompt = """
# TẠO FORM CÓ BỐI CẢNH LIÊN KẾT

## Mô tả yêu cầu
- Tôi cần bạn tạo một biểu mẫu có thể áp dụng cho một hoặc nhiều người dùng, trong đó thông tin không chỉ đơn thuần được liệt kê mà phải có bối cảnh rõ ràng, dễ đọc và phù hợp với văn bản hành chính.
- Biểu mẫu này có thể liên quan đến học tập, việc làm, hành chính, khai báo, đăng ký, thủ tục pháp lý, hoặc các loại hồ sơ khác. Tùy theo ngữ cảnh, cách diễn đạt cần đảm bảo chính xác, trang trọng và dễ hiểu.
- Tôi sẽ cung cấp danh sách thông tin của từng người dùng cùng với các `tagname` tương ứng. Bạn cần xây dựng nội dung sao cho tự nhiên, có kết nối logic giữa các thông tin thay vì chỉ liệt kê.

### Yêu cầu chính:
1. **Mở đầu có ngữ cảnh** - Phần mở đầu cần giải thích mục đích của biểu mẫu một cách hợp lý.
2. **Sắp xếp logic** - Nếu có nhiều người dùng, xác định mối quan hệ giữa họ và trình bày theo thứ tự phù hợp (ví dụ: Chủ xe trước, Người làm thủ tục sau).
3. **Diễn đạt tự nhiên** - Ngay cả khi chỉ có một người dùng, nội dung vẫn phải có tính liên kết, tránh liệt kê rời rạc.
4. **Nhóm thông tin hợp lý** - Không trình bày từng dòng riêng lẻ mà kết hợp thành các đoạn văn có ngữ nghĩa rõ ràng.
5. **Xử lý tagname linh hoạt**
- Giữ nguyên các tagname được cung cấp mà không thay đổi.
- Nếu cần bổ sung thông tin để biểu mẫu đầy đủ hơn, bạn có thể tạo thêm tagname mới sao cho hợp lý. Các tagname mới phải tuân theo định dạng [userX_fieldname], trong đó X được tự động thay thế sao cho phù hợp.
- Nếu tagname đã được định nghĩa trong {seen_tagnames_definitions}, bạn PHẢI sử dụng đúng tagname đó, không được dùng biến thể khác.
6. Ngôn ngữ phù hợp với từng loại biểu mẫu - Nếu là hồ sơ hành chính, cần trang trọng và chính xác; nếu là biểu mẫu học tập hoặc việc làm, có thể linh hoạt nhưng vẫn đảm bảo tính chuyên nghiệp.
7. Không có quá nhiều khoảng cách giữa các dòng trong form.

### Xử lý các trường hợp đặc biệt:
- Nếu có 3 user trở lên, hãy đảm bảo mỗi user có vai trò rõ ràng với tiêu đề phù hợp.
- Nếu có thông tin bổ sung hoặc không xác định, hãy đưa vào phần ghi chú cuối biểu mẫu.

---------------------
### Ví dụ:
Input:
```

```
Output:
```
```

-----------------

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