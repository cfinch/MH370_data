"""Parse text files and concatenate into CSV files"""
import os
import csv

def concatenate(firstPage, lastPage, dataPath, outFileName):
    """Concatenates multiple text files into a single CSV document,
    following Excel conventions.
    Arguments:
    firstPage
    lastPage
    dataPath
    outFileName
    """
    outFile = open(outFileName, "w")
    writer = csv.writer(outFile)
    writer.writerow(["Date", "Time", "Channel Name", "Ocean Region", "GES ID (octal)", "Channel Unit ID", "Channel Type", "SU Type", "Burst Frequency Offset (Hz) BFO", "Burst Timing Offset (microseconds) BTO"])

    for pageNumber in range(firstPage, lastPage + 1):
        inFileName = "text_p{:02d}.txt".format(pageNumber)
        print(inFileName)
        inFile = open(dataPath + os.sep + inFileName, "r")

        for line in inFile.readlines():
            string = line.strip()
            if len(string) > 0:
                words = string.split()

                # Fix OCR errors
                # Replace , with . in time field
                words[1] = words[1].replace(",", ".")

                # Replace | and l with I in Channel Name field
                words[2] = words[2].replace("l", "I")
                words[2] = words[2].replace("|", "I")

                words[5] = words[5].replace("ll", "11")

                # Create list for writing to CSV file
                data = ["" for i in range(10)]
                data[:6] = words[:6]
                data[6] = " ".join((words[6].strip(), words[7].strip()))
                if words[-1].isdigit() and words[-2].isdigit():
                    data[9] = words[-1]
                    data[8] = words[-2]
                    sutype = " ".join(words[8:-2])
                elif words[-1].isdigit():
                    data[8] = words[-1]
                    sutype = " ".join(words[8:-1])
                else:
                    sutype = " ".join(words[8:])
                data[7] = sutype
                print(data)
                writer.writerow(data)

        inFile.close()

    outFile.close()


# Setup
dataPath = "Pages"

# Pre-flight data: pages 3-19
concatenate(3, 19, dataPath, "preflight.csv")

# In-flight data: pages 20-41
concatenate(20, 41, dataPath, "inflight.csv")

# Appendix 1, pages 42-45
concatenate(42, 45, dataPath, "appendix1.csv")

# Appendix 2, pages 46-47
concatenate(46, 47, dataPath, "appendix2.csv")

