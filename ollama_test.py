import os
import asyncio
import litellm

# Optional: make LiteLLM verbose to see requests
litellm.set_verbose = True

# Configure the Ollama API endpoint and dummy key
# Use host.docker.internal:11434 if running inside Docker
litellm.api_base = os.getenv("LITELLM_API_BASE", "http://localhost:11434")
litellm.api_key = os.getenv("LITELLM_API_KEY", "ollama")

# Choose an installed model (check with `ollama list`)
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "ollama/llama3.3:70b")

async def test_ollama():
    """
    Send a tiny request to Ollama via LiteLLM and print the result.
    """
    print(f"🔍 Testing LiteLLM → Ollama connection to {litellm.api_base} using model {OLLAMA_MODEL}")

    try:
        response = await litellm.acompletion(
            model=OLLAMA_MODEL,
            messages=[
                {"role": "system", "content": "You are a concise assistant."},
                {"role": "user", "content": "Say 'Hello from Ollama!' in one short sentence."},
            ],
            stream=False,
            max_tokens=64,         # cap output
            temperature=0.2,
            request_timeout=20,    # seconds before giving up
            force_timeout=20,
        )

        print("\n✅ Ollama responded successfully!")
        print("Response:\n" + "-"*40)
        print(response["choices"][0]["message"]["content"].strip())
        print("-"*40)

    except Exception as e:
        print("\n❌ Ollama test failed:")
        print(e)

if __name__ == "__main__":
    asyncio.run(test_ollama())
