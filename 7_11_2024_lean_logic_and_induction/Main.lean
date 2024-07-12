import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.Finset

/- Supply proofs for 2 out of the 3 assignments.
   Do all 3 for 5 points of extra credit.

   All assignments can be proven through induction and appropriate use of library functions and logic operations.
-/

-- Assignment 1: Show that 2^n % 7 = 1, 2, or 4 for all n.
theorem assignment1 : ∀ n:ℕ, 2^n % 7 = 1 ∨ 2^n % 7 = 2 ∨ 2^n % 7 = 4 := by
  intro n
  induction n with
  | zero => -- base case is left
    left
    simp
  | succ n ih =>
    cases ih with
    | inl ih_left => -- 2^n % 7 = 1 so then 2^(n + 1) % 7 = 2 so right left
      right
      left
      ring_nf -- compute
      rw [Nat.mul_mod] -- rewrite
      rw [ih_left] -- substitute
      simp -- simplify
    | inr ih_right =>
      cases ih_right with
      | inl ih_right_left => -- 2^n % 7 = 2 so then 2^(n + 1) % 7 = 4 so right right
        right
        right
        ring_nf
        rw [Nat.mul_mod]
        rw [ih_right_left]
        simp
      | inr ih_right_right => -- 2^n % 7 = 4 so then 2^(n + 1) % 7 = 1 so left
        left
        ring_nf
        rw [Nat.mul_mod]
        rw [ih_right_right]
        simp

-- Assignment 2: Show that (1-x)*(1+x+x^2+...+x^{n-1}) = (1-x^n)
theorem assignment2
    (x:ℝ)
    : ∀ n:ℕ, (1-x)*(∑ i ∈ Finset.range n, x^i) = 1-x^n := by
  intro n
  induction n with
  | zero =>
    simp
  | succ n ih =>
    rw [Finset.sum_range_succ] -- reduce
    rw [left_distrib] -- distribute
    simp [ih] -- substitute
    ring -- compute

-- Assignment 3: Show that if a_0 = 0, a_{n+1} = 2*a_n+1 then a_n = 2^n-1.
theorem assignment3
    (a: ℕ → ℝ) (h_zero: a 0 = 0) (h_rec: ∀ n:ℕ, a (n+1) = 2 * (a n) + 1)
    : ∀ n:ℕ, a n = 2^n - 1 := by
  intro n
  induction n with
  | zero =>
    simp [h_zero]
  | succ n ih =>
    simp [h_rec, ih] -- substitute
    ring -- compute
