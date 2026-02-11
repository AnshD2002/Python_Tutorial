# Essential Data Structures: A Quick Reference

Understanding how data is organized is the first step toward writing efficient code. Here is a breakdown of the five primary data structures.

---

## 1. Arrays
Arrays are the most fundamental data structure. They store elements of the **same type** in **contiguous memory locations**.

* **Logic:** Static size and indexed access.
* **Best for:** When you know the number of elements in advance and need fast access via index.



---

## 2. Linked Lists
A Linked List is a **dynamic** data structure where each element (node) contains both the data and a pointer to the next node in the sequence.

* **Logic:** Elements are not stored in adjacent memory; they are "linked" by addresses.
* **Best for:** Frequent insertions and deletions where memory size is unpredictable.



---

## 3. Stacks
Stacks follow the **LIFO (Last-In-First-Out)** principle. Imagine a stack of books; you can only add or remove the one on top.

* **Logic:** Primarily uses `push` (add) and `pop` (remove) operations.
* **Best for:** Function call management (the stack trace) and undo/redo operations.



---

## 4. Queues
Queues follow the **FIFO (First-In-First-Out)** principle. This is exactly like a line at a grocery store—the first person in is the first person out.

* **Logic:** Elements are added at the back (`enqueue`) and removed from the front (`dequeue`).
* **Best for:** Task scheduling, handling asynchronous data transfer, and printer buffers.



---

## 5. Hash Tables
Hash Tables store data in **key-value pairs**. They use a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

* **Logic:** Direct mapping allows for nearly instantaneous data retrieval.
* **Best for:** Databases, caches, and sets where unique lookups are frequent.



---

## Performance Summary

| Data Structure | Access Time | Search Time | Insertion/Deletion |
| :--- | :--- | :--- | :--- |
| **Array** | $O(1)$ | $O(n)$ | $O(n)$ |
| **Linked List** | $O(n)$ | $O(n)$ | $O(1)$ |
| **Stack** | $O(n)$ | $O(n)$ | $O(1)$ |
| **Queue** | $O(n)$ | $O(n)$ | $O(1)$ |
| **Hash Table** | $N/A$ | $O(1)$ | $O(1)$ |

> **Note:** Time complexities are based on average-case scenarios.