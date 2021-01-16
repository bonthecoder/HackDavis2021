from canvasapi import Canvas 

API_URL = "https://canvas.ucdavis.edu/"
# need this to work with unique users, not just me
API_KEY = "3438~S5MKJLaQYYFCVtVHFHQnxmSwi1hhoyMx7LfOl9Ih0ecClOUrQJTun5wZ0dzzFxqe"

canvas = Canvas(API_URL, API_KEY)

user = canvas.get_current_user()

print("User: " + user.name)

courses = user.get_courses(enrollment_state="active")

# Need a way to only get the courses for the current quarter 
# Parse string for quarter and year?
print(user.name + "'s active courses:")
for course in courses:
    if course.name != None:
        print(course.name)