import hashlib
import xml.etree.ElementTree as ET


def hash_file(filepath, block_size=65536):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(block_size):
            hasher.update(chunk)
    return hasher.hexdigest()


def remove_duplicates(file_paths):
    hash_dict = {}
    unique_files = []

    for path in file_paths:
        try:
            file_hash = hash_file(path)
        except Exception as e:
            print(f"Error reading {path}: {e}")
            continue

        if file_hash not in hash_dict:
            hash_dict[file_hash] = path
            unique_files.append(path)

    return unique_files


def find_elements_by_tag_with_depth(element, target_tag, depth=0, results=None):
    if results is None:
        results = []

    if element.tag == target_tag:
        results.append((element, depth))

    for child in element:
        find_elements_by_tag_with_depth(child, target_tag, depth + 1, results)

    return results


def get_all_elements(target_tag: str, file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return find_elements_by_tag_with_depth(root, target_tag)
