score = 0


def quiz():
    global score

    q1 = input("What was Shaquille O'Neal's jersey number while on the Los Angeles Lakers?")

    if q1 == "34":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    q2_correct = ["1", "one"]
    q2 = input("How many league MVP awards has Kobe Bryant won?")
    q2 = q2.lower()

    if q2 in q2_correct:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    q3_correct = ["0", "none", "zero"]
    q3 = input("How many Finals game 7's has Michael Jordan played in?")
    q3 = q3.lower()

    if q3 in q3_correct:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    q4_correct = ["stephen curry", "steph curry", "curry", "steph"]
    q4 = input("Who is widely regarded as the greatest shooter in league history?")
    q4 = q4.lower()

    if q4 in q4_correct:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    percentage = score/4
    print(f"{score}/4 or {percentage}")


quiz()
