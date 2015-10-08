from src.text_box import TextBox


if __name__ == '__main__':
    txt_box = TextBox(100, 200)
    txt_box.set_text('foobar')
    print '> max fnt size: ', txt_box.get_max_fnt_size()
    print '> scaling: ', txt_box.get_scaling()