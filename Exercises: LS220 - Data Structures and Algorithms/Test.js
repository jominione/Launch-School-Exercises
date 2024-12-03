class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

function deleteTwos(head) {
  let dummy = new ListNode();
  dummy.next = head;
  let prev = dummy;
  let curr = head;

  while (curr) {
    if (curr.val === 2) {
      prev.next = curr.next;
    } else {
      prev = curr;
    }
    curr = curr.next;
  }

  return dummy.next;
}

// Helper function to format the linked list into a string
function stringifyList(head) {
  let curr = head;
  let result = "";
  while (curr !== null) {
    result += curr.val + " -> ";
    curr = curr.next;
  }
  result += "null";
  return result;
}

// Test case 1
const head1 = new ListNode(1);
head1.next = new ListNode(2);
head1.next.next = new ListNode(3);
head1.next.next.next = new ListNode(2);
head1.next.next.next.next = new ListNode(4);

console.log("Input: ", stringifyList(head1));
console.log("Output:", stringifyList(deleteTwos(head1)));
// Input:  1 -> 2 -> 3 -> 2 -> 4 -> null
// Output: 1 -> 3 -> 4 -> null

// Test case 2
const head2 = new ListNode(2);
head2.next = new ListNode(3);
head2.next.next = new ListNode(2);

console.log("Input: ", stringifyList(head2));
console.log("Output:", stringifyList(deleteTwos(head2)));
// Input:  2 -> 3 -> 2 -> null
// Output: 3 -> null