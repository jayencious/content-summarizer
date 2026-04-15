# Content Summarizer

This repository houses a simple yet functional content summarizer built with Python. It leverages the power of Google's Gemini API for text summarization and presents it through a basic graphical user interface (GUI) created with Tkinter.

## Key Features:

*   **Google Gemini API Integration:** Utilizes the advanced capabilities of Google's Gemini API to intelligently summarize textual content.
*   **Tkinter GUI:** Provides a user-friendly interface for easy input and output.  Simply paste your text, click a button, and see the summary!
*   **Secure Credential Management:** Employs the `python-dotenv` library to securely manage and protect sensitive API keys and credentials, preventing them from being exposed in the codebase.

## Technologies Used:

*   **Python:** The core programming language for the summarizer logic and GUI.
*   **`google-genai`:**  Python library for interacting with Google's Gemini API.      
*   **`python-dotenv`:** Used to load environment variables from a `.env` file, ensuring secure storage of API keys.
*   **Tkinter:** Python's standard GUI library, used to create the application's interface.   

## Getting Started:

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd content-summarizer
    ```

2.  **Set up your environment:**

    *   Install the required dependencies:

        ```bash
        pip install google-genai python-dotenv tkinter
        ```

    *   Obtain an API key from Google's Gemini API.

    *   Create a `.env` file in the project root directory and add your API key:

        ```
        API_KEY=YOUR_API_KEY
        ```

3.  **Run the application:**

    ```bash
    python src/main.py  # Or the name of your main script file
    ```

## Contributing:

Contributions are welcome! Feel free to submit pull requests with improvements, bug fixes, or new features.

## Developers:
- [Joel Robert Lakra](https://github.com.jayencious)
- [Sparsh Mishra](https://github.com/maj0rkeen)
- [Trisha Raj](https://github.com/trisharaj11)
- [Debangshu Roy](https://github.com/)
