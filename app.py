import gradio as gr
from transformers import AutoTokenizer, T5ForConditionalGeneration

# Load the correct model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")


# Define inference function for translation with language selection
def translate_text(text, language):
    language_code = {
        "French": "translate English to French",
        "German": "translate English to German",
        "Romanian": "translate English to Romanian",
        "English": "translate French to English"  # Assuming reverse translation for English
    }

    # Prepare the input with the selected language
    input_ids = tokenizer(f"{language_code[language]}: {text}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Create Gradio app interface
input_text = gr.Textbox(lines=3, placeholder="Enter text to translate")
language_dropdown = gr.Dropdown(choices=["French", "German", "Romanian", "English"], label="Select target language")
output_text = gr.Textbox(label="Translated Text")

gr.Interface(fn=translate_text, inputs=[input_text, language_dropdown], outputs=output_text,
             title="T5 Translator").launch()