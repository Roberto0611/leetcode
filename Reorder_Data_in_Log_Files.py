def reorderLogFiles(logs):
    digits = []
    letters = []

    # split
    for log in logs:
        id_,content = log.split(" ",1)
        # digit or alpha?
        if content[0].isalpha():
            letters.append(log)
        else:
            digits.append(log)
    # sort
    letters.sort(key=lambda x: (x.split(" ",1)[1], x.split(" ",1)[0]))

    return letters + digits

## call
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))