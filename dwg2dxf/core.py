import os
import subprocess
import ezdxf
from .utils import find_oda_converter

def convert_dwg_to_dxf(dwg_path, output_dir=None):
    oda_converter = find_oda_converter()
    if oda_converter is None:
        raise FileNotFoundError("ODAFileConverter.exe not found in PATH or known directories.")

    if not os.path.exists(dwg_path):
        raise FileNotFoundError(f"DWG file does not exist: {dwg_path}")

    if output_dir is None:
        output_dir = os.path.dirname(dwg_path)

    command = f'"{oda_converter}" "{os.path.abspath(dwg_path)}" "{output_dir}" ACAD2013 DXF 1 0 1'

    subprocess.run(command, shell=True, check=True)

    base_name = os.path.splitext(os.path.basename(dwg_path))[0]
    dxf_file = os.path.join(output_dir, base_name + ".dxf")

    if not os.path.exists(dxf_file):
        raise FileNotFoundError(f"DXF output not found: {dxf_file}")

    return dxf_file

def read_dxf_entities(dxf_file):
    doc = ezdxf.readfile(dxf_file)
    msp = doc.modelspace()

    entity_summary = {}
    for entity in msp:
        entity_type = entity.dxftype()
        entity_summary[entity_type] = entity_summary.get(entity_type, 0) + 1

    return entity_summary
