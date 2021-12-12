import re

RE_SUBTITLES = re.compile(r'\d+\n(\d{2}):(\d{2}):(\d{2}),(\d{3}).*?\n(.*?)(?:\n\n|$)', re.DOTALL)


def extract_from_srt(srt_contents):
    result = []
    for line in RE_SUBTITLES.findall(srt_contents):
        h, m, s, ms, text = line
        h, m, s, ms = int(h), int(m), int(s), int(ms)
        result_ms = (h*60*60*1000)+(m*60*1000)+(s*1000)+ms
        result.append((result_ms, text))
    return result

