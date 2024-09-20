from transformers import AutoTokenizer, T5ForConditionalGeneration

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

# Define inference function for translation
def translate_text(text, target_language):
    language_code = {
        "French": "translate English to French",
        "German": "translate English to German",
        "Romanian": "translate English to Romanian",
    }
    translation_task = language_code.get(target_language, "translate English to French")
    input_ids = tokenizer(f"{translation_task}: {text}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=60, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
