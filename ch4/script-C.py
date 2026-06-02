import numpy as np
from pathlib import Path

# write output next to this file, regardless of working directory
OUT_PATH = Path(__file__).parent / "script-C-output.tsv"

def test_matrix(rows, cols, rng):
    """Generate a rows x cols random matrix and flatten it into a (rows*cols, 3)
    table of (row, column, result), where result is 1 if the element is > 0.5 else 0.

    Row/column are 1-indexed to match the book's MATLAB convention (loop is
    0-indexed internally, then +1 for output -- same idea as script-A's suffixes).
    """
    matrix = rng.random((rows, cols))
    records = []
    for r in range(rows):
        for c in range(cols):
            result = 1 if matrix[r, c] > 0.5 else 0
            records.append((r + 1, c + 1, result))
    return np.array(records, dtype=int)

if __name__ == '__main__':
    rng = np.random.default_rng()

    # 10. build the 32 x 3 table from a 4 x 8 matrix: (row, column, result)
    data = test_matrix(4, 8, rng)

    # 11. write a tab-delimited text file with a label row Excel/Calc can read.
    #     comments='' strips numpy's default '# ' so the first row is clean labels.
    np.savetxt(OUT_PATH, data, fmt='%d', delimiter='\t',
               header='row\tcolumn\tresult', comments='')

    print("wrote {}x{} table to {}".format(data.shape[0], data.shape[1], OUT_PATH))
