import random
num=int(input("Enter number of candidates: "))
cand=input(f'Enter {num} candidates now:\n').split()
print("Candidates are: ",cand)
print("Voting is live....please wait for the results...")
print("Voting has been finished.... and wait is over")
print("Here are the results")
votes=[]
for x in range(0,num):
    c=random.randrange(1,100,3)
    votes.append(c)
for i in range(num):
    print(cand[i],':',votes[i])
print("Hence the winner is...")
maximum=max(votes)
count=0
for r in range(num):
    if votes[r]==maximum:
        count=r
print(cand[count],':',maximum)
