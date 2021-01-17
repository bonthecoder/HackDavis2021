from canvasapi import Canvas
from datetime import datetime, timezone
import copy

#-----------------------
# course.calendar["ics"]
#-----------------------

<<<<<<< HEAD
class Assignment:
  
  def __init__(self, name, date, courseID):
    self.name = name
    self.date = date
    self.courseID = courseID


=======
>>>>>>> d6453f58c9be73a3191c5c47b69708cf415c4067
# This function opens a file specified by the user (or the default file)
# It reads the contents of the file and stores them into a dictionary in the following order:
# URL
# API KEY
# (uhh is there anything else we could save time by reading from the file?)
# Returns the dictionary of file contents
def readDataFromFile():
  defaultFileName = "reminders_passwords.txt"
  print("\nDefault file is", defaultFileName)
  userFile = input("Press enter to read data from default file, or paste your own filename: ")
  if userFile != "":
    # the user entered a file, so we're temporarily changing the default filename
    defaultFileName = userFile
  try:
    f = open(defaultFileName)
  except:
    print("The file", defaultFileName, "failed to open...\nThe program will now terminate")
    kill
  file = f.readlines()
  data = {}
  data["URL"] = file[0].strip()
  data["KEY"] = file[1].strip()
  if len(file) >= 2:
    data["OTHER"] = file[2:]
  return data

# This function takes a dictionary of data (which includes a URL and a KEY)
# and makes a Canvas object. Then from the Canvas object, it finds a user.
# If the Canvas has multiple users (is this even possible?) then the current user
# chooses which is the correct user to use
# Returns the data dictionary, with the USER and CANVAS keys added
def getCanvasAndUser(data):
  try:
    canvas = Canvas(data["URL"], data["KEY"])
  except:
    print("\nA canvas with that data was not found...\nThe program will now terminate")
    kill
  
  #print("\nGot canvas:",canvas)
  data["CANVAS"] = canvas
  current = canvas.get_current_user()
  print("\nWelcome,", current.name)
  data["USER"] = current
  return data

# This function takes a dictionary of data (which includes URL, KEY, USER)
# and makes a list of all the current classes the user is enrolled in
# "Current" classes are chosen by checking the current data and comparing it with
# the dates of each Quarter (r.i.p. the semester system)
# Returns the dictionary with the COURSES key added
def getCurrentCourses(data):
  today = datetime.today()
  # now have access to:
  # date.year
  # date.month
  # date.day

  # Determine which quarter we're in

  # FQ: September through December
  FQ = datetime(today.year, 9, 1)
  # WQ: January through March
  WQ = datetime(today.year, 1, 1)
  # SQ: April through June
  SQ = datetime(today.year, 4, 1)
  # fuck summer session for now

  if today < SQ:
      curQuarter = "WQ"
  elif today < FQ:
      curQuarter = "SQ"
  else:
      curQuarter = "FQ"

  curYear = str(today.year)
  curCourses = []
  
  courses = data["USER"].get_courses(enrollment_state="active")
  
  print(data["USER"].name + "'s active courses:")
  for course in courses:
      if (curYear in course.course_code) and (curQuarter in course.course_code):
          # print(course.calendar["ics"])
          # this is what we had
          #curCourses.append(course.course_code)
          # but I think we should put in the course itself
          curCourses.append(course)
          print(course.name)

  data["COURSES"] = curCourses
  return data

# This function takes a dictionary of data (which includes COURSES)
# and makes a list of assignments for each course in COURSES
# Key is the course, and value is a list of Assignment objects
# Returns the dictionary of course : assignmenents
def getCurrentAssignments(data):
  # a dictionary where we link a class ID to its list of assignments
  # class1 : [assignment1, assignment2, etc]
  classAssignments = {}
  print("\nLoading assignments...",end='')
  for course in data["COURSES"]:
    print(".",end='')
    todo = course.get_assignments()
    assignments = []
    #print("--------------------------\nListing assignments for", course.name)
    for ass in todo:
      try:
        #print(ass.name, "is due at", utc_to_local(ass.due_at_date))
        # for now, just appending the the assignment to the list of assignments
        # WE SHOULD CONSIDER CHECKING THE DUE DATE OF THE ASSIGNMENT BEFORE ADDING IT THOUGH
        assignments.append(ass)
      except:
        # assignments with no due dates just won't get added
        pass

    # now make the dictionary entry
    classAssignments[course] = copy.deepcopy(assignments) # doing the copy because I'm nervous about how Python references work...
  #print("\nHere's the guts of an Assignment object:")
  #print( (data["COURSES"][0].get_assignments())[0].__dict__ )
  print()
  return classAssignments

# This fucntion converts a datetime object's timezone
# It came from the internet
def utc_to_local(utc_dt):
  return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

# This function takes the dictionary of active courses w/ their assignments
# It goes through each course and adds each assignment to a big list
# Returns a list of Assignment objects
def getAssignmentList(courseAssignments):
  now = datetime.now().astimezone(tz=None)
  assignmentList = []
  for course in courseAssignments.keys():
    for assignment in courseAssignments[course]:
      # aware >= naive
      try:
        if assignment.due_at_date >= now:
          assignmentList.append(assignment)
      except:
        # naughty assignments don't get added
        pass
  print("There are a total of", len(assignmentList), "assignments. Good luck.")
  return assignmentList

# This function is used by the sorting function
def getElementDueDate(elem):
  return elem.due_at_date

def getElementCourseID(elem):
  return elem.course_id

def getElementName(elem):
  return elem.name

# This function prints the assignments as pretty as possible :)
def printAssignments(assignments):
  maxlength = 0
  for assignment in assignments:
    if len(assignment.name) > maxlength:
      maxlength = len(assignment.name)
  for assignment in assignments:
    print(assignment.name,end='')
    ii = len(assignment.name)
    while ii < maxlength:
      print(" ",end='')
      ii += 1
    print(' ', assignment.due_at_date, " (class ID = ", assignment.course_id,")", sep='')
  return

def getSorted(assignments):
  choice = int(input("Make a selection:\nSorted by due date  (1)\nSorted by course id (2)\nSorted by name      (3)\nChoice: "))
  if choice == 1:
    assignments.sort(key=getElementDueDate)
    return assignments
  elif choice == 2:
    assignments.sort(key=getElementCourseID)
    return assignments
  elif choice == 3:
    assignments.sort(key=getElementName)
    return assignments
  else:
    print("Dumbass choice!")
    return assignments

# main
if __name__ == '__main__':
  
  data = readDataFromFile()
  data = getCanvasAndUser(data)
  data = getCurrentCourses(data)
  
  courseAssignments = getCurrentAssignments(data)
  
  # make a list of our Assignment objects
  assList = getAssignmentList( courseAssignments )
  
  # we can group them in colors based on assignment.assignment_group_id
  # or even better, color them based on course id
  
  printAssignments(getSorted(assList))
  
  

