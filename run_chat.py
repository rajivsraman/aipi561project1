from chatbot import TitanChatBot

bot = TitanChatBot()

print("Titan Bedrock Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        break

    response = bot.ask(user_input)
    print("AI:", response)