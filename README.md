# Python part 2: Functions, classes and more!

To make this tutorial a little more coherent, we are going to build a maze generator and a maze solver using python.

## 1 A quick revision: Variables, arrays, loops
To start off, let's write a program that makes a 20x20 grid filled with the character `'.'`. Think you're up to it?

<details>
  <summary>Show me the answer</summary>
  
    grid = []
    for i in range(20):
        row = []
        for j in range(20):
            row.push('.')
        grid.push(row)
</details>
