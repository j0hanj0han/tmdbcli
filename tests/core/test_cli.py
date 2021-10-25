
from click.testing import CliRunner
import pytest


from tmdbcli.core.cli import castingfinder


import unittest
from unittest.mock import patch


def test_castingfinder():
  options_parameters='Unknown_actor1, Unknown_actor2'
  # Given
  runner = CliRunner()
  result = runner.invoke(castingfinder, ['--actors', options_parameters ])
  # Then
  assert result.exit_code == 0
  assert result.output == 'Hello Peter!\n'