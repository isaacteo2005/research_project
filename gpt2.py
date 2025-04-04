from transformers import pipeline
generator = pipeline("text-generation", model="gpt2-large")
chatlog = []
output = generator("Calculate 2 + 2"
                  ,max_length=100,
                 num_return_sequences=1,
                 temperature=0.7,
                 top_k=50,
                 top_p=0.95,
                 do_sample=True)

for i, seq in enumerate(output):
    print(f"Sequence {i+1}: {seq['generated_text']}\n")

