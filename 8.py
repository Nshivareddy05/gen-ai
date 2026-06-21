!pip install cohere --quiet

import cohere

co = cohere.Client("YOUR_API_KEY") 
text = "AI is transforming industries and raising ethical concerns."

response = co.chat(
    message=f"Give: 1. Title 2. Summary 3. Conclusion\nText: {text}",
    model="command-r-08-2024"
)

print(response.text)
