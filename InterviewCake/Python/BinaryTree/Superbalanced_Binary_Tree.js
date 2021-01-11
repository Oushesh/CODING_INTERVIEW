class BinaryTreeNode
{
  constructor(value)
  {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insertLeft(value)
  {
    this.left = new BinaryTreeNode(value);
    return this.left;
  }

  insertRight(value)
  {
    this.right = new BinaryTreeNode(value);
    return this.right;
  }
}

//  A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one

// Recursive Solution
function checkIfSuperBalanced(tree)
{
  let minDepth = Infinity;
  let maxDepth = 0;

  function findMinMaxDepth(node, depth) {
    // Short circuit at this point, no point going further
    if (maxDepth - minDepth > 1) {
      return;
    }

    if (node.left) {
      findMinMaxDepth(node.left, depth + 1);
    }

    if (node.right) {
      findMinMaxDepth(node.right, depth + 1);
    }

    if (!node.left && !node.right)
    {
      // Will keep incrementing as you go further down the tree
      if (depth > maxDepth) {
        maxDepth = depth;
      }

      // Will only happen once
      if (depth < minDepth) {
        minDepth = depth;
      }
    }
  }

  findMinMaxDepth(tree, 0);

  console.log('Max depth:', maxDepth); // Depends if short circuited, might not be actual max depth
  console.log('Min depth:', minDepth);
  return maxDepth - minDepth <= 1;
}

// Example - False for min depth of 1 and max depth of 3
const newTree = new BinaryTreeNode(0);
newTree.insertLeft(1);
newTree.insertRight(1).insertLeft(2).insertRight(3);
const isSuperBalanced = checkIfSuperBalanced(newTree);
console.log('Is it super balanced?', checkIfSuperBalanced(newTree), newTree);

// Example - True for min depth of 2 and max depth of 3
const newTree2 = new BinaryTreeNode(0);
newTree2.insertLeft(1).insertRight(2);
newTree2.insertRight(1).insertLeft(2).insertRight(3);
console.log('Is it super balanced?', checkIfSuperBalanced(newTree2), newTree2);
