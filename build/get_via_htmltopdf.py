import requests
from api import HtmlToPdfDotNet

FILENAME = "NguyenKiemHung_CV.pdf"
FILENAME_LOCAL = "CV_Local.pdf"
# response_tunnel = requests.get("http://localhost:4040/api/tunnels").json()
# url = response_tunnel["tunnels"][0]["public_url"] + "/docs/"
# print(f"\nURL Tunnel is: '{url}'.")
# # url = "https://www.html-to-pdf.net" # debug only
# print(f"\nConverting to PDF from: '{url}'.")
# pdf_content = HtmlToPdfDotNet().convert_pdf(url)
with open(FILENAME, "wb") as firstfile, open(FILENAME_LOCAL, "rb") as secondfile
    # read content from second file 
    for line in secondfile: 
        # write content to frst file 
        firstfile.write(line)
print(f"Downloaded PDF file: '{FILENAME}'.")
