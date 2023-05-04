import csv

def main() :

    line_dict = {"1호선":[], "2호선":[], "3호선":[], "4호선":[], "5호선":[], "6호선":[], "7호선":[], "8호선":[], "9호선":[]}

    f = open("q3.csv","r",encoding="UTF-8")
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

    passanger_nums = [0 for i in range(0,len(line_dict))]

    line_num = 0
    for key in line_dict.keys() :
        line_list = line_dict[key]
        for row in line_list :
            passanger_nums[line_num] += row[4] + row[5]
        line_num += 1    

    maximum_line = ""
    maximum_line_num = max(passanger_nums)
    minimum_line = ""
    minimum_line_num = min(passanger_nums)

    second_max_line = ""
    second_max_line_num = 0
    second_min_line = ""
    second_min_line_num = maximum_line_num

    for i, n in enumerate(passanger_nums) :
        if n == maximum_line_num :
            maximum_line = str(i+1)+"호선"
            continue
        if n == minimum_line_num :
            minimum_line = str(i+1)+"호선"
            continue
        if second_max_line_num < n :
            second_max_line = str(i+1)+"호선"
            second_max_line_num = n
            continue
        if second_min_line_num > n :
            second_min_line = str(i+1)+"호선"
            second_min_line_num = n
            continue

    print("*** Subway Report for Seoul on March 2023 ***")
    print("1st Busiest Line :",maximum_line,"({0:d})".format(maximum_line_num))
    print("2nd Busiest Line :",second_max_line,"({0:d})".format(second_max_line_num))
    print("1st Least used Line :",minimum_line,"({0:d})".format(minimum_line_num))
    print("2nd Least used Line :",second_min_line,"({0:d})".format(second_min_line_num))

if __name__ == "__main__" :
    main()
