# IIS-A2
# Was this you?

A Python terminal prototype for shared streaming accounts. It checks whether a new viewing session is unusual for the account holder's profile and, if so, explains why and asks "Was this you?" before learning from it.

## Project status
- **Implemented:** genre-share profile built from confirmed history; unusualness rule (a genre under 10% of the profile is rare; a session is unusual if at least half its titles are rare); user-friendly language thats easy to understand; yes / no / unclear → learned / ignored / pending; review of pending sessions; no checks until 5 sessions.
- **Simulated:** 16 example titles in 6 genres and a hard-coded week of viewing in `main.py`.
- **Not built / planned:** undo a decision, separate household profiles, real streaming data, a recommender, a graphical interface.

## Technology
- Python 3 standard library only; no packages, no API keys.
- A simple rule rather than a trained model, so the reasons shown always match the decision.

## Running it
    python main.py
Answer the prompts as the account holder: `no` for the child's cartoons, `no` for the friend's horror, press Enter (no answer) for "Deep Sea Dive", `yes` for "The Final Frontier", then `y` at the pending review.

## Development record
Full notes on what changed, why and how I checked it: [DEVLOG.md](DEVLOG.md). Commit history: [commits](https://github.com/noor-546/IIS-A2/commits/main).
1. One-page spec (`SPEC.md`), example catalogue and viewing history.
2. Profile built from genre shares; checked by hand (crime 45%).
3. Unusualness rule, tested on child, usual and half-horror sessions.
4. "Was this you?" prompt; fixed a bug where "n" was not recorded as ignored.
5. Changed from "learn if no answer" to a pending list (design change, spec updated).
6. Friendlier wording; removed scores from messages.
7. Review of pending sessions; fixed duplicates and ordering found in testing.

## AI assistance
I used Claude (Anthropic) as a tutor and reviewer. It explained Python compared with C, set each step, gave some code (e.g. `get_genre`, the counting part of `build_profile`, `explain`, and the skeletons of `check_session` and `review_pending`), reviewed my code and errors, helped write up this README, and drafted the system diagram layout. I wrote the spec, catalogue and history, the share calculation, the rare-genre check, the answer handling and the pending list, chose the design changes, and tested each step myself.

## Additional files
- `SPEC.md`: one-page plan.
- `DEVLOG.md`: development log.