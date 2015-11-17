"""7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name."""

# Use the file name mbox-short.txt as the file name


fname = raw_input("Enter file name: ")
fh = open(fname)

count = 0
sumtotal = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num = line.split()
    count = count + 1
    sumtotal = sumtotal + float(num[1])

print "Average is " sumtotal / count
