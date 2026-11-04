# DA5401 starting kit

| File | Purpose |
|---|---|
| `solution.py` | **Your framework.** Empty template with the required `StudentSolution` class and the rules; fill in the three methods |
| `make_submission.py` | Trains your framework on the three development sets, saves the models and threshold, builds `submission.zip` and checks it |
| `local_test.py` | Quick local estimate: 80/20 split of each development set |
| `problems.py` | Problem definitions used by the two scripts (your framework must not use it) |
| `requirements.txt` | The exact library versions on the leaderboard (Python 3.11) |

## Steps

1. Create a Python 3.11 environment and install the leaderboard versions:
   `pip install -r requirements.txt`
   Models saved with other versions may fail to load or predict differently on the leaderboard.
2. Write your framework in `solution.py`. Keep `StudentSolution` and its three methods. All preprocessing must
   happen inside the fitted object, because the leaderboard passes it raw features.
3. Check it locally:
   `python local_test.py path/to/folder_with_the_development_csvs`
4. Build your submission:
   `python make_submission.py path/to/folder_with_the_development_csvs`
   This writes `submission.zip`:
   ```
   submission.zip
   ├── solution.py           your framework code (plus any other .py helper files)
   ├── p1_model.joblib       fitted StudentSolution for P1 (preprocessing + model)
   ├── p2_model.joblib       fitted StudentSolution for P2
   ├── p3_model.joblib       fitted StudentSolution for P3
   ├── p3_threshold.json     {"threshold": ...} from get_threshold() on P3
   └── manifest.json         Python and library versions used
   ```
5. Upload `submission.zip` on the **My Submissions** tab. Then choose which of your submissions is shown on
   the leaderboard.

See the **Submission** page for the full rules.
