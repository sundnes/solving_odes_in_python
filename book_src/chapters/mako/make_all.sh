#!/bin/sh
# Remember --no_mako (include in make.sh)
# PDF
bash make.sh main_mako --no_mako --no_abort
# HTML
bash ../make_html.sh main_mako --no_mako --no_abort
# Must do a hack because of # #include examples in the file
# (preprocess will try to include...so we write # INCLUDE instead
# and edit here)
doconce replace '# INCLUDE' '# #include' *.html ._*.html sphinx-uio/_build/html/*.html sphinx-uio/_build/html/.*.html
dest=../../../pub/mako/html
doconce replace '# INCLUDE' '# #include' $dest/*.html $dest/._*.html $dest/sphinx/*.html $dest/sphinx/.*.html
