// Problem:
/*
Sum of Pairs Squares

Write a function sumOfPairsSquares(numbers) that takes an array of numbers
as input and returns an array of pairs of numbers whose sum is a
perfect square. The result array should be sorted in ascending order of values.

You may not use Math.sqrt().

// Test cases
puts sumOfPairsSquares([0, 1]) == [[0, 1]]
puts sumOfPairsSquares([1, 2, 3, 4, 5]) == [[1, 3], [4, 5]]
puts sumOfPairsSquares([1, 9, 16, 402, 528]) == [[1, 528], [9, 16]]
puts sumOfPairsSquares([2, 4, 6, 8]) == []
puts sumOfPairsSquares([]) == []

*/

// Rules:
//      Explicit Requirements:
//        - Sum of pairs must be perfect squares.
//        - Output is nested array or empty array.


//      Implicit Requirements:
//        - Input integers are unique.
//        - Pair are made up of unique integers.

// Questions:




// Input:


// Output:


// Data Structures: 
// Input -> array of integers -> nested array or empty array.

// Algorithm:
// - Initialise a results empty array.
// - Have a nested loop with outer loop being first integers.
// - Inner loop being second integer to compare agaisnt first integer.
// - Within inner loop want to have if statement to check the sum of first and second integers sum to perfect square. If true push to results array.
// - Once nested loop completes sort results array in ascending order.
// - return results array.
// - Helper function to verify if a sum is perfect number.
// - Want to use a while loop because iterations is undetermined.
// - Use counter starting with 1.
// - To check if perfect is a perfect number use squareRoot as divisor of modulo operator. 
//    - if the result of the modulo equals square than it is a perfect square.
// 
// - When squareRoot > perfect end loop.


// Test cases
console.log(sumOfPairsSquares([0, 1]));
// Output: [[0, 1]]

console.log(sumOfPairsSquares([1, 2, 3, 4, 5]));
// Output: [[1, 3], [4, 5]]

console.log(sumOfPairsSquares([1, 9, 16, 402, 528]));
// Output: [[1, 528], [9, 16]]

console.log(sumOfPairsSquares([2, 4, 6, 8]));
// Output: []

console.log(sumOfPairsSquares([]));

// Implementation:

function sumOfPairsSquares(numbers) {
  let results = [];

  return;
}

function isPerfectNumber(first, second) {
  let perfect = first + second;


  if (perfect % squareRoot === 0) {
    return true;
  } else if (squareRoot > perfect) {
    return false;
  }
}



// begin
// P - Understanding the Problem:
// - Goal: understand what you're being asked to do
//   - Read the problem description
//   - Identify expected input and output
//   - Establish rules/requirements/define the boundaries of the problem
//   - Ask clarifying questions
//   - Take your time on this step!

// E - Examples and Test Cases:
// - Goal: further expand and clarify understanding about what you're being asked to do 
//   - Use examples/test cases to confirm or refute assumptions made about the problem in the previous step

// D - Data Structures:
// - Goal: begin to think logically about the problem
//   - What data structures could we use to solve this problem?
//     - What does our data look like when we get it? (input)
//     - What does our data look like when we return it? (output?)
//     - What does our data need to look like in the intermediate steps?

// A - Algorithm:
// - Goal: write out steps to solve the given problem in plain English
//   - A logical sequence of steps for accomplishing a task/objective
//   - Start high level, but make sure you've thought through and have provided sufficient detail for working through the most difficult parts of the problem
//   - Stay programming-language-agnostic
//   - Can create substeps for different parts or separate concerns into a helper method
//   - You can (and should) revisit your algorithm during the implementation stage if you need to refine your logic
//   - Before moving onto implementing the algorithm, check it against a few test cases

// C - Implementing a Solution in Code:
// - Goal: translate the algorithm into your programming language of choice
//   - Code with intent. Avoid hack and slash 
// - TEST FREQUENTLY
//   - Use the REPL or run your code as a file
//   - When testing your code, always have an idea in place of what you're expecting
//   - If you find that your algorithm doesn't work, return there FIRST if needed and THEN fix your code
// end