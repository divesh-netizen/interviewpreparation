# OCR Study Architecture

This is the step-by-step architecture for learning OCR, text extraction, and document understanding using local and open-source tools only.

We will use your real sample documents from:

- `OCR-Text-Extraction/Delivery Notes`
- `OCR-Text-Extraction/Purchase Invoices`

## Main Goal

Build a small local OCR application while learning:

- how PDF text extraction works
- when OCR is needed
- how preprocessing improves OCR
- how to extract structured invoice and delivery note fields
- how to explain all of this in interviews

## The Small Application We Will Build

We will build a local document extraction app that:

1. reads PDFs from your two sample folders
2. checks whether text can be extracted directly
3. runs OCR when direct extraction is not enough
4. extracts useful fields from invoices and delivery notes
5. saves results in structured JSON

## Local and Open-Source Tools We Will Use

- `PyMuPDF` or `pdfplumber` for direct PDF text extraction
- `pdf2image` or Poppler for converting PDF pages into images
- `OpenCV` for preprocessing
- `Tesseract` with `pytesseract` for OCR
- optional later comparison with `EasyOCR` or `PaddleOCR`

## The 3-Step Plan

## Step 1: Understand the Documents and Extraction Basics

Focus:

- understand the difference between digital PDFs and scanned PDFs
- learn direct text extraction first
- inspect your invoices and delivery notes
- identify common fields such as invoice number, supplier, date, totals, item lines, and delivery note number

What you will learn:

- when OCR is not needed
- why PDF extraction can fail on layout-heavy documents
- how invoices and delivery notes differ

Output of Step 1:

- a document analysis note
- extracted raw text samples
- a field checklist for both document types

## Step 2: Build the Local OCR Pipeline App

Focus:

- convert PDF pages to images
- preprocess them using OpenCV
- run OCR using Tesseract
- compare OCR output before and after preprocessing
- route between direct extraction and OCR

What you will learn:

- OCR pipeline design
- preprocessing effects
- recognition errors and debugging
- choosing the right tool for the right input

Output of Step 2:

- a working local Python app
- extracted text output
- JSON output per document

## Step 3: Extract Structured Data and Prepare for Interviews

Focus:

- turn raw OCR text into useful fields
- use regex and parsing rules for invoices and delivery notes
- measure output quality
- prepare notes and interview answers

What you will learn:

- postprocessing and validation
- field extraction logic
- OCR system tradeoffs
- how to explain the architecture clearly in interviews

Output of Step 3:

- structured extraction results
- interview notes
- interview Q&A
- end-to-end understanding of the whole system

## Study Order

We will go one step at a time in this order:

1. document understanding and extraction basics
2. OCR pipeline implementation
3. structured extraction and interview preparation

## Current Recommendation

Start with Step 1 first.

Reason:

- it gives you the mental model
- it prevents unnecessary OCR
- it helps us design better extraction rules before writing code

## Folder Map

- `docs/STUDY-ARCHITECTURE.md`: overall study roadmap
- `docs/STEP-1-NOTES.md`: notes for understanding documents and extraction
- `docs/INTERVIEW-QA.md`: OCR interview questions and answers
- `app/README.md`: app architecture and implementation roadmap
- `output/`: extracted text and JSON results later

## What We Will Do Next

Next, we should begin Step 1:

1. inspect sample PDFs
2. determine digital vs scanned
3. extract text from a few examples
4. identify important fields to capture later
