# -----------------------------------
# import
# -----------------------------------
import htmlwriter
from htmlwriter import HtmlTableWriter, Cell

# -----------------------------------
# define
# -----------------------------------
OUT_FNAME = 'sample.html'
CSS_FNAME = "sample.css"
IMG_OK = './icon/ok_1.png'
IMG_NG = './icon/ng_1.png'
IMG_LINK = './icon/link_1.png'

# -----------------------------------
# class
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------

# -----------------------------------
# main
# -----------------------------------

def main():
    writer = HtmlTableWriter(OUT_FNAME,
                             title='Result Viewer',
                             header='Result Viewer ver.1',
                             css_fname=CSS_FNAME)

    writer.add_summary([
        Cell(htmlwriter.TYPE_TEXT, text='information'),
        Cell(htmlwriter.TYPE_LINK, text='google', link='https://www.google.co.jp/')
    ])

    writer.add_row([
        Cell(htmlwriter.TYPE_TEXT, text='No.'),
        Cell(htmlwriter.TYPE_TEXT, text='ファイル名'),
        Cell(htmlwriter.TYPE_TEXT, text='結果'),
        Cell(htmlwriter.TYPE_TEXT, text='ログフォルダ')
    ])

    import random
    nmax = 100
    for i in range(nmax):
        rand_num = random.randint(1, 10)
        if rand_num % 2 == 0:
            img = IMG_OK
        else:
            img = IMG_NG

        writer.add_row([
            Cell(htmlwriter.TYPE_TEXT, text='{}/{}'.format(i + 1, nmax)),
            Cell(htmlwriter.TYPE_TEXT, text='{:08}.txt'.format(i)),
            Cell(htmlwriter.TYPE_IMG, img=img),
            Cell(htmlwriter.TYPE_LINK, img=IMG_LINK, link='./')
        ])

    writer.write()


if __name__ == '__main__':
    main()