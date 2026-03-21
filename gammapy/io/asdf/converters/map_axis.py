from asdf.extension import Converter


class MapAxisConverter(Converter):
    """Map axis converter."""

    tags = ["asdf://gammapy.org/gammapy/tags/map_axis-1.0.0"]
    types = ["gammapy.maps.MapAxis"]

    def to_yaml_tree(self, obj, tag, ctx):
        return {
            "name": obj.name,
            "nodes": obj._nodes,
            "unit": str(obj.unit),
            "interp": obj.interp,
            "node_type": obj.node_type,
            "boundary_type": obj._boundary_type,
        }

    def from_yaml_tree(self, node, tag, ctx):
        from gammapy.maps import MapAxis
        import astropy.units as u

        return MapAxis(
            name=node["name"],
            nodes=node["nodes"] * u.Unit(node["unit"]),
            interp=node["interp"],
            node_type=node["node_type"],
            boundary_type=node.get("boundary_type", "monotonic"),
        )
