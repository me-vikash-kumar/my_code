# scores = [0, 1, 2, 3, 4, 5, 6]
# New_scores = [["neither even nor odd", ["odd", "Even"][i%2==0]][i==0] for i in scores]
# print(New_scores)

scores = [0, 1, 2, 3, 4, 5, 6]
New_scores = [["neither even nor odd", ["odd", "Even"][i%2==0]][i!=0] for i in scores]
print(New_scores)