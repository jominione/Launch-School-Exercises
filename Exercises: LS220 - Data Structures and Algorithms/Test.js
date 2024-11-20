console.log(findInNestedArray([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 19) === false);
console.log(findInNestedArray([[15, 25, 35], [45, 55, 65], [75, 85, 95]], 5) === false);

function findInNestedArray(matrix, target) {
  let leftArr = 0;
  let rightArr = matrix.length - 1;
  let subarray = [];
  let left = 0;
  let right = subarray.length - 1;

  while (leftArr <= rightArr) {
    let midArr = Math.floor((leftArr + rightArr) / 2);
    if ((matrix[0][0] > target) || (matrix[matrix.length - 1][matrix[matrix.length - 1].length - 1] < target)) {
      return false;
    } 

  }

  return false;
}