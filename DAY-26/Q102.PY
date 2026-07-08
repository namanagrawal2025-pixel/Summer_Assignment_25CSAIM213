def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote. Wait for " + str(18 - age) + " more years."

def main():
    user_age = int(input("Enter your age: "))
    result = check_voting_eligibility(user_age)
    print(result)

main()
