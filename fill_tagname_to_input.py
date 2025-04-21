import os
from Tagnames.define_tagnames import generate_tagnames
from Utils.text_processing import Text_Processing
import json 
import re

# General

# Folder addresses Data_x
input_folder = "Data\LLM_Data\Gemini\Test\Input"
input_folders = [input_folder]
label_folder = "Data\LLM_Data\Gemini\Test\Label"
output_folder = "Data\LLM_Data\Gemini\Test\Output"


# # Rule
# input_folder = "Data\Rule_Data\Test\Input"
# input_folders = [input_folder]
# label_folder = "Data\Rule_Data\Test\Label"
# output_folder = "Data\Rule_Data\Test\Output"



# Ensuse output folder exists
os.makedirs(output_folder, exist_ok=True)

# ============= 1. Generates tagnames =============
for input_folder in input_folders:
    generate_tagnames(input_folder, output_folder)

# ============= 2. Process the output =============
def fix_infinity_space(text):
    # Replace more than 2 consecutive spaces with exactly 2 spaces
    text = re.sub(r' {3,}', '  ', text)
    
    # Replace more than 2 consecutive newlines with exactly 2 newlines
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()


def normalize_filled_date_expression(text):
    """
    Các trường hợp được hỗ trợ:

    1. [#another], ngày [#another] tháng [#another] năm [#another]
    2. [#another], ngày [#another], tháng [#another], năm [#another]
    3. Ngày [#another] tháng [#another] năm [#another]
    4. ngày [#another] tháng [#another] năm [#another]
    5. Ngày [#another], tháng [#another], năm [#another]

    Những trường hợp không xử lý:
    1. {text}: ngày [#another] tháng [#another] năm [#another]
    2. ngày [userX_tagname] tháng [userX_tagname] năm [userX_tagname]
    3. {text} ngày [#another] tháng [#another] năm [#another]
    """

    # Mẫu chính cho các kiểu ngày
    date_pattern = re.compile(
        r"(?:\[(?P<place>#another)\],*\s*)?"                      # [place], (tùy chọn)
        r"(?:ngày|Ngày)\s*\[(?P<day>#another)\]\s*,?\s*"          # ngày [day],
        r"(?:tháng|Tháng)\s*\[(?P<month>#another)\]\s*,?\s*"      # tháng [month],
        r"(?:năm|Năm)\s*(?:20\s*)?\[(?P<year>#another)\]"         # năm 20 [year]
    )


    # Mẫu loại trừ
    exclude_patterns = [
        r"^[^:]+:\s*ngày\s*\[#another\]\s*tháng\s*\[#another\]\s*năm\s*\[#another\]",
        r"ngày\s*\[user[^\]]+\]\s*tháng\s*\[user[^\]]+\]\s*năm\s*\[user[^\]]+\]",
        r"\w+\s*ngày\s*\[#another\]\s*tháng\s*\[#another\]\s*năm\s*\[#another\]",
        r"\b(?!tại\b)\w+\s*\[#another\],*\s*ngày\s*\[#another\]\s*tháng\s*\[#another\]\s*năm\s*\[#another\]",
        r"\w+\s*\[user[^\]]+\]\s*tại\s*\[#another\]",
    ]

    exclude_regexes = [re.compile(p) for p in exclude_patterns]

    # Hàm thay thế ngày
    def replace_date(match):
        if "năm 20" in text:
          if match.group("place"):
              return "[place], ngày [day] tháng [month] năm 20 [year]"
          else:
              return "ngày [day] tháng [month] năm 20 [year]"
        else:
          if match.group("place"):
              return "[place], ngày [day] tháng [month] năm [year]"
          else:
              return "ngày [day] tháng [month] năm [year]"

    # Xử lý từng dòng một
    lines = text.splitlines()
    normalized_lines = []

    for line in lines:
        # Nếu dòng khớp với bất kỳ mẫu loại trừ nào → giữ nguyên
        if any(p.search(line) for p in exclude_regexes):
            normalized_lines.append(line)
        else:
            # Thay thế biểu thức ngày nếu có
            normalized_lines.append(date_pattern.sub(replace_date, line))

    return "\n".join(normalized_lines)


def normalize_receiver_expression(text):
    """
    Chuẩn hóa dòng người nhận từ các định dạng như:
    - 'Kính gửi: [#another]'
    - 'Kính gửi: `text` [#another]'
    - 'Kính gửi: Trung tâm [user_tag]'
    - 'Kính gửi : ABC XYZ [user_tag]'
    
    Thành 'Kính gửi: [receiver]'.
    """
    pattern = r"Kính\s+gửi\s*:\s*(?:.*?\s)?\[[^\]]+\]"
    replacement = "Kính gửi: [receiver]"
    return re.sub(pattern, replacement, text, flags=re.IGNORECASE)


