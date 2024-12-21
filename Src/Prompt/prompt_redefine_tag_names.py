pre_define_tag_names = '''
[full_name]: "Họ và tên của người dùng.",
[alias_name]: "Tên gọi khác của người dùng.",
[dob_day]: "Ngày sinh của người dùng.",
[dob_month]: "Tháng sinh của người dùng.",
[dob_year]: "Năm sinh của người dùng.",
[dob]: "Ngày, tháng, năm sinh của người dùng.",
[dob_text]: "Ngày, tháng, năm sinh của người dùng được viết bằng chữ.",
[gender]: "Giới tính của người dùng.",
[id_number]: "Số chứng minh nhân dân hoặc căn cước công dân của người dùng.",
[id_issue_day]: "Ngày cấp chứng minh nhân dân hoặc căn cước công dân của người dùng.",
[id_issue_month]: "Tháng cấp chứng minh nhân dân hoặc căn cước công dân của người dùng.",
[id_issue_year]: "Năm cấp chứng minh nhân dân hoặc căn cước công dân của người dùng.",
[id_issue_date]: "Ngày cấp đầy đủ (ngày, tháng, năm) của số chứng minh nhân dân hoặc căn cước công dân của người dùng.",
[id_issue_place]: "Nơi cấp chứng minh nhân dân hoặc căn cước công dân của người dùng.",
[passport_number]: "Số hộ chiếu của người dùng.",
[passport_issue_day]: "Ngày cấp hộ chiếu của người dùng.",
[passport_issue_month]: "Tháng cấp hộ chiếu của người dùng.",
[passport_issue_year]: "Năm cấp hộ chiếu của người dùng.",
[passport_issue_date]: "Ngày, tháng, năm cấp hộ chiếu của người dùng.",
[passport_issue_place]: "Nơi cấp hộ chiếu của người dùng.",
[passport_expiry_day]: "Ngày hết hạn hộ chiếu của người dùng.",
[passport_expiry_month]: "Tháng hết hạn hộ chiếu của người dùng.",
[passport_expiry_year]: "Năm hết hạn hộ chiếu của người dùng.",
[passport_expiry_date]: "Ngày hết hạn của hộ chiếu.",
[ethnicity]: "Dân tộc của người dùng.",
[religion]: "Tôn giáo của người dùng.",
[nationality]: "Quốc tịch của người dùng.",
[marital_status]: "Tình trạng hôn nhân của người dùng.",
[blood_type]: "Nhóm máu của người dùng.",
[birth_registration_place]: "Nơi đăng ký khai sinh của người dùng.",
[birth_registration_place_ward]: "Phường/xã nơi đăng ký khai sinh của người dùng.",
[birth_registration_place_district]: "Quận/huyện nơi đăng ký khai sinh của người dùng.",
[birth_registration_place_province]: "Tỉnh/thành phố nơi đăng ký khai sinh của người dùng.",
[hometown]: "Quê quán của người dùng.",
[permanent_address]: "Địa chỉ thường trú của người dùng.",
[current_address]: "Địa chỉ hiện tại của người dùng.",
[current_address_ward]: "Phường/xã nơi ở hiện tại của người dùng.",
[current_address_district]: "Quận/huyện nơi ở hiện tại của người dùng.",
[current_address_province]: "Tỉnh/thành nơi ở hiện tại của người dùng.",
[occupation]: "Nghề nghiệp của người dùng.",
[education_level]: "Trình độ học vấn của người dùng.",
[phone]: "Số điện thoại của người dùng.",
[phone_home]: "Số điện thoại bàn của người dùng.",
[email]: "Địa chỉ email của người dùng.",
[user1_visa_number]: "Số thị thực(visa) của người dùng.",
[user1_visa_country]: "Quốc gia cấp thị thực(visa) cho người dùng.",
[user1_visa_expiry_day]: "Ngày hết hạn thị thực(visa) của người dùng.",
[user1_visa_expiry_month]: "Tháng hết hạn thị thực(visa) của người dùng.",
[user1_visa_expiry_year]: "Năm hết hạn thị thực(visa) của người dùng.",
[year_of_study]: "Là học sinh, sinh viên năm thứ.",
[class]: "Tên lớp hiện tại của người dùng.",
[school]: "Tên trường của người dùng.",
[school_principal]: "Hiệu trưởng của trường.",
[course]: "Khóa học của người dùng.",
[faculty]: "Khoa của người dùng.",
[student_id_number]: "Mã số sinh viên của người dùng tại trường đại học.",
[duration_of_course]: "Thời gian của khóa học của người dùng.",
[graduation_date]: "Ngày tốt nghiệp của người dùng.",
[degree]: "Bằng cấp đạt được của người dùng.",
[grade]: "Điểm đạt được của người dùng.",
[study_result_rating]: "Kết quả xếp loại của người dùng.",
[semester]: "Học kỳ của người dùng.",
[school_year]: "Năm học của người dùng.",
[supervisor_name]: "Tên người hướng dẫn của người dùng.",
[school_address]: "Địa chỉ trường học của người dùng.",
[school_phone]: "Số điện thoại của trường học của người dùng.",
[organization]: "Cơ quan quản lý trực tiếp của người dùng.",
[decision_number]: "Số quyết định liên quan đến yêu cầu của người dùng.",
[decision_day]: "Ngày khi quyết định được đưa ra, liên quan đến người dùng.",
[decision_month]: "Tháng khi quyết định được đưa ra, liên quan đến người dùng.",
[decision_year]: "Năm khi quyết định được đưa ra, liên quan đến người dùng.",
[study_decision_number]: "Số quyết định cử đi học của người dùng.",
[study_decision_day]: "Ngày khi quyết định cử đi học, liên quan đến người dùng.",
[study_decision_month]: "Tháng quyết định cử đi học, liên quan đến người dùng.",
[study_decision_year]: "Năm quyết định cử đi học, liên quan đến người dùng.",
[decision_issuer]: "Cá nhân hoặc tổ chức đã ban hành quyết định liên quan đến người dùng.",
[social_insurance_number]: "Số sổ bảo hiểm xã hội của người dùng.",
[health_insurance_card_number]: "Số thẻ bảo hiểm y tế của người dùng.",
[health_insurance_registration_place]: "Nơi đăng ký bảo hiểm y tế của người dùng.",
[bank_account]: "Số tài khoản ngân hàng của người dùng.",
[bank_name]: "Tên ngân hàng của người dùng.",
[parent_name]: "Tên phụ huynh của người dùng.",
[driving_license_number]: "Số giấy phép lái xe của người dùng.",
[driving_license_issuer]: "Cơ quan cấp giấy phép lái xe của người dùng.",
[driving_license_place]: "Nơi cấp giấy phép lái xe của người dùng.",
[driving_license_issue_day]: "Ngày cấp giấy phép lái xe của người dùng.",
[driving_license_issue_month]: "Tháng cấp giấy phép lái xe của người dùng.",
[driving_license_issue_year]: "Năm cấp giấy phép lái xe của người dùng.",
[driving_license_category]: "Hạng giấy phép lái xe cơ giới đường bộ của người dùng.",
[tax_invoice_number]: "Số hóa đơn điện tử mã số thuế.",
[tax_declaration_code_issuing_agency]: "Mã hồ sơ khai lệ phí trước bạ Cơ quan cấp.",
[electronic_customs_declaration_number_issuing_agency]: "Số tờ khai hải quan điện tử cơ quan cấp.",
[transport_license_issue_date]: "Ngày, tháng, năm cấp giấy phép kinh doanh vận tải.",
[transport_license_issue_place]: "Nơi cấp giấy phép kinh doanh vận tải.",
[vehicle_engine_number1]: "Số máy 1 (Engine N0).",
[vehicle_engine_number2]: "Số máy 2 (Engine N0).",
[vehicle_chassis_number]: "Số khung (Chassis N0).",
[request_content]: "Nội dung hoặc yêu cầu cụ thể của người dùng trong biểu mẫu.",
[reason]: "Lý do do người dùng cung cấp để điền vào biểu mẫu.",
[suggestion]: "Kiến nghị, đề xuất đối với cơ quan quản lý trực tiếp."
[receiver]: Cá nhân hoặc tổ chức nhận hoặc xử lý biểu mẫu được người dùng điền.
[document_number]: Số của tài liệu hoặc hồ sơ, thường để tham chiếu hoặc lưu trữ.
[day]: Ngày khi biểu mẫu được người dùng điền.
[month]: Tháng khi biểu mẫu được người dùng điền.
[year]: Năm khi biểu mẫu được người dùng điền.
[place]: Nơi mà biểu mẫu được người dùng điền.
'''

