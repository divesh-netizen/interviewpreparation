# OCR Interview Questions and Answers

These are the interview-oriented notes for the OCR study project.

## 1. What is OCR?

OCR stands for Optical Character Recognition. It is the process of converting text visible inside images or scanned documents into machine-readable text.

## 2. What is the difference between text extraction and OCR?

Text extraction reads text that already exists in a file, such as a digital PDF. OCR is used when the text is only visible as pixels in an image or scanned PDF.

## 3. When should you avoid OCR?

You should avoid OCR when the PDF already contains embedded selectable text. Direct extraction is usually faster, more accurate, and easier to structure.

## 4. What are the main stages of an OCR pipeline?

The main stages are input classification, preprocessing, text detection, text recognition, postprocessing, field extraction, validation, and structured output generation.

## 5. Why is preprocessing important in OCR?

Preprocessing improves image quality before recognition. Operations like thresholding, denoising, resizing, and deskewing can significantly improve OCR accuracy.

## 6. What are common OCR errors?

Common errors include confusing similar characters such as `O` and `0`, bad reading order, missed table structure, low confidence on blurry scans, and errors from skewed or noisy pages.

## 7. How do you decide between direct extraction and OCR?

First check whether the PDF contains real text objects. If yes, try direct extraction first. If the document is scanned or extraction quality is poor, then use OCR.

## 8. Why are invoices and delivery notes harder than plain text documents?

They often contain tables, mixed layouts, line items, stamps, totals, and key-value regions. This makes both extraction and parsing more difficult than simple paragraphs.

## 9. What tools can be used in a local open-source OCR project?

You can use `PyMuPDF` or `pdfplumber` for direct extraction, `pdf2image` for conversion, `OpenCV` for preprocessing, and `Tesseract` with `pytesseract` for OCR.

## 10. What is Tesseract?

Tesseract is an open-source OCR engine widely used for printed text recognition. It is a strong learning tool and works well on clean document images, though it has limitations on complex layouts and poor-quality scans.

## 11. What is the role of OpenCV in an OCR system?

OpenCV is used for image preprocessing. It helps improve OCR inputs by handling grayscale conversion, thresholding, denoising, resizing, and basic layout cleanup.

## 12. How would you evaluate OCR quality?

You can evaluate OCR quality using character accuracy, word accuracy, field extraction accuracy, and manual comparison of outputs across sample documents.

## 13. What is postprocessing in OCR?

Postprocessing is the cleanup stage after recognition. It may include removing noise, fixing common OCR mistakes, validating dates or amounts, and extracting structured fields with rules or regex.

## 14. Why is JSON output useful in document extraction systems?

JSON is useful because it preserves structure. It makes it easier to store fields like invoice number, date, supplier, totals, and line items for downstream systems.

## 15. How would you design a small OCR app for invoices and delivery notes?

I would first classify the input document, try direct PDF extraction, fall back to OCR when needed, preprocess pages with OpenCV, run Tesseract, extract key fields using rules, validate important fields like dates and totals, and save the results as JSON.

## 16. What are the limitations of a basic OCR system?

A basic OCR system may struggle with handwriting, low-resolution scans, multi-column layouts, merged table cells, stamps, and inconsistent document templates.

## 17. Why is routing logic important in a document processing pipeline?

Routing logic prevents overusing OCR. It helps the system choose the best processing path, such as direct extraction for digital PDFs and OCR for scanned or image-heavy pages.

## 18. How would you improve a weak OCR result?

I would improve the image using preprocessing, test different OCR settings, crop noisy regions, validate the page orientation, and compare with a more modern OCR library if needed.

## 19. What is the difference between OCR and document understanding?

OCR focuses on recognizing text. Document understanding goes further by identifying layout, tables, form fields, relationships between text blocks, and semantic structure.

## 20. What did you learn from building a local OCR application?

I learned that direct extraction should be preferred whenever possible, preprocessing has a major impact on OCR quality, layout-heavy business documents need careful parsing, and a practical OCR system is really a pipeline of extraction, recognition, cleanup, validation, and structured output.
