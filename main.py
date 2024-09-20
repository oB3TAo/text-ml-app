import gradio as gr
from translation import translate_text
from summarization import summarize_text
from sentiment_analysis import analyze_sentiment
from grammar_correction import correct_text
from character_count import count_characters
from examples import (translation_examples, summarization_examples,
                      sentiment_examples, grammar_examples,
                      character_count_examples)

# Create Gradio app with tabs for different functionalities
with gr.Blocks() as demo:
    gr.Markdown("# Multilingual Translator and Text Analysis Tool")

    with gr.Tab("Translation"):
        input_text_trans = gr.Textbox(lines=3, placeholder="Enter text", label="Input Text (English)")
        target_language_dropdown = gr.Dropdown(choices=["French", "German", "Romanian"],
                                               label="Select target language", value="French")
        output_text_trans = gr.Textbox(label="Translated Text", interactive=True)
        translate_btn = gr.Button("Translate")
        translate_btn.click(fn=translate_text, inputs=[input_text_trans, target_language_dropdown],
                            outputs=output_text_trans)
        gr.Examples(translation_examples, inputs=[input_text_trans, target_language_dropdown])

    with gr.Tab("Summarization"):
        input_text_summarize = gr.Textbox(lines=5, placeholder="Enter text to summarize", label="Input Text")
        summarized_text = gr.Textbox(label="Summary", interactive=False)
        summarize_btn = gr.Button("Summarize")
        summarize_btn.click(fn=summarize_text, inputs=input_text_summarize, outputs=summarized_text)
        gr.Examples(summarization_examples, inputs=input_text_summarize)

    with gr.Tab("Sentiment Analysis"):
        input_text_sentiment = gr.Textbox(lines=3, placeholder="Enter text to analyze", label="Input Text")
        sentiment_output = gr.Textbox(label="Sentiment", interactive=False)
        sentiment_btn = gr.Button("Analyze Sentiment")
        sentiment_btn.click(fn=analyze_sentiment, inputs=input_text_sentiment, outputs=sentiment_output)
        gr.Examples(sentiment_examples, inputs=input_text_sentiment)

    with gr.Tab("Grammar Correction"):
        input_text_correct = gr.Textbox(lines=3, placeholder="Enter text for grammar correction", label="Input Text")
        corrected_text = gr.Textbox(label="Corrected Text", interactive=False)
        correct_btn = gr.Button("Correct Grammar")
        correct_btn.click(fn=correct_text, inputs=input_text_correct, outputs=corrected_text)
        gr.Examples(grammar_examples, inputs=input_text_correct)

    with gr.Tab("Character Count"):
        input_text_count = gr.Textbox(lines=3, placeholder="Enter text to count characters", label="Input Text")
        character_count = gr.Textbox(label="Character Count", interactive=False)
        count_btn = gr.Button("Count Characters")
        count_btn.click(fn=count_characters, inputs=input_text_count, outputs=character_count)
        gr.Examples(character_count_examples, inputs=input_text_count)

demo.launch()
