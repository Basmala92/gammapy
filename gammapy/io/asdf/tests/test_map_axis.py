import asdf
from numpy.testing import assert_allclose
from gammapy.maps import MapAxis


def test_map_axis_roundtrip(tmp_path):
    axis = MapAxis.from_bounds(
        1,
        100,
        nbin=10,
        unit="TeV",
        name="energy",
        interp="log",
    )

    af = asdf.AsdfFile({"axis": axis})
    af.write_to(tmp_path / "test_map_axis.asdf")

    with asdf.open(tmp_path / "test_map_axis.asdf") as af1:
        axis_rt = af1["axis"]

    assert axis_rt.name == axis.name
    assert axis_rt.interp == axis.interp
    assert str(axis_rt.unit) == str(axis.unit)
    assert axis_rt.node_type == axis.node_type
    assert axis_rt._boundary_type == axis._boundary_type
    assert_allclose(axis_rt.edges.value, axis.edges.value)
