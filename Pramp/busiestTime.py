from collections import defaultdict
def find_busiest_period(data):
  """
  0, 1 and 2 
  Timestamp, the count of visitors, and whether the visitors entered or exited the mall (0 for exit and 1 for entrance), respectively
  [ 1440084737, 4, 0 ]
  
  returns the time at which the mall reached its busiest 
  moment last year.
  1 -- entrance
  
  return the earliest one 
  data = [ [1487799425, 14, 1], --> 14
           [1487799425, 4,  0], --> 10
           [1487799425, 2,  0], --> 8
           [1487800378, 10, 1], --> 18
           [1487801478, 18, 0], --> 0  -->
           [1487801478, 18, 1], --> 18
           [1487901013, 1,  0], --> 17
           [1487901211, 7,  1], --> 17+7 --> 24
           [1487901211, 7,  0] ] --> 17
           1487800378
     {
     1487799425: 8, 1487800378: 10, 1487801478: 0, 1487901013: 1, 1487901211:0
     }
     for timestamp, num, flag in data:
        
  """
  myHash = defaultdict(int)
  for timeStamp, num, flag in data:
      if flag == 1:  myHash[timeStamp] += num
      else: myHash[timeStamp] -= num
  maxValue = 0
  for aKey, aValue in myHash.items(): maxValue = max(maxValue, aValue)
  myList = []
  for aKey, aValue in myHash.items():
    if aValue == maxValue: myList.append(aKey)
  return min(myList)
print(find_busiest_period(
    [ [1487799425, 14, 1], 
    [1487799425, 4,  0],
    [1487799425, 2,  0],
    [1487800378, 10, 1],
    [1487801478, 18, 0],
    [1487801478, 18, 1],
    [1487901013, 1,  0],
    [1487901211, 7,  1],
    [1487901211, 7,  0] ]
))