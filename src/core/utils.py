def deep_merge(target: dict, delta: dict) -> None:
    for key, value in delta.items():
        if key in target:
            current_entry = target[key]

            if isinstance(current_entry, dict) and isinstance(value, dict):
                deep_merge(current_entry, value)

            elif isinstance(current_entry, list) and isinstance(value, list):
                current_entry.extend(value)

            else:
                target[key] = value
        else:
            target[key] = value
