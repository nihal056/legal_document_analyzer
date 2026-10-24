"""Legal Document Analyzer

Sends a piece of legal text to the Google Gemini API and prints a summary,
key clauses and risks. The model is asked to reply as JSON, and the JSON is
parsed in Python so each part can be used separately.

Rebuilt from the Colab notebook written on 28 May 2026. The only change is
that the API key is read from the GEMINI_API_KEY environment variable instead
of Colab secrets, so the script runs outside Colab.
"""

import json
import os

from google import genai

MODEL = "gemini-2.5-flash"

SAMPLE_TEXT = """
This Employment Agreement is entered into between ABC Company
and John Smith. The employee will work for a period of 2 years
starting January 1st 2026. The salary will be 45,000 euro per year
paid monthly. Either party may terminate this agreement with
30 days written notice. The employee must not work for any
competitor for 6 months after leaving the company.
"""

PROMPT_TEMPLATE = """
You are a legal document analyser. Analyse this legal text and return
your response ONLY as valid JSON with exactly this structure:
{{
  "summary": "2 sentence summary here",
  "key_clauses": ["clause 1", "clause 2", "clause 3"],
  "risks": ["risk 1", "risk 2", "risk 3"]
}}

Do not include any text before or after the JSON.

Legal text:
{legal_text}
"""


def analyse(legal_text: str) -> dict:
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model=MODEL,
        contents=PROMPT_TEMPLATE.format(legal_text=legal_text),
    )
    clean = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(clean)


def show(data: dict) -> None:
    print("SUMMARY:")
    print(data["summary"])
    print("\nKEY CLAUSES:")
    for clause in data["key_clauses"]:
        print("-", clause)
    print("\nRISKS:")
    for risk in data["risks"]:
        print("-", risk)


if __name__ == "__main__":
    show(analyse(SAMPLE_TEXT))
