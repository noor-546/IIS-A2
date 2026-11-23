# Development log

## 1. Spec and example data
-Wrote a one page spec to help plan the project, created a catalogue of 16 example titles across 6 genres and a 6 session viewing history for the account holder.
-The spec kept the scope to one inference so it was achievable. 6 genres let the account holders usual viewing (e.g. crime, drama) look clearly different from a childs or a friends (e.g. horror). A 6 session viewing history was used as minimum sessions is set to 5 so that the system has suffient data to compare to when learning from new sessions.
-Check: Printed each sessions genres, every title was found so the names matched the catalogue.

## 2. Profile from history
-'build_profile' counts genres across the user history and turns counts into shares.
-The profile is what the system has learned and what new sessions are compared against
-Check: worked out calculations (e.g. 11 titles, 5 crime = 45%), output matched my calculations

## 3. Unusualness rule
-A genre under 10% of the profiles viewings counts as rare where score=share of the session's titles in rare genres; flag if the score is at least 0.5
-Every reason showed to the user comes from these numbers
-Checked with 3 test sessions: child's kids titles 1.00 (unusual), users usual viewing 0.00 (typical), half horror 0.50 (unusual)
-Decision: kept 0.5, so a half-unusual session is asked about; asking costs one answer, while missing it lets someone else's viewing into the profile

## 4. "Was this you?" prompt
-'check_session' learns automatically while there are fewer than 5 viewing sessions, learns typical sessions and for unusual ones it asks "was this you?" to confirm if it was someone else using the users account or if the user is just trying something new.
-Bug found in testing: when user types (yes/no), typing "n" went to the else branch, which printed "ignored" but never added the session to the ignored list
-Fix: used '.strip().lower()' on the answer and accepting y/yes and n/no
-Check: ran it again; "NO" and "n" both worked and session appeared in Ignored sessions.

## 5. Pending list
-Unclear answers keep the session in a pending list, where its not learned until the user decides.
-Learning by default could let a child's session into the profile whenever the account holder doesn't answer, which is the problem this project is to solve.
-Error occurred as pending was not defined; fixed by adding 'pending = []'
-Check: pressed enter instead of typing yes/no and it showed the pending message and appeared in pending sessions.

## 6. User friendly wording
-Removed scores from the messages shown by the system because the number means nothing to the user.
-Messages now show what happens to user recommendations so it is easier for them to understand what is going on.
-Check: ran it again; made sure all the messages were shown correctly and easy to read.

## 7. Review pending sessions
-At the end of a run pending sessions are asked about again; yes learns, no ignores and unclear remains pending.
-Before this, a pending session stayed stuck forever and user has no way to resolve. This helps user stay in control.
-Bug found while testing: yes/no didn't remove the session from the pending list and the review ran after the final profile was printed. Fixed by adding 'pending.remove(session)'
-Check: left documentary pending then typed "yes" and documentary went from 8% to 14% in final profile. Press enter both times and it stayed pending once, with the "still waiting" message.

## Observations from testing
-The system adapts slowly (e.g. after one "yes", documentaries were 8% of the profile (under 10%), so the second documentary was still asked about; after two it would be 14% and learned without asking)
-This is cautious adaptation, but it means asking more than once about a genuine new interest
-In one test I answered "yes" to the child's cartoons by mistake, and kids became 13% of the profile. There is no way to undo a decision yet, so one wrong answer changes recommendations. Undo is planned.

## AI assistance