# GPT PowerApps: TuanGPT

![image](https://github.com/user-attachments/assets/2523e0e0-ff7d-4d8c-b71d-6260e7a5f193)

## Introduction
TuanGPT - GPT PowerApps is an innovative project designed to leverage the capabilities of natural language processing (NLP) through the integration of three main tools: Predict Next Word, QA Chatbot, and Resume Screening. This project is developed using Python Flask for the backend, HTML and CSS for the frontend, and deployed using AWS CodePipeline and AWS Beanstalk. The purpose of this report is to present the design, development, and deployment processes of TuanGPT - GPT PowerApps.

![image](https://github.com/user-attachments/assets/42eec356-d00c-481b-ab41-ff4238f6b338)

## Project Overview

### 1. Predict next word
- **Objective**: The Predict Next Word tool aims to provide users with a predictive text feature that suggests the next word in a sentence based on the input provided.
- **Implementation**: Utilizing Gemini pro language model, the tool analyzes the context of the input text and predicts the most likely next word. This feature is particularly useful for writing assistance and enhancing user productivity.
- **User Interaction**: Users input a partial sentence, and the tool generates a prediction for the next word, which can then be accepted or modified by the user.

![image](https://github.com/user-attachments/assets/39025649-048d-4f8e-a0e0-99db3f9db6b5)

### 2. Chatbot
- **Objective**: The QA Chatbot is designed to answer short questions posed by users, leveraging the natural language understanding capabilities of Gemini pro.
- **Implementation**: The chatbot processes user queries, searches for relevant information within its trained dataset, and provides concise and accurate answers. This tool is beneficial for quick information retrieval and customer support applications.
- **User Interaction**: Users type a question into the chatbot interface, and the bot responds with a well-formulated answer, simulating a conversational experience.


![image](https://github.com/user-attachments/assets/99f1288e-24a1-493d-99e1-1cc41797a85d)

### 3. Resume screening
- **Objective**: The Resume Screening tool automates the extraction of key information from resumes, such as the candidate's name, email, and job position.
- **Implementation**: By parsing the content of uploaded resume files, the tool identifies and extracts relevant data points. This feature streamlines the hiring process by quickly sifting through large volumes of resumes to find suitable candidates.
- **User Interaction**: Users upload a resume file, and the tool displays the extracted information, making it easier for HR personnel to review and manage candidate details.

![image](https://github.com/user-attachments/assets/e02ad923-a7e3-4094-a39a-f2de81c9a6b7)

## Development
- **Backend Development**: The backend is developed using Python Flask, which provides a robust framework for handling HTTP requests and managing the logic of the application.
- **Frontend Development**: HTML and CSS are used to create a user-friendly and visually appealing interface. The frontend interacts with the backend through API calls, ensuring a seamless - user experience.

## Deployment
### 1. AWS CodePipeline
- Automated the build, test, and deployment processes.
- Ensured continuous integration and delivery, enabling rapid updates and improvements.
  
  ![image](https://github.com/user-attachments/assets/9cd9b432-9dbe-4134-b47f-324f32917c2c)

### 2. AWS Beanstalk
- Provided a scalable environment for deploying the web application.
- Managed the infrastructure, allowing the development team to focus on application functionality.

  ![image](https://github.com/user-attachments/assets/5ecd703f-4b0b-472e-bb14-d8016337a18c)

## Conclusion
TuanGPT-GPTPowerApps showcases the transformative power of AI in elevating user experiences and streamlining workflows. With the **Predict Next Word** tool, users can supercharge their writing efficiency, effortlessly predicting what comes next in their sentences. The **QA Chatbot** is a swift and reliable information companion, delivering instant answers and enhancing user interaction. Meanwhile, the **Resume Screening** tool revolutionizes the hiring process, making it smoother and more efficient for recruiters.

This innovative project, developed using PythonFlask and deployed through AWSServices, ensures top-notch scalability and reliability. By harnessing the power of these technologies, **TuanGPT-GPTPowerApps** guarantees user satisfaction and sets a new standard for practical AI applications in various domains.

## Try out my project

- **Way 1**: Check out my project [GPT-PowerApps](http://gpt-powerapps.ap-southeast-1.elasticbeanstalk.com/resume-screening)

- **Way 2**: Scan my QR Code

  ![qrcode_gpt-powerapps ap-southeast-1 elasticbeanstalk com](https://github.com/user-attachments/assets/8d514684-7e35-494f-915c-18516f162550)