# 2.1 From forms response by LLM --> get tagnames to input forms --> remove different tagnames
# list_input_debug = ["input_125.txt", "data_167.txt", "data_198.txt", "data_22.txt"]
# For filling just some form (Chỉ định chỉ điền một số form để test --> debugging)
def filled_input_from_filled_form(input_folder, output_folder, process_folder):
    for index, filename in enumerate(os.listdir(output_folder)):
        if (index+1)%1==0:
            print(f"Process until {index+1}")
        if filename.endswith(".txt") :
            print(filename)
            # if filename == "data_125.txt":
                # continue
            # else:
            #     print("found")
            # Input - filled
            file_input_dir = input_folder + "/" + filename
            file_filled_dir = output_folder + "/" + filename
            # Read
            input_text = Text_Processing().Read_txt_file(file_input_dir).strip()
            filled_text = Text_Processing().Read_txt_file(file_filled_dir).strip()
            # Fix infinity space
            input_text = fix_infinity_space(input_text)
            filled_text = fix_infinity_space(filled_text)

            # Replace all ".........." by "[another]"
            input_text = input_text.replace("..........", "[#another]")
            filled_text = filled_text.replace("..........", "[#another]")


            try:
                # Fill input by LLM form
                filled_input_text,copy_contextual_input = Text_Processing().fill_input_by_llm_form(
                    filled_text, input_text
                )
                filled_input_text = normalize_filled_date_expression(filled_input_text)
                filled_input_text = normalize_receiver_expression(filled_input_text)
                # print(filled_input_text)
                # print(f"filled_input_text: {filled_input_text}")
                # Debugging: Save copy_contextual_input to Temp/Copy_Contextual_Input/filename.json
                os.makedirs(f"{output_folder}/Copy_Contextual_Input", exist_ok=True)
                # Save the list to a JSON file
                copy_contextual_input_dir = f"{output_folder}/Copy_Contextual_Input/" + filename + ".json"
                with open(copy_contextual_input_dir, "w", encoding="utf-8") as f:
                    json.dump(copy_contextual_input, f, ensure_ascii=False, indent=4)

                # Save 
                output_path = process_folder + "/" + filename
                # output_path_different = process_folder + "/Differents/" + filename
                Text_Processing().Save_txt_file(output_path, filled_input_text)

            except Exception as e:
                print(f"Error: {e} at file {filename}")
                break

process_folder = f"{output_folder}\Processed_Output"
os.makedirs(process_folder, exist_ok=True)
for input_folder in input_folders:
    filled_input_from_filled_form(input_folder, output_folder, process_folder)


def filled_input_from_label_form(input_folder, label_folder, process_folder):
    for index, filename in enumerate(os.listdir(label_folder)):
        if (index+1)%1==0:
            print(f"Process until {index+1}")
        if filename.endswith(".txt") :
            
            file_input_dir = input_folder + "/" + filename
            file_filled_dir = label_folder + "/" + filename
            # Read
            input_text = Text_Processing().Read_txt_file(file_input_dir).strip()
            filled_text = Text_Processing().Read_txt_file(file_filled_dir).strip()
            # Fix infinity space
            input_text = fix_infinity_space(input_text)
            filled_text = fix_infinity_space(filled_text)
            # Replace all ".........." by "[another]"
            input_text = input_text.replace("..........", "[#another]")
            filled_text = filled_text.replace("..........", "[#another]")

            try:
                # Fill input by LLM form
                filled_input_text,copy_contextual_input = Text_Processing().fill_input_by_label_form(
                    filled_text, input_text
                )
                
                # Debugging: Save copy_contextual_input to Temp/Copy_Contextual_Input/filename.json
                os.makedirs(f"{label_folder}/Copy_Contextual_Input", exist_ok=True)
                # Save the list to a JSON file
                copy_contextual_input_dir = f"{label_folder}/Copy_Contextual_Input/" + filename + ".json"
                with open(copy_contextual_input_dir, "w", encoding="utf-8") as f:
                    json.dump(copy_contextual_input, f, ensure_ascii=False, indent=4)

                # Save 
                output_path = process_folder + "/" + filename
                Text_Processing().Save_txt_file(output_path, filled_input_text)
            except Exception as e:
                print(f"Error: {e} at file {filename}")
                break

process_label_folder = f"{label_folder}\Processed_Label"
os.makedirs(process_label_folder, exist_ok=True)
for input_folder in input_folders:
    filled_input_from_label_form(input_folder, label_folder, process_label_folder)



# 2.2 Remove different tagnames from process output folder
for index, filename in enumerate(os.listdir(process_folder)):
# for index, filename in enumerate(list_specific_forms): # Debugging
    if filename.endswith(".txt"):
        # Input - filled
        file_process_output_dir = process_folder + "/" + filename
        # Read
        process_output_text = Text_Processing().Read_txt_file(file_process_output_dir).strip()
        # Print debug
        try:
            # Remove different tagnames
            process_output_text_different = Text_Processing().remove_different_tagnames(
                process_output_text
            )
            # Save
            output_path_different = process_folder + "/Differents/" + filename
            Text_Processing().Save_txt_file(output_path_different, process_output_text_different)

        except Exception as e:
            print(f"Error: {e} at file {filename}")
            break


# 2.2 Remove different tagnames from label folder
for index, filename in enumerate(os.listdir(process_label_folder)):
    if filename.endswith(".txt"):
        # Input - filled
        file_label_dir = process_label_folder + "/" + filename
        # Read
        label_text = Text_Processing().Read_txt_file(file_label_dir).strip()
        # Print debug
        try:
            # Remove different tagnames
            label_text_different = Text_Processing().remove_different_tagnames(
                label_text
            )
            # Save
            output_path_different = process_label_folder + "/Differents/" + filename
            Text_Processing().Save_txt_file(output_path_different, label_text_different)

        except Exception as e:
            print(f"Error: {e} at file {filename}")
            break

