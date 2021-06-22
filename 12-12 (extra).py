scores = {"Literature": 70, "Math": 60, "Foreign Language": 50}
subject = input("Input subject:")
if subject in scores:
    print(scores[subject])
else:
    print("No score is recorded")
