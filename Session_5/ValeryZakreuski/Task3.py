# Implement a function which receives file path and returns names of top
# performer students.
import csv


# printing the best students(default = 5)
def get_top_performers(file_path, number=5):
    # opening file with students data
    with open(file_path, "r") as csv_students_file:
        # unpacking and putting it on the list
        students_data = list(csv.reader(csv_students_file, delimiter=","))
    # sorting it by the second index(average mark)
    students_data = sorted(students_data[1:], key=lambda x: float(x[2]), reverse=True)
    # returning list with the NUMBER elements(sorted previously)
    return list(students_data[:number][i][0] for i in range(number))


def export_csv(file_path):
    with open(file_path, "r") as csv_students_data:
        students_data = list(csv.reader(csv_students_data, delimiter=","))
        # opening file to write out
    with open("students_ordered_by_age.csv", "w", newline="") as file_out:
        data_writer = csv.writer(file_out)
        # writing header(name,age,av. mark)
        data_writer.writerow((students_data[0]))
        # sorting the list with students data. 1 index - age
        students_data = sorted(students_data[1:], key=lambda x: float(x[1]), reverse=True)
        for line in students_data:
            data_writer.writerow(line)

# print(get_top_performers("data/students.csv"))
# export_csv("data/students.csv")
