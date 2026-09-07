from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
import os

# Load environment variables (OPENAI_API_KEY)
load_dotenv()

# Model: gpt-4o-mini | Provider: openai
model = init_chat_model("gpt-4o-mini", model_provider="openai")

def generate_explanation(input_text):
  
  #PromptStructure
  prompt_template_str = 
  """You are a professional tech lead,explain {term} to interviwer in a way that is:
1)simple english but clear technical way
2)give example to elabrorate
3)provide the 3 following questions with answers that might be ask about {term}..."""

  prompt_template = PromptTemplate.from_template(prompt_template_str)
  prompt = prompt_template.format(term=input_text)

  response = model.invoke(prompt)
  print(response.text)
  return response.text #or resoponse.content

#UI
import gradio as gr

demo = gr.Interface(
    fn=generate_explanation,
    inputs=[gr.Textbox(label="Enter a tech term", lines=1)],
    outputs=[gr.Textbox(label="Interview Prep", lines=10)],
    flagging_mode="never",
    title="Tech Interview Prep",
    description="Get a simple explanation + interview Q&As for any tech term"
)

