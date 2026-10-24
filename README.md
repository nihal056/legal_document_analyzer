# Legal Document Analyzer

A small Python project that sends legal text to the Google Gemini API and returns a summary, key clauses and risks as structured JSON.

## How it works

1. The legal text is placed inside a prompt that tells the model to act as a legal document analyser.
2. The prompt asks for a reply in one fixed JSON format: `summary`, `key_clauses` and `risks`.
3. The script sends the prompt to Gemini (`gemini-2.5-flash`) and cleans the reply.
4. The reply is parsed with `json.loads`, so each part can be used on its own.

## Example output

From one run on a short sample employment agreement:

```
SUMMARY:
This Employment Agreement is between ABC Company and John Smith, setting a 2-year term starting January 1st 2026, with an annual salary of 45,000 euro. It includes provisions for termination with 30 days' notice and a 6-month post-employment non-compete clause.

KEY CLAUSES:
- Employment for a period of 2 years starting January 1st 2026.
- Annual salary of 45,000 euro, paid monthly.
- Either party may terminate the agreement with 30 days written notice.
- Employee must not work for any competitor for 6 months after leaving the company.

RISKS:
- The 6-month non-compete clause restricts the employee's ability to seek employment with competitors immediately after leaving.
- The 30-day notice period for termination may be relatively short for the employee to find new employment or for the employer to find a replacement.
- Despite a stated 2-year term, the 30-day termination clause allows for early cessation, potentially impacting job security for the employee or retention for the employer.
```

## Run it

1. Get a free API key from Google AI Studio (aistudio.google.com/apikey).
2. Install the package and set the key as an environment variable:

```
pip install -r requirements.txt
set GEMINI_API_KEY=your_key_here      (Windows Command Prompt)
export GEMINI_API_KEY=your_key_here   (Mac or Linux)
python legal_document_analyzer.py
```

Never put the API key in the code or commit it to GitHub.

## Status

Personal project, built to learn the Gemini API, prompt engineering and JSON parsing. It was tested on one short sample employment agreement. It does not read PDF files yet, and the output has not been checked by a lawyer, so it is not legal advice.
