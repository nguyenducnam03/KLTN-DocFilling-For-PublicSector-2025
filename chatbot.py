import chainlit as cl
from chainlit.input_widget import Switch, Slider

#Import from another files
import MyClasses
import constant_value as CONST

@cl.on_chat_start
async def on_chat_start():
    # Chat setting
    settings = await cl.ChatSettings(
        [
        Slider(id="Temperature",label="Temperature",initial=0,min=0,max=1,step=0.02,),
        Slider(id="Top-k",label = "Top-k", initial = 1, min = 1, max = 100, step = 1),
        Slider(id="Top-p",label = "Top-p",initial = 1, min = 0,max = 1,step = 0.02),
        Slider(id="mnt", label = "Max new tokens", initial = 4000, min = 0, max = 8000, step = 100),
        Switch(id="New", label="New", initial=True),
        ]
    ).send()

    # ======================Ảnh bìa======================
    image = cl.Image(path="./fill_form.jpg", name="image1", display="inline")
    await cl.Message(
        content="Tôi là chatbot có nhiệm vụ chính là điền thông tin vào document.",
        elements=[image],
    ).send()  

    # ======================Insert file need to fullfill======================
    files = None
    while files == None:
        files = await cl.AskFileMessage(
            content="Upload form bạn cần điền thông tin!", accept=["text/plain"]
        ).send()
    text_file = files[0]
    with open(text_file.path, "r", encoding="utf-8") as f:
        text = f.read()  

    # print("text \n:",text)
    await cl.Message(content=f"Content:").send()
    await cl.Message(content=text).send()

    ## ======================Handling======================
    llm = MyClasses.LLM_Gemini(CONST.API_KEY)
    handle_text = MyClasses.Text_Processing()

    blanked_text, count_blank = handle_text.generate_uniform(text)
    await cl.Message(content=f"Blanked text: \n {blanked_text}").send()
    blank_to_tagnames = llm.blank_to_tagnames(blanked_text, CONST.tag_names) ##**Important**

    list_tag_names = list(blank_to_tagnames.values())
    # await cl.Message(content=f"List of tagnames: \n {list_tag_names}").send()
    list_values = llm.translate_tag_names(list_tag_names, CONST.translations)
    # await cl.Message(content=f"List of values: \n {list_values}").send()

    ## ======================DATABASE======================
    '''Pro làm nhen'''

    #Requires users to enter content
    await cl.Message(
        content = "Hãy nhập thông tin để tôi giúp bạn điền vào!"
    ).send()

    # # ---------------------- Save user session ---------------------
    cl.user_session.set("blank_to_tagnames",blank_to_tagnames)
    cl.user_session.set("count_blank",count_blank)
    cl.user_session.set("handle_text",handle_text)
    cl.user_session.set("llm",llm)
    cl.user_session.set("blanked_text", blanked_text)
    cl.user_session.set("list_tag_names", list_tag_names)
    cl.user_session.set("list_values", list_values)

@cl.on_message
async def main(message: cl.Message):
    # cl.user_session.set("memory", ConversationBufferMemory(return_messages=True))
    # # ---------------------- Take again user session ---------------------
    blank_to_tagnames = cl.user_session.get("blank_to_tagnames")
    count_blank = cl.user_session.get("count_blank")
    handle_text = cl.user_session.get("handle_text")
    llm = cl.user_session.get("llm")
    blanked_text = cl.user_session.get("blanked_text")
    list_tag_names = cl.user_session.get("list_tag_names")
    list_values = cl.user_session.get("list_values")

    
    # Get response
    context = message.content

    #Get infor context by LLM
    value_keys_to_context_value = llm.extract_content(context, list_values) ##**Important**
    # print("value_keys_to_context_value: \n",value_keys_to_context_value)
    # await cl.Message(
    #     content = f"value_keys_to_context_value: \n {value_keys_to_context_value}"
    # ).send()  

    ##============================Filled Form============================
    filled_form = handle_text.fill_form(blanked_text, blank_to_tagnames, value_keys_to_context_value)
    # print("filled_form: \n",filled_form)
    # await cl.Message(
    #     content = f"Filled form: \n {filled_form}"
    # ).send()
    

# ------------------------------ Stop section ------------------------------
@cl.on_stop
async def on_stop():
    print("Người dùng muốn dừng công việc này!")

# ------------------------------ End section ------------------------------
@cl.on_chat_end
async def on_chat_end():
    print("Người dùng đã ngắt kết nối!")

# --------------------------- Authentication -------------------------------
# @cl.password_auth_callback
# def auth_callback(username: str, password: str):
#     # Fetch the user matching username from your database
#     # and compare the hashed password with the value stored in the database
#     if (username, password) == ("LHH", "1323"):
#         return cl.User(
#             identifier="LHH", metadata={"role": "admin", "provider": "credentials"}
#         )
#     else:
#         return None
    
# ----------------------------- Chat settings update --------------------------
# @cl.on_settings_update
# async def setup_agent(settings):
#     print("on_settings_update", settings)

