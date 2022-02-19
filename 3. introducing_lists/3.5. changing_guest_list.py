# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.

dinner = ['john', 'linda', 'peter']

print(f"It's seems that {dinner[0].title()} has contretemps. So he doesn't come.")

dinner[0] = 'jose'

print(f"Therefore, I will invite my friend {dinner[0].title()}.")
print(dinner)
print()
print(f"{dinner[0].title()}, I'd love to dinner with you today. Are you available?")
print(f"{dinner[1].title()}, I will cook that cuban chicken for us to dinner!")
print(f"Could you confirm my invitation for dinner, {dinner[2].title()}?")

