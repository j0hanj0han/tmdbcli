import pytest
from click.testing import CliRunner

from tmdbcli.core.cli import castingfinder


@pytest.mark.parametrize(
    "option_put, result_exit_code_expected",
    [(["--actors", "gérard depardieu, christian clavier"], 0), ([], 2)],
)
def test_castingfinder(option_put, result_exit_code_expected):
    # Given
    runner = CliRunner()
    # when
    result = runner.invoke(castingfinder, option_put)
    # Then
    assert result.exit_code == result_exit_code_expected
    assert type(result.output) == str

    if result.exit_code == 2:
        assert "Missing" in result.output
    elif result.exit_code == 0:
        assert "Astérix" in result.output
