import multiprocessing
import os
from parse_sheet import get_sheet_data
from generate_barcode import generate_barcode

AUTOCOLLANTS_PATH = "sheets/AUTOCOLLANTS_GROUPED.xlsx"
SHEET_NAMES = ["3by5", "5by7", "CORRIDOR"]
THREAD_COUNT = multiprocessing.cpu_count()

def main():
    bar_codes = []
    
    print("Generating barcodes...")
    for sheet_name in SHEET_NAMES:
        data = get_sheet_data(AUTOCOLLANTS_PATH, sheet_name)
        for category, code in data:
            output_dir = f"barcodes/{sheet_name}/{category}/"
            output_file = f"{output_dir}{code}.png"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            bar_codes.append((code, output_file))

    with multiprocessing.Pool(THREAD_COUNT) as pool:
        pool.starmap(generate_barcode, bar_codes)

    print("Done!")
            
if __name__ == "__main__":
    main()