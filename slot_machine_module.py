import random

slot_machine_emojis = {
    "emoji1": "🙂",
    "emoji2": "😈",
    "emoji3": "👌🏼",
    "emoji4": "🔥",
    "emoji5": "🌙",
    "emoji6": "⭐️"
}


def machine_emoji_selector(bet):
    choices = ["emoji1", "emoji2", "emoji3", "emoji4", "emoji5", "emoji6"]
    emoji1 = random.choice(choices)
    emoji2 = random.choice(choices)
    emoji3 = random.choice(choices)
    print(f"{slot_machine_emojis.get(emoji1)} | {slot_machine_emojis.get(emoji2)} | {slot_machine_emojis.get(emoji3)}")
    if emoji1 != emoji2 != emoji3:
        print("All 3 different")
        reward = 0
        print(f"You won ${reward}")
        return reward
    elif emoji1 == emoji2 or emoji3 == emoji2 or emoji1 == emoji3:
        print("2 same")
        reward = bet * 2
        print(f"You won ${reward}")
        return reward
    elif emoji1 == emoji2 == emoji3:
        print("All 3 Same. Jackpot!!!")
        reward = bet * 10
        print(f"You won ${reward}!!!")
        return reward


def user_continue():
    user_continue_input = input("Continue? (y/n): ").lower()
    return user_continue_input


