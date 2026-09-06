# Reproduction and interview guide

## A practical two-session exercise

Session one: run the six samples and 22 tests, open the HTML report, and manually check cases 02 and 04 against the raw `.eml` files. Calculate an attachment SHA-256 separately. Explain why a hash identifies bytes but does not establish that a file is malicious. Record results in your own notes.

Session two: change the reply-domain behavior with a narrow, explicit partner exception and write both a legitimate-pair test and an attacker-pair test. Add a seventh sample you authored. Predict the output before running it, then document any difference. Do not claim this improvement until it exists and you have run it.

## Questions to practice aloud

1. Why can an Authentication-Results header be forged? What evidence establishes the trusted receiving boundary?
2. Why is a passing DMARC result insufficient to prove an email safe?
3. How do the visible URL, actual target host, and an HTTP redirect differ?
4. Which bytes are hashed for the message and for attachments?
5. Why does a benign control belong in a detection project?
6. What would you investigate after confirming a click? Which additional evidence is required before claiming compromise?
7. Why are message URLs defanged and HTML escaped in the report?
8. Which messages will this parser miss? How would you measure coverage on a representative, labelled dataset?

## Honest explanation after reproduction

“I worked through an AI-assisted offline email-triage project. It parses synthetic messages, preserves source hashes, extracts URLs and attachment metadata, and explains observations that need review. I reproduced the tests and manually checked [only list cases you actually checked]. The benign partner case helped me understand false positives. The tool does not authenticate a message or decide whether a user was compromised. My own contribution was [describe an actual change and its test].”

Before reproduction, say: “My portfolio contains an AI-assisted lab that I am preparing to reproduce.” Do not substitute a repository's existence for personal understanding.
