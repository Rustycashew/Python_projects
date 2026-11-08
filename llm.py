from openai import OpenAI

system_prompt = """
You are an assistant who analyzes the contents of a given website and provide a short on poin t summary of it , while ignoring any 
navigation related text. Respond in markdown. Do not wrap it around codeblock, only respond in markdown."""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary, if it includs any news or announcments,
summarize them too. """

def messages_for(website):
    return[
        {"role":"system","content":system_prompt}
        {"role":"user","content": user_prompt_prefix + website}
    ]

OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(base_url = OLLAMA_BASE_URL,api_key="ollama")

def summarize(url):
    website = fetch_website_contents(url)
    response = ollama.chat.completions.create(
        model = "llama3.2:1b",
        messages = messages_for(website)
    )
    return response.choices[0].message.content

    summarize("docs.python.org")