```text
#  _   _
# | | | |_   _  __ _  ___
# | |_| | | | |/ _` |/ _ \
# |  _  | |_| | (_| | (_) |
# |_| |_|\__,_|\__, |\___/
#              |___/
#
```

Hugo: The blazing fast static site generator.
==============================================

Hugo is a static site generator written in Go language. It generates a frame work that can be configured to
create just about any website for any situation. It can use yaml, tomly, or even json to store it's
configuration. Markdown is used for content creation, and raw data can be created with either csv or json
files.

On working with Hugo
---------------------

Not all static site generators are created equal. After starting out using jekyll, then moving to hexo, I
finally came into form using Hugo. Ever since, creation of static websites has been a blissful existence. What
sets Hugo apart from the rest of the pack is frankly it's creator, [Bjorn Erik Pedersen](https://github.com/bep). 
Bjorn plays one hell of a mean saxophone, is very polite, and has taken a hands on approach to the management
of the hugo project. Hugo leverages the speed of Google's Go Language, Go was built from the ground up to live
on the web, so it was a perfect fit to perform the task. Hugo can take a stack of markdown files and compile a rich,
featureful, and robust website in a matter of secs. What it generates will be static, meaning there will be no
need for additional support services, which only increases it's appeal to webdevelopers. Hugo can also be used
to manage external libraries and dependencies allowing it to leverage all that is needed to meet any web
developer's needs, and once it has generated that website, Hugo can be used as a development server to test
the website out. It is truly a write it and rip it solution. 

Our coverage of Hugo will include three topics. First are configuration values, then hugo templating syntax
will be discussed, and the third topic is yet to be determined.

### Configuration

When it comes to configuring a site in Hugo, what is most important to distinguish are values that are
theme dependent from values that are theme independent. There are configuration variables and values that
regardless of how the template framework is structured will alter the content of the site and cause a change
in what is generated. Then there are values that are completely dependent on the structure of the framework,
and if used or not used will cause the generation of a website to fail.

### Go Templating

Here we have some templating tags:

- `.` = Current Context
- `$.` = refers to the current context in a range or code block.
- `|` = Is a pipe, and can be used to pipe values to functions or methods.
- `$` = Can be used to indicate a variable.
- `:=` = Is used to initialize a variable.
- `=` = Can be used to assign a variable a value.
- `.Page` = Refers to the given page.
- `.Site` = Refers to the site in it's entirety.
- `{{/* Comment */}}` = Is of course a comment.
- `{{- /* No whitespace comment */ -}}` = Is a comment without whitespaces.
- `{{ partial "footer.html" }}` = `Partial` is used to access the theme's partials
- `{{ partialCached "footer.html" }}` = will give you access to a cached partial
- `{{ template "_internal/pagination.html" . }}` = will allow you to access hugo's built in tempaltes.

- [Go HTML Templating Cheatsheet](go_html_template_cheatsheet)

### References

- https://retrolog.io/blog/creating-a-hugo-theme-from-scratch/
- https://draft.dev/learn/creating-hugo-themes
