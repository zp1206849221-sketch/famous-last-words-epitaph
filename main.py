import os

# Final: the twist is him; the tombstone stamps the ticket "won't fix".
ENTRY = (
    "Here lies a senior developer. He hunted one bug for ten years. "
    "Found it in the end: it was him. Status: won't fix."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
