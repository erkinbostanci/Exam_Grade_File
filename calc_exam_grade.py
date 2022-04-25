def exam_grade(line):

    global grade
    line = line[:-1]

    listing = line.split(",")

    name = listing[0]

    grade1 = int(listing[1])

    grade2 = int(listing[2])

    grade3 = int(listing[3])

    calc_grade = grade1 * (3/10) + grade2 * (3/10) + grade3 * (4/10)

    if (calc_grade >= 90):
        grade = "AA"
    elif (calc_grade >= 85):
        grade = "BA"
    elif (calc_grade >= 80):
        grade = "BB"
    elif (calc_grade >= 75):
        grade = "CB"
    elif (calc_grade >= 70):
        grade = "CC"
    elif (calc_grade >= 65):
        grade = "DC"
    elif (calc_grade >= 60):
        grade = "DD"
    elif (calc_grade >= 55):
        grade = "FD"
    else:
        grade = "FF"

    return name + "------------------> " + grade + "\n"


with open("name_list.txt","r",encoding= "utf-8") as file:

    passed=[]
    dn_passed=[]
    for i in file:
        exam_grade(i)
        if (grade == "FF" or grade=="FD"):
            dn_passed.append(exam_grade(i))
        else:
            passed.append(exam_grade(i))
    with open("passed.txt","w",encoding="utf-8") as file2:
        for i in passed:
            file2.write(i)
    with open("dn_passed.txt","w",encoding="utf-8") as file3:
        for i in dn_passed:
            file3.write(i)
