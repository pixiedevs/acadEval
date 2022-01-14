def predictMark(marks: list) -> float:
    if len(marks) == 1:
        return marks[0]

    elif len(marks) < 1:
        return 0

    increment = []
    incSum = 0

    for i in range(len(marks)-1):
        increment.append(marks[i+1] - marks[i])

    for inc in increment:
        incSum += inc

    incAvg = incSum / len(increment)

    prediction = round(marks[-1] + incAvg, 2)
    sortedMarks = sorted(marks)

    if prediction >= 10 or prediction < sortedMarks[-1]:
        prediction = (sortedMarks[-1] + sortedMarks[-2]) / 2

    return prediction
