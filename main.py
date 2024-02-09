import random


def coinflip():
    consecutiveHeads = 0
    consecutiveTails = 0
    totalFlips = 0
    requiredHeadsInRow = 10  # Initial target for consecutive Heads

    while consecutiveHeads < requiredHeadsInRow:
        coins = ["Heads", "Tails"]
        result = random.choice(coins)
        totalFlips += 1

        if result == "Heads":
            consecutiveHeads += 1
            consecutiveTails = 0  # Reset consecutive Tails count
        elif result == "Tails":
            consecutiveTails += 1
            consecutiveHeads = 0  # Reset consecutive Heads count

        # Check if Tails matches the current target for consecutive Heads and increase the target
        if consecutiveTails == requiredHeadsInRow:
            requiredHeadsInRow += 1
            consecutiveTails = 0  # Reset consecutive Tails count to avoid immediate increment

        print(
            f"Flip {totalFlips}: {result} - {consecutiveHeads} consecutive Heads, {consecutiveTails} consecutive Tails, Target: {requiredHeadsInRow} Heads in a row")

    print(f"It took a total of {totalFlips} flips to achieve {requiredHeadsInRow} Heads in a row.")


# Call the function
coinflip()
