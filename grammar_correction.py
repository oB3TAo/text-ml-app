from transformers import pipeline

# Load the grammar correction model
grammar_correction_model = pipeline(task="text2text-generation", model="hassaanik/grammar-correction-model")

def correct_text(text):
    result = grammar_correction_model(text, max_length=200, num_beams=5, no_repeat_ngram_size=2)
    return result[0]['generated_text']
