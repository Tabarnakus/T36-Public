import unittest
from fractions import Fraction
from pathlib import Path
from tempfile import TemporaryDirectory
from reproduce import load_rows, analyze, exact_wilcoxon_two_sided

class ReceiptTests(unittest.TestCase):
    def test_original_aggregates(self):
        rows=load_rows()
        self.assertEqual(len(rows),6)
        result=analyze(rows)
        self.assertEqual(result['new_higher_pairs'],6)
        self.assertAlmostEqual(result['mean_paired_delta_percentage_points'],14.583333,places=6)
        self.assertEqual(result['wilcoxon_exact_two_sided_p'],0.03125)
        self.assertEqual(result['wilcoxon_W_min'],0.0)
    def test_counts_sum_to_40(self):
        for _,n,a,b in load_rows():
            self.assertEqual(n,40)
            self.assertGreaterEqual(a,0)
            self.assertLessEqual(b,n)
    def test_ranks_mixed_sign(self):
        r=exact_wilcoxon_two_sided([Fraction(1),Fraction(-2)])
        self.assertEqual(r['p_two_sided_exact'],1.0)
    def test_changed_input_changes_measured_result(self):
        rows=load_rows()
        result=analyze(rows)
        w,n,a,b=rows[0]
        mutated=[(w,n,a,b-1)]+rows[1:]
        self.assertNotEqual(analyze(mutated)['mean_paired_delta_percentage_points'],result['mean_paired_delta_percentage_points'])

    def test_tied_ranks(self):
        result=exact_wilcoxon_two_sided([Fraction(1),Fraction(1),Fraction(-1)])
        self.assertEqual(result['W_min'],2.0)
        self.assertEqual(result['p_two_sided_exact'],1.0)

    def test_all_zero_rejected(self):
        with self.assertRaises(ValueError):
            exact_wilcoxon_two_sided([Fraction(0),Fraction(0)])

    def test_duplicate_ids_fail(self):
        with TemporaryDirectory() as d:
            p=Path(d)/'rows.csv'
            p.write_text('window,steps_per_condition,old_split_count,new_split_count\nX,40,2,3\nX,40,3,4\n')
            with self.assertRaises(ValueError):load_rows(p)
    def test_out_of_bounds_fail(self):
        with TemporaryDirectory() as d:
            p=Path(d)/'rows.csv'
            p.write_text('window,steps_per_condition,old_split_count,new_split_count\nX,40,41,20\n')
            with self.assertRaises(ValueError):load_rows(p)

if __name__ == '__main__': unittest.main()
