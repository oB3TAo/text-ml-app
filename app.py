import gradio as gr
from transformers import AutoTokenizer, T5ForConditionalGeneration

# Load the correct model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

# Define inference function for translation from English to the target language
def translate_text(text, target_language):
    # Define language codes for English to other language translations
    language_code = {
        "French": "translate English to French",
        "German": "translate English to German",
        "Romanian": "translate English to Romanian",
    }

    # Prepare the input with the selected language
    translation_task = language_code[target_language]
    input_ids = tokenizer(f"{translation_task}: {text}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Define examples with translations from English to the target languages
examples = [
    ["I love machine learning", "French"],
    ["I enjoy reading books", "German"],
    ["The weather is nice today", "Romanian"],
    ["Technology is advancing rapidly", "French"],
    ["This is a fascinating project", "German"],
]

# Create Gradio app interface
input_text = gr.Textbox(lines=3, placeholder="Enter text to translate from English", label="Input Text (English)")
target_language_dropdown = gr.Dropdown(choices=["French", "German", "Romanian"],
                                       label="Select target language", value="French")
output_text = gr.Textbox(label="Translated Text", interactive=True)

# UI Enhancements
clear_btn = gr.Button("Clear Text")

# Launch the Gradio interface with only English-to-target language translation
gr.Interface(
    fn=translate_text,
    inputs=[input_text, target_language_dropdown],
    outputs=output_text,
    examples=examples,
    live=True,
    title="English to Multilingual Translator (French, German, Romanian)",
    description="Translate text from English to French, German, or Romanian.",
).launch()
