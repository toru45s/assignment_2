import math
from datetime import datetime
from .constants import DATE_FORMAT

class Helper:
  @staticmethod
  def get_current_date():
    date = datetime.now().strftime(DATE_FORMAT)
    return date

  @staticmethod
  def calculate(a, b, c):
      """
      Calculate the result of the expression: b + (sqrt(c^3)/a) * 10
      
      Steps:
      1. Compute c^3 (c cubed)
      2. Calculate the square root of c^3
      3. Divide the square root by a
      4. Multiply the division result by 10
      5. Add b to the result
      
      Args:
          a: Denominator value (must be non-zero)
          b: Base value to add to the expression
          c: Value to be cubed and square-rooted
      
      Returns:
          The calculated result
      """
      if a == 0:
          raise ValueError("Parameter 'a' cannot be zero (division by zero)")
      
      # Step 1: Compute c^3 (c cubed)
      c_cubed = c**3
      
      # Step 2: Calculate the square root of c^3
      sqrt_c_cubed = math.sqrt(c_cubed)
      
      # Step 3: Divide the square root by a
      division_result = sqrt_c_cubed / a
      
      # Step 4: Multiply the division result by 10
      multiplication_result = division_result * 10
      
      # Step 5: Add b to the result
      final_result = b + multiplication_result
      
      return  {
        "step1": c_cubed,
        "step2": sqrt_c_cubed,
        "step3": division_result,
        "step4": multiplication_result,
        "step5": final_result
      }