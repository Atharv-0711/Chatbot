# How to Set the Google Gemini API Key

To enable the chatbot to use Google Gemini API, you need to set the `GOOGLE_GEMINI_API_KEY` environment variable with your Google Gemini API key.

## Option 1: Using .env file (Recommended for Development)

1. Open the `.env` file in the project root directory.
2. Replace `your_google_gemini_api_key_here` with your actual Google Gemini API key.
3. Save the file.

The app will automatically load the key from the `.env` file.

## Option 2: Setting Environment Variable Directly

### Steps for Windows

1. Open the Start menu and search for "Environment Variables".
2. Click on "Edit the system environment variables".
3. In the System Properties window, click on the "Environment Variables..." button.
4. Under "User variables" or "System variables", click "New...".
5. Set the variable name as `GOOGLE_GEMINI_API_KEY`.
6. Set the variable value as your Google Gemini API key.
7. Click OK to save and close all dialogs.
8. Restart your terminal or IDE to apply the changes.

### Steps for macOS/Linux

1. Open your terminal.
2. Run the command:
   ```bash
   export GOOGLE_GEMINI_API_KEY="your_google_gemini_api_key_here"
   ```
3. To make it permanent, add the above line to your shell profile file (`~/.bashrc`, `~/.zshrc`, etc.).
4. Restart your terminal or IDE.

## Verify

You can verify the environment variable is set by running:

```bash
echo $GOOGLE_GEMINI_API_KEY  # macOS/Linux
echo %GOOGLE_GEMINI_API_KEY% # Windows CMD
```

After setting the API key, restart your Flask app and the chatbot will be able to generate AI responses.

If you need help obtaining a Google Gemini API key, visit: https://makersuite.google.com/app/apikey
