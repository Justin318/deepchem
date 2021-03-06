"""
Tests for DataLoader class
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

__author__ = "Bharath Ramsundar"
__copyright__ = "Copyright 2016, Stanford University"
__license__ = "GPL"

import os
import unittest
import tempfile
import shutil
from deepchem.models.tests import TestAPI
from deepchem.featurizers.featurize import DataLoader
from deepchem.featurizers.fingerprints import CircularFingerprint

class TestDataLoader(TestAPI):
  """
  Test Data Featurizer class.
  """
  def test_log_solubility_dataset(self):
    """Test of loading for simple log-solubility dataset."""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = "../../models/tests/example.csv"
    input_file = os.path.join(current_dir, input_file)

    tasks = ["log-solubility"]
    smiles_field = "smiles"
    loader = DataLoader(tasks=tasks,
                        smiles_field=self.smiles_field,
                        featurizer=CircularFingerprint(size=1024),
                        verbosity="low")
    dataset = loader.featurize(input_file, self.data_dir)
    
    assert len(dataset) == 10
