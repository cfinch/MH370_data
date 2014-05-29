Data for Flight MH370

Aircraft Location Data
----------------------
To my knowledge, precise aircraft location data has not been released. If this
data is available, please add it!

Satellite Data
--------------
This data was extracted from the PDF file provided by the government of
Malaysia to the public at the URL shown in Reference 1. The process used to
extract the data is described below.

KNOWN ERRORS
The OCR software (tesseract) had some problems recognizing periods and colons
in the time stamps for the in-flight data. For some reason, the pre-flight data
and the Appendices did not have this issue.

I have not attempted to correct any errors in the PDF. The PDF contains
at least one error. On page 41, the date flips from 7/03/2014 to 8/03/2014 at
midnight. The author probably intended for the date to flip to 7/04/2014.

NOTES
I split the first column (Time) into separate columns for Date and Time

EXTRACTION PROCESS
Convert a multi-page PDF to a series of images:
gs -r300 -sDEVICE=pngmono -dTextAlphaBits=4 -o Pages/mh370_p%02d.png mh370.pdf 

To crop out headers and page numbers, first find the bounding box [2]:
gs -q -dBATCH -dNOPAUSE -sDEVICE=bbox -dLastPage=1 mh370.pdf 2>&1 | grep %%BoundingBox

Result in points (72p = 1 inch): %%BoundingBox: 42 51 768 544
lower left corner: (42, 51) upper right corner: (768, 544)
Need to multiply size by 720/72 because of 720dpi output

Produce a test PNG by cropping table header and page number:
gs -dNOPAUSE -dBATCH -sDEVICE=pnggray -r720 -dFirstPage=4 -dLastPage=4 -sOutputFile=test.png -g7690x3940 -c "<</Install {0 -75 translate}>> setpagedevice" -f mh370.pdf

gs -dNOPAUSE -dBATCH -sDEVICE=pnggray -r720 -dFirstPage=21 -dLastPage=21 -sOutputFile=test.png -g7690x4100 -c "<</Install {0 -75 translate}>> setpagedevice" -f mh370.pdf

Cropping for pages 4-20:
gs -dNOPAUSE -dBATCH -sDEVICE=pngmono -r720 -sOutputFile=Pages/mh370_p%02d.png -g7690x3940 -dFirstPage=1 -dLastPage=20 -c "<</Install {0 -75 translate}>> setpagedevice" -f mh370.pdf

Cropping for pages 21-41:
gs -dNOPAUSE -dBATCH -sDEVICE=pngmono -r720 -sOutputFile=Pages/mh370_p%02d.png -g7690x4100 -c "<</Install {0 -75 translate}>> setpagedevice" -f mh370.pdf

OCR to convert image to text:
tesseract mh370_p04.png text_p04 -psm 6 

REFERENCES
[1] http://www.dca.gov.my/mainpage/MH370%20Data%20Communication%20Logs.pdf
[2] http://stackoverflow.com/questions/12484353/how-to-crop-a-section-of-a-pdf-file-to-png-using-ghostscript
[3] https://code.google.com/p/tesseract-ocr/
