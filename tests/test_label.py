import unittest
from click.testing import CliRunner
from os import path
from pathlib import Path
import os
import shutil, tempfile
import pandas as pd
import numpy as np

from tofspec.cli import label

class SetupTestCase(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_files_dir = os.path.join(os.getcwd(), "tests/datafiles")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_label_csv_smiles(self):
        runner = CliRunner()
        result = runner.invoke(label, 
                    [
                        "-o",
                        os.path.join(self.test_dir, "output.csv"),
                        "-ts",
                        "timestamp",
                        os.path.join(self.test_files_dir, "test_compounds.csv"),
                    ]
                )

        # did it succeed?
        self.assertEqual(result.exit_code, 0)

        # did it output the correct text?
        self.assertTrue("Saving file" in result.output)

        # make sure the file exists
        p = Path(self.test_dir + "/output.csv")
        self.assertTrue(p.exists())

    def test_label_csv_mf(self):
        runner = CliRunner()
        result = runner.invoke(label, 
                    [
                        "-o",
                        os.path.join(self.test_dir, "output.csv"),
                        "-ts",
                        "timestamp",
                        "-col=mf",
                        os.path.join(self.test_files_dir, "test_compounds_mf.csv"),
                    ]
                )

        # did it succeed?
        self.assertEqual(result.exit_code, 0)

        # did it output the correct text?
        self.assertTrue("Saving file" in result.output)

        # make sure the file exists
        p = Path(self.test_dir + "/output.csv")
        self.assertTrue(p.exists())