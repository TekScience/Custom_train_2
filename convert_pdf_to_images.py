import os
from pdf2image import convert_from_path

pdf_dir = r"D:\Dreap_Requirements\testing\samples"
save_dir = r"D:\Dreap_Requirements\testing\output"
os.chdir(pdf_dir)

for pdf_file in os.listdir(pdf_dir):

    if pdf_file.endswith(".pdf"):

        pages = convert_from_path(pdf_file, 300, poppler_path=r'D:\Dreap_Requirements\poppler-0.68.0\bin')
        pdf_file = pdf_file[:-4]

        for page in pages:

           page.save(os.path.join(save_dir, "%s-page%d.jpg" % (pdf_file,pages.index(page)) ), "JPEG")
