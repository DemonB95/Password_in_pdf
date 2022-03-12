#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyPDF2 import PdfFileReader,PdfFileWriter


# In[2]:


file_pdf=PdfFileReader('End.pdf')
out_pdf=PdfFileWriter()


# In[3]:


file_pdf


# In[4]:


for i in range(file_pdf.numPages):
  page_details=file_pdf.getPage(i)
  out_pdf.addPage(page_details) 


# In[5]:


password="Anit@2022"
out_pdf.encrypt(password)


# In[6]:


with open("encryptedEnd.pdf","wb") as filename:
  out_pdf.write(filename)


# In[ ]:




