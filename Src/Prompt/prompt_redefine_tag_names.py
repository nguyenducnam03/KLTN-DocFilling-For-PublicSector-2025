redefine_full_name_template_prompt =  '''
# Hãy thực hiện tác vụ sau đây:  
1. Đọc nội dung văn bản bên dưới.  
2. Xác định tất cả các thông tin liên quan đến từng người dùng (user) trong văn bản, bao gồm:  
   - Họ và tên.  
   - Ngày/tháng/năm sinh.  
   - Giới tính (nếu có).  
   - Giấy tờ tùy thân (số CMND, ngày cấp, nơi cấp).  
   - Địa chỉ (hộ khẩu thường trú, nơi ở hiện tại).  
   - Quan hệ với người chết (nếu có).  
3. Với mỗi thông tin liên quan đến một user:  
   - Đổi các tag tương ứng thành dạng `[userX_<field_name>]`, với `X` là thứ tự xuất hiện của người đó trong danh sách (bắt đầu từ 1), và `<field_name>` là trường thông tin (ví dụ: `full_name`, `dob_day`, `id_number`, v.v.).  
  - Nếu tag đã đúng định dạng, kiểm tra xem thứ tự `X` có khớp với thứ tự thực tế của user trong văn bản hay không. Nếu không khớp, chỉnh sửa lại cho đúng.

**Lưu ý**:  
- Chỉ chỉnh sửa các tag liên quan đến thông tin của user.  
- Không chỉnh sửa các tag không liên quan đến thông tin cá nhân của user.  
 

**Yêu cầu đầu ra**:  
- Trả về văn bản sau khi đã chỉnh sửa đúng các tag thông tin liên quan đến từng user, đảm bảo thứ tự và định dạng chính xác.

 
# Ví dụ
Đầu vào:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
---------------
TỜ KHAI ĐỀ NGHỊ HỖ TRỢ CHI PHÍ MAI TÁNG
(Áp dụng đối với đối tượng quy định tại Điều 5, khoản 1 Điều 14 Nghị định số [document_number])
I. THÔNG TIN NGƯỜI CHẾT ĐƯỢC MAI TÁNG (Nếu có)
1. Họ và tên (Viết chữ in hoa). [deceased_full_name]
Ngày/tháng/năm sinh: [deceased_dob_day]/[deceased_dob_month]/[deceased_dob_year] Giới tính: [deceased_gender] Dân tộc: [deceased_ethnicity]
2. Hộ khẩu thường trú: [deceased_permanent_address]
3. Ngày [deceased_death_day] tháng [deceased_death_month] năm [deceased_death_year] chết
4. Nguyên nhân chết [deceased_death_reason]
5. Thời gian mai táng [deceased_burial_time]
6. Địa điểm mai táng [deceased_burial_location]
II. THÔNG TIN CƠ QUAN, TỔ CHỨC, HỘ GIA ĐÌNH, CÁ NHÂN ĐỨNG RA MAI TÁNG CHO NGƯỜI CHẾT
1. Trường hợp cơ quan, tổ chức đứng ra mai táng
a) Tên cơ quan, tổ chức: [organisation_name]
- Địa chỉ: [organisation_address]
b) Họ và tên người đại diện cơ quan: [organisation_representative_name]
- Chức vụ: [organisation_representative_position]
2. Trường hợp hộ gia đình, cá nhân đứng ra mai táng
a) Họ và tên (Chủ hộ hoặc người đại diện). [user1_full_name]
Ngày/tháng/năm sinh: [user1_dob_day]/[user1_dob_month]/[user1_dob_year]
Giấy CMND số: [user1_id_number] cấp ngày [user1_id_issue_date] Nơi cấp [user1_id_issue_place]
b) Hộ khẩu thường trú: [user1_permanent_address]
Nơi ở: [user1_current_address]
c) Quan hệ với người chết: [user1_relationship_with_deceased]
Tôi xin cam đoan những lời khai trên là đúng, nếu có điều gì khai không đúng tôi xin chịu trách nhiệm hoàn toàn.

Ngày [day] tháng [month] năm [year]
Người khai
(Ký, ghi rõ họ tên. Nếu cơ quan, tổ chức thì ký, đóng dấu)
```
Đầu ra:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
---------------
TỜ KHAI ĐỀ NGHỊ HỖ TRỢ CHI PHÍ MAI TÁNG
(Áp dụng đối với đối tượng quy định tại Điều 5, khoản 1 Điều 14 Nghị định số [document_number])
I. THÔNG TIN NGƯỜI CHẾT ĐƯỢC MAI TÁNG (Nếu có)
1. Họ và tên (Viết chữ in hoa). [deceased_full_name]
Ngày/tháng/năm sinh: [user1_dob_day]/[user1_dob_month]/[user1_dob_year] Giới tính: [user1_gender] Dân tộc: [user1_ethnicity]
2. Hộ khẩu thường trú: [user1_permanent_address]
3. Ngày [user1_death_day] tháng [user1_death_month] năm [user1_death_year] chết
4. Nguyên nhân chết [user1_death_reason]
5. Thời gian mai táng [user1_burial_time]
6. Địa điểm mai táng [user1_burial_location]
II. THÔNG TIN CƠ QUAN, TỔ CHỨC, HỘ GIA ĐÌNH, CÁ NHÂN ĐỨNG RA MAI TÁNG CHO NGƯỜI CHẾT
1. Trường hợp cơ quan, tổ chức đứng ra mai táng
a) Tên cơ quan, tổ chức: [organisation_name]
- Địa chỉ: [organisation_address]
b) Họ và tên người đại diện cơ quan: [organisation_representative_name]
- Chức vụ: [organisation_representative_position]
2. Trường hợp hộ gia đình, cá nhân đứng ra mai táng
a) Họ và tên (Chủ hộ hoặc người đại diện). [user2_full_name]
Ngày/tháng/năm sinh: [user2_dob_day]/[user2_dob_month]/[user2_dob_year]
Giấy CMND số: [user2_id_number] cấp ngày [user2_id_issue_date] Nơi cấp [user2_id_issue_place]
b) Hộ khẩu thường trú: [user2_permanent_address]
Nơi ở: [user2_current_address]
c) Quan hệ với người chết: [user2_relationship_with_user1]
Tôi xin cam đoan những lời khai trên là đúng, nếu có điều gì khai không đúng tôi xin chịu trách nhiệm hoàn toàn.

Ngày [day] tháng [month] năm [year]
Người khai
(Ký, ghi rõ họ tên. Nếu cơ quan, tổ chức thì ký, đóng dấu)
```

# Ví dụ
Đầu vào:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc

GIẤY ĐỀ NGHỊ NHẬN CHẾ ĐỘ BẢO HIỂM XÃ HỘI
KHI NGƯỜI HƯỞNG TỪ TRẦN

Kính gửi: Bảo hiểm xã hội [local_insurance_office]
Tôi tên là: [user1_full_name] Sinh ngày [user1_dob_day] tháng [user1_dob_month] năm [user1_dob_year]
Số chứng minh nhân dân [user1_id_number] Ngày cấp: [user1_id_issue_date] Nơi cấp: [user1_id_issue_place]
Nơi cư trú (ghi rõ: số nhà, đường phố, tổ/xã/phường): [user1_current_address]
Số điện thoại liên hệ: [user1_phone]
Mối quan hệ với người từ trần: [user1_relationship_with_deceased]
Tôi xin thay mặt cho tất cả thân nhân là [user1_number_of_relatives] người, gồm:
1. Ông (Bà): [user2_full_name] Sinh ngày [user2_dob_day] tháng [user2_dob_month] năm [user2_dob_year]
Nơi cư trú: [user2_current_address]
Mối quan hệ với người từ trần: [user2_relationship_with_deceased]
2. Ông (Bà): [user3_full_name] Sinh ngày [user3_dob_day] tháng [user3_dob_month] năm [user3_dob_year]
Nơi cư trú: [user3_current_address]
Mối quan hệ với người từ trần: [user3_relationship_with_deceased]
3. [user4_full_name]
để nhận chế độ BHXH của người đang hưởng chế độ BHXH đã từ trần là Ông (Bà): [user5_full_name]
Số sổ BHXH: [user5_social_insurance_number] Chết ngày [user5_death_day] tháng [user5_death_month] năm [user5_death_year]
Nơi đang nhận lương hưu, trợ cấp BHXH: [user5_benefit_receiving_location]
Tôi xin cam đoan những nội dung kê khai trên đây là đầy đủ, đúng sự thật và chịu trách nhiệm trước pháp luật về nội dung kê khai cũng như trong trường hợp xảy ra tranh chấp về việc nhận lương hưu, trợ cấp BHXH theo chế độ của người hưởng đã từ trần. Đề nghị cơ quan BHXH xem xét, giải quyết chế độ BHXH cho gia đình chúng tôi theo quy định.

[user1_current_address], ngày [user1_submission_day] tháng [user1_submission_month] năm [user1_submission_year]
Xác nhận của chính quyền địa phương
nơi người đề nghị đang cư trú
(Ký, ghi rõ họ tên và đóng dấu) [place], ngày [day]tháng[month] năm[year]
Người đề nghị
(ký, ghi rõ họ tên)

Chữ ký của các thân nhân
Người thứ nhất: [user2_signature]
(Ký, ghi rõ họ tên)

Người thứ hai: [user3_signature]
(Ký, ghi rõ họ tên)

Người thứ ba: [user4_signature]
(Ký, ghi rõ họ tên)

Xét duyệt của cơ quan BHXH
- Tổng số tháng được truy lĩnh: [deceased_benefit_backpay_months] tháng
Từ tháng [deceased_benefit_backpay_start_month] năm [deceased_benefit_backpay_start_year] đến tháng [deceased_benefit_backpay_end_month] năm [deceased_benefit_backpay_end_year]
- Tổng số tiền được truy lĩnh: [deceased_benefit_backpay_amount] đồng
Bằng chữ: [deceased_benefit_backpay_amount_words]
[local_insurance_office], ngày [insurance_office_decision_day] tháng [insurance_office_decision_month] năm [insurance_office_decision_year]
Giám đốc BHXH
(Ký tên, đóng dấu)
```
Đầu ra:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc

GIẤY ĐỀ NGHỊ NHẬN CHẾ ĐỘ BẢO HIỂM XÃ HỘI
KHI NGƯỜI HƯỞNG TỪ TRẦN

Kính gửi: Bảo hiểm xã hội [local_insurance_office]
Tôi tên là: [user1_full_name] Sinh ngày [user1_dob_day] tháng [user1_dob_month] năm [user1_dob_year]
Số chứng minh nhân dân [user1_id_number] Ngày cấp: [user1_id_issue_date] Nơi cấp: [user1_id_issue_place]
Nơi cư trú (ghi rõ: số nhà, đường phố, tổ/xã/phường): [user1_current_address]
Số điện thoại liên hệ: [user1_phone]
Mối quan hệ với người từ trần: [user1_relationship_with_deceased]
Tôi xin thay mặt cho tất cả thân nhân là [user1_number_of_relatives] người, gồm:
1. Ông (Bà): [user2_full_name] Sinh ngày [user2_dob_day] tháng [user2_dob_month] năm [user2_dob_year]
Nơi cư trú: [user2_current_address]
Mối quan hệ với người từ trần: [user2_relationship_with_deceased]
2. Ông (Bà): [user3_full_name] Sinh ngày [user3_dob_day] tháng [user3_dob_month] năm [user3_dob_year]
Nơi cư trú: [user3_current_address]
Mối quan hệ với người từ trần: [user3_relationship_with_deceased]
3. [user4_full_name]
để nhận chế độ BHXH của người đang hưởng chế độ BHXH đã từ trần là Ông (Bà): [deceased_full_name]
Số sổ BHXH: [deceased_social_insurance_number] Chết ngày [deceased_death_day] tháng [deceased_death_month] năm [deceased_death_year]
Nơi đang nhận lương hưu, trợ cấp BHXH: [deceased_benefit_receiving_location]
Tôi xin cam đoan những nội dung kê khai trên đây là đầy đủ, đúng sự thật và chịu trách nhiệm trước pháp luật về nội dung kê khai cũng như trong trường hợp xảy ra tranh chấp về việc nhận lương hưu, trợ cấp BHXH theo chế độ của người hưởng đã từ trần. Đề nghị cơ quan BHXH xem xét, giải quyết chế độ BHXH cho gia đình chúng tôi theo quy định.

[user1_current_address], ngày [user1_submission_day] tháng [user1_submission_month] năm [user1_submission_year]
Xác nhận của chính quyền địa phương
nơi người đề nghị đang cư trú
(Ký, ghi rõ họ tên và đóng dấu) [place], ngày [day]tháng[month] năm[year]
Người đề nghị
(ký, ghi rõ họ tên)

Chữ ký của các thân nhân
Người thứ nhất: [user2_signature]
(Ký, ghi rõ họ tên)

Người thứ hai: [user3_signature]
(Ký, ghi rõ họ tên)

Người thứ ba: [user4_signature]
(Ký, ghi rõ họ tên)

Xét duyệt của cơ quan BHXH
- Tổng số tháng được truy lĩnh: [deceased_benefit_backpay_months] tháng
Từ tháng [deceased_benefit_backpay_start_month] năm [deceased_benefit_backpay_start_year] đến tháng [deceased_benefit_backpay_end_month] năm [deceased_benefit_backpay_end_year]
- Tổng số tiền được truy lĩnh: [deceased_benefit_backpay_amount] đồng
Bằng chữ: [deceased_benefit_backpay_amount_words]
[local_insurance_office], ngày [insurance_office_decision_day] tháng [insurance_office_decision_month] năm [insurance_office_decision_year]
Giám đốc BHXH
(Ký tên, đóng dấu)
```

# Ví dụ
Đầu vào:
```
CƠ QUAN CẤP GIẤY PHÉP
XÂY DỰNG [new_tagname]
-------
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
---------------
    [place], ngày [day] tháng [month] năm [year]
GIẤY PHÉP XÂY DỰNG
Số:    [document_number]/GPXD
(Sử dụng cho công trình không theo tuyến)

1. Cấp cho: [user1_full_name]
Địa chỉ: số nhà: [user1_house_number] đường (phố) [user1_street] phường (xã): [user1_ward] quận (huyện) [user1_district] tỉnh/thành phố [user1_province]
2. Được phép xây dựng công trình: (tên công trình) [user1_construction_name]
- Theo thiết kế: [user1_construction_design]
- Do: (tên tổ chức tư vấn) [user1_consultant_name] lập

- Chủ nhiệm, chủ trì thiết kế: [user1_design_leader]
- Đơn vị thẩm định, thẩm tra (nếu có): [user1_audit_unit]
- Chủ trì thẩm tra thiết kế: [user1_audit_leader]
- Gồm các nội dung sau:

+ Vị trí xây dựng (ghi rõ lô đất, địa chỉ): [user1_construction_location]
+ Cốt nền xây dựng công trình: [user1_construction_foundation]
+ Mật độ xây dựng: [user1_construction_density] hệ số sử dụng đất: [user1_land_use_coefficient]
+ Chỉ giới đường đỏ: [user1_red_line], chỉ giới xây dựng: [user1_construction_line]
+ Màu sắc công trình (nếu có): [user1_construction_color]
+ Chiều sâu công trình (tính từ cốt 0,00 đối với công trình có tầng hầm): [user1_construction_depth]
Đối với công trình dân dụng và công trình có kết cấu dạng nhà, bổ sung các nội dung sau:

+ Diện tích xây dựng tầng 1 (tầng trệt): [user1_construction_floor_area] m2

+ Tổng diện tích sàn (bao gồm cả tầng hầm và tầng lửng): [user1_construction_total_area] m2

+ Chiều cao công trình: [user1_construction_height] m;

+ Số tầng (trong đó ghi rõ số tầng hầm và tầng lửng): [user1_construction_floors]
3. Giấy tờ về đất đai: [user1_land_documents]
4. Giấy phép này có hiệu lực khởi công xây dựng trong thời hạn 12 tháng kể từ ngày cấp; quá thời hạn trên thì phải đề nghị gia hạn giấy phép xây dựng.

 

Nơi nhận:
- Chủ đầu tư;
- Lưu: VT, [new_tagname]
THỦ TRƯỞNG CƠ QUAN
CẤP GIẤY PHÉP XÂY DỰNG
(Ký tên, đóng dấu)
```
Đầu ra:
```
CƠ QUAN CẤP GIẤY PHÉP
XÂY DỰNG [new_tagname]
-------
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
---------------
    [place], ngày [day] tháng [month] năm [year]
GIẤY PHÉP XÂY DỰNG
Số:    [document_number]/GPXD
(Sử dụng cho công trình không theo tuyến)

1. Cấp cho: [user1_full_name]
Địa chỉ: số nhà: [user1_house_number] đường (phố) [user1_street] phường (xã): [user1_ward] quận (huyện) [user1_district] tỉnh/thành phố [user1_province]
2. Được phép xây dựng công trình: (tên công trình) [user1_construction_name]
- Theo thiết kế: [user1_construction_design]
- Do: (tên tổ chức tư vấn) [user1_consultant_name] lập

- Chủ nhiệm, chủ trì thiết kế: [user2_full_name]
- Đơn vị thẩm định, thẩm tra (nếu có): [user3_full_name]
- Chủ trì thẩm tra thiết kế: [user3_full_name]
- Gồm các nội dung sau:

+ Vị trí xây dựng (ghi rõ lô đất, địa chỉ): [user1_construction_location]
+ Cốt nền xây dựng công trình: [user1_construction_foundation]
+ Mật độ xây dựng: [user1_construction_density] hệ số sử dụng đất: [user1_land_use_coefficient]
+ Chỉ giới đường đỏ: [user1_red_line], chỉ giới xây dựng: [user1_construction_line]
+ Màu sắc công trình (nếu có): [user1_construction_color]
+ Chiều sâu công trình (tính từ cốt 0,00 đối với công trình có tầng hầm): [user1_construction_depth]
Đối với công trình dân dụng và công trình có kết cấu dạng nhà, bổ sung các nội dung sau:

+ Diện tích xây dựng tầng 1 (tầng trệt): [user1_construction_floor_area] m2

+ Tổng diện tích sàn (bao gồm cả tầng hầm và tầng lửng): [user1_construction_total_area] m2

+ Chiều cao công trình: [user1_construction_height] m;

+ Số tầng (trong đó ghi rõ số tầng hầm và tầng lửng): [user1_construction_floors]
3. Giấy tờ về đất đai: [user1_land_documents]
4. Giấy phép này có hiệu lực khởi công xây dựng trong thời hạn 12 tháng kể từ ngày cấp; quá thời hạn trên thì phải đề nghị gia hạn giấy phép xây dựng.

 

Nơi nhận:
- Chủ đầu tư;
- Lưu: VT, [new_tagname]
THỦ TRƯỞNG CƠ QUAN
CẤP GIẤY PHÉP XÂY DỰNG
(Ký tên, đóng dấu)
```

# Ví dụ
Đầu vào:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc 

ĐƠN ĐỀ NGHỊ CHI TRẢ TIỀN MIỄN, GIẢM HỌC PHÍ
(Dùng cho học sinh, sinh viên đang học tại các cơ sở giáo dục nghề nghiệp và giáo dục đại học tư thục)
Kính gửi: Tên cơ sở giáo dục nghề nghiệp và giáo dục đại học tư thục.
Họ và tên: [user1_full_name]
Ngày, tháng, năm sinh: [user1_dob]
Nơi sinh: [user1_birthplace]
Lớp: [user1_class] Khóa [user1_course] Khoa: [user1_faculty]
Họ tên cha/mẹ học sinh, sinh viên: [user1_parent_name]
Hộ khẩu thường trú (ghi đầy đủ): [user1_permanent_address]
Xã (Phường): [user1_ward] Huyện (Quận): [user1_district]
Tỉnh (Thành phố): [user1_province]
Thuộc đối tượng: [user1_student_type] (ghi rõ đối tượng được quy định tại Nghị định số 81/2021/NĐ-CP)
Căn cứ vào Nghị định số 81/2021/NĐ-CP của Chính phủ, tôi làm đơn này đề nghị được xem xét, giải quyết để được cấp bù tiền hỗ trợ miễn, giảm học phí theo quy định và chế độ hiện hành.
 
 	[place], ngày [day] tháng [month] năm [year]
Người làm đơn (3)
(Ký tên và ghi rõ họ tên)
 

```
Đầu ra:
```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc 

ĐƠN ĐỀ NGHỊ CHI TRẢ TIỀN MIỄN, GIẢM HỌC PHÍ
(Dùng cho học sinh, sinh viên đang học tại các cơ sở giáo dục nghề nghiệp và giáo dục đại học tư thục)
Kính gửi: Tên cơ sở giáo dục nghề nghiệp và giáo dục đại học tư thục.
Họ và tên: [user1_full_name]
Ngày, tháng, năm sinh: [user1_dob]
Nơi sinh: [user1_birthplace]
Lớp: [user1_class] Khóa [user1_course] Khoa: [user1_faculty]
Họ tên cha/mẹ học sinh, sinh viên: [user2_full_name]
Hộ khẩu thường trú (ghi đầy đủ): [user2_permanent_address]
Xã (Phường): [user2_ward] Huyện (Quận): [user2_district]
Tỉnh (Thành phố): [user2_province]
Thuộc đối tượng: [user2_student_type] (ghi rõ đối tượng được quy định tại Nghị định số 81/2021/NĐ-CP)
Căn cứ vào Nghị định số 81/2021/NĐ-CP của Chính phủ, tôi làm đơn này đề nghị được xem xét, giải quyết để được cấp bù tiền hỗ trợ miễn, giảm học phí theo quy định và chế độ hiện hành.
 
 	[place], ngày [day] tháng [month] năm [year]
Người làm đơn (3)
(Ký tên và ghi rõ họ tên)
 

```

# Ví dụ
Đầu vào:
```
{form}
```
'''

