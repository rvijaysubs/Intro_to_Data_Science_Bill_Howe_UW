import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    friendA = record[0]
    friendB = record[1]

    # Adding both 
    key = friendA + ":" + friendB
    mr.emit_intermediate(key, 1)
    key = friendB + ":" + friendA
    mr.emit_intermediate(key, -1)

def reducer(key, list_of_values):

    sum = 0
    for i in list_of_values:
        sum += i
    if sum != 0:
        values = key.split(":")
        mr.emit((values[0], values[1]))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
