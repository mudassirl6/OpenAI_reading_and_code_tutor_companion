# Langchain_reading_and_code_tutor_companion
Virtual Tutor for Coding Practice and Personalized Reading Companion 📚💻

This application provides a virtual tutor experience for both coding practice and reading assistance. It leverages OpenAI’s GPT-3.5-turbo model to generate summaries, contextual explanations, and simplify passages for easy understanding. Additionally, the Virtual Coding Tutor can provide hints and explanations for code snippets, making it an ideal tool for students and developers.

Table of Contents

	1.	Features
	2.	Setup
	3.	Environment Variables
	4.	Usage
	5.	Project Structure
	6.	License



 Features

	•	Reading Companion:
	•	Generate summaries, background context, and simplified explanations for passages of text.
	•	Virtual Coding Tutor:
	•	Get coding hints and explanations for code snippets, aiding in understanding and debugging code.
	•	Session Progress Tracking:
	•	Track and save user queries and responses in a local JSON file to review past sessions.


 Setup

Prerequisites

	•	Python 3.7 or above is required to run this application.
	•	Install the required libraries:

 pip install openai streamlit python-dotenv
 openai_key=your_openai_api_key_here


 Run the application by executing the following command:

 streamlit run <file_name.py>

 Interface

	1.	Navigation: Use the sidebar to select between “Reading Companion” and “Virtual Coding Tutor.”
	2.	Reading Companion Mode:
	•	Enter a text passage in the provided text area.
	•	Use buttons to get a summary, context, or simplified explanation.
	3.	Virtual Coding Tutor Mode:
	•	Enter a code snippet or coding challenge.
	•	Use buttons to get coding hints or explanations.
	•	Each response is saved in a JSON file named progress.json to track your learning.

Progress Tracker

The app saves user input and generated responses in a progress.json file, allowing you to review your learning progress.

Project Structure

	•	main.py: The main script that runs the Streamlit app, containing all the logic for reading assistance, coding tutoring, and UI elements.
	•	progress.json: Stores user queries and model responses for session tracking (auto-generated).

License

This project is licensed under the MIT
