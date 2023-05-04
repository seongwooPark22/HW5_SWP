import csv

def main() : 
    avg_cel = 0
    avg_min_cel = 0
    avg_max_cel = 0

    valid_day_num = 0

    f = open("q1.csv","r",encoding="cp949")
    data = csv.reader(f,delimiter=',')
    header = next(data)
    for row in data:
        if row[2] == "" or row[3] == "" or row[4] == "" :
            continue
        valid_day_num += 1;

        row[2] = float(row[2])
        row[3] = float(row[3])
        row[4] = float(row[4])

        avg_cel += row[2]
        avg_min_cel += row[3]
        avg_max_cel += row[4]

    avg_cel /= valid_day_num;
    avg_min_cel /= valid_day_num;
    avg_max_cel /= valid_day_num;

    f.close()

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: {0:.2f} Celsius".format(avg_cel))
    print("Average Minimum Temperature: {0:.2f} Celsius".format(avg_min_cel))
    print("Average Maximum Temperature: {0:.2f} Celsius".format(avg_max_cel))

if __name__ == "__main__" :
    main()

