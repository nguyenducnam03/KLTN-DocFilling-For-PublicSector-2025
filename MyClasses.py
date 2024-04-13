import google.generativeai as genai
import constant_value as CONST
import re

class LLM_Gemini:
    def __init__(self, api_key):
        # Set up the model
        genai.configure(api_key=api_key)
        generation_config = {
        "temperature": 0,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 4096,
        }
        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
        ]
        #Model
        self.model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
        
    def print_hello(self):
        print("Hello")
        
    def blank_to_tagnames(self, text_with_blank, tagnames):
        """
        text_with_blank: form with (Blank_x)....
        tagnames: list of tag names
        return: list of tagnames coressponding to the blanks
        """
        #Get response
        prompt_parts = CONST.template_blank_to_tagname.format(tag_names=tagnames, Abstract = text_with_blank)
        response = self.model.generate_content(prompt_parts)
        response = response.text
        #Handle response
        try:
            response = re.search(r'Answer:(.*)', response, re.DOTALL).group(1).strip()
        except:
            pass
        list_tag_names = []
        pattern1 = r'Blank\d+:'
        pattern2 = r':\s*(.*)'

        blank_to_tagnames = {}

        matches1 = re.findall(pattern1, response)
        matches2 = re.findall(pattern2, response)
        for match1,match2 in zip(matches1, matches2):
            temp1 = match1.replace(":","").strip()
            temp2 = match2.replace("]","").strip()
            
            blank_to_tagnames[temp1] = temp2
            
        return blank_to_tagnames  

    def translate_tag_names(self, list_tag_names, translations):
        """
        Convert from list_tag_names into values
        Example: #Full_name --> Họ và tên
        list_tag_names: list of tag names
        translations: dictionary of translations
        """
        list_value_keys = [] #
        pattern = r'#(\w+)'
        for tag_name in list_tag_names:
            match = re.search(pattern, tag_name)
            temp = match.group(0)
            list_value_keys.append(translations[temp])
            temp = temp.replace("#","")
        return list_value_keys
    
    def extract_content(self, Abstract, list_value_keys):
        #Convert Question to right format
        Question = """"""
        for item in list_value_keys:
            Question += item + "\n"
        #Get response
        prompt_parts = CONST.template_extract_content.format(Abstract = Abstract, Question = Question)
        response = self.model.generate_content(prompt_parts)
        response = response.text

        #Handle this response
        pattern1 = r'\[(.*?)\s*:'
        pattern2 = r':\s*(.*)'

        value_keys_to_context_value = {}
        try:
            response = re.search(r'Answer:(.*)', response, re.DOTALL).group(1).strip()
        except:
            pass

        matches1 = re.findall(pattern1, response)
        matches2 = re.findall(pattern2, response)
        for match1,match2 in zip(matches1, matches2):
            temp1 = match1.replace(":","").strip()
            temp2 = match2.replace("]","").strip()
            if temp1 not in value_keys_to_context_value:
                value_keys_to_context_value[temp1] = []  # Initialize list for the key if it doesn't exist
            value_keys_to_context_value[temp1].append(temp2)

        return value_keys_to_context_value
    
class Text_Processing:
    def __init__(self):
        pass
    def min_uniform(self,a, b):
        """
        This function server for function generat_uniform
        """
        if a == -1 and b != -1:
            return b
        if b == -1 and a != -1:
            return a
        if a == -1 and b == -1:
            return -1
        if a < b:
            return a
        else:
            return b
        
    def generate_uniform(self,Question):
        count = 0
        # Initialize a counter for numbering the placeholders
        placeholder_counter = 1

        type1 = ".."
        type2 = "…"
        first_index = self.min_uniform(Question.find(type1), Question.find(type2))
        # Loop through the question and replace the placeholders with the numbered placeholders
        while first_index != -1:
            # Replace the first occurrence of the placeholder with the formatted numbered placeholder
            count += 1
            Question = Question[:first_index] + "(Blank" + str(placeholder_counter) + ")" + Question[first_index:]
            #Index }
            start_index = first_index+2+(len(str(placeholder_counter)))+5
            end_index = start_index
            # Increment the counter
            placeholder_counter += 1

            while (end_index < (len(Question))) and (Question[end_index] == "…" or Question[end_index] == "."):
                end_index  += 1

            if (end_index+1 < (len(Question))) and (Question[end_index] == "\n") and (Question[end_index+1] == "…" or Question[end_index+1] == "."):
                end_index  += 1

            while (end_index < (len(Question))) and (Question[end_index] == "…" or Question[end_index] == "."):
                end_index  += 1
            if end_index == 212:
                a = 2+3
            try:
                Question = Question[:start_index] + Question[end_index:]
            except:
                Question = Question[:start_index]
            # Find the indices of the next placeholders
            first_index = self.min_uniform(Question.find(type1), Question.find(type2))
        return Question, count

    def fill_form(self,blanked_text, blank_to_tagnames, value_keys_to_context_value):
        """
        From values, and blanked form
        Fill value into this blank
        """
        print("blanked form: \n",blanked_text)
        print("blank_to_tagnames: \n", blank_to_tagnames)
        print("value_keys_to_context_value: \n", value_keys_to_context_value)
        return blanked_text




#
