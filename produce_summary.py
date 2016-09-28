# This program takes a list of log files and uses the function
# delivery_report to print the number of melons delivery, the type of melon
# delivered, and the total amount of money ($) made from the delivery.

def delivery_report(files):
    """print delivery report of cost, amount sold, type"""
    # Iterate through files
    for file in files:
        the_file = open(file)
        # Iterate through lines in file, breaking lines by '|' into list of
        # strings
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')
            print "Delivered {} {}s for total of ${}".format(words[1], words[0],
                                                             words[2])
        the_file.close()
# List files to be used and call function deliery_report
files = ["um-deliveries-20140519.txt", "um-deliveries-20140520.txt", 
         "um-deliveries-20140521.txt"]
delivery_report(files)