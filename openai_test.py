import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",

  messages=[
    {
      "role": "user",
      "content": "write a email to boss for resignation?"
    },
    {
      "role": "assistant",
      "content": "Subject: Resignation Letter\n\nDear [Boss's Name],\n\nI hope this email finds you well. After giving thorough consideration to my professional journey and personal goals, I have made the difficult decision to resign from my position at [Company Name], effective [last"
    }
  ],
  prompt=prompt,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
'''
{
  "id": "chatcmpl-7jqnvRbuAzV0EsTEkpr27q7vlG6PT",
  "object": "chat.completion",
  "created": 1691162095,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "working day, typically two weeks from the date of resignation].\n\nI would like to express my deepest gratitude for the opportunities and support you have provided me during my tenure here. It has been a pleasure working under your leadership and guidance. I am grateful for the knowledge and skills I have gained, as well as the relationships I have built with my colleagues. I truly appreciate the trust you have placed in me and the confidence you have shown in my abilities.\n\nI have accepted an offer for a new opportunity that aligns more closely with my long-term career aspirations and personal growth. While it was not an easy decision to make, I believe it is the right step for me at this point in my professional journey.\n\nIn order to ensure a smooth transition, I am committed to completing any pending tasks or projects that you deem necessary for the continuation of the team's success. I will work closely with my colleagues to hand over my responsibilities and provide any necessary documentation or training before my departure.\n\nPlease let me know how I can best assist you during this transition period. I am open to discussing the timeline and any specific requirements you may have. Additionally, if there is anything I can do to help find and train my replacement, please do not hesitate to let me know.\n\nOnce again, I want"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 71,
    "completion_tokens": 256,
    "total_tokens": 327
  }
}
'''
