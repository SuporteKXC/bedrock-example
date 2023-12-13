import boto3
import json

prompt = f"You should write in Portuguese."

while(True):
        
    print("\n\nEscreva o prompt: \n")
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

    response = bedrock.invoke_model_with_response_stream(
        body=body, 
        modelId=model_id, 
        accept="application/json",
        contentType="application/json",
    )
    stream = response.get('body')
    output = []

    if stream:
        for event in stream:
            chunk = event.get('chunk')
            if chunk:
                chunk_obj = json.loads(chunk.get('bytes').decode())
                text = chunk_obj['completion']
                prompt = prompt + text
                print(text, end='')