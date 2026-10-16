# %pip install openai
from openai import OpenAI
import config
# Prompt 
SYSTEM_PROMPT = "تو یه دستیار فروشگاهی فارسی هستی. فقط بر اساس اطلاعات داده‌شده پاسخ می‌دی."

RAG_TEMPLATE = """با استفاده از اطلاعات زیر به سؤال پاسخ بده.

اطلاعات:
{context}

سؤال:
{query}

فقط بر اساس اطلاعات ارائه‌شده پاسخ بده.
اگر پاسخ در اطلاعات وجود ندارد، بگو:
«اطلاعات کافی در اسناد موجود نیست.»"""

NO_CONTEXT_RESPONSE = "اطلاعات کافی در اسناد موجود نیست."
# Client 
_client = OpenAI(
    api_key=config.OPENAI_API_KEY,
    base_url=config.OPENAI_BASE_URL
)
# Generate 
def generate(messages):
    """Send messages to GapGPT API and return the response."""
    response = _client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=messages,
        max_tokens=config.MAX_NEW_TOKENS,
        temperature=config.TEMPERATURE
    )
    return response.choices[0].message.content
# Test
if __name__ == "__main__":
    messages = [{"role": "user", "content": "سلام پایتخت ایران کجاست؟"}]
    print(generate(messages))
