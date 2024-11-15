v1 = '2'
v2 = '2.0.0'
v3 = '2.14.3'
v4 = '2.0.0.4.23'

def version_compare(version1, version2):
    # Split version strings by '.' and convert each part to an integer
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    
    # Fill in the mission zeros for shorter builds
    max_length = max(len(v1_parts), len(v2_parts))
    
    # Pad the shorter version with zeros (2.0 becomes 2.0.0.0 if needed, etc)
    v1_parts.extend([0] * (max_length - len(v1_parts)))
    v2_parts.extend([0] * (max_length - len(v2_parts)))
    
    # Compare each part of the versions
    for part1, part2 in zip(v1_parts, v2_parts):
        if part1 < part2:
            return -1
        elif part1 > part2:
            return 1
    
    # If all parts are equal, return 0
    return 0