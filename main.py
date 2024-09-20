import gradio as gr
from translation import translate_text
from summarization import summarize_text
from sentiment_analysis import analyze_sentiment
from grammar_correction import correct_text
from character_count import count_characters
from examples import (translation_examples, summarization_examples,
                      sentiment_examples, grammar_examples,
                      character_count_examples)

# Initialize the Gradio interface
with gr.Blocks() as demo:
    # Main title
    gr.Markdown("# Multilingual Translator and Text Analysis Tool")

    # Translation Tab
    with gr.Tab("Translation"):
        input_text_trans = gr.Textbox(lines=3, placeholder="Enter English text", label="Input Text (English)")
        target_language_dropdown = gr.Dropdown(choices=["French", "German", "Romanian"],
                                               label="Select Target Language", value="French")
        output_text_trans = gr.Textbox(label="Translated Text", interactive=False)
        translate_btn = gr.Button("Translate")

        # Button Click Logic
        translate_btn.click(fn=translate_text,
                            inputs=[input_text_trans, target_language_dropdown],
                            outputs=output_text_trans)

        # Translation Examples
        gr.Examples(translation_examples, inputs=[input_text_trans, target_language_dropdown])

    # Summarization Tab
    with gr.Tab("Summarization"):
        input_text_summarize = gr.Textbox(lines=5, placeholder="Enter text to summarize", label="Input Text")
        summarized_text = gr.Textbox(label="Summary", interactive=False)
        summarize_btn = gr.Button("Summarize")

        # Button Click Logic
        summarize_btn.click(fn=summarize_text,
                            inputs=input_text_summarize,
                            outputs=summarized_text)

        # Summarization Examples
        gr.Examples(summarization_examples, inputs=input_text_summarize)

    # Sentiment Analysis Tab
    with gr.Tab("Sentiment Analysis"):
        input_text_sentiment = gr.Textbox(lines=3, placeholder="Enter text to analyze sentiment", label="Input Text")
        sentiment_output = gr.Textbox(label="Sentiment Result", interactive=False)
        sentiment_btn = gr.Button("Analyze Sentiment")

        # Button Click Logic
        sentiment_btn.click(fn=analyze_sentiment,
                            inputs=input_text_sentiment,
                            outputs=sentiment_output)

        # Sentiment Analysis Examples
        gr.Examples(sentiment_examples, inputs=input_text_sentiment)

    # Grammar Correction Tab
    with gr.Tab("Grammar Correction"):
        input_text_correct = gr.Textbox(lines=3, placeholder="Enter text for grammar correction", label="Input Text")
        corrected_text = gr.Textbox(label="Corrected Text", interactive=False)
        correct_btn = gr.Button("Correct Grammar")

        # Button Click Logic
        correct_btn.click(fn=correct_text,
                          inputs=input_text_correct,
                          outputs=corrected_text)

        # Grammar Correction Examples
        gr.Examples(grammar_examples, inputs=input_text_correct)

    # Character Count Tab
    with gr.Tab("Character Count"):
        input_text_count = gr.Textbox(lines=3, placeholder="Enter text to count characters", label="Input Text")
        character_count = gr.Textbox(label="Character Count Result", interactive=False)
        count_btn = gr.Button("Count Characters")

        # Button Click Logic
        count_btn.click(fn=count_characters,
                        inputs=input_text_count,
                        outputs=character_count)

        # Character Count Examples
        gr.Examples(character_count_examples, inputs=input_text_count)

# Launch the app
demo.launch()
