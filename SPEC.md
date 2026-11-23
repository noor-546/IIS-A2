# Spec: Was this you?

## User goal- what is the account trying to achieve?
Account holder wants recommendations that reflect their own viewing even when others use the account

## Input- what does the system recieve? (ie. viewing session, list of titles each with genre)
a new viewing session: the titles each with the genre watched in one sitting. perhaps including the time spent watching.

account viewing history: past sessions that the system has learned, which the profile is built from

answer from account holder (system asks "was this you?" to confirm whether it should learn from a viewing session or to ignore it)

## The one inference- what does it decide? (is the session unusual for this profile?)
compare the genres in the new viewing session to the ones the account typically watches- if most of the session is genres rarely watched by the account then flag it up as unusual.

## Response- what does it show? what can user do?
Not unusual: system learns from session automatically, maybe short message saying so

unusual: holds the session back and asks "was this you?" and show why. user answers yes (learn it) or no (ignore)

## Fallback- what happens if profile is too new to judge, or no response from user?
if profile is too new, learn automatically without asking until at least 5 sessions so that there is something sufficient to compare to.

if user doesn't answer, wait don't learn- user can always go back to account history and undo what was learned from the session though if necessary.

## Not in scope- what won't get built