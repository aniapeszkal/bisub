from app import extract_from_srt


def test_always_passes():
    """Just to check if pytest discovers the tests file."""
    pass


def test_extracting_timestamps_and_subtitles_using_regex():
    test_input = '''
1
00:00:06,000 --> 00:00:12,074
line one

2
00:00:21,980 --> 00:00:24,596
more
than
one
line

778
11:53:23,305 --> 00:54:23,746
the last line
    '''.strip()
    expected = [
        (6000, 'line one'),
        (21980, 'more\nthan\none\nline'),
        ((11*60*60*1000)+(53*60*1000)+23305, 'the last line'),
    ]
    assert extract_from_srt(test_input) == expected


def test_whole_file_just_count():
    assert len(extract_from_srt(open('sample.pl').read())) == 767
