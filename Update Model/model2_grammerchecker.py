import nltk
from typing import Dict, List

nltk.download('punkt')

class SinhalaChecker:
    def __init__(self):
        """Initialize the Sinhala spelling and grammar checker."""
        self.verb_rules = {
            "කළෙමි": {"tense": "past", "subject": ["මම"]},
            "කරමි": {"tense": "non-past", "subject": ["මම"]},
            "කතා කළෙමි": {"tense": "past", "subject": ["මම"]},
            "කතා කරමි": {"tense": "non-past", "subject": ["මම"]},
            "ලිවෙමි": {"tense": "past", "subject": ["මම"]},
            "ලියමි": {"tense": "non-past", "subject": ["මම"]},
            "පැදවූවෙමි": {"tense": "past", "subject": ["මම"]},
            "පදවමි": {"tense": "non-past", "subject": ["මම"]},
            "ආදරය කළෙමි": {"tense": "past", "subject": ["මම"]},
            "ආදරය කරමි": {"tense": "non-past", "subject": ["මම"]},
            "දුන්නෙමි": {"tense": "past", "subject": ["මම"]},
            "දෙමි": {"tense": "non-past", "subject": ["මම"]},
            "සිනාසුනෙමි": {"tense": "past", "subject": ["මම"]},
            "සිනාසෙමි": {"tense": "non-past", "subject": ["මම"]},
            "ගත්තෙමි": {"tense": "past", "subject": ["මම"]},
            "ගනිමි": {"tense": "non-past", "subject": ["මම"]},
            "කතා කළේය": {"tense": "past", "subject": ["ඔහු"]},
            "කතා කරයි": {"tense": "non-past", "subject": ["ඔහු"]},
            "ලිවේය": {"tense": "past", "subject": ["ඔහු"]},
            "ලියයි": {"tense": "non-past", "subject": ["ඔහු"]},
            "පැදවූයේය": {"tense": "past", "subject": ["ඔහු"]},
            "පදවයි": {"tense": "non-past", "subject": ["ඔහු"]},
            "ආදරය කළේය": {"tense": "past", "subject": ["ඔහු"]},
            "ආදරය කරයි": {"tense": "non-past", "subject": ["ඔහු"]},
            "දුන්නේය": {"tense": "past", "subject": ["ඔහු"]},
            "දෙයි": {"tense": "non-past", "subject": ["ඔහු"]},
            "සිනාසුනේය": {"tense": "past", "subject": ["ඔහු"]},
            "සිනාසෙයි": {"tense": "non-past", "subject": ["ඔහු"]},
            "ගත්තේය": {"tense": "past", "subject": ["ඔහු"]},
            "ගනියි": {"tense": "non-past", "subject": ["ඔහු"]},
            "කතා කළෙමු": {"tense": "past", "subject": ["අපි"]},
            "කතා කරමු": {"tense": "non-past", "subject": ["අපි"]},
            "ලිවෙමු": {"tense": "past", "subject": ["අපි"]},
            "ලියමු": {"tense": "non-past", "subject": ["අපි"]},
            "පැදවූවෙමු": {"tense": "past", "subject": ["අපි"]},
            "පදවමු": {"tense": "non-past", "subject": ["අපි"]},
            "ආදරය කළෙමු": {"tense": "past", "subject": ["අපි"]},
            "ආදරය කරමු": {"tense": "non-past", "subject": ["අපි"]},
            "දුන්නෙමු": {"tense": "past", "subject": ["අපි"]},
            "දෙමු": {"tense": "non-past", "subject": ["අපි"]},
            "සිනාසුනෙමු": {"tense": "past", "subject": ["අපි"]},
            "සිනාසෙමු": {"tense": "non-past", "subject": ["අපි"]},
            "ගත්තෙමු": {"tense": "past", "subject": ["අපි"]},
            "ගනිමු": {"tense": "non-past", "subject": ["අපි"]},
        }
    #Tokenize the Sinhala sentence.
    def tokenize_sentence(self, sentence: str) -> List[str]:
        return sentence.split()
    
    #Check grammar rules for a given Sinhala sentence.
    def check_grammar_rules(self, sentence: str) -> List[Dict[str, str]]:
        tokens = self.tokenize_sentence(sentence)
        errors = []

        for word in tokens:
            if word in self.verb_rules:
                rule = self.verb_rules[word]
                if not any(subject in sentence for subject in rule["subject"]):
                    errors.append({
                        "error": f"Incorrect subject-verb agreement for '{word}'",
                        "suggestion": f"Use subject '{rule['subject'][0]}' with '{word}'"
                    })

        # Check for subject-verb consistency
        if sentence.startswith("අපි") and not sentence.endswith("මු"):
            errors.append({
                "error": "A sentence starting with 'අපි' should end with 'මු'.",
                "suggestion": "Ensure the sentence ends with 'මු'."
            })
        elif sentence.startswith("මම") and not sentence.endswith("මි"):
            errors.append({
                "error": "A sentence starting with 'මම' should end with 'මි'.",
                "suggestion": "Ensure the sentence ends with 'මි'."
            })

        return errors

def grammar_check(text: str) -> Dict:
    checker = SinhalaChecker()
    errors = checker.check_grammar_rules(text)
    return {
        "original_text": text,
        "grammar_errors": errors
    }


if __name__ == "__main__":
    input_text = input("Enter a Sinhala sentence for grammar checking: ").strip()
    if input_text:
        result = grammar_check(input_text)
        print("\n=== Grammar Check Results ===")
        print(f"Original Text: {result['original_text']}")
        if result['grammar_errors']:
            for error in result['grammar_errors']:
                print(f"- {error['error']}")
                print(f"  Suggestion: {error['suggestion']}")
        else:
            print("No grammar errors found.")
    else:
        print("No input provided. Exiting.")
