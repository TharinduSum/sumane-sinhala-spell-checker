import streamlit as st
from model2_spellchecker import spell_check
from spelling_checker import advanced_spell_check
from model2_grammerchecker import grammar_check
import google.generativeai as genai

# Configure the Generative AI client
genai_client = genai.configure(api_key="AIzaSyAhHtvLGXYmM1vheQjs3Vngk4N_kUfHSIo")  # Replace with your API key
model = genai.GenerativeModel("gemini-1.5-flash")

#Process Sinhala text through spelling and grammar models,  and consolidate results via Gemini AI.
def process_text(input_text):
    
    results = {
        "spell_checked": "",
        "advanced_spell_checked": "",
        "grammar_suggestions": "",
        "generative_ai_output": "",
        "error": "",
    }

    try:
        # Step 1: Spell Check using model2_spellchecker
        spell_checked, _ = spell_check(input_text)
        results["spell_checked"] = spell_checked
    except Exception as e:
        results["error"] += f"Error in model2_spellchecker: {str(e)}\n"

    try:
        # Step 2: Advanced Spell Check using spelling_checker
        advanced_spell_checked = advanced_spell_check(input_text)
        results["advanced_spell_checked"] = advanced_spell_checked
    except Exception as e:
        results["error"] += f"Error in spelling_checker: {str(e)}\n"

    try:
        # Step 3: Grammar Check using model2_grammarchecker
        grammar_results = grammar_check(input_text)
        grammar_errors = [
            f"{error['error']} - Suggestion: {error['suggestion']}"
            for error in grammar_results.get("grammar_errors", [])
        ]
        results["grammar_suggestions"] = "\n".join(grammar_errors) if grammar_errors else "No grammar errors detected."
    except Exception as e:
        results["error"] += f"Error in model2_grammarchecker: {str(e)}\n"

    # Generative AI Consolidation
    prompt = f"""
    Analyze and correct the following text:
    Original User Input: "{input_text}"

    Spell Check Results:
    1. model2_spellchecker: "{results['spell_checked']}"
    2. spelling_checker: "{results['advanced_spell_checked']}"

    Grammar Check Suggestions:
    "{results['grammar_suggestions']}"

    Task:
    1. Identify the best spell check result.
    2. Integrate the grammar suggestions to create a grammatically correct and natural sentence.
    3. Provide a detailed explanation of the changes made, including spelling and grammar adjustments.
    """
    try:
        response = model.generate_content(prompt)
        results["generative_ai_output"] = response.text
    except Exception as e:
        results["error"] += f"Error in Generative AI processing: {str(e)}\n"

    return results

# Streamlit Interface
st.title("Sinhala Spelling and Grammar Checker")
st.markdown("""
This application performs:
- **Spell Checking**: Identifies and corrects spelling errors in Sinhala text.
- **Grammar Checking**: Suggests improvements for grammatical errors.
- **Generative AI Integration**: Consolidates results for a refined output.
""")

# Text input area
input_text = st.text_area("Enter Sinhala Text", "")

# Button to process the input
if st.button("Check Text"):
    if input_text.strip():
        # Process the text
        results = process_text(input_text.strip())

        # Display spell check results
        st.subheader("Spell Check Results")
        st.write(f"Basic Spell Checked Text: {results.get('spell_checked', 'No result')}")
        st.write(f"Advanced Spell Checked Text: {results.get('advanced_spell_checked', 'No result')}")

        # Display grammar suggestions
        st.subheader("Grammar Suggestions")
        st.write(results.get("grammar_suggestions", "No grammar suggestions found."))

        # Display generative AI output
        st.subheader("Generative AI Consolidation")
        st.write(results.get("generative_ai_output", "No output from Generative AI."))

        # Display errors if any
        if results.get("error"):
            st.subheader("Errors")
            st.error(results["error"])
    else:
        st.error("Please enter text to process.")
