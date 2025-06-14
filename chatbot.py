import boto3
import json

class TitanChatBot:
    def __init__(self, region="us-east-1"):
        self.bedrock = boto3.client("bedrock-runtime", region_name=region)
        self.model_id = "amazon.titan-text-premier-v1:0"
        self.history = []  # Stores previous chat turns

    def build_prompt(self, user_input: str) -> str:
        """
        Builds the full prompt including chat history and current input.
        """
        self.history.append(f"User: {user_input}")
        trimmed_history = self.history[-6:]  # Keep last 3 exchanges
        return "\n".join(trimmed_history) + "\nAI:"

    def ask(self, user_input: str) -> str:
        """
        Sends a prompt to the Titan model and returns its response.
        """
        prompt = self.build_prompt(user_input)

        body = {
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 512,
                "temperature": 0.7,
                "topP": 0.9
            }
        }

        try:
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                contentType="application/json",
                accept="application/json",
                body=json.dumps(body)
            )

            result = json.loads(response['body'].read())
            output = result['results'][0]['outputText'].strip()
            self.history.append(f"AI: {output}")
            return output

        except Exception as e:
            return f"ERROR: {str(e)}"
