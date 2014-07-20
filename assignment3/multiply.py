import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix_name = record[0]
    row = record[1]
    column = record[2]
    value = record[3]

##    rdict_key = matrix_name + str(row) + str(column)
##    rdict = {}
##    rdict[rdict_key] = value

    if matrix_name == "a":
        for i in range(5):
            key = str(row) + str(i)
            mr.emit_intermediate(key, record)
    elif matrix_name == "b":
        for i in range(5):
            key = str(i) + str(column)
            mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    rcolumn = int(key[1:])
    rrow = int(key[:1])
##    print key + "====" + str(rrow) + "====" + str(rcolumn)

    value = 0
    for item in list_of_values:
            if item[0] == "a":
                arow = item[1]
                acolumn = item[2]
                avalue = item[3]
##                print "a" + str(arow) + "," + str(acolumn) + "," + str(avalue)
                for item1 in list_of_values:
                    if item1[0] == "b":
                        brow = item1[1]
                        bcolumn = item1[2]
                        bvalue = item1[3]
##                        print "b" + str(brow) + "," + str(bcolumn) + "," + str(bvalue)
                        if brow == acolumn and bcolumn == rcolumn:
                            value += (avalue * bvalue)
                            break
        
    if value > 0:
        mr.emit((rrow, rcolumn, value))
##    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
