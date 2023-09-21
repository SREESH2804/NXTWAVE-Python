def get_scores(ball_score_list):
  ball_score_dict = {}
  for item in ball_score_list:
    pair = item.split(":")
    key,value = pair[0], int(pair[1])
    if key in ball_score_dict:
        score = ball_score_dict[key]
        ball_score_dict[key] = score + value
    else:
      ball_score_dict[key] = value
  
  return ball_score_dict 
a = input().split(",")
b = get_scores(a)

e = b.items()
c =sorted(e)
print(c)

