from pathlib import Path
from asdf.resource import DirectoryResourceMapping

schemas_path = Path(__file__).parent / "schemas"


def get_extensions():
    """
    Get the extension instances for Gammapy.
    This method is registered with the
    asdf.extensions entry point in pyproject.toml.

    Returns
    -------
    list of asdf.extension.Extension
    """
    from .extension import GammapyExtension

    return [GammapyExtension()]


def get_resource_mappings():
    """
    Get the resource mapping instances for the Gammapy schemas.
    This method is registered with the
    asdf.resource_mappings entry point in pyproject.toml.

    Returns
    -------
    list of collections.abc.Mapping
    """
    return [
        DirectoryResourceMapping(
            schemas_path / "gammapy.org" / "gammapy",
            "asdf://gammapy.org/gammapy/schemas/",
            recursive=True,
        )
    ]
