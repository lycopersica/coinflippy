import tkinter as tk
import random


def flip_coin():
    global consecutiveHeads, consecutiveTails, totalFlips, requiredHeadsInRow, maxConsecutiveHeads, maxConsecutiveTails

    coins = ["Heads", "Tails"]
    result = random.choice(coins)
    totalFlips += 1

    if result == "Heads":
        consecutiveHeads += 1
        consecutiveTails = 0  # Reset consecutive Tails count
        if consecutiveHeads > maxConsecutiveHeads:
            maxConsecutiveHeads = consecutiveHeads
    elif result == "Tails":
        consecutiveTails += 1
        consecutiveHeads = 0  # Reset consecutive Heads count
        if consecutiveTails > maxConsecutiveTails:
            maxConsecutiveTails = consecutiveTails

    if consecutiveTails == requiredHeadsInRow:
        requiredHeadsInRow += 1
        consecutiveTails = 0  # Reset consecutive Tails to avoid immediate increment

    update_labels(result)


def update_labels(result):
    global consecutiveHeads, consecutiveTails, totalFlips, requiredHeadsInRow, maxConsecutiveHeads, maxConsecutiveTails

    result_label.config(text=f"Last flip: {result}")
    status_label.config(
        text=f"Flips: {totalFlips}, {consecutiveHeads} consecutive Heads, {consecutiveTails} consecutive Tails, Target: {requiredHeadsInRow} Heads in a row")
    max_streak_label.config(
        text=f"Max Heads in a row: {maxConsecutiveHeads}, Max Tails in a row: {maxConsecutiveTails}")
    if consecutiveHeads >= requiredHeadsInRow:
        status_label.config(text=f"Goal achieved: {requiredHeadsInRow} Heads in a row in {totalFlips} flips!")


# Initialize counters and records
consecutiveHeads = 0
consecutiveTails = 0
totalFlips = 0
requiredHeadsInRow = 10
maxConsecutiveHeads = 0
maxConsecutiveTails = 0

# Set up the GUI
root = tk.Tk()
root.title("Coin Flip Simulator")

result_label = tk.Label(root, text="Flip the coin to start", font=('Helvetica', 14))
result_label.pack(pady=20)

status_label = tk.Label(root, text="", font=('Helvetica', 12))
status_label.pack(pady=10)

max_streak_label = tk.Label(root, text="", font=('Helvetica', 12))
max_streak_label.pack(pady=10)

flip_button = tk.Button(root, text="Flip Coin", command=flip_coin, font=('Helvetica', 14))
flip_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
