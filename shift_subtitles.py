# this program can be used to shift subtitle timings in an SRT file
import pysrt
from datetime import timedelta

path = r"file_path.srt"

print("Loading:", path)

subs = pysrt.open(path, encoding="utf-8")
print("Loaded subtitles:", len(subs))

# Shift amount (negative = earlier, positive = later)
shift = timedelta(seconds=0.9)
shift_ms = int(shift.total_seconds() * 1000)

# Apply shift
for s in subs:
    s.start.ordinal += shift_ms
    s.end.ordinal += shift_ms

output_file = "output_fixed.srt"
subs.save(output_file, encoding="utf-8")

print("Saved to:", output_file)
print("Subtitle shift applied successfully!")


