#!/bin/bash -x
# Compile the book to LaTeX/PDF.
#
# Usage: make.sh [nospell]
#
# With nospell, spellchecking is skipped.

set -x

name=ode_book
#name=test
encoding="--encoding=utf-8"

CHAPTER=chapter
BOOK=book
APPENDIX=appendix

function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

rm tmp_*

if [ $# -ge 1 ]; then
  spellcheck=$1
else
  spellcheck=spell
fi

cd ../chapters
for name in ode_intro rungekutta1 rungekutta2 adaptive disease_modeling diffeq 
do
  cp $name.do.txt tmp.do.txt
  #doconce subst 'FIGURE: +\[fig-(.+?)/(.+?),' 'FIGURE: [https://raw.githubusercontent.com/hplgit/scipro-primer/master/slides/\g<1>/html/fig-\g<1>/\g<2>.png,' tmp.do.txt
  doconce replace "../chapters/" "./" tmp.do.txt
  #hacks to fix references to other chapters
  doconce replace ref{ch:ode_intro} 1 tmp.do.txt
  doconce replace ref{ch:runge_kutta} 2 tmp.do.txt
  doconce replace ref{ch:stiff} 3 tmp.do.txt
  doconce replace ref{ch:adaptive} 4 tmp.do.txt
  doconce replace ref{ch:disease_models} 5 tmp.do.txt
  doconce replace ref{ch:diff_eq} A tmp.do.txt

  doconce replace ref{sec:ode_sys} 1.4 tmp.do.txt

  #more hacks to remove footnote labels, not supported by notebook format
  #footnote bodies should be removed by preprocessor if statements
  system doconce subst "\[\^.*\]" "" tmp.do.txt
  system doconce format ipynb tmp  --allow_refs_to_external_docs #$opt
  mv -f tmp.ipynb ../../docs/ipynb/$name.ipynb
done

#system makeindex $name
#system pdflatex $name

# Publish
#cp book.pdf ../../pub

# index file for book and all chapters
#cd ../chapters
#cp index_files.do.txt index.do.txt
#system doconce format html index --html_style=bootstrap --html_links_in_new_window --html_bootstrap_navbar=off
#cp index.html ../../pub
#rm -f index.*
#cd -

# Report typical problems with the book (too long lines,
# undefined labels, etc.). Here we report lines that are more than 10pt
# too long.
#doconce latex_problems $name.log 10

# Check grammar in MS Word:
# doconce spellcheck tmp_mako__book.do.txt
# load tmp_stripped_book.do.txt into Word
