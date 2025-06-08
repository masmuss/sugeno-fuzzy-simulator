def perform_categorical_evaluation(df, actual_col, predict_col):
    """
    Function to evaluate a pair of categorical columns.
    The 'Positive' class is defined as the 'Optimal' category.
    Returns confusion matrix and evaluation metrics.
    """

    # --- Initialize confusion matrix counters ---
    tp, tn, fp, fn = 0, 0, 0, 0

    # --- Define which class is considered 'Positive' ---
    # In this context, 'Optimal' is the positive class.
    positive_class = 'optimal'

    # --- Iterate through each row in the DataFrame ---
    for index, row in df.iterrows():
        try:
            # 1. Get actual and predicted values, convert to lowercase and strip whitespace
            actual_value = str(row[actual_col]).strip().lower()
            predict_value = str(row[predict_col]).strip().lower()

            # 2. Determine if actual and predicted values are positive cases
            is_actual_positive = (actual_value == positive_class)
            is_predict_positive = (predict_value == positive_class)

            # 3. Update confusion matrix based on comparison
            if is_predict_positive and is_actual_positive:
                tp += 1  # True Positive
            elif not is_predict_positive and not is_actual_positive:
                tn += 1  # True Negative
            elif is_predict_positive and not is_actual_positive:
                fp += 1  # False Positive
            elif not is_predict_positive and is_actual_positive:
                fn += 1  # False Negative
        except (ValueError, TypeError, KeyError):
            # Skip row if there is missing data or other errors
            continue

    # --- Calculate total valid data points ---
    total_data = tp + tn + fp + fn
    if total_data == 0:
        return {"error": "No valid data available for evaluation."}

    # --- Calculate evaluation metrics ---
    accuracy = (tp + tn) / total_data
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0

    # --- Return confusion matrix and metrics as a dictionary ---
    return {
        "confusion_matrix": {"TP": tp, "TN": tn, "FP": fp, "FN": fn},
        "metrics": {"Akurasi": accuracy, "Presisi": precision, "Recall": recall}
    }