import os
import re

def classify_prompt(prompt):
    prompt_lower = prompt.lower()
    keywords_map = {
        "linked_list": ["linked list", "node", "pointer", "linkedlist"],
        "array": ["array", "subarray", "sort array", "reverse array"],
        "tree": ["tree", "binary tree", "bst", "root", "node"],
        "graph": ["graph", "edges", "vertices", "adjacency"],
        "string": ["string", "substring", "palindrome"],
        "dynamic_programming": ["dp", "dynamic programming", "memoization"],
        "sorting": ["sort", "merge sort", "quick sort", "bubble sort"],
        "searching": ["search", "binary search", "linear search"],
        "math": ["factorial", "prime", "gcd", "lcm", "math"],
    }
    for topic, keywords in keywords_map.items():
        if any(k in prompt_lower for k in keywords):
            return topic
    return "misc"

def sanitize_filename(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    text = text.strip('_')
    return text[:50]

def extract_function_name(code):
    """Simple regex to find the first function name in the code."""
    match = re.search(r'def\s+(\w+)\s*\(', code)
    return match.group(1) if match else None

def extract_print_statements(code):
    """Extract all print() lines from the code."""
    return re.findall(r'print\(.*\)', code)

def merge_codes(existing_code, new_code):
    """
    Merge new_code into existing_code:
    - Keep one function definition (the first found).
    - Append only new print statements (examples) that are missing.
    """
    existing_func_name = extract_function_name(existing_code)
    new_func_name = extract_function_name(new_code)

    # If function names differ or none found, fallback: overwrite file with new_code
    if not existing_func_name or not new_func_name or existing_func_name != new_func_name:
        return new_code

    # Extract print statements from both
    existing_prints = set(extract_print_statements(existing_code))
    new_prints = extract_print_statements(new_code)

    # Append only new print statements that do not exist
    appended_prints = [p for p in new_prints if p not in existing_prints]

    # Remove existing prints from existing_code
    existing_code_no_prints = re.sub(r'\nprint\(.*\)', '', existing_code)

    # Append new print statements at the end
    merged_code = existing_code_no_prints.strip() + '\n\n' + '\n'.join(appended_prints) + '\n'

    return merged_code

def save_code_by_prompt(prompt, code):
    topic_folder = classify_prompt(prompt)
    base_folder = os.path.join("workspace", topic_folder)
    os.makedirs(base_folder, exist_ok=True)

    filename_base = sanitize_filename(prompt)
    filepath = os.path.join(base_folder, f"{filename_base}.py")

    if os.path.exists(filepath):
        # File exists - read existing code
        with open(filepath, "r") as f:
            existing_code = f.read()

        # Merge with new code and add repeated prompt comment at top
        merged_code = merge_codes(existing_code, code)
        if not merged_code.startswith("# This code corresponds to repeated/similar prompt"):
            merged_code = "# This code corresponds to repeated/similar prompt\n\n" + merged_code

        with open(filepath, "w") as f:
            f.write(merged_code)
    else:
        # New file, just write code
        with open(filepath, "w") as f:
            f.write(code)

    return filepath, base_folder
