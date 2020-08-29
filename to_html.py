
import sys, os, markdown
import re

try:
    from urllib.parse import urlparse
    from urllib.parse import urlunparse
except ImportError:
    from urlparse import urlparse
    from urlparse import urlunparse


TEMPLATE="""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
    <title>{{title}}</title>
    <link rel="stylesheet" href="https://ibrevdo.github.io/notes/css/common.css">
</head>

<body>

<div id="navbar">
    <ul>
    <li><a  href="/index.html">Home</a></li>
    <li><a  href="/linux/index.html">Linux</a></li>
    <li><a  href="/programming/index.html">Programming</a></li>
    <li><a  href="/computing/index.html">Computing</a></li>
    <li><a  href="/studies/index.html">Studies</a></li>
    <li><a  href="/webtools/webtools.html">Webtools</a></li>
    <li><a  href="/travel/index.html">Travel</a></li>
    <li><a  href="/media/index.html">Media</a></li>
    <li><a  href="/etc/index.html">Etc</a></li>
    </ul>
</div>

{{toc}}


<div class="content">
    <div class="folder">
        <p>&#60;{{folder}}&#62;</p>    
    </div>
    {{content}}
</div>

<div id="path">
    ~/git/notes/{{path}}
</div>

</body>
</html> 
"""

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

#def my_url_builder(label, base, end):
#    url=base+label.replace('-','/')+end
#    return url

def my_build_url(urlo, base, end, url_whitespace, url_case):

    """ Build and return a valid url.
    Parameters
    ----------
    urlo            A ParseResult object returned by urlparse
    base            base_url from config
    end             end_url from config
    url_whitespace  url_whitespace from config
    url_case        url_case from config
    Returns
    -------
    URL string
    """
    if not urlo.netloc:
        if not end:
            clean_target = re.sub(r'\s+', url_whitespace, urlo.path)
        else:
            clean_target = re.sub(r'\s+', url_whitespace, urlo.path.rstrip('/'))
            clean_target = os.path.splitext(clean_target)[0]
            if clean_target.endswith(end):
                end = ''
        if base.endswith('/'):
            path = "%s%s%s" % (base, clean_target.lstrip('/'), end)
        elif base and not clean_target.startswith('/'):
            path = "%s/%s%s" % (base, clean_target, end)
        else:
            path = "%s%s%s" % (base, clean_target, end)
        if url_case == 'lowercase':
            urlo = urlo._replace(path=path.lower() )
        elif url_case == 'uppercase':
            urlo = urlo._replace(path=path.upper() )
        else:
            urlo = urlo._replace(path=path)
    return urlunparse(urlo)


def main():
    for root, dirs, files in os.walk("md"):
        for file in files:
            if file.endswith(".md"):
                input_file_path = os.path.join(root, file)
                output_file_path = input_file_path.replace("md/","docs/").replace(".md", ".html")
                ensure_dir(output_file_path)


                with open(input_file_path, "r", encoding="utf-8") as input_file:
                    text = input_file.read()

                extensions=[ 
                        'toc',
                        'mdx_wikilink_plus',
                        'tables',
                        'meta',
                        'fenced_code' ]

                md_configs  = {
                        'mdx_wikilink_plus' : {
                            'end_url' : '.html',
                            'build_url' : my_build_url
                            },
                        }
                
                md = markdown.Markdown(extensions = extensions,extension_configs=md_configs)
                html = md.convert(text)
                doc = TEMPLATE.replace('{{content}}',html)
                doc = doc.replace('{{toc}}',md.toc)

                m = re.match("<h1.*>(.*)</h1>",html)
                if m is not None:
                    title = m.groups()[0]
                    doc = doc.replace('{{title}}',"Igor's notes: "+title)
                else:
                    doc = doc.replace('{{title}}',"Igor's notes")
                
                doc = doc.replace('{{path}}',input_file_path)
                

                m = re.match("md/(.*)/\w*\.md",input_file_path)
                if m is not None:
                    folder = m.groups()[0]
                    doc = doc.replace('{{folder}}',folder)
                else:
                    doc = doc.replace('{{folder}}',"")

                with open(output_file_path, "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
                    output_file.write(doc)

if __name__ == '__main__':
    sys.exit(main())