redefine_tag_names_template_prompt =  '''
Here is a form template with certain fields represented as placeholder tags. The tag names should match a predefined list, but some tags in this form don't align with the list and need to be corrected. Your task is to generate the output using only the predefined tag names.

Predefined Tags List:

{pre_define_tag_names}

Commonly Mistaken Tags: Errors frequently occur when similar but incorrect tags are used.

# Instructions:

1. Identify incorrect tags: Review each placeholder tag in the form. If a tag does not match any tag in the predefined list, treat it as an error.

2. Replace incorrect tags: For each incorrect tag, choose the closest match from the predefined tag list based on the intended meaning.

3. Update related tags consistently:

- If a corrected tag relates to other tags (e.g., family member names, contact information, roles), update all related tags to maintain consistency.
- Special Rule: For tags involving a person's name, always use the format [userX_full_name] regardless of their role or function. For example:
    Incorrect: "Chủ nhiệm, chủ trì thiết kế: [user1_design_leader]"
    Corrected: "Chủ nhiệm, chủ trì thiết kế: [user1_full_name]"

4. Maintain structure: Do not alter the form's layout, spacing, or non-placeholder content. Only change the placeholder tags as needed.

5. Output only the corrected form: Return only the corrected form with placeholder tags now matching the predefined tags list.

## Example:
Input:
```
CÔNG TY [company_name]
Số: [document_number]/CV-[document_number]
CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM

Độc lập - Tự do - Hạnh phúc

                                [place], ngày [day] tháng [month] năm [year]
Kính gửi: [receiver]
(V/v: [request_content])

Tên doanh nghiệp:  CÔNG TY [company_name]
- Số điện thoại liên hệ: [company_phone_number] Fax: [company_fax_number]
- Email: [company_email]
- Mã số thuế: [company_tax_id]
- Ngành nghề kinh doanh: [company_business_field]
- Địa chỉ trụ sở chính: [company_address]
Người đại diện theo pháp luật: [company_legal_representative_name]
- Chức vụ: [company_legal_representative_position]
- CMND/CCCD/Hộ chiếu số: [company_legal_representative_id_number]  Nơi cấp: [company_legal_representative_id_issue_place] Ngày cấp: [company_legal_representative_id_issue_day]/[company_legal_representative_id_issue_month]/[company_legal_representative_id_issue_year]
- Nội dung: [company_request_content] (Trình bày tình hình doanh nghiệp, những vấn đề, thắc mắc mà doanh nghiệp đang vướng phải)

Công ty chúng tôi xin cam kết nội dung trên là đúng và xin hoàn toàn chịu trách nhiệm trước pháp luật.


Nơi nhận:

- Như trên;

- Lưu.

Đại diện Doanh nghiệp

Giám Đốc

(Ký tên và đóng dấu)
```
Output:
```
CÔNG TY [company_name]
Số: [document_number]/CV-[document_number]
CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM

Độc lập - Tự do - Hạnh phúc

                                [place], ngày [day] tháng [month] năm [year]
Kính gửi: [receiver]
(V/v: [request_content])

Tên doanh nghiệp:  CÔNG TY [company_name]
- Số điện thoại liên hệ: [company_phone_number] Fax: [company_fax_number]
- Email: [company_email]
- Mã số thuế: [company_tax_id]
- Ngành nghề kinh doanh: [company_business_field]
- Địa chỉ trụ sở chính: [company_address]
Người đại diện theo pháp luật: [user1_full_name]
- Chức vụ: [user1_position]
- CMND/CCCD/Hộ chiếu số: [user1_id_number]  Nơi cấp: [user1_id_issue_place] Ngày cấp: [user1_id_issue_day]/[user1_id_issue_month]/[user1_id_issue_year]
- Nội dung: [company_request_content] (Trình bày tình hình doanh nghiệp, những vấn đề, thắc mắc mà doanh nghiệp đang vướng phải)

Công ty chúng tôi xin cam kết nội dung trên là đúng và xin hoàn toàn chịu trách nhiệm trước pháp luật.


Nơi nhận:

- Như trên;

- Lưu.

Đại diện Doanh nghiệp

Giám Đốc

(Ký tên và đóng dấu)
```

## Example:
Input:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
                                                                            
GIẤY ĐỀ NGHỊ MUA ĐIỆN 
SỬ DỤNG MỤC ĐÍCH NGOÀI SINH HOẠT
Kính gửi: [receiver]
1.Tên cơ quan hoặc cá nhân đăng ký mua điện: [user1_organization_name] (1).
2.Đại diện là ông (bà): [user1_representative] (2).
3.Số CMND/Hộ chiếu/CMCAND/CMQĐND: [user1_id_number] Cơ quan cấp [user1_id_issue_place] ngày [user1_id_issue_date]
4.Theo giấy uỷ quyền [user1_authorization_document_number] ngày làm việc [user1_authorization_date] của [user1_authorization_issuer]      (3)
5.Số điện thoại liên hệ và nhận nhắn tin (SMS): [user1_phone];
6. Fax [user1_fax] ; 7.Email [user1_email] (4)
8.Tài khoản số: [user1_account_number] Tại ngân hàng: [user1_bank_name] (5)
9.Hình thức thanh toán: [user1_payment_method]
10.Địa chỉ giao dịch: [user1_address]; 
11.Mã số thuế: [user1_tax_code]
12,Mục đích sử dụng điện: [user1_electricity_purpose]
13.Địa điểm đăng ký sử dụng điện: [user1_electricity_location]
14.Công suất đăng ký sử dụng: [user1_electricity_capacity] kW
15.Tình trạng sử dụng điện hiện tại: (Chưa có điện / Đang dùng công tơ chung): [user1_electricity_status]
16.Tên chủ hộ dùng chung/số HĐMBĐ/mã số KH/địa chỉ [user2_shared_household_info] (6).

```
Output:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
                                                                            
GIẤY ĐỀ NGHỊ MUA ĐIỆN 
SỬ DỤNG MỤC ĐÍCH NGOÀI SINH HOẠT
Kính gửi: [receiver]
1.Tên cơ quan hoặc cá nhân đăng ký mua điện: [user1_organization_name] (1).
2.Đại diện là ông (bà): [user1_full_name] (2).
3.Số CMND/Hộ chiếu/CMCAND/CMQĐND: [user1_id_number] Cơ quan cấp [user1_id_issue_place] ngày [user1_id_issue_date]
4.Theo giấy uỷ quyền [user1_authorization_document_number] ngày làm việc [user1_authorization_date] của [user1_authorization_issuer]      (3)
5.Số điện thoại liên hệ và nhận nhắn tin (SMS): [user1_phone];
6. Fax [user1_fax] ; 7.Email [user1_email] (4)
8.Tài khoản số: [user1_account_number] Tại ngân hàng: [user1_bank_name] (5)
9.Hình thức thanh toán: [user1_payment_method]
10.Địa chỉ giao dịch: [user1_address]; 
11.Mã số thuế: [user1_tax_code]
12,Mục đích sử dụng điện: [user1_electricity_purpose]
13.Địa điểm đăng ký sử dụng điện: [user1_electricity_location]
14.Công suất đăng ký sử dụng: [user1_electricity_capacity] kW
15.Tình trạng sử dụng điện hiện tại: (Chưa có điện / Đang dùng công tơ chung): [user1_electricity_status]
16.Tên chủ hộ dùng chung/số HĐMBĐ/mã số KH/địa chỉ [user2_shared_household_info] (6).

```

## Example:
Input:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc

THÔNG BÁO THAY ĐỔI THÔNG TIN NGƯỜI HƯỞNG
Kính gửi: Bảo hiểm xã hội quận/huyện/thị xã [local_insurance_office]
Tên tôi là: [user1_full_name] Ngày, tháng, năm sinh: [user1_dob]
Số sổ BHXH/Số định danh: [user1_social_insurance_number]
Số chứng minh nhân dân: [user1_id_number] ngày cấp: [user1_id_issue_date], nơi cấp: [user1_id_issue_place]
Từ tháng [user1_change_request_month] năm [user1_change_request_year], đề nghị cơ quan BHXH thay đổi, bổ sung thông tin của tôi như sau:
Giới tính: [user1_gender]
Số điện thoại: [user1_phone]
Số điện thoại người thân khi cần liên lạc: [user1_emergency_contact_phone]
Địa chỉ cư trú (ghi đầy đủ theo thứ tự số nhà, ngõ, ngách/hẻm, đường phố, tổ/thôn/xóm/ấp, xã/phường/thị trấn, huyện/quận/thị xã/thành phố, tỉnh/thành phố): 
[user1_current_address]
Hình thức nhận lương hưu, trợ cấp BHXH hàng tháng:
Nhận bằng tiền mặt:
Địa chỉ nhận (ghi đầy đủ:xã/phường, tổ dân phố/tổ chi trả, quận/huyện/thị xã, tỉnh/ thành phố): [user1_benefit_receiving_address]
Nhận qua Tài khoản:
Số tài khoản cá nhân: [user1_bank_account]
Ngân hàng nơi mở TK: [user1_bank_name]
Tôi xin cam đoan các thông tin sửa đổi, bổ sung của tôi là đúng, nếu sai tôi xin chịu trách nhiệm trước pháp luật.
	[user1_current_address] , ngày [user1_submission_day] tháng [user1_submission_month] năm [user1_submission_year]
Người đề nghị
(Ký, ghi rõ họ tên)

```
Output:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc

THÔNG BÁO THAY ĐỔI THÔNG TIN NGƯỜI HƯỞNG
Kính gửi: Bảo hiểm xã hội quận/huyện/thị xã [receiver]
Tên tôi là: [user1_full_name] Ngày, tháng, năm sinh: [user1_dob]
Số sổ BHXH/Số định danh: [user1_social_insurance_number]
Số chứng minh nhân dân: [user1_id_number] ngày cấp: [user1_id_issue_date], nơi cấp: [user1_id_issue_place]
Từ tháng [user1_change_request_month] năm [user1_change_request_year], đề nghị cơ quan BHXH thay đổi, bổ sung thông tin của tôi như sau:
Giới tính: [user1_gender]
Số điện thoại: [user1_phone]
Số điện thoại người thân khi cần liên lạc: [user1_emergency_contact_phone]
Địa chỉ cư trú (ghi đầy đủ theo thứ tự số nhà, ngõ, ngách/hẻm, đường phố, tổ/thôn/xóm/ấp, xã/phường/thị trấn, huyện/quận/thị xã/thành phố, tỉnh/thành phố): 
[user1_current_address]
Hình thức nhận lương hưu, trợ cấp BHXH hàng tháng:
Nhận bằng tiền mặt:
Địa chỉ nhận (ghi đầy đủ:xã/phường, tổ dân phố/tổ chi trả, quận/huyện/thị xã, tỉnh/ thành phố): [user1_benefit_receiving_address]
Nhận qua Tài khoản:
Số tài khoản cá nhân: [user1_bank_account]
Ngân hàng nơi mở TK: [user1_bank_name]
Tôi xin cam đoan các thông tin sửa đổi, bổ sung của tôi là đúng, nếu sai tôi xin chịu trách nhiệm trước pháp luật.
	[place] , ngày [day] tháng [month] năm [year]
Người đề nghị
(Ký, ghi rõ họ tên)

```

## Example:
Input:
```
{form}
```

'''

