def bmi_calculate(line):

    line = line[:-1]

    list = line.split(",")

    name = list[0]

    data1 = int(list[1])

    data2 = int(list[2])

    bmi =round( data1/((data2/100)**2),2)
    if (bmi < 18.5):
        bodytype ="Underweight"
    elif (18.5 <= bmi < 25):
        bodytype="Normal Weight"
    elif (25 <= bmi < 30):
        bodytype="Overweight"
    elif (30 <= bmi):
        bodytype="Obesity"
    else:
        bodytype= "Dead"

    return name + "  => BMI: " + str(bmi) +"  ----->  " + bodytype + "\n"


with open("input.txt","r",encoding= "utf-8") as file:

    type_list = []

    for i in file:

        type_list.append(bmi_calculate(i))

    with open("output.txt","w",encoding="utf-8") as file2:

        for i in type_list:
            file2.write(i)

"""HASAN KAAN KAHRAMAN """
