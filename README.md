# 01. Sinhala Spelling and Grammer Checker

This is Artificial Intteligence mini project by @TharinduSum and @tharuu.

## Installation

Clone the Git repository.

Run sinhala-spelling-checker.py file 

```bash
python sinhala-checker.py
```

## Output by Code

![image alt](https://github.com/TharinduSum/sumane-sinhala-spell-checker/blob/main/output1.jpg?raw=true)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

# 02. Sinhala Spelling and Grammar Checker

A Python-based tool that uses Google's Gemini AI to check spelling and grammar in Sinhala text. This tool is specifically designed to work in Google Colab, making it accessible without local setup requirements.

## Features

- Real-time spelling and grammar checking for Sinhala text
- Detailed analysis and suggestions for improvements
- User-friendly interface with bilingual prompts
- Error handling for API interactions
- Continuous operation mode with easy exit option

## Prerequisites

- Google Colab account
- Google Gemini API key (available from Google AI Studio)
- Basic familiarity with Google Colab

## Getting Started

### Getting Your API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Save the API key securely - you'll need it to run the program

### Running the Program

1. Open [Google Colab](https://colab.research.google.com/)
2. Create a new notebook
3. Copy the entire code from `sinhala_checker.py` into a code cell
4. Run the cell
5. When prompted, enter your Gemini API key
6. Start checking your Sinhala text!

## Usage

After starting the program:

1. Enter the text you want to check when prompted
2. The program will analyze your text and provide:
   - Spelling errors (if any)
   - Grammar errors (if any)
   - Suggested corrections
   - Explanations of the errors
3. Type 'exit' to quit the program

## Example

```python
# Input
මම ගෙදර යනවා.

# Output
විශ්ලේෂණය:
1. Spelling errors: None
2. Grammar errors: None
3. Suggested corrections: N/A
4. Explanation: The sentence is grammatically correct.
```

## Error Messages

Common error messages and their solutions:

- "Error: Invalid API key" - Double-check your API key
- "Error occurred during API call" - Check your internet connection
- "Please type something" - Input field cannot be empty

## Limitations

- Requires active internet connection
- API usage may be subject to rate limits
- Accuracy depends on Gemini AI's understanding of Sinhala

## Contributing

Feel free to fork this project and submit pull requests for any improvements you develop.

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
- Create an issue in the GitHub repository
- Contact the maintainer
- Check Google's Gemini API documentation for API-specific issues

## Acknowledgments

- Google Gemini AI for providing the language processing capabilities
- The Sinhala computing community for their continuous support
