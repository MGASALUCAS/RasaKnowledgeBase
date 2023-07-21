# Rasa Knowledge Base - Your Gateway to Enhanced Chatbot Experiences.
 
Welcome to Rasa Knowledge Base, a revolutionary project that combines the power of the Rasa chatbot with cutting-edge technologies to provide seamless conversational AI experiences. This comprehensive README will guide you through setting up and utilizing our solution, empowering you to build highly efficient chatbots that draw knowledge from documents effortlessly.


## Introduction
At Rasa Knowledge Base, we understand the challenges developers face when building chatbots. Often, these chatbots struggle to provide precise answers, especially when dealing with large volumes of information. Our mission is to overcome this limitation, offering a codeless proof of concept that allows developers and non-technical individuals to harness the full potential of Rasa and OpenAI API.

## Project Structure
The project comprises two essential parts:

Rasa Chatbot: A customized Rasa chatbot with improved credentials, rules, stories, and NLU data, ensuring enhanced performance and accuracy. The trained model serves as an API for seamless interactions.

Flask App: An elegant Flask application that simplifies the process of uploading a prompt document and external documents. These documents serve as a knowledge base for the chatbot, enabling it to provide expert responses.

## Getting Started
To begin using Rasa Knowledge Base, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/MGASALUCAS/RasaKnowledgeBase.git

cd rasa-knowledge-base

Install the required dependencies:
Copy code
pip install -r requirements.txt
Improvements to the Rasa Chatbot
Our solution enhances the Rasa chatbot by optimizing the credentials, rules, stories, and NLU data. To replicate these improvements, follow these steps:


Replace the default credentials, rules, stories, and NLU data with the optimized versions from our project.

Train the Rasa chatbot:

Copy code
rasa train
Running the Rasa Chatbot API
To run the Rasa chatbot as an API, execute the following commands:

Run the Rasa API server:
css
Copy code
rasa run -m models --enable-api --cors "*" --debug
Start the Rasa action server:
Copy code
rasa run actions --cors "*" --debug
The Flask App - Simplified Knowledge Base

Our elegant Flask app simplifies the process of uploading prompt documents and external documents, which become a rich knowledge base for the chatbot.

Running the Flask App
To run the Flask app, execute the following command:

Copy code
python app.py
Then, access the app in your web browser at: http://127.0.0.1:5000

Future Enhancements
We are committed to continually improving Rasa Knowledge Base. Our future plans include integrating additional natural language processing capabilities, improving summarization algorithms, and expanding the chatbot's understanding of various document formats.

Images:
![Screenshot 2023-07-21 104937](https://github.com/MGASALUCAS/RasaKnowledgeBase/assets/88959075/de7a0a71-9e46-421e-a881-badd1b61f2ce)


![Screenshot 2023-07-21 105118](https://github.com/MGASALUCAS/RasaKnowledgeBase/assets/88959075/9cbda876-54cf-4222-a2ca-aab9c82fceae)

Contributing
We welcome contributions from the open-source community. If you have ideas for enhancements or bug fixes, feel free to submit a pull request.

License
Rasa Knowledge Base is licensed under the MIT License. See LICENSE for more details.

Thank you for choosing Rasa Knowledge Base! We look forward to witnessing your innovative and impactful chatbot creations. Happy Chatbotting! 🤖💬
