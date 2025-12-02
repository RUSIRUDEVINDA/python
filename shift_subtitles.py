import pysrt
from datetime import timedelta

path = r"C:\Users\Asus\Downloads\Supernatural-S15-E13\Supernatural [S15  E13]\Supernatural - 15x13 - Destiny's Child.POKE.English.C.orig.Addic7ed.com.srt"

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

output_file = "output_fixed(1).srt"
subs.save(output_file, encoding="utf-8")

print("Saved to:", output_file)
print("Subtitle shift applied successfully!")
