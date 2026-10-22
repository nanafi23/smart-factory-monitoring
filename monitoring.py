"""Rule-based evaluation of simulated readings; not a predictive model."""
def get_status(temperature, vibration):
    if temperature > 90 or vibration > 80:
        return 'CRITICAL'
    if temperature > 75:
        return 'WARNING'
    return 'NORMAL'


def health_score(temperature, vibration):
    """Original coursework heuristic, bounded to 0–100."""
    return min(100, max(0, 100 - int(temperature * 0.5 + vibration * 0.3)))
