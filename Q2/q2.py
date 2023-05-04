import csv

def main() : 
    largest_gap_day = ""
    largest_gap_val = 0
    smallest_gap_day = ""
    smallest_gap_val = 10000

    f = open("q2.csv","r",encoding="cp949")
    data = csv.reader(f,delimiter=',')
    header = next(data)
    for row in data:
        if row[3] == "" or row[4] == "" :
            continue
        row[2] = float(row[2])
        row[3] = float(row[3])
        row[4] = float(row[4])
        gap = row[4] - row[3]
        if largest_gap_val < gap :
            largest_gap_day = row[0]
            largest_gap_val = gap
        if smallest_gap_val > gap :
            smallest_gap_day = row[0]
            smallest_gap_val = gap

    f.close()

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperature Variation:", largest_gap_day)
    print("Maximum Temperature Difference: {0:.1f} Celsius".format(largest_gap_val))
    print("Day with the Smallest Temperature Variation:", smallest_gap_day)
    print("Minimum Temperature Difference: {0:.1f} Celsius".format(smallest_gap_val))

if __name__ == "__main__" :
    main()
