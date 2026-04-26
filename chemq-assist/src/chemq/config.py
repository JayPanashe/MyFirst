"""Configuration helpers for ChemQ Assist."""

from dataclasses import dataclass


@dataclass(slots=True)
class ChemQSettings:
    """Runtime settings for ChemQ Assist workflows."""

    project_name: str = "chemq-assist"
    environment: str = "dev"
    alphafold_api_base_url: str = "https://alphafold.ebi.ac.uk"


def get_default_settings() -> ChemQSettings:
    """Return default application settings."""

    return ChemQSettings()
