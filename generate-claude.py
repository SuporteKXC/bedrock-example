import boto3
import json

prompt = f"You should write in Portuguese. "

while(True):
        
    print("\nEscreva o prompt: \n")
    user_input = input()

    prompt = prompt + f"\n\nHuman:{user_input}\n\nAssistant:"

    print(f"\nPrompt: {prompt}\n")

    bedrock = boto3.client(service_name="bedrock-runtime")
    payload = {
        "prompt": prompt,
        "max_tokens_to_sample": 4000,
        "temperature": 0.8,
        "top_p": 0.8,
    }

    print("\nGerando resposta...\n")
    body = json.dumps(payload)
    model_id = "anthropic.claude-v2"
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json",
    )

    response_body = json.loads(response.get("body").read())

    print(response_body)

    response_text = response_body.get("completion")

    prompt = prompt + response_text

    print(response_text)