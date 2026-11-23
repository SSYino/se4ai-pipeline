# Reflection

Name:

Answer each question in 2–3 sentences.

**1. Which antipatterns from the lecture did `train_all.py` show? Point to the lines.**

> `train_all.py` demonstrates the **Big-ass script architecture** antipattern because collection, cleaning, feature engineering, training, evaluation, and saving are all combined in one top-to-bottom script (the numbered blocks at lines 14–36) from a jupyter notebook probably. It also demonstrates **set and forget** because it doesnt plan for regular retraining and hard-codes certain inputs too.

**2. Suppose there were no test and no evaluation gate. What would have happened when the 2026 batch arrived? Think about both the crash and the missing `sqft` values.**

> Without tests or an evaluation gate, the date strings in the 2026 batch would make the fixed date parser crash. Missing `sqft` values could also flow into training unnoticed, producing a model trained on untrusted inputs.

**3. In the real marketplace, which non-ML parts of the system should trigger this pipeline or feed it data?**

> The sales export or transaction database should trigger the pipeline when a new batch is complete, while a data-validation service or feature store should provide the cleaned training data. A model registry and deployment service should consume a passing model, and monitoring should trigger retraining when data drift or prediction error increases.
