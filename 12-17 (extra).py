scores = {}
for n in range(5):
    new_name = input("Input name:")
    new_score = int(input("Input score:"))
    scores[new_name] = new_score 
print("Passed students are as follows")
for k, v in scores.items():
    if v>=70 and v<=100:
        print(k)
        
#these bonus assignments are way too hard what the fuck?
#there are probably alternative solutions but just finding this took way too long
#if anyone did find a different solution plz hmu
#also the two pages about keys() and values() before this exercise were absolutely useless why did they add them
