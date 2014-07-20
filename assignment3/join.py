import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts

    for item in list_of_values:
        if item[0] == "order":
            for item1 in list_of_values:
                joined_tuple = []
                if item1[0] == "line_item":
                    for x in item:
                        joined_tuple.append(x)
                    for x in item1:
                        joined_tuple.append(x)
                    mr.emit(joined_tuple)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
