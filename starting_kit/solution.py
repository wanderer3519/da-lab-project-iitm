"""DA5401 course project: submission template (solution.py).

Write your whole framework in this file (extra helper .py files next to it are allowed). Keep the class name
StudentSolution and the three method signatures below.

How it is used
--------------
make_submission.py does, for each public problem, on your computer:

    solution = StudentSolution()
    solution.fit(X, y, metadata)          # X: DataFrame of raw features, y: Series of 0/1 labels
    joblib.dump(solution, "pN_model.joblib")
    # for P3 only: get_threshold() is saved in p3_threshold.json

The leaderboard then loads each saved object and calls

    p = solution.predict_proba(X_holdout, metadata)

on the RAW hidden holdout features: the same columns as the development file, without the target and
record_id. Nothing is refitted on the leaderboard. So everything needed to go from raw features to
probabilities (imputation, encoding, scaling, feature engineering, the model itself) must be learned in
fit() and stored inside the object. Holdout data can contain category values or missing values that do not
appear in the development data.

metadata
--------
A dict with these keys:
    objective             "roc_auc", "log_loss" or "decision_cost"
    greater_is_better     True for roc_auc, False otherwise
    requires_threshold    True when a decision threshold is needed (alert when probability >= threshold)
    cost_false_positive   cost of one false positive (decision_cost only, otherwise None)
    cost_false_negative   cost of one false negative (decision_cost only, otherwise None)
    positive_label        1

Rules
-----
- Train only on the data passed to fit(). Choose the threshold using the development data only.
- Do not identify or special-case a dataset (feature names, row or column counts, specific values): this same
  file is retrained on unseen problems in the private evaluation.
- Use only the libraries in requirements.txt, with exactly those versions.
"""


class StudentSolution:
    def __init__(self):
        # Set up anything your framework needs to remember between fit() and predict_proba().
        pass

    def fit(self, X, y, metadata):
        """Learn everything from the development data: preprocessing, model selection, tuning, final model and,
        when metadata["requires_threshold"] is True, the decision threshold.

        X: pandas DataFrame of raw features (no target, no record_id)
        y: pandas Series of 0/1 labels
        Returns self.
        """
        raise NotImplementedError("implement fit()")

    def predict_proba(self, X, metadata):
        """Return the probability of the positive class for every row of X.

        X: pandas DataFrame of raw features with the same columns as in fit()
        Returns a 1-D array of len(X) values in [0, 1] (an (n, 2) array is also accepted; column 1 is used).
        """
        raise NotImplementedError("implement predict_proba()")

    def get_threshold(self):
        """Return the decision threshold chosen in fit(), a number in [0, 1].

        Only used when metadata["requires_threshold"] is True. A case is an alert when
        probability >= threshold.
        """
        raise NotImplementedError("implement get_threshold()")
