# # get the timing of the different  student
# student_arrived_timings1 = [0, -1, 2, 1]
# # get the threshold value of the professor
# professor_threshold1 = 2
# get the timing of the different  student
student_arrived_timings = [-93 ,-86, 49, -62, -90, -63, 40, 72, 11, 67]
# get the threshold value of the professor
professor_threshold = 4

# Complete the angryProfessor function below.
def angryProfessor(professor_threshold, student_arrived_timings):
    student_attended = 0
    # check the timing of the student arrived with the professor threshold
    for i in range(0, len(student_arrived_timings)):
        # check the timing for which student actually attended the class
        if student_arrived_timings[i] <= 0:
            # count the number of student in are present in the class
            student_attended = student_attended + 1

    # check the professor expected threshold is equal to the student attend
    if student_attended >= professor_threshold:
        # professor cancel the class
        return "NO"
    else:
        # professor not canceling the class
        return "YES"


print(angryProfessor(professor_threshold, student_arrived_timings))
# print(angryProfessor(professor_threshold1, student_arrived_timings1))
