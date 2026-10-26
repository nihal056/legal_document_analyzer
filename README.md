# Legal Document Analyzer

A Python notebook that sends a legal document to the Google Gemini API and returns a short summary, the key clauses and the possible risks. Every clause and risk comes with a short quote from the document, and the code checks that each quote really appears in the text.

This is a learning project. It gives general information, not legal advice, and it can be wrong.

## What it does

1. Takes the document text and wraps it in `<document>` tags. The prompt tells Gemini to treat everything inside the tags as text to read and never to follow instructions found inside it.
2. Asks Gemini for a reply in a fixed JSON shape (summary, key clauses, risks with a severity of low, medium or high).
3. Checks the reply with Pydantic. A reply that is broken or has the wrong shape is rejected.
4. Retries up to 3 times when the server is busy, the network drops or the reply is not valid. A wrong API key stops straight away.
5. Logs the time and the token counts of each call.
6. Checks that every quote Gemini gave is really in the original document.
7. Lets Gemini call a small glossary function (`lookup_legal_term`) when it explains the risks in plain English. This is function calling.

## How to run it

1. Get a free Gemini API key from Google AI Studio.
2. Install the packages: `pip install -r requirements.txt`
3. Start Jupyter: `jupyter notebook`, then open `legal_document_analyzer.ipynb`.
4. In the settings cell near the top, replace the text `API KEY` with your own key, then run the cells from top to bottom.

Never save or upload the notebook with your real key in it.

## Results

The last cell runs three short sample documents (an employment agreement, an NDA and a lease) that I wrote for this test. It counts how many expected facts, such as "2 years", "45,000" or "20,000", appear in the output, and how many quotes really appear in the document. The fact check is simple word matching, so it is a rough check and not a measure of accuracy.

| Prompt version | Facts found | Quotes found in the document |
|---|---|---|
| First version | 12 of 13 | 16 of 16 |
| Current version (asks for exact amounts and dates) | 13 of 13 | 15 of 15 |

In the first version, the one missed fact was the NDA penalty amount (20,000 euro). The output said "a significant financial penalty" without the figure. I added a line to the prompt asking for exact amounts, durations and dates, and the figure now appears. I ran the current version more than once and it found all 13 facts each time.

The output is not identical from run to run, even with temperature set to 0. For example, the NDA gave 1 risk in some runs and 3 risks in others, and the number of quotes changed between 4 and 7. So the quote totals above are from one run. I tuned the prompt on these same three samples, so the 13 of 13 is partly fitted to this test and would probably be lower on documents the prompt has not seen.

The notebook waits and retries when the free tier rate limit is hit (5 requests per minute, 20 per day for this model).

## Limits

- Only tested on three short documents. Real contracts are longer and messier.
- Gemini can miss risks or rate them differently from a lawyer.
- It knows nothing about the law outside the document, so it cannot say whether a clause is legal or enforceable.
- Only plain text is supported in this version.

## What I would add next

PDF input, a command line version, unit tests, and a larger test set with real contracts.
