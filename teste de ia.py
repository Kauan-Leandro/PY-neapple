from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
