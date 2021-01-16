
from canvasapi import Canvas
import urllib.request
import pandas as pd
import pprint


# big ideas:

# User inputs the url
# User inputs their api_key
# User inputs (or chooses) the user
# User inputs (or chooses) the course id
# User inputs (or chooses) the quiz id
# All user submissions get downloaded
# more stuff happens


# potentially useful API functions:
# course .get_quizzes() returns a list of quizzes
# course .get_recent_students() returns a list of students in order
                            # of how recently they've logged on
# course .get_user(userID) returns the User
# course .get_users() returns all users!
# quiz .get_submissions() returns all submissions
# quiz .get_statistics() returns all statistics (rebeca said this was good?)
# quizSubmission .get_submission_questions() returns quizSubmissionQuestion's
# quizSubmission .update_score_and_comments() somehow send the "fudge points"??


class Student:

    # this is the initializer for classes
    # all class methods have the first argument as "self"
    # it's sort of like the "this" word in C++, except not a pointer
    def __init__(self, ID, NAME):
        # empty dictionary of student interactions
        # each student that "self" interacts with will be put in the dictionary
        # student_id : time_interacted
        self.interactions = {}
        self.id = ID
        self.name = NAME

    # for adding an interaction with a single other student
    def addInteraction(self, ID, TIME):
        if ID in self.interactions:
            self.interactions[ID] += TIME
        else:
            self.interactions[ID] = TIME

    # for adding an interaction with 2+ students (like in a group)
    def addInteractions(self, IDs, TIMEs):
        if len(IDs) != len(TIMEs):
            print("Problem in the addInteractions method!\nExiting without changing interaction times")
        for ii in range(len(IDs)):
            if IDs[ii] in self.interactions:
                self.interactions[IDs[ii]] += TIMEs[ii]
            else:
                self.interactions[IDs[ii]] = TIMEs[ii]



def getAPIURL():
    default = "https://canvas.ucdavis.edu"
    print("\nDefault URL is '",default,"'",sep='')
    url = input("Paste custom url, or press enter to use default: ")
    if url == "":
        return default
    return url


def getAPIKEY():
    default = "password.txt"
    print("\nDefault file is '",default,"'",sep='')
    key = input("Paste custom key, or press enter to read from file: ")
    if key == "":
        try:
            f = open(default,'r')
        except:
            print(default,"does not exist...")
            print("Let's try this again...")
            return getAPIKEY()
        else:
            data = f.readlines()
            f.close()
            if len(data) == 1:
                return data[0].strip()
            elif len(data) > 1:
                print("Multiple lines were found in",default)
                line = int(input("Which line is the API key? "))
                return data[line].strip()
            else:
                print(default,"was empty...")
                print("Let's try this again...")
                return getAPIKEY()
    return key

            
def getCanvas(url, key):
    print("\nGetting a canvas from '",url,"' with key '",key,"'",sep='')
    try:
        canvas = Canvas(url, key)
    except:
        print("A canvas with those specifications was not found. Good luck")
    else:
        return canvas


def getUser(canvas):
    current = canvas.get_current_user()
    print("\nThe current user is '",current,"'",sep='')
    user = input("Press enter to continue, or paste a different user ID: ")
    if user == "":
        return current
    try:
        current = canvas.get_user(int(user))
    except:
        print("User",int(user),"doesn't seem to exist on that canvas...")
        print("Let's try this again...")
        return getUser(canvas)
    else:
        return current
    
    # get list of users
    print(canvas.get_current_user())

def getCourse(canvas):
    num = input("\nPaste the course ID, or press enter to see the course list: ")
    if num != "":
        # user entered a course number. We need to check if it's legit
        try:
            course = canvas.get_course(int(num))
        except:
            # it wasn't legit :(
            print("Course",int(num),"doesn't seem to exist on that canvas...")
            print("Let's try this again...")
            return getCourse(canvas)
        else:
            # it was legit :)
            return course
    else:
        # user didn't enter a number. Display course list and have them choose
        courses = canvas.get_courses()
        for c in courses:
            try:
                print(c.name,", ",c.id,sep='')
            except:
                # sometimes the course is a dud and we just have to go with it
                pass
        num = input("Paste the course ID from the list: ")
        # user entered a course number. We need to check if it's legit
        try:
            course = canvas.get_course(int(num))
        except:
            # it wasn't legit :(
            print("Course",int(num),"doesn't seem to exist on that canvas...")
            print("Let's try this again...")
            return getCourse(canvas)
        else:
            # it was legit :)
            return course

