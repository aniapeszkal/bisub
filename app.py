import re
with open('sample.pl') as f:
    sample = f.read()
RE_SUBTITLES = r'\d+\n(\d{2}):(\d{2}):(\d{2}),(\d{3}).*?\n(.*?)(?:\n\n|$)'
re.findall(RE_SUBTITLES, sample, re.DOTALL)