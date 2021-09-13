textList = ["This is Delhi \n","This is Paris \n","This is London \n"]

outF = open("myOutFile.txt", "w")
for line in textList:
  # write line to output file
  outF.write(line)
outF.close()
