import ffmpeg


def test_empty_string_input_option_has_no_value():
    args = ffmpeg.input('in.mp4', noautorotate='', ss=3).output('o.jpg').get_args()
    assert args == ['-noautorotate', '-ss', '3', '-i', 'in.mp4', 'o.jpg']


def test_empty_string_output_option_has_no_value():
    args = ffmpeg.input('in.mp4').output('o.mp4', shortest='').get_args()
    assert args == ['-i', 'in.mp4', '-shortest', 'o.mp4']


def test_convert_kwargs_empty_string_none_and_zero():
    args = ffmpeg._utils.convert_kwargs_to_cmd_line_args(
        {'a': '', 'b': None, 'c': 0, 'd': ['x', '']}
    )
    assert args == ['-a', '-b', '-c', '0', '-d', 'x', '-d']


def test_convert_kwargs_false_stays_value():
    args = ffmpeg._utils.convert_kwargs_to_cmd_line_args({'a': False})
    assert args == ['-a', 'False']
