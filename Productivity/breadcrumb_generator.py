#!/usr/bin/env python3

time = input('How long do you want the time? ')
lists = range(0, int(input('How much do you want the checklist? ')))
title = f'''The breadcrumb method. The idea is to check the list every 5 minuts to give you some kind of achivement and automatically boost productivity. It's not just 5 minutes it could be 10 minute or 15 minute or even 1 hour.

---
# Template - {time} minutes streak
Check this mark every {time} minutes

'''

with open("breadcrumb1.md", 'a') as file:
    file.write(title)
    for list in lists:
        file.write(f"- [ ] {time} minute\n")
