RANGES  = []
OFFSETS = []

def insert_in_array(ranges, offsets, idx, idA, offset, rng):
    '''
        3 cas :
            [ida, ...]             [0, ...]      => remplacer uniquement 0 par offset
            [ida - k, ida + range] [..., value]  => Ajouter [ida, (ida + range)] dans ranges et [offset] dans offset
            [ida - k1, ida + k2]   [...]         => Ajouter [ida, (ida + range)] dans ranges et [offset, 0] dans offset
    '''
    if len(ranges) != len(offsets):
        raise Exception(f"Array has different size {ranges} {offsets}")

    if not ranges:
        return [idA, idA + rng], [offset, 0]

    if ranges[idx] == idA:
        ranges[idx] = idA + rng
        add_offset = [offset]
        add_ranges  = [idA]
    elif ranges[idx] == idA + rng:
        add_offset = [offset]
        add_ranges = [idA]
    else:
        add_offset = [offset, 0]
        add_ranges  = [idA, idA + rng]
    


    ranges = ranges[:idx] + add_ranges + ranges[idx:]
    offset = offsets[:idx] + add_offset + offsets[idx:]
    return ranges, offset

def string_to_array(ranges, offsets, s):
    listed_input = s.split(" ")
    ida = int(listed_input[0])
    idb = int(listed_input[1])
    rng = int(listed_input[2])
    i = 0
    while i < len(ranges):
        if ranges[i] >= idb:
            return insert_in_array(ranges, offsets, i, idb, ida - idb, rng)
        i += 1
    ranges.append(idb)
    ranges.append(idb + rng)
    offsets.append(ida - idb)
    offsets.append(0)
    return ranges, offsets

def get_idb(ida, ranges, offset):
  i = 0
  while i < len(ranges) - 1:
      if ranges[i + 1] > ida:
        return offset[i] + ida # We are in a specific range
      i += 1
  return ida # Out of bound


def update_ranges_offsets(ranges, offsets):
    if ranges[0] != 0:
        ranges  = [0] + ranges
        offsets = [0] + offsets
    RANGES.append(ranges)
    OFFSETS.append(offsets)

def input_to_array(path):
    with open(path, "r") as f:
        current_range  = []
        current_offset = []
        nb_line = 0
        for line in f:
            if len(line) == 1:
                continue 
            if "map" in line:
                if not current_range:
                    continue
                update_ranges_offsets(current_range, current_offset)
                current_range  = []
                current_offset = []
            else:
                current_range, current_offset = string_to_array(current_range, current_offset, line)
        update_ranges_offsets(current_range, current_offset)


input_to_array('input.txt')
res = []
seeds = "104847962 3583832 1212568077 114894281 3890048781 333451605 1520059863 217361990 310308287 12785610 3492562455 292968049 1901414562 516150861 2474299950 152867148 3394639029 59690410 862612782 176128197".split()
for seed in seeds:
    current_id = int(seed)
    for ranges, offsets in zip(RANGES, OFFSETS):
        current_id = get_idb(current_id, ranges, offsets)
    res.append(current_id)
print(min(res))
