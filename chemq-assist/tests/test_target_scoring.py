from chemq.opportunities.scoring import score_target


def test_score_target_average() -> None:
    assert score_target(structure_evidence=0.9, partner_fit=0.6, feasibility=0.3) == 0.6
