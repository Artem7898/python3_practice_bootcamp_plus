def handle(cmd: str) -> str:
    parts = cmd.strip().split()
    if not parts:
        return "Type /help"
    if parts[0] == "/help":
        return "Commands: /echo TEXT | /sum A B | /help"
    if parts[0] == "/echo":
        return " ".join(parts[1:]) if len(parts) > 1 else ""
    if parts[0] == "/sum":
        if len(parts) != 3:
            return "Usage: /sum A B"
        try:
            a, b = float(parts[1]), float(parts[2])
        except ValueError:
            return "Numbers only"
        return str(a + b)
    return "Unknown command"
