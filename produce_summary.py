# This program opens log files for each day, and prints the count, type of melon
# and total amount sold in $
#
# It could definitely be broken into functions


print "Day 1"
the_file = open("um-deliveries-20140519.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print "Delivered {} {}s for total of ${}".format(
        count, melon, amount)
the_file.close()


print "Day 2"
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print "Delivered {} {}s for total of ${}".format(
        count, melon, amount)
the_file.close()


print "Day 3"
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print "Delivered {} {}s for total of ${}".format(
        count, melon, amount)
the_file.close()
