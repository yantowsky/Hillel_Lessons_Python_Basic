import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as in_file:
        cleaned_html = re.sub(r'<[^>]+>', '', in_file.read())
        text_without_empty_line = "\n".join(
            line.strip()
                for line in cleaned_html.splitlines()
                    if line.strip()
        )


    with codecs.open(result_file, 'w', 'utf-8') as out_file:
        out_file.write(text_without_empty_line)


delete_html_tags('draft.html', 'my_cleaned.txt')
