import MapReduce
import sys
import hashlib

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

    value = record[1]
    trimmed = value[:-10]
    key = hash(trimmed)

    mr.emit_intermediate(key, trimmed)

def reducer(key, list_of_values):
    mr.emit((list_of_values[0]))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
