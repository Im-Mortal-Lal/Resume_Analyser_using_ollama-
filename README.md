# Resume Analyzer using Ollama

## Overview

Resume Analyzer using Ollama is an AI-powered web application that analyzes resumes and evaluates their compatibility with Applicant Tracking Systems (ATS). The application extracts text from PDF resumes and leverages the **Qwen2.5:3B** large language model running locally through **Ollama** to generate detailed resume insights.

The application provides an ATS score, summarizes the resume, identifies missing skills, highlights weaknesses, recommends improvements, suggests suitable job roles, and generates interview questions with sample answers.

---

## Features

- PDF resume upload and text extraction
- AI-powered resume analysis using Qwen2.5:3B
- ATS score evaluation (Out of 100)
- Resume summary
- Identification of resume weaknesses
- Missing skills analysis
- Resume improvement recommendations
- Job role suitability assessment
- Interview questions with sample answers
- Download extracted resume text

---

## Technologies Used

- Python
- Streamlit
- Ollama
- Qwen2.5:3B
- PyPDF2

---

## Project Structure

```
Resume_Analyser_using_Ollama/
│
├── app.py                 # Streamlit application
├── analyzer.py            # AI analysis using Ollama
├── pdf_reader.py          # PDF text extraction
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Im-Mortal-Lal/Resume_Analyser_using_ollama-.git
cd Resume_Analyser_using_Ollama
```

### Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install streamlit ollama PyPDF2
```

---

## Installing Ollama

Download and install Ollama from:

https://ollama.com

After installation, pull the required model:

```bash
ollama pull qwen2.5:3b
```

Verify the installation:

```bash
ollama list
```

---

## Running the Application

Start the Ollama server if it is not already running.

Launch the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## AI Evaluation Criteria

The application evaluates resumes based on the following criteria:

1. ATS Score (Out of 100)
2. Resume Summary
3. Resume Weaknesses
4. Missing Skills
5. Improvement Suggestions
6. Job Role Suitability
7. Five Interview Questions with Sample Answers

---

## Prompt Used

```text
You are an experienced HR Manager and ATS Resume Expert.

Analyze the following resume and provide a comprehensive evaluation including:

- Summary of key qualifications and experience
- Strengths and areas for improvement
- Recommendations for optimization
- Suitability for specific job roles

1. ATS Score (Out of 100)
2. Resume Summary
3. Weaknesses
4. Missing Skills
5. Improvement Suggestions
6. Job Role Suitability
7. Five Interview Questions with Answers

Resume:
{resume}
```

---

## Example Output

```
ATS Score: 87/100

Resume Summary

...

Weaknesses

...

Missing Skills

...

Improvement Suggestions

...

Suitable Job Roles

...

Interview Questions

1.
2.
3.
4.
5.
```

---

## Dependencies

```
streamlit
ollama
PyPDF2
```

---

## Future Enhancements

- Resume and Job Description matching
- Support for DOCX resumes
- Resume keyword highlighting
- Resume comparison
- Export analysis to PDF
- Support for multiple language models
- Enhanced ATS scoring metrics
- Improved user interface

---

## Author

**Lalit Koturu**

GitHub: https://github.com/Im-Mortal-Lal

---
