# 创建人类消息模板，包含一个变量占位符 {word_count}
human_prompt = "Summarize our conversation so far in {word_count} words."
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

# 创建聊天提示模板，包含两个部分：
# 1. MessagesPlaceholder - 用于插入对话历史
# 2. human_message_template - 用于插入新的人类消息
chat_prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="conversation"), 
    human_message_template
])