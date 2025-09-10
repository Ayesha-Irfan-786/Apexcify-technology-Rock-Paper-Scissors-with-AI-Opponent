

# 📑 Project Report: Rock-Paper-Scissors Game with AI Opponent

## 1. Introduction

Games have always been an exciting way to learn programming and logic building. One of the simplest yet engaging games is **Rock-Paper-Scissors**, a hand game usually played between two people. The rules are:

* Rock beats Scissors
* Scissors beats Paper
* Paper beats Rock

In this project, the game is implemented in **Python** where the user plays against the computer (AI opponent). The computer makes random choices using Python’s `random` module. An advanced version of the game can also make the AI learn user patterns and improve its predictions.

---

## 2. Objectives

* To implement the Rock-Paper-Scissors game using Python.
* To understand and apply **control flow statements** (if/else).
* To apply **randomization** for computer’s choice.
* To build **basic game logic**.
* (Optional) Extend the game with a simple AI that learns from the user’s past moves.
* To create a **web-based interface** where users can play the game in a browser.

---

## 3. Tools and Technologies

* **Programming Language:** Python
* **Libraries Used:**

  * `random` → for generating computer’s random choice
  * `Flask` → for building a simple web interface
  * `HTML/CSS/JavaScript` → for front-end user interface

---

## 4. Methodology

1. **Game Logic:**

   * The player chooses Rock, Paper, or Scissors.
   * The computer randomly chooses one option.
   * An if-else structure checks the winner.

2. **AI Opponent:**

   * In the basic version, AI is fully random.
   * In the advanced version, AI can track user’s past choices and predict their next move with simple probability.

3. **Web Interface:**

   * A Flask app is created to run the game in a web browser.
   * User-friendly interface similar to an online game with buttons for Rock, Paper, and Scissors.

---

## 5. Implementation

* **Step 1:** Created Python script `rps_basic.py` for command-line gameplay.
* **Step 2:** Used `random.choice()` to generate computer moves.
* **Step 3:** Applied conditional logic to decide the winner.
* **Step 4:** Converted the script into a **Flask web application** so that the game can be played through a browser.

---

## 6. Results

* The game runs successfully on the terminal and the web interface.
* Users can select their moves and instantly see the result.
* The computer opponent provides fair random competition.
* The web version provides a modern interface making the game more interactive.

---

## 7. Future Work

* Add user login and score history.
* Implement a stronger AI that learns and predicts user patterns.
* Add sound effects and animations for better user experience.
* Extend the game to multiplayer online mode.

---

## 8. Conclusion

The Rock-Paper-Scissors project demonstrates how a simple childhood game can be implemented using Python programming. The project helped in understanding **randomization, control flow, and basic AI concepts**. By extending the project into a web-based application, it provides a user-friendly interface and demonstrates how Python can be integrated with web technologies.

