def CSVsum(filename):
    with open(filename, "r") as file:
        for line in file:
            if line.isnumeric == False:
                line.slice()
            elif line.isnumeric == True:
                collumns = line.split(",")
                val1 = collumns[1]
                val2 = collumns[2]
                val3 = collumns[3]
                val1 = float(val1)
                val2 = float(val2)
                val3 = float(val3)
                fval1 = sum(val1)
                fval2 = sum(val2)
                fval3 = sum(val3)
                res = [fval1, fval2, fval3]
                return res