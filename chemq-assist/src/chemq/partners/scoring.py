"""Partner scoring placeholder logic."""


def score_partner(technical_fit: float, scientific_credibility: float) -> float:
    """Compute a simple weighted partner score."""

    return round((technical_fit * 0.6) + (scientific_credibility * 0.4), 4)
