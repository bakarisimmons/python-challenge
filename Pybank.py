import csv

budget_data_path = "Resources/budget_data.csv"

with open(budget_data, "r") as csvfile:

    csvreader = csv.reader(cvsfile, delimiter=",")

    first_row = next(csvreader)

    count = 1
    total= int(first_row[1])
    cur = int(first_row[1])
    cur_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    change_list = []
    increase_month = ""
    decrease_month = ""

    for row in csvreader:
        cur_change = int(row[1]) - cur
        change_list.append(cur_change)
        if cur_change > greatest_increase:
            greatest_increase = cur_change
            increase_month = row [0]

        if cur_change < greatest_decrease
            greatest_decrease = cur_change
            decrease_month = row [0]
        cur = int(row[1])
        count += 1
        total += int(row[1])

    output = (
        f"Financial Analysis\n"
        f"-----------------------------\n"
        f"Total Months: {count}\n"
        f"Average Change: ${sum(change_list) / len(change_list):.2f}\n"
        f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n"
    )

    print(output)

    with open(budget_data.csv, "w") as budget_data.csv:
        budget_data.csv.write(output)


