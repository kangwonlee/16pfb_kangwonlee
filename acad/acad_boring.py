def main():
    outer_diameter_mm = 50
    inner_diameters_mm = (40, 20, 30, 20, 10)
    stage_lengths_mm = (15, 20, 15, 20, 30)
    hollow_axle(outer_diameter_mm, inner_diameters_mm, stage_lengths_mm)


def hollow_axle(outer_diameter_mm, inner_diameters_mm, stage_lengths_mm):
    length_mm = sum(stage_lengths_mm)
    outer_radius_mm = outer_diameter_mm * 0.5
    inner_radius_mm = []
    for di_mm in inner_diameters_mm:
        inner_radius_mm.append(di_mm * 0.5)
    upper_coordinates_mm = build_upper_coordinates(inner_radius_mm, length_mm, outer_radius_mm, stage_lengths_mm)
    print upper_coordinates_mm
    lower_coordinates_mm = []
    for xy in upper_coordinates_mm:
        lower_coordinates_mm.append((xy[0], -xy[1]))
    with open('boring.scr', 'w') as f:
        write_upper_section(f, upper_coordinates_mm)
        hatch_upper(f, upper_coordinates_mm)
        write_upper_section(f, lower_coordinates_mm)
        f.write('zoom e\n')
        f.close()


def write_upper_section(f, upper_coordinates_mm):
        f.write('line')
        f.write(' ')
        for xy in upper_coordinates_mm:
            f.write('%g,%g' % xy)
            f.write(' ')
        f.write('c\n')


def hatch_upper(f, upper_coordinates_mm):
    f.write('-Hatch ')
    f.write('%g,%g ' % (upper_coordinates_mm[0][0] - 1, upper_coordinates_mm[0][1] - 1))
    f.write('\n')


def build_lower_coordinates(inner_radius_mm, length_mm, outer_radius_mm, section_lengths_mm):
    lower_coordinates_mm = [(length_mm, -outer_radius_mm),
                            (0.0, outer_radius_mm),
                            ]
    x = 0.0
    for ri_mm, section_length_mm in zip(inner_radius_mm, section_lengths_mm):
        lower_coordinates_mm.append((x, ri_mm))
        x += section_length_mm
        lower_coordinates_mm.append((x, ri_mm))
    return lower_coordinates_mm


def build_upper_coordinates(inner_radius_mm, length_mm, outer_radius_mm, section_lengths_mm):
    upper_coordinates_mm = [(length_mm, outer_radius_mm),
                            (0.0, outer_radius_mm),
                            ]
    x = 0.0
    for ri_mm, section_length_mm in zip(inner_radius_mm, section_lengths_mm):
        upper_coordinates_mm.append((x, ri_mm))
        x += section_length_mm
        upper_coordinates_mm.append((x, ri_mm))
    return upper_coordinates_mm


if __name__ == '__main__':
    main()
