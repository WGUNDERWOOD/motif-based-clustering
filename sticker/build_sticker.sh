pdflatex sticker.tex &&
    convert -density 500 sticker.pdf sticker.png &&
    hexsticker sticker.png -o hex_sticker.png --border-size 120 --border-color "#6a668A" --supersample 2 &&
    convert hex_sticker.png -resize 150 hex_sticker_small.png &&
    optipng -o3 hex_sticker.png
    optipng -o3 hex_sticker_small.png
