# Transform a molecule from GJF format to XYZ format.
# gjf_fn: GJF file name
# xyz_fn: XYZ file name

import os
# 定义gif2xyz的函数
def gjf2xyz(gjf_fn, xyz_fn):
    atoms_lines = []
    with open(gjf_fn, "r") as file:
        for lines in file:
            columns = lines.strip().split()
            if len(columns) == 4:
                atoms_lines.append(lines)
            else:
                continue

    # 将提取内容写入新的xyz文件
    with open(xyz_fn, 'w') as f:
        atoms_number = len(atoms_lines)
        f.write(str(atoms_number)+ '\n')
        f.write("changed by python" + '\n')
        for line in atoms_lines:
            f.write(line)

gjf_fn = "ch4.gjf"
xyz_fn = "ch4.xyz"
gjf2xyz(gjf_fn, xyz_fn)

