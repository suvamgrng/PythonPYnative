#    Dictionary Filter: Extract pairs where value exceeds a threshold.
scores = {"Alice": 85,
          "Bob": 70,
          "Charlie": 95,
          "David": 60}
passing_student = {}
for name, score in scores.items():
    if score >= 75:
        passing_student[name] = score
print(passing_student)