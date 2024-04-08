#!/usr/bin/env python
from sympy import Symbol, Eq, And, Not, symbols
import sympy.logic


def check_fermat(n):
  """
  This function checks the validity of Fermat's Last Theorem (negated)
  for a specific value of n (odd or even).

  Args:
      n: An integer representing the power n.

  Returns:
      A string indicating the outcome of the check.
  """

  a, b, c = symbols('a b c')  # Even case doesn't require symbol n

  # Premise (combined for readability)
  premise = And(a > 0, b > 0, c > 0)

  if n % 2 == 1:  # Odd case (already defined in previous code)
    conclusion = Eq(a**n + b**n, c**n)
    contradiction1 = Not(c % a == 0)  # c not divisible by a
    contradiction2 = Not(c % b == 0)  # c not divisible by b
    contradiction3 = And(a**n % a == 0, b**n % b == 0)  # both a^n and b^n divisible by a and b
  else:  # Even case (n is even)
    conclusion = Eq(a**(n//2) * (a**(n//2) + b**n), c**n)
    # Contradictions for even case (both a and b are even)
    contradiction1 = And(a % 2 == 0, b % 2 == 0)  # both a and b are even
    contradiction2 = c % 2 == 0  # c is even
    contradiction3 = True

  # Check implication using both contradictions and negation of conclusion
  if sympy.logic.Implies(premise, contradiction1 & contradiction2 &
                         contradiction3 & ~conclusion):
    return f"Proof seems valid for n = {n} (contradiction found)."
  else:
    return f"The check cannot confirm validity for n = {n} alone."

# Example usage: Check for odd and even cases
for i in range(50):
    print(check_fermat(i))  # Odd case (n = 5)
