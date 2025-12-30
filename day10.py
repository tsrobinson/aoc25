import re
import numpy as np


def conv_target(target: str) -> list[int]:
    return [int(c == "#") for c in target]


def conv_button(button: tuple, length: int) -> list[int]:
    res = [0] * length
    for i in button:
        res[i] = 1
    return res


def rref_gf2(M: np.ndarray, m: int):
    """
    In-place-ish RREF over GF(2) on augmented matrix M of shape (n, m+1).
    Returns:
      M_red: reduced matrix
      pivot_row_for_col: length m, pivot_row_for_col[c] = row index or -1 if free col
    """
    M = M.copy().astype(np.uint8)
    n = M.shape[0]
    pivot_row_for_col = [-1] * m

    row = 0
    for col in range(m):
        # find a pivot row at/under current row with a 1 in this col
        piv = None
        for r in range(row, n):
            if M[r, col] == 1:
                piv = r
                break
        if piv is None:
            continue

        # swap pivot row into place
        if piv != row:
            M[[row, piv]] = M[[piv, row]]

        pivot_row_for_col[col] = row

        # eliminate this col from all other rows
        mask = M[:, col] == 1
        mask[row] = False
        M[mask] ^= M[row]

        row += 1
        if row == n:
            break

    return M, pivot_row_for_col


if __name__ == "__main__":

    with open("data/day10.txt") as f:
        tasks = f.read().splitlines()

    mpress = 0

    for task in tasks:
        target = re.findall(r"(?<=\[).+(?=\])", task)[0]
        buttons = re.findall(r"(?<=\]\s).+(?=\s\{)", task)[0].split(" ")
        buttons = [tuple(int(i) for i in re.findall(r"\d+", b)) for b in buttons]

        n = len(target)
        m = len(buttons)

        A = np.array(list(zip(*[conv_button(button, n) for button in buttons]))).astype(
            np.uint8
        )
        b = np.array(conv_target(target), dtype=np.uint8)  # shape (n,)
        M = np.concatenate([A, b[:, None]], axis=1)
        Mred, pivrow = rref_gf2(M, m)
        x0 = np.zeros(m, dtype=np.uint8)
        for col in range(m):
            r = pivrow[col]
            if r != -1:
                x0[col] = Mred[r, m]

        free_cols = [c for c in range(m) if pivrow[c] == -1]
        basis = []

        for fc in free_cols:
            v = np.zeros(m, dtype=np.uint8)
            v[fc] = 1
            # pivot variables depend on free variables according to pivot rows
            for pc in range(m):
                r = pivrow[pc]
                if r != -1 and Mred[r, fc] == 1:
                    v[pc] = 1
            basis.append(v)

        k = len(basis)
        best = x0.copy()
        best_w = int(best.sum())

        for mask in range(1 << k):
            x = x0.copy()
            for j in range(k):
                if (mask >> j) & 1:
                    x ^= basis[j]
            w = int(x.sum())
            if w < best_w:
                best_w = w
                best = x

        min_presses = best_w
        mpress += min_presses
        assert np.all((A @ best) % 2 == b)

    print(mpress)
