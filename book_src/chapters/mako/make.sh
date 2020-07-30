# Cannot use ../make.sh because of the # INCLUDE construction
#bash -x ../make.sh main_mako --no_mako

# Must do a hack because of # #include examples in the file
# (preprocess will try to include...so we write # INCLUDE instead
# and edit here)

mainname=$1
shift
args="$@"

# Strip off main_ in $mainname to get the nickname
nickname=`echo $mainname | sed 's/main_//'`

# Individual chapter documents will have formulations like
# "In this ${BOOK}" or "in this ${CHAPTER}" to be transformed
# to "In this document" when the chapter stands on its own, while
# for a book we want "In this book" and "in this chapter".
CHAPTER=document
BOOK=document
APPENDIX=document

# Function for running operating system commands. The script aborts
# if the execution is unsuccessful. All doconce, latex, etc. commands
# in this script are run with the system function such that the script
# stops when the first error is encountered.
function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

rm -fr tmp_*

# Perform spell checking
system doconce spellcheck -d .dict4spell.txt *.do.txt

# Copy common newcommands
system preprocess -DFORMAT=pdflatex ../newcommands.p.tex > newcommands_keep.tex
# Copy ptex2tex configuration file if not using the newer --latex_code_style=...
#cp ../.ptex2tex.cfg .

opt="CHAPTER=$CHAPTER BOOK=$BOOK APPENDIX=$APPENDIX"

# Paper version (--device=paper)
system doconce format pdflatex ${mainname} $opt --device=paper --latex_admon_color=1,1,1 --latex_admon=mdfbox $args --latex_list_of_exercises=toc --latex_table_format=left "--latex_code_style=default:lst[style=blue1]@pypro:lst[style=blue1bar]@dat:lst[style=gray]@sys:vrb[frame=lines,label=\\fbox{{\tiny Terminal}},framesep=2.5mm,framerule=0.7pt]"
# code style: blue boxes, darker-color frame for complete boxs, and terminal
# style for sys
# alternative code style: blue boxes with plain verbatim for all code, special
# terminal style for sys (gives larger colored framed than the lst-style above)
#"--latex_code_style=default:vrb-blue1@sys:vrb[frame=lines,label=\\fbox{{\tiny Terminal}},framesep=2.5mm,framerule=0.7pt]"

# Auto-editing of .tex file (tailored adjustments)
doconce replace 'linecolor=black,' 'linecolor=darkblue,' ${mainname}.tex
doconce subst 'frametitlebackgroundcolor=.*?,' 'frametitlebackgroundcolor=blue!5,' ${mainname}.tex
doconce replace '# INCLUDE' '# #include' ${mainname}.tex
# Special fix for unwanted footnote in URLs in tex demo code
doconce subst 'sampler\.py\}\\footnote.+' 'sampler.py}}' ${mainname}.tex
doconce subst 'sampler\.m\}\\footnote.+' 'sampler.m}}' ${mainname}.tex

rm -rf ${mainname}.aux ${mainname}.ind ${mainname}.idx ${mainname}.bbl ${mainname}.toc ${mainname}.loe
system pdflatex ${mainname}
bibtex ${mainname}
makeindex ${mainname}
system pdflatex ${mainname}
system pdflatex ${mainname}
mv -f ${mainname}.pdf ${nickname}-4print.pdf  # drop main_ prefix in PDF

# Electronic version
system doconce format pdflatex ${mainname} $opt --device=screen --latex_admon_color=1,1,1 --latex_admon=mdfbox $args --latex_list_of_exercises=toc --latex_table_format=left "--latex_code_style=default:vrb-blue1@sys:vrb[frame=lines,label=\\fbox{{\tiny Terminal}},framesep=2.5mm,framerule=0.7pt]"
# Auto-editing of .tex file (tailored adjustments)
doconce replace 'linecolor=black,' 'linecolor=darkblue,' ${mainname}.tex
doconce subst 'frametitlebackgroundcolor=.*?,' 'frametitlebackgroundcolor=blue!5,' ${mainname}.tex
system pdflatex ${mainname}
bibtex ${mainname}
makeindex ${mainname}
system pdflatex ${mainname}
system pdflatex ${mainname}
mv -f ${mainname}.pdf ${nickname}.pdf  # drop main_ prefix in PDF

# Publish
dest=/some/repo/some/where
dest=../../../pub
if [ ! -d $dest ]; then
exit 0  # drop publishing
fi
dest=$dest/$nickname
if [ ! -d $dest ]; then
  mkdir $dest
  mkdir $dest/pdf
  mkdir $dest/html
fi
cp ${nickname}*.pdf $dest/pdf/

# If published in an external repo and the current writing repo is
# private, all the source files for programs need to be copied to
# the publishing repo as well.

# Could make other versions, A4, 2 pages per sheet, etc.
