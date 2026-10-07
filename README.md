# AI Annual Report Analyzer
An LLM-powered Python application that analyzes annual report text and converts unstructured business information into structured data.
The project uses Qwen via Alibaba Cloud Model Studio, Python, SQLite, and modular Python components. It is designed as a practical project for exploring the integration of Large Language Models with financial research and structured data processing.
Overview
Annual reports contain a large amount of unstructured information about a company’s business, revenue sources, competitive advantages, risks, and future outlook.
This project uses an LLM to extract these key aspects from annual report text and store the results in a SQLite database.
The current workflow is:
```text
Annual Report Text
       ↓
Python
       ↓
LLM (Qwen)
       ↓
Structured JSON
       ↓
Python Processing
       ↓
SQLite Database
       ↓
Query & Display
```
The project is currently implemented as a command-line application. A future version will expose the analysis functionality through FastAPI and provide a web interface.

⸻

Features
* Analyze annual report text with an LLM
* Extract structured company information
* Generate JSON-formatted analysis
* Identify:
    * Main business
    * Revenue drivers
    * Competitive advantages
    * Risks
    * Management outlook
* Store analysis results in SQLite
* Prevent duplicate records for the same company and reporting year
* Query previously stored analysis results
* Modular Python project structure
* Environment-based API key management

⸻

Extracted Information
For each annual report, the model extracts the following fields:
{
  "business": "...",
  "revenue_drivers": [],
  "competitive_advantages": [],
  "risks": [],
  "management_outlook": []
}
Field descriptions
| Field | Description |
| :--- | :--- |
| `business` | Summary of the company's main business |
| `revenue_drivers` | Main sources or drivers of revenue |
| `competitive_advantages` | Competitive strengths explicitly supported by the source text |
| `risks` | Risks explicitly mentioned in the source text |
| `management_outlook` | Management's expectations or outlook for future development |
The model is instructed not to invent information that is not supported by the provided text.

⸻

Project Structure
```text
ai-annual-report-analyzer/
│
├── main.py
├── config.py
├── llm.py
├── analysis.py
├── database.py
│
├── data/
│   └── example_annual_report.txt
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```
main.py
The entry point of the application.
It coordinates the complete workflow:
```text
User Input
   ↓
Annual Report Analysis
   ↓
Database Storage
   ↓
Database Query
   ↓
Result Display
```
analysis.py
Responsible for the analysis logic.
Main responsibilities:
* Build the LLM prompt
* Send annual report text to the LLM
* Parse the JSON response
* Convert list fields into JSON strings for SQLite storage
* Prepare structured data for the database layer
llm.py
Responsible for communication with the LLM API.
It:
* Loads the API key from environment variables
* Creates the OpenAI-compatible client
* Sends prompts to Qwen
* Returns the model’s response
database.py
Responsible for SQLite operations.
Current responsibilities include:
* Creating the database table
* Establishing database connections
* Inserting analysis results
* Querying stored records
config.py
Stores non-sensitive project configuration, such as:
MODEL = "qwen-flash"
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
DB_PATH = "annual_report.db"
API keys are not stored in this file.
data/
Contains a small example annual report text file for testing and demonstration.
Large original annual reports are intentionally not included.

⸻

Requirements
* Python 3.10+
* Alibaba Cloud Model Studio / DashScope API access
* A Qwen model supported by the configured account
Python packages:
openai
python-dotenv
SQLite is included with Python and does not require a separate installation.

⸻

Installation
Clone the repository:
git clone <your-repository-url>
cd ai-annual-report-analyzer
Create a virtual environment:
python -m venv .venv
Activate it.
macOS / Linux
source .venv/bin/activate
Windows
.venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt

⸻

Configuration
Create a .env file in the project root:
DASHSCOPE_API_KEY=your_api_key_here
The API key is loaded through python-dotenv.
The .env file should never be committed to GitHub.
Example .gitignore:
.env
annual_report.db
__pycache__/
.venv/

⸻

Usage
Run:
python main.py
The program asks for:
Company name:
Report year:
Annual report text:
The program then:
1. Creates the SQLite table if it does not already exist.
2. Sends the annual report text to Qwen.
3. Parses the structured JSON response.
4. Converts list fields into JSON strings.
5. Stores the result in SQLite.
6. Queries the database.
7. Prints the analysis result.

⸻

