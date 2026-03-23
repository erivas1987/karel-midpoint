# karel-midpoint
# Two-Beeper Shrinking Approach

## 📌 Overview

This project implements a solution to the classic **Midpoint Finder** problem using **Karel the Robot** (Python version).

The strategy:

> Place beepers at both ends of the row and progressively shrink the distance between them until the midpoint is found.

---

## 🚀 Algorithm Idea

The algorithm works in three main phases:

### 1. Initialize Boundaries

* Place a beeper at each end of the row (the "corners").
* These beepers act as **moving boundaries**.

### 2. Shrink Toward the Center

* Repeatedly:

  * Move to a boundary beeper
  * Remove it
  * Move one step inward
  * Place it again
* This effectively shifts both boundaries toward the center.

### 3. Detect the Midpoint

* The process continues until:

  * The two beepers become **adjacent**, or
  * They overlap on the same cell
* At that point:

  * The midpoint has been found
  * The right beeper is removed
  * Karel is positioned on the middle cell

---
## ⚙️ Implementation Details

* The robot:

  * Moves back and forth across the row
  * Detects boundaries via `beepers_present()`
  * Uses turning and movement helpers to simulate bidirectional traversal

* Special handling is included for small worlds (e.g., 2x2), ensuring correctness in edge cases.

---

## 📂 Project Structure

```
.
├── main.py   # Karel program
└── README.md # Project documentation
```

---

## ▶️ How to Run

1. Install or use an environment that supports Stanford Karel (e.g., Code in Place or Stanford’s online IDE).
2. Place `main.py` in your project.
3. Run the program.

---
## 💡 Future Improvements

* Eliminate special-case handling (e.g., 2x2 worlds)
* Reduce unnecessary full traversals
* Improve readability with clearer movement invariants

---

## 🙌 Acknowledgments

Programming exercises from **Stanford University**, widely used to teach algorithmic thinking and problem-solving fundamentals.
https://codeinplace.stanford.edu/public/ide/a/midpoint
---

## 🧑‍💻 Author

Ernesto Rivas Garcia

---

## 📜 License

This project is for educational purposes.
