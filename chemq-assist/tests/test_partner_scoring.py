from chemq.partners.scoring import score_partner


def test_score_partner_weighted_average() -> None:
    assert score_partner(technical_fit=0.8, scientific_credibility=0.5) == 0.68
