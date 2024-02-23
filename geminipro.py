"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="Your API Key")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    # "threshold": "NEGLIGIBLE"
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

# model = genai.GenerativeModel('gemini-pro-vision') # Vision model
# model = genai.GenerativeModel('gemini-pro-text', safety_settings=safety_settings) # Text model
# model = genai.GenerativeModel('gemini-lite', safety_settings=safety_settings) # Lite version of text model
# model = genai.GenerativeModel('gemini-pro-audio') # Audio model   


model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

convo.send_message("tell me something about tollywood industry")
print(convo.last.text)

# model = genai.GenerativeModel("gemini-pro-text")
# # model = genai.GenerativeModel("gemini-pro-text", safety_settings=safety_settings)

# # Initialize the conversation
# convo = model.start_chat(history=[])

# Get user input
# while True:
#     # Get user input as voice or text
#     user_input = input("You: ")

#     # Send the user input to the model
#     convo.send_message(user_input)

#     # Get the model response
#     response = convo.last.text

#     # Output the response as text or voice
#     if "voice" in user_input:
#         # Output the response as voice
#         print(f"Assistant (voice): {response}")
#     else:
#         # Output the response as text
#         print(f"Assistant (text): {response}")