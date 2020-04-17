import csv
from pathlib import Path

root_dir = Path("/Users/arminbahl/Dropbox/Fish1.5_Exp2_JoAr2/Registration/EM-Refbrain_Registration")
with open(root_dir / "bigwarp_landmarks_EM_stack_to_z_brain.csv", newline='') as f:

    reader = csv.reader(f)
    fw = open(root_dir / "bigwarp_landmarks_z_brain_to_EM_stack.csv", "w", newline='')
    writer = csv.writer(fw, quoting=csv.QUOTE_ALL)
    for row in reader:
        new_row = [row[0],
                   row[1],
                   str(float(row[5])),
                   str(float(row[6])),
                   str(float(row[7])),
                   str(float(row[2])),
                   str(float(row[3])),
                   str(float(row[4]))]

        print(row)
        writer.writerow(new_row)

    fw.close()
