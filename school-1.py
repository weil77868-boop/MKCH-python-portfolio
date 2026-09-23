scores = [78,92,-65,88,73,95,81,69,84,90,43,54,67,51,90,91,45,11,27,99]


highest = max(scores)
lowest = min(scores)
average = sum(scores)/len(scores)
top3 = sorted(scores, reverse = True)[:3]
print("===成績分析===")
print(f"最高:{highest}\n最低:{lowest}\n平均:{average}\n前三名:{top3}")


passed = {
    score for score in scores
    if score >= 60
}
print(f"及格人數:{len(passed)}")

higher_than_avg = {
    h_score for h_score in scores
    if h_score > average
}
print(f"高於平均分人數:{len(higher_than_avg)}")