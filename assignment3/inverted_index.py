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
    document_id = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, document_id)

def reducer(key, list_of_values):
    # Removing the duplicates from the list
    # Actually the mapper should have not let duplicates go
    # but I could not find anyway I could stop it at the mapper itself
    mr.emit((key, list(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
