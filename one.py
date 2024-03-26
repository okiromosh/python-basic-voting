nominee_1 = input("Enter Nominee 1: ")
nominee_2 = input("Enter Nominee 2: ")

nominee_1_votes = 0
nominee_2_votes = 0

voters_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_of_voters = len(voters_id)

while True:
    if voters_id == []:
        print("Voting Session Is Over")

        if nominee_1_votes > nominee_2_votes:
            percent = (nominee_1_votes/num_of_voters)*100
            print(f"{nominee_1} has won with {percent}% of votes")
            break

        elif nominee_2_votes > nominee_1_votes:
            percent = (nominee_2_votes/num_of_voters)*100
            print(f"{nominee_2} has won with {percent}% of votes")
            break

    else:
        voter = int(input("Enter your voter id: "))
        if voter in voters_id:
            print("You are a valid voter")
            voters_id.remove(voter)
            vote = int(input(f"Please vote 1({nominee_1}) or 2({nominee_2}): "))
            if vote == 1:
                nominee_1_votes += 1
                print("Thank you for voting")

            elif vote == 2:
                nominee_2_votes += 1
                print("Thank you for voting")

        else:
            print("You are not a voter or have already voted")



