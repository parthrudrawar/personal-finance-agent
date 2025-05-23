def generate_suggestions(report):
    """Generate simple suggestions based on budget report."""
    suggestions = []
    for cat, data in report.items():
        if data['status'] == 'Over':
            suggestions.append(f"Reduce spending on {cat}. You're over budget by ${abs(data['difference']):.2f}.")
        else:
            suggestions.append(f"Good job on {cat}, you are within your budget.")
    return suggestions
