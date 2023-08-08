  # Exercise 1
def freeFall(val,isD):
    #Looks to see if isD is true if it is it take Val to be the distance and will carry out an equation to find the Time
    if isD == True:
        sum1=((2*val/9.81)**(1/2))
        # It returns the result of the sum to 2 decimal digits
        return (round(sum1, 2))
    #If isD is false then Val is Time and the equation to find the distance is then carried out
    if isD == False:
        sum2=((1/2)*9.81*(val**2))
        return (round(sum2, 2))
        

# Exercise 2
def RPS(s):
  text = s
  # Take the input and translate each letter. R to P, P to S, S to R. Then return the result
  return (text.translate(str.maketrans({"R": "P", "P": "S", "S": "R"})))


# Exercise 3
def list2str(l):
  ltos = "".join(map(str, l))
  newltos = "["+ltos+"]"
  return (newltos.translate(str.maketrans({"'": "", "," : "", " ": ""})))


# Exercise 4
def textPreprocessing(text):
  # takse text and removes the punctuation
  ptext = text.translate(str.maketrans({".":"","?":"",",":"",":":"",";":"","-":"","[":"","]":"","{":"","}":"","(":"",")":""}))
  # converts the text to lowercase
  ltext = ptext.lower()
  # the words are then stemmed before being converted into a list
  stext = ltext.translate(str.maketrans({"s":""}))
  stext2 = stext.replace("ing","").replace("ed","")
  lst = list(stext2.split(" "))
  # list of words to be removed
  stoptext = ["i","a","about","am","an","are","as","at","be","by","for","from","how","in","is","it","of","on","or","that","the","this","to","was","what","when","where","who","will","with","i"]
  # result looks at each element of list and if it appears in stoptext it is removed from result
  res = [x
    for x in lst
    if x not in stoptext
  ]
  # the result is then returned
  return res

# Exercise 5
def isGreaterThan(dict1,dict2):
  res = True
  if dict1.keys()!=dict2.keys():
    res = False
  if dict1.values()==dict2.values():
    res = False
    for i in dict2:
      if dict2["a"]<dict1["a"]:
        res = False
      if dict2["b"]<dict1["b"]:
        res = False
      else:
        res = True
  return res
  




# Exercise 6
def CSVsum(filename):
  with open(filename, "r") as file:
  # row = file.readline().split(",")
    val1 = 0
    val2 = 0
    val3 = 0
    for row in file:
      val1 += int(row[13])
      val2 += int(row[14])
      val3 += int(row[15])
    return [val1, val2, val3]
    
    #for line in file:
      #if line.isnumeric == False:
        #line.slice()
      #elif line.isnumeric == True:
        
        #return res


# Exercise 7
def str2list(s):
  stack = [[]]
  #itterates through every element in the string
  for i in s:
    #if the item in the string equals [ append the item to be an actual bracket
    if i == "[":
      stack[-1].append([])
      stack.append(stack[-1][-1])
    #if the item in the string equals ] append the item to be an actual bracket
    elif i == "]":
      stack.pop()
      #if a closing bracket without an opening bracket is detected give an error message
      if not stack:
        return "error: missing opening bracket"
    else:
      #if an opening bracket without an closing bracket is detected give an error message
      stack[-1].append(i)
  if len(stack) > 1:
    return "error: missing closing bracket"
  #return the converted list "[a[bc]]" returns ["a",["b","c"]] assert test keeps asking for "a" to be on its own for some reason
  return stack.pop()


  


# Exercise 8
#def spacemonSim(roster1,roster2):
 #   return None


# Exercise 9
#def rewardShortPath(env):
  #  return None


# Exercise 10
#def cliqueCounter(network):
 #   return None
