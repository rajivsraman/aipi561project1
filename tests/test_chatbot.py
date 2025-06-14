from chatbot import TitanChatBot\

def test_conversation_memory():
    print("\nRunning test_conversation_memory...")
    bot = TitanChatBot()
    # Simulate a conversation about astronomy
    bot.history = [
        "User: What is a black hole?",
        "AI: A black hole is a region in space where gravity is so strong that nothing, not even light, can escape.",
        "User: Can black holes die?",
        "AI: Yes, through a process called Hawking radiation, black holes can slowly lose mass and eventually evaporate."
    ]
    prompt = bot.build_prompt("What happens when two black holes merge?")
    print("Trimmed Prompt:\n", prompt)
    line_count = len(prompt.splitlines())
    print(f"Prompt has {line_count} lines")
    assert line_count <= 7
    print("test_conversation_memory passed.")


def test_error_handling(monkeypatch):
    print("\nRunning test_error_handling...")

    bot = TitanChatBot()

    def simulated_bedrock_failure(*args, **kwargs):
        raise Exception("Simulated Bedrock API failure")

    monkeypatch.setattr(bot.bedrock, "invoke_model", simulated_bedrock_failure)

    result = bot.ask("What's the weather like on Mars?")
    print("Response:", result)
    assert "ERROR" in result
    print("test_error_handling passed.")
