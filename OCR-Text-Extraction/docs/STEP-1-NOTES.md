# Step 1 Notes: Documents and Extraction Basics

This note file is for understanding your documents before building OCR.

## What We Are Studying First

We are learning how to answer these questions:

1. Is this PDF digital or scanned?
2. Can text be extracted directly?
3. If direct extraction works, is OCR still needed?
4. What fields matter in delivery notes and purchase invoices?

## Delivery Notes Usually Contain

- delivery note number
- supplier name
- customer name
- date
- item descriptions
- quantities
- references
- signatures or stamps

## Purchase Invoices Usually Contain

- invoice number
- supplier name
- buyer name
- invoice date
- due date
- tax or VAT details
- line items
- subtotal
- total amount

## Important Concepts

### Digital PDF

A digital PDF usually contains actual text objects.

That means:

- you can often select text
- direct extraction is faster and cleaner than OCR
- OCR may reduce quality if used unnecessarily

### Scanned PDF

A scanned PDF is usually just page images inside a PDF container.

That means:

- text is not stored as characters
- OCR is needed
- preprocessing may improve quality a lot

### Why Layout Matters

Invoices and delivery notes are not simple paragraphs.

They often have:

- headers
- tables
- key-value fields
- multiple columns
- stamps and handwritten marks

This is why extraction can become messy even when text exists.

## What We Need to Learn in Step 1

- how to inspect a PDF
- how to test direct extraction
- how to decide whether OCR is needed
- how to list the fields we actually want from each document type

## Step 1 Deliverables

- 3-5 sample files reviewed
- direct extraction tested
- a list of fields for delivery notes
- a list of fields for invoices
- notes about common problems

## Quick Field Checklist

### Delivery Note Fields

- document type
- note number
- date
- supplier
- customer
- line items
- quantities

### Purchase Invoice Fields

- document type
- invoice number
- invoice date
- supplier
- buyer
- tax amount
- subtotal
- total
- currency

## Questions to Keep in Mind

- Is the reading order correct?
- Are tables preserved or flattened?
- Are dates and totals easy to identify?
- Do file types behave consistently across both folders?