Database Design
The project uses SQLite with the following table:
CREATE TABLE IF NOT EXISTS annual_report_analysis (
    id INTEGER PRIMARY KEY,
    company TEXT,
    report_year INTEGER,
    source_text TEXT,
    business TEXT,
    revenue_drivers TEXT,
    competitive_advantages TEXT,
    risks TEXT,
    management_outlook TEXT,
    UNIQUE(company, report_year)
);
The combination of:
company + report_year
is unique.
Therefore, the same company’s annual report for the same year will not be inserted twice.
List-type fields are stored as JSON strings because SQLite does not have a native Python list type.
For example:
[
    "Revenue growth",
    "Increasing customer demand"
]
is stored as:
["Revenue growth", "Increasing customer demand"]
and converted back to a Python list with json.loads() when displaying the results.

⸻

Design Principles
1. Separate LLM logic from database logic
The project separates:
```text
LLM API
   ↓
analysis
   ↓
database
```
This makes each component easier to understand, test, and modify.
2. Structured output instead of free-form text
Instead of asking the model to generate an ordinary paragraph, the project requires a fixed JSON structure.
This makes the model output easier to process programmatically.
3. Source-grounded extraction
The model is instructed to use only information explicitly supported by the provided annual report text.
This is particularly important for financial information, where unsupported claims can lead to misleading conclusions.
4. Human verification
LLM-generated analysis should be treated as an analytical aid rather than authoritative financial research.
Important information should be checked against the original annual report and other primary sources.

⸻

Example Workflow
A simplified example:
```text
Example Annual Report
        ↓
   Qwen Analysis
        ↓
┌──────────────────────────────┐
│ business                     │
│ revenue_drivers              │
│ competitive_advantages       │
│ risks                        │
│ management_outlook           │
└──────────────────────────────┘
        ↓
      SQLite
        ↓
   Query Results
```
⸻

Current Limitations
The current version is intentionally simple.
1. Text input
The current version expects annual report text to be provided directly.
Future versions will support file uploads.
2. Long annual reports
The current version is designed for relatively short text sections.
A complete annual report can contain hundreds of pages and should not simply be sent to the model as one request.
Future versions may implement:
* Section-aware text extraction
* Sentence/paragraph chunking
* Overlapping chunks
* Map-Reduce summarization
* Section-level analysis
3. LLM output reliability
Although the prompt requires valid JSON, model output can occasionally fail to follow the requested structure.
Future versions may introduce stronger schema validation and retry mechanisms.
4. No financial conclusions
The project extracts and organizes information from annual reports. It does not provide investment recommendations or automatically determine whether a stock should be bought or sold.

⸻

Future Development
Version 1 — Current
```text
Annual Report Text
        ↓
Qwen
        ↓
JSON
        ↓
SQLite
```
Version 2 — FastAPI
Expose the analysis functionality through a REST API:
```text
Client
  ↓
POST /analyze
  ↓
FastAPI
  ↓
LLM Analysis
  ↓
SQLite
  ↓
JSON Response
```
Version 3 — Web Interface
Build a lightweight frontend using:
* HTML
* CSS
* JavaScript
* Fetch API
The user will be able to submit annual report text through a browser and view structured analysis results.
Version 4 — File Upload
Support uploading annual report text files and eventually PDF documents.
Version 5 — Long Document Processing
Support complete annual reports through:
* Text extraction
* Section-aware chunking
* Multi-step LLM analysis
* Result aggregation
Version 6 — Financial Research Workflow
Potential future integration with financial data:
```text
Annual Reports
      +
Market Data
      +
Company Information
      ↓
Python / SQL
      ↓
LLM Analysis
      ↓
Structured Database
      ↓
Financial Research Notes
```
⸻

What I Learned
This project was built to practice the integration of several technologies rather than focusing on a single library.
Key concepts include:
* Python modular programming
* OpenAI-compatible LLM APIs
* Qwen model integration
* Prompt engineering
* Structured JSON output
* JSON parsing
* Exception handling
* SQLite database design
* SQL operations
* Data serialization
* Environment variable management
* Separation of application responsibilities

⸻

Disclaimer
This project is for educational and research purposes.
The generated analysis is produced with the assistance of an LLM and may contain errors or omissions. It should not be considered professional investment advice or a substitute for reading the original annual report and conducting independent research.

⸻

License
This project is intended primarily as a personal learning and portfolio project.
If a formal open-source license is added in the future, it will be specified here.