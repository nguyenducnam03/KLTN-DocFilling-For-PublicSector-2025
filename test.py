import os
from Tagnames.define_tagnames import define_tagname
from Config.LLM import gemini
from Utils.text_processing import Text_Processing

def generate_tagnames(input_folder, output_folder):
    T = True
    while T:
        T = False
        files_to_process = [filename for filename in os.listdir(output_folder) if filename.endswith(".txt")]
        for index, filename in enumerate(os.listdir(input_folder)[692:]):
            if filename.endswith(".txt"):
                if filename in files_to_process:
                    continue
                else:
                    T = True
                # Read txt
                file_path = input_folder + "/" + filename
                text = Text_Processing().Read_txt_file(file_path)
                try:
                    llm_filled = define_tagname(gemini, text)
                    # llm_filled = define_tagname_Nam_ver1(gemini, text)
                    # Save to output_folder
                    output_path = output_folder + "/" + filename
                    Text_Processing().Save_txt_file(output_path, llm_filled)
                    print(f"File {filename} is generated successfully!!")
                except Exception as e:
                    print(f"Error: {e} at file {filename}")
                    continue


generate_tagnames("Input", "Output")