def getQuiz(course):
    num = input("\nPaste the quiz ID, or press enter to see the quiz list: ")
    if num != "":
        # user entered a quiz number. We need to check if it's legit
        try:
            quiz = course.get_quiz(int(num))
        except:
            # it wasn't legit :(
            print("Quiz",int(num),"doesn't seem to exist in that course...")
            print("Let's try this again...")
            return getQuiz(course)
        else:
            # it was legit :)
            return quiz
    else:
        # user didn't enter a number. Display quiz list and have them choose
        quizzes = course.get_quizzes()
        for q in quizzes:
            try:
                print(q.title,", ",q.id,sep='')
            except:
                # just in case some quizzes are duds? We don't want to crash
                pass
        num = input("Paste the quiz ID from the list: ")
        # user entered a quiz number. We need to check if it's legit
        try:
            quiz = course.get_quiz(int(num))
        except:
            # it wasn't legit :(
            print("Quiz",int(num),"doesn't seem to exist in that course...")
            print("Let's try this again...")
            return getQuiz(course)
        else:
            # it was legit :)
            return quiz

def getAssignment(course):
    num = input("\nPaste the assignment ID, or press enter to see the quiz list: ")
    if num != "":
        # user entered an assignment number. We need to check if it's legit
        try:
            ass = course.get_assignment(int(num))
        except:
            # it wasn't legit :(
            print("Assignment",int(num),"doesn't seem to exist in that course...")
            print("Let's try this again...")
            return getAssignment(course)
        else:
            # it was legit :)
            return ass
    else:
        # user didn't enter a number. Display assignment list and have them choose
        asses = course.get_assignments()
        print(asses[0].__dict__)
        for a in asses:
            try:
                print(a)
            except:
                # just in case some assignments are duds? We don't want to crash
                pass
        num = input("Paste the assignment ID from the list: ")
        # user entered an assignment number. We need to check if it's legit
        try:
            ass = course.get_assignment(int(num))
        except:
            # it wasn't legit :(
            print("Assignment",int(num),"doesn't seem to exist in that course...")
            print("Let's try this again...")
            return getAssignment(course)
        else:
            # it was legit :)
            return ass

def getSubmissions(quiz):
    subs = quiz.create_report("student_analysis")
    print()
    print(subs.__dict__)
    print()
    url = subs.url
    data = pandas.read_csv(url)


def getQuizSubmissions(quiz):
    stats = list(quiz.get_statistics())[0]  # there should always be a single element in this list
    #print("Stats:",stats)
    #print()
    #print(stats.__dict__)
    #print()
    for question_stats in stats.question_statistics:
            # last answer means don't give points so don't look at it
            #for answer in question_stats['answers'][:-1]:
        print("------------------------------------------")
        print("Question stats:",question_stats)
        for answer in question_stats["answers"]:
            print()
            print("Answer:",answer)
    return
    print("Statistics:")
    stats = quiz.get_statistics()
    print(stats[0])
    print()
    print(stats[0].__dict__)
    print()

    reports = quiz.get_all_quiz_reports(report_type="student_analysis")
    for r in reports:
        print(r.__dict__)
        print()
        
    print("Submissions:")
    qs = quiz.get_submissions()
    print(qs[0])
    print()
    print(qs[0].__dict__)
    print()
    
    print("Submission Questions:")
    sq = qs[0].get_submission_questions()
    print(sq)
    print()
    print(sq.__dict__)
    

##############################
######## Main Function #######
##############################

if __name__ == "__main__":
    
    # get user input for the url
    url = getAPIURL()
    print("Got url: '",url,"'",sep='')

    # get user input for the api key
    key = getAPIKEY()
    print("Got key: '",key,"'",sep='')

    # now we have enough information to make our canvas object
    canvas = getCanvas(url, key)
    print("Got canvas: '",canvas,"'",sep='')

    # OHH OKAY IT LOOKS LIKE THIS ONE MIGHT NOT EVEN BE NEEDED! WHOOPS
    # get user input for the canvas's user
    user = getUser(canvas)
    print("Got user: '",user,"'",sep='')
    
    # get user input for the course
    course = getCourse(canvas)
    print("Got course: '",course,"'",sep='')

    # get user input the for the quiz
    quiz = getQuiz(course)
    print("Got quiz: '",quiz,"'",sep='')

    # get user input for the assignment
    #assignment = getAssignment(course)
    #print("Got assignment: '",assignment,"'",sep='')

    #getQuizSubmissions(quiz)
    #getSubmissions(quiz)

    #quiz = canvasClass.get_quiz(QUIZ_ID)
    studentReport = quiz.create_report("student_analysis")
    print(studentReport.__dict__)
    url = studentReport.file["url"]
    studentData = pd.read_csv(url)
    for key in studentData.keys():
        print("-------------------------")
        print("Key:",key, sep='\n')
        print("-----------")
        print("Value:",studentData[key],sep='\n')
    f = open("output.txt","w")
    f.writelines(studentData)
    f.close()
    print("Just out of curiousity, what's studentData[1]?")
    print(studentData.iat[0,8])
    print("Just out of curiousity, what's studentData[8]?")
    print(studentData.iat[1,9])


    

    
    
    
    
