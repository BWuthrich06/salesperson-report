"""Generate sales report showing total melons each salesperson sold."""


# salespeople = []            
# melons_sold = []

# f = open('sales-report.txt')            #Opens up the sales report file

# for line in f:                          #Iterates through each line in file
#     line = line.rstrip()                #Stripping white space off right side of each line
#     entries = line.split('|')           #Spliting each line at the "|" into a list
#     salesperson = entries[0]            #assigning index 0 of entries to salesperson
#     melons = int(entries[2])            #assiging index 2 of entries as number of melons

#     if salesperson in salespeople:                      #checking to see if salesperson is in the salespeople list
#         position = salespeople.index(salesperson)       #if in list, find position of salesperson as index in salespeople list
#         melons_sold[position] += melons                 #Increment the melon count in the melon_sold at position index of salesperson
        
#     else:                                               #salesperson not in list
#         salespeople.append(salesperson)                 #adding salesperson to salespeople list
#         melons_sold.append(melons)                      #adding number of melons sold to melon_sold list


# for i in range(len(salespeople)):                                       #interate through the length of salespeople list
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')             #print out statement of each salesperson and how many melons each person sold



def get_melons_sold(filename):

    melons_sold = {}

    file = open(filename)

    for line in file:
        line = line.rstrip().split("|")

        name = line[0]
        count = line[2]
        count = int(count)
        

        if name not in melons_sold:
            melons_sold[name] = count

        else:
            melons_sold[name] += count

    return melons_sold



def get_sales_report(melons_sold):

    for person, count in melons_sold.items():
        print(f"{person} sold {count} melons")

    
print(get_sales_report(get_melons_sold("sales-report.txt")))  #function calling sales report as input calling get melons sold function with input as text file to read.

    
