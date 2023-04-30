# -*- coding: utf-8 -*-
"""pdf2word.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WjDHRli7VLUI9n1VYKDckbeTBaQzWXN_
"""

pip install PyPDF2

pip install python_docx

import PyPDF2
from docx import Document
from PyPDF2 import PdfReader

with open('dummy.pdf', 'rb') as file:
  reader = PdfReader("dummy.pdf")
  number_of_pages = len(reader.pages)

  document = Document()

  for page in reader.pages:
      text = page.extract_text()

  document.add_paragraph(text)

  document.save('dummy1.docx')