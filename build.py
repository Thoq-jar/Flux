import os, glob, re


def combine_python_files(source_dir, output_file):
    flux_import_pattern = re.compile(r'^\s*(import|from)\s+.*flux.*$')
    main_block_pattern = re.compile(r'^\s*if\s+__name__\s*==\s*[\'"]__main__[\'"]\s*:\s*$')
    main_blocks, python_files = [], glob.glob(os.path.join(source_dir, "*.py"))

    with open(output_file, 'w') as outfile:
        outfile.write("###\n")
        outfile.write(" # Flux Build System\n")
        outfile.write(" # License: MIT LICENSE\n")
        outfile.write(" # Project: https://github.com/Thoq-jar/Flux\n")
        outfile.write(" # Copyright (c) Thoq 2024 - Present\n###\n\n")

        for fname in python_files:
            with open(fname) as infile:
                outfile.write(f"# [Flux/build] Start of {fname}\n")
                current_block, inside_main_block = [], False
                for line in infile:
                    if main_block_pattern.match(line):
                        inside_main_block, current_block = True, [line]
                    elif inside_main_block:
                        if not line.strip():
                            inside_main_block, current_block = False, main_blocks.append(''.join(current_block)) or []
                        else:
                            current_block.append(line)
                    elif not flux_import_pattern.match(line):
                        outfile.write(line)
                if current_block: main_blocks.append(''.join(current_block))
                outfile.write("# End of {fname}\n\n")
        outfile.write("# [Flux/build] Start of __main__ blocks\n")
        for block in main_blocks: outfile.write(block)
        outfile.write("# End of __main__ blocks\n")

    print(f"[Flux/build] Combined {len(python_files)} files into {output_file}")


if __name__ == "__main__":
    source_directory, output_filename = "src", "flux.py"
    combine_python_files(source_directory, output_filename)