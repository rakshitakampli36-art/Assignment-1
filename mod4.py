def performance_evaluation():
    print("performance_evaluation")
    total = 0

    for i in range(1, 4):
        rating = int(input(f"Enter Rating {i} (1-5): "))
        total += rating

    average = total / 3

    if average >= 4:
        result = "Excellent"
    elif average >= 3:
        result = "Good"
    else:
        result = "Needs Improvement"

    print("Average Rating:", average)
    print("Performance:", result)
performance_evaluation()
