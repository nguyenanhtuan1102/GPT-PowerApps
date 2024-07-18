from flask import Flask, render_template, request, redirect, url_for, flash
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import fitz
import os
from dotenv import load_dotenv

application = Flask(__name__)
app = application

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))
generation_config = {
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 500
        }

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

model = genai.GenerativeModel(model_name = "models/gemini-pro",
                                   generation_config = generation_config,
                                   safety_settings = safety_settings)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict-next-word', methods=['GET', 'POST'])
def predict_next_word():
    if request.method == "POST":
        user_input = request.form['user_input_pwn']
        model_pnw = model.generate_content(f"Show me the next word of this sentence: {user_input}. Just only write the word. Don't format anything. Capitalize the first letter of the word.")
        text_pnw = model_pnw.text
        return render_template('predict_next_word.html', text_pnw=text_pnw)
    else:
        return render_template('predict_next_word.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == "POST":
        user_input = request.form['user_input_cb']
        model_cb = model.generate_content(f"Answer this question: {user_input}. Just write the anwser in 1 line. Don't format anything.")
        text_cb = model_cb.text
        return render_template('chatbot.html', text_cb=text_cb)
    else:
        return render_template('chatbot.html')

@app.route('/resume-screening', methods=['GET', 'POST'])
def resume_screening():
    if request.method == 'POST':
        if 'resume' not in request.files:
            return "No file part"
        file = request.files['resume']
        if file.filename == '':
            return "No selected file"
        if file and file.filename.endswith('.pdf'):
            pdf_content = extract_text_from_pdf(file)
            role_rs = model.generate_content(f"Screen this resume: {pdf_content}. What is job position of this resume. Just write the answer. Don't format anything. Capitalize the first letter of the word.")
            text_role_rs = role_rs.text

            name_rs = model.generate_content(f"Screen this resume: {pdf_content}. What is the name of applicant. Just write the answer. Don't format anything. Capitalinze the first letter of each word.")
            text_name_rs = name_rs.text

            email_rs = model.generate_content(f"Screen this resume: {pdf_content}. What is the email of applicant. Just write the answer. Don't format anything.")
            text_email_rs = email_rs.text

            return render_template('resume_screening.html', text_name_rs=text_name_rs, text_email_rs=text_email_rs, text_role_rs=text_role_rs)
    return render_template('resume_screening.html')

def extract_text_from_pdf(pdf_file):
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

if __name__ == '__main__':
    app.run(debug=True)