import os
from Tagnames.define_tagnames import generate_tagnames
from Utils.text_processing import Text_Processing
import json 
from Config.config import Data_num, Output_num, Type, Label_Input_num
import re

# General

# Folder addresses Data_x
input_folder = "Data/Rule_Data/Test/Input"
input_folders = [input_folder]
label_folder = "Data\Rule_Data\Test\Label"
output_folder = "Data\Rule_Data\Test\Output"


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

