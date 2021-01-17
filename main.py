from canvasapi import Canvas
import datetime

#-----------------------
# course.calendar["ics"]
#-----------------------


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
# Returns the data dictionary, with the
def getCanvasAndUser(data):
  try:
    canvas = Canvas(data["URL"], data["KEY"])
  except:
    print("\nA canvas with that data was not found...\nThe program will now terminate")
    kill
  
  print("\nGot canvas:",canvas)
  data["CANVAS"] = canvas
  current = canvas.get_current_user()
  print("Welcome,", current.name)
  data["USER"] = current
  return data

def getCurrentCourses(data):
  date = datetime.date.today()
  print("\nCurrent date: '", date, "'", sep='')
  # now have access to:
  # date.year
  # date.month
  # date.day

  # FQ, WQ, SQ, SS1, SS2
  
  # FQ: September through December
  # WQ: January through March
    # SQ:
  # Determine which quarter we're in
  curYear = str(date.year)
  curQuarter = "WQ"
  curCourses = []
  
  courses = data["USER"].get_courses(enrollment_state="active")
  
  for course in courses:
      if (curYear in course.course_code) and (curQuarter in course.course_code):
          # print(course.calendar["ics"])
          curCourses.append(course.course_code)
      # name, id, course_code

  print(data["USER"].name + "'s active courses:")
  print(curCourses)
  data["COURSES"] = curCourses
  return data

#API_URL = "https://canvas.ucdavis.edu/"
# need this to work with unique users, not just me
# Bwahaha now that I have your key I can turn in all your assignments for you  >:)
#API_KEY = "3438~S5MKJLaQYYFCVtVHFHQnxmSwi1hhoyMx7LfOl9Ih0ecClOUrQJTun5wZ0dzzFxqe"

#canvas = Canvas(API_URL, API_KEY)

#user = canvas.get_current_user()

#print("User: " + user.name)

#courses = user.get_courses(enrollment_state="active")

# Need a way to only get the courses for the current quarter
# Parse string for quarter and year?

if __name__ == '__main__':
  
  data = readDataFromFile()
  data = getCanvasAndUser(data)
  data = getCurrentCourses(data)



