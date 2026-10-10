# AI Annual Report Analyzer

An AI-powered annual report analysis tool built with Python, Qwen, FastAPI, and SQLite. It extracts key business information from Chinese listed companies’ annual report text and returns structured JSON results.

Features

* AI-powered analysis: Uses Qwen to analyze annual report text.
* Structured output: Extracts business descriptions, revenue drivers, competitive advantages, risks, and management outlook.
* Text file upload: Accepts .txt files through a FastAPI endpoint.
* Database storage: Saves analysis results in a SQLite database.
* Modular design: Separates API handling, LLM calls, analysis logic, and database operations.

Tech Stack

* Python
* FastAPI
* Pydantic
* Qwen API (OpenAI-compatible interface)
* SQLite
* OpenAI Python SDK
* python-dotenv
* Uvicorn

Project Structure
```text
annual_report_analyzer/
├── api.py
├── main.py
├── analysis.py
├── llm.py
├── database.py
├── config.py
├── data/
│   └── example_annual_report.txt
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```
The .env file and the SQLite database are local runtime files and should not be committed to GitHub.

How It Works
```text
Upload a .txt file
        ↓
      FastAPI
        ↓
Extract text content
        ↓
      Qwen API
        ↓
Structured JSON result
        ↓
      SQLite
        ↓
Return the analysis result
```
Analysis Fields

The application extracts the following information:

Field Description
business A concise description of the company’s main business
revenue_drivers Main revenue sources and revenue drivers
competitive_advantages Competitive advantages mentioned in the source text
risks Risks explicitly mentioned in the source text
management_outlook Management’s views on future development

The model is instructed to use only the supplied text and avoid inventing information that is not supported by the source.

Requirements

* Python 3.10 or later
* An Alibaba Cloud Model Studio API key with access to the configured model
* Internet access for API requests

Installation

Clone the repository and enter the project directory:

git clone git@github.com:kirot2026/AI-annual-report-analyzer.git
cd annual_report_analyzer

Create and activate a virtual environment:

python -m venv .venv

On macOS or Linux:

source .venv/bin/activate

On Windows:

.venv\Scripts\activate

Install the dependencies:

pip install -r requirements.txt

Configuration

Create a .env file in the project root directory:

DASHSCOPE_API_KEY=your_api_key_here

Configure the model name, API base URL, and database path in config.py as required by your local setup.

Never commit your real API key to GitHub.

Run the Application

Start the FastAPI development server from the project root:

uvicorn api:app --reload

Open the interactive API documentation at:

http://127.0.0.1:8000/docs

Find the POST /analyze endpoint and select Try it out.

Provide the following fields:

* file: A .txt file containing annual report text, encoded as UTF-8.
* company: The company name.
* report_year: The annual report year.

Execute the request to receive the structured analysis result.

The application creates the database table when the FastAPI application starts and stores analysis results in SQLite.

Example Output

{
  "business": "The company is primarily engaged in ...",
  "revenue_drivers": [
    "..."
  ],
  "competitive_advantages": [
    "..."
  ],
  "risks": [
    "..."
  ],
  "management_outlook": [
    "..."
  ]
}

The example above illustrates the output structure. Actual results depend on the uploaded text and the model’s response.

Current Limitations

* Supports .txt uploads only; PDF parsing and OCR are not implemented.
* Designed for relatively short text excerpts rather than complete annual reports.
* Analysis quality depends on the supplied text and the model’s output.
* Model-generated findings should be checked against the original annual report.
* This version provides a backend API; a web-based user interface is planned for a future iteration.

What I Learned

Through this project, I practiced:

* Calling an LLM through an API.
* Designing prompts for structured output.
* Parsing JSON responses in Python.
* Organizing code into reusable modules.
* Handling file uploads with FastAPI.
* Using Pydantic to validate request fields.
* Storing structured analysis results in SQLite.
* Connecting an LLM workflow with a web API.

Future Improvements

* Build a simple web interface for uploading annual report files.
* Support PDF text extraction.
* Improve long-document processing through text chunking and multi-stage summarization.
* Add database queries for viewing previous analyses.
* Improve error handling and input validation.

Disclaimer

This project is for learning and research purposes only. AI-generated analysis may contain errors or omissions and should not be treated as investment advice. Always verify important findings against the original disclosures.
