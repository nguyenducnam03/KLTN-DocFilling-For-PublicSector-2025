convert_random_form_to_meaningful_template = '''
# PROMPT: CHUYỂN ĐỔI RANDOM FORM THÀNH FORM CÓ Ý NGHĨA

Bạn được cung cấp hai nguồn dữ liệu sau:

## 1. DANH SÁCH MẪU FORM CÓ Ý NGHĨA
Các mẫu này đã được định dạng, nhóm thông tin theo logic và trình bày rõ ràng. Chúng sẽ là nguồn tham khảo để xác định cách sắp xếp, đặt tên và
định dạng các trường thông tin.

## 2. RANDOM FORM
Một form chứa các trường thông tin với thứ tự, tên gọi và định dạng không nhất quán, có thể có dữ liệu trùng lặp hoặc không cần thiết.

---

## NHIỆM VỤ CỦA BẠN:

### PHÂN TÍCH & NHÓM NHÓM:
    Dựa vào danh sách các mẫu form có ý nghĩa, hãy phân loại các trường thông tin thành các nhóm hợp lý như:
    **I. THÔNG TIN CÁ NHÂN**
    - Họ và tên
    - Họ, chữ đệm, tên
    - Ngày sinh (ngày, tháng, năm)
    - Giới tính
    - Dân tộc
    - Quốc tịch
    - Tôn giáo
    - Nơi sinh / Nguyên quán
    - Nơi đăng ký khai sinh
    - Số CCCD/CMND
    - Ngày cấp CCCD/CMND
    - Nơi cấp CCCD/CMND
    - Hộ chiếu (số hộ chiếu, ngày cấp, nơi cấp)
    - Số định danh cá nhân
    - Trình độ học vấn
    - Nghề nghiệp

    **II. ĐỊA CHỈ & LIÊN HỆ**
    - Địa chỉ thường trú
    - Địa chỉ hiện tại
    - Phường/Xã
    - Quận/Huyện
    - Tỉnh/Thành phố
    - Số điện thoại (cố định, di động)
    - Email
    - Địa chỉ liên hệ (nơi cư trú, nơi làm việc)

    **III. THÔNG TIN HỌC TẬP**
    - Quyết định cử đi học (số quyết định, ngày quyết định)
    - Cơ quan/quốc gia cử đi học
    - Thời gian học tập (tại nước ngoài, trong nước)
    - Thời gian gia hạn học tập (tháng, năm)
    - Ngày tốt nghiệp
    - Ngày về nước
    - Kết quả học tập (điểm, xếp loại, văn bằng, chứng chỉ)
    - Tên cơ sở giáo dục (ghi bằng tiếng Việt và tiếng Anh)
    - Tên đề tài luận văn, luận án, chuyên đề thực tập
    - Tên người hướng dẫn (giáo sư, giảng viên)
    - Đánh giá, nhận xét của cơ sở giáo dục hoặc người hướng dẫn
    - Nguyện vọng, đề nghị liên quan đến học tập

    **IV. THÔNG TIN VIỆC LÀM & HỒ SƠ CÔNG CHỨC**
    - Tên cơ quan, đơn vị công tác
    - Mã số, số hiệu cán bộ (nếu có)
    - Chức vụ, vị trí công tác
    - Địa chỉ cơ quan
    - Số điện thoại, email liên hệ cơ quan
    - Ngày vào làm việc
    - Lịch sử công tác (nếu cần)
    - Kiến nghị, đề xuất, cam kết liên quan đến công việc

    **V. THÔNG TIN PHƯƠNG TIỆN & LÁI XE**
    - Số giấy phép lái xe
    - Ngày cấp giấy phép lái xe
    - Nơi cấp giấy phép lái xe
    - Cơ quan cấp giấy phép lái xe
    - Lý do xin cấp/đổi mới giấy phép lái xe (nếu áp dụng)
    - Thông tin về phương tiện (nếu có yêu cầu: biển số xe, loại xe, v.v.)

    **VI. THÔNG TIN HÔN NHÂN & GIA ĐÌNH**
    - Tình trạng hôn nhân
    - Tên vợ/chồng (nếu đã kết hôn)
    - Ngày kết hôn
    - Số giấy đăng ký kết hôn
    - Thông tin về con cái (họ tên, ngày sinh, quan hệ với người đăng ký)

    **VII. THÔNG TIN KINH TẾ, DOANH NGHIỆP & THUẾ**
    - Số đăng ký kinh doanh
    - Mã số thuế
    - Số sổ BHXH (Bảo hiểm xã hội)
    - Thông tin về tài sản (nếu cần)
    - Các chứng từ liên quan đến thuế, kinh doanh

    **VIII. THÔNG TIN KHÁC (ĐIỀU CHỈNH THEO MỤC ĐÍCH HỒ SƠ)**
    - Nguyện vọng, đề nghị, kiến nghị, đề xuất
    - Số hiệu hồ sơ, mã hồ sơ
    - Ngày lập hồ sơ, ngày báo cáo
    - Nơi lập hồ sơ, nơi ký
    - Tên và chữ ký người làm đơn (người báo cáo)
    - Cam kết, lời cam đoan (xác nhận tính trung thực của thông tin)
    - Các trường phụ trợ khác theo từng loại dịch vụ công (ví dụ: dịch vụ y tế: số bảo hiểm y tế, thông tin bệnh án; dịch vụ nhà nước khác: số sổ tạm trú/thường trú, thời gian cư trú, v.v.)

    **LƯU Ý:**
    - Các trường trên có thể thay đổi hoặc bổ sung tùy theo từng loại hình dịch vụ công cụ thể (ví dụ: giáo dục, y tế, giao thông, việc làm, hôn nhân gia đình, kinh tế,...).
    - Một số form có thể không bao gồm tất cả các trường; bạn cần chọn lọc và sắp xếp theo đúng yêu cầu của từng dịch vụ.
    - Khi xây dựng hoặc chuyển đổi form, hãy đảm bảo tính thống nhất, rõ ràng và đầy đủ thông tin cần thiết cho từng loại hình dịch vụ công.


### LOẠI BỎ & HỢP NHẤT:
  Kiểm tra và loại bỏ các trường thông tin trùng lặp hoặc không cần thiết.
  Nếu có các biểu diễn khác nhau của cùng một thông tin (ví dụ: ngày sinh được trình bày theo nhiều định dạng), hãy hợp nhất thành một định dạng thống nhất.

### ĐẶT TÊN & ĐỊNH DẠNG:
  Đổi tên các trường để trở nên rõ ràng, dễ hiểu và thống nhất với các mẫu form có ý nghĩa.
  Định dạng ngày tháng theo chuẩn dễ hiểu (ví dụ: DD/MM/YYYY).
  Giữ nguyên các placeholder (ví dụ: [user1_full_name]) để làm vị trí cho dữ liệu.

---

## VÍ DỤ:
Input(Random Form):
```
{random_form}
```
Output(Meaningful Form):
'''