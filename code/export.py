def export(path, base_sizes, base_scale, object_sizes, object_scale):
    out = open(path,'w+')
    out.write('union(){')
    for i in range(len(base_sizes)):
        out.write(f'translate([0,0,{i*base_scale}])cube([{base_sizes[i]},{base_sizes[i]},{base_scale}], center=true);\n')
    for i in range(len(object_sizes)):
        out.write(f'translate([0,0,{len(base_sizes)*base_scale+i*object_scale}])cube([{object_sizes[i]},{object_sizes[i]},{object_scale}], center=true);\n')
    out.write('}')