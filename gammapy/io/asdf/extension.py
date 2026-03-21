from asdf.extension import Extension, TagDefinition
from .converters.map_axis import MapAxisConverter


class GammapyExtension(Extension):
    """Gammapy ASDF extension"""

    extension_uri = "asdf://gammapy.org/gammapy/extensions/gammapy-1.0.0"
    converters = [MapAxisConverter()]
    tags = [
        TagDefinition(
            "asdf://gammapy.org/gammapy/tags/map_axis-1.0.0",
            schema_uris=["asdf://gammapy.org/gammapy/schemas/map_axis-1.0.0"],
        )
    ]
