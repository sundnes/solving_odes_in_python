<%
def chversion(text_IT1413, text_IT1713b, text_general,
              text_book1, text_book2):
    if COURSE == 'IT1713':
        return text_IT1413
    elif COURSE == 'IT1713b':
        text_IT1413b
    elif COURSE == 'general':
        return text_general
    elif COURSE == 'book1':
        return text_book1
    elif COURSE == 'book2':
        return text_book2
    else:
        return 'XXX WRONG value of COURSE: %s' % COURSE
%>
