# Day 12: Inheritance


class Student(Person):

    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        numScores = len(self.scores)
        total, avg = 0, 0
        grade = ''
        for i in range(numScores):
            total += self.scores[i]
        avg = int(total / numScores)
        if avg >= 90 and avg <= 100:
            grade = 'O'
        elif avg >= 80 and avg < 90:
            grade = 'E'
        elif avg >= 70 and avg < 80:
            grade = 'A'
        elif avg >= 55 and avg < 70:
            grade = 'P'
        elif avg >= 40 and avg < 55:
            grade = 'D'
        else:
            grade = 'T'
        return (grade)
