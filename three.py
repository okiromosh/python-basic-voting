# Generate the list of nominee options with corresponding numbers
nominees = ["nom1", "nom2", "nom3"]

nominee_options = []

voters_id = [1, 2, 3, 4]
voters = voters_id.copy()  # Make a copy of voters_id list

num_of_voters = len(voters)

nominee_votes = {nominee: 0 for nominee in nominees}

for i, nominee in enumerate(nominees):
    nominee_option = f"{i + 1}. {nominee}"
    nominee_options.append(nominee_option)

nominee_options_text = "\n".join(nominee_options)

for _ in range(num_of_voters):
    voter = int(input("Enter your voter id: "))
    if voter in voters:
        print("You are a valid voter")
        voters.remove(voter)

        # Prompt the voter to choose a nominee using the generated options
        vote_prompt = "Please vote for a nominee by entering the corresponding number:\n" + nominee_options_text + "\n"
        vote = int(input(vote_prompt))

        if 1 <= vote <= len(nominees):
            nominee_votes[nominees[vote - 1]] += 1
            print("Thank you for voting")
        else:
            print("Invalid nominee number. Please try again.")
    else:
        print("You are not a voter or have already voted")

max_votes = max(nominee_votes.values())
winners = [nominee for nominee, votes in nominee_votes.items() if votes == max_votes]

if len(winners) == 1:
    winner_name = winners[0]
    percent = (max_votes / num_of_voters) * 100
    print(f"{winner_name} has won with {percent}% of votes")
else:
    print("It's a tie between the following nominees:")
    for winner in winners:
        percent = (nominee_votes[winner] / num_of_voters) * 100  # Use nominee_votes dictionary
        print(f"{winner} with {percent}% of votes")