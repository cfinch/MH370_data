import subprocess
import os

# The following pages require manual cleanup after OCR:
# Pages 3 and 20: section titles
# Pages 36-41: comments in tables
# Pages 42 and 45: Appendix headers

for pageNumber in range(3, 48):
    inFileName = "Pages/mh370_p{:02d}.png".format(pageNumber)
    print(inFileName)
    outFileName = "Pages/text_p{:02d}".format(pageNumber)
    print(outFileName)
    subprocess.call(["tesseract", inFileName, outFileName, "-psm", "6"])
