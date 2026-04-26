from chemq.config import ChemQSettings, get_default_settings


def test_default_settings() -> None:
    settings = get_default_settings()
    assert isinstance(settings, ChemQSettings)
    assert settings.project_name == "chemq-assist"
    assert settings.alphafold_api_base_url.startswith("https://")
