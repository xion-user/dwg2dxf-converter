import argparse
from dwg2dxf.core import convert_dwg_to_dxf, read_dxf_entities

def main():
    parser = argparse.ArgumentParser(description="DWG to DXF Converter and Entity Reader")
    parser.add_argument("dwg_file", help="Input DWG file path")
    parser.add_argument("--output-dir", help="Output directory", default=None)

    args = parser.parse_args()

    try:
        dxf = convert_dwg_to_dxf(args.dwg_file, args.output_dir)
        entities = read_dxf_entities(dxf)

        print(f"\nEntities in {dxf}:")
        for etype, count in entities.items():
            print(f"  - {etype}: {count}")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
