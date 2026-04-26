# Local OCR App Plan

This folder will contain the small local application we build during the study process.

## App Goal

Create a simple document processor for:

- delivery notes
- purchase invoices

The app will use local and open-source tools only.

## Planned Features

### Phase A

- load PDF files from the two sample folders
- inspect each PDF
- try direct text extraction first

### Phase B

- convert PDFs to page images when needed
- preprocess images with OpenCV
- run OCR with Tesseract

### Phase C

- extract structured fields
- save results as JSON
- compare outputs across document types

## Expected Learning Outcomes

By building this app, you will understand:

- how to choose extraction vs OCR
- how preprocessing affects OCR quality
- how to parse business documents
- how to explain the system in interviews

## Proposed Future Files

- `main.py`
- `extract_pdf_text.py`
- `preprocess.py`
- `ocr_engine.py`
- `field_parser.py`
- `schemas.py`

## First Build Step

The first coding step should be to inspect a few sample PDFs and test direct extraction before writing OCR code.
