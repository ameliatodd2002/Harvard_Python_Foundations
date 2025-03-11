def count_enrollments(course_dict):
    course_totals = {}
    for course_list in course_dict.values():
        for course in course_list:
            if not (course in course_totals):
                course_totals[course] = 1
            else:
                course_totals[course] += 1
    return course_totals


def main():
    enrollments = {'Rogers, Steve': ['CS1', 'MATH23', 'STAT100],
                'Lang, Scott': ['BIO101', 'CS1', 'MATH23', 'HIST50']}
    count_enrollments(enrollments)

main()