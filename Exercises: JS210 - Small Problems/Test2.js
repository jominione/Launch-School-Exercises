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