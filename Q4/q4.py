import csv

def main() :
    line_dict = {"1호선":[], "2호선":[], "3호선":[], "4호선":[]}

    f = open("q4.csv","r",encoding="UTF-8")
    data = csv.reader(f,delimiter=',')
    header = next(data)
    for row in data:
        if row[2] == "" or row[3] == "" or row[4] == "" or row[5] == "":
            continue
            
        row[4] = int(row[4])
        row[5] = int(row[5])

        if row[1] in line_dict.keys():
            line_dict[row[1]].append(row)

    f.close()

    print("*** Subway Report for Seoul on March 2023 ***")
    line_num = 0
    for key in line_dict.keys() :
        line_list = line_dict[key]
        print("Line",line_num+1,":")
        pass_num = 0

        max_station_name = ""
        max_station_val = 0
        for row in line_list :
            pass_num = row[4] + row[5]
            if ( pass_num > max_station_val ) :
                max_station_val = pass_num
                max_station_name = row[3]
        min_station_name = ""
        min_station_val = max_station_val
        for row in line_list :
            pass_num = row[4] + row[5]
            if ( pass_num < min_station_val ) :
                min_station_val = pass_num
                min_station_name = row[3]

        print("Busiest Station:", max_station_name, "({0:d})".format(max_station_val))
        print("Least used Station:", min_station_name, "({0:d})".format(min_station_val))
        line_num += 1

if __name__ == "__main__" :
    main()

