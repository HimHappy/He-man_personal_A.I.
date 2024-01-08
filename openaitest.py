from openai import OpenAI
client = OpenAI()
# add your openai api key to system enviroment that is much efficient

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write an email for sick leave\n"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
