```text
 _  _                 _____               _      _   _
| || |_  _ __ _ ___  |_   _|__ _ __  _ __| |__ _| |_(_)_ _  __ _
| __ | || / _` / _ \   | |/ -_) '  \| '_ \ / _` |  _| | ' \/ _` |
|_||_|\_,_\__, \___/   |_|\___|_|_|_| .__/_\__,_|\__|_|_||_\__, |
          |___/                     |_|                    |___/
```

Hugo Templating
===============

Creating templates for hugo is something that can be difficult to master, a such skills are often reserved for those
individuals who work with javascript, Go Language, and Html on a permanent daily basis. But regardless of this
limitation, with effort, one can expect to get by with their dabbling in the language.


Go Templating
-------------

As previously mentioned, Hugo uses a templating language which is a subset of the Go programming language. It’s sort of
a markup language specific to go, but it does more than provide document styling. There is little else but a page which
mentions text templating in the go manual. Which for the most part, has been copied here.

Here we have our quick reference of go template tags again:

<pre>
- "." = Current Context
- "$." = refers to the current context in a range or code block.
- "|" = Is a pipe, and can be used to pipe values to functions or methods.
- "$" = Can be used to indicate a variable.
- ":=" = Is used to initialize a variable.
- "=" = Can be used to assign a variable a value.
- ".Page" = Refers to the given page.
- ".Site" = Refers to the site in it's entirety.
- ".Site.data" = Refers to the data folder of the site.
- "{{/* Comment */}}" = Is of course a comment.
- "{{- /* No whitespace comment */ -}}" = Is a comment without whitespaces.
- '{{ partial "footer.html" }}' = `Partial` is used to access the theme's partials
- '{{ partialCached "footer.html" }}' = will give you access to a cached partial
- '{{ template "_internal/pagination.html" . }}' = will allow you to access hugo's built in tempaltes.
</pre>

### Go Template Language Hangups

Because Go template language is more functional than a markup language, but not expansive enough to be it's own programming language. A developer will run into situations where the usual method is nonexistent. We will call these hangups. 

1. Concatenation of strings: Use print or printf to concat strings. 


Hugo Template Lookup
--------------------

When Hugo begins to render content it determines where to begin looking for templates by five important
factors:

1. Kind - What kind of template are we looking for? (Home page, or single page)
2. Layout - What is the layout of the content supposed to be.
4. Output Format - What format is the content supposed to be rendered to?
5. Language - What language should the content be rendered in?
6. Type - What type of content should be rendered?
7. Section - Is the content a Section, taxonomy or term?

From there almost all template lookup orders flow from high specificity to low specificity. Meaning Hugo will look for
the most specific templates first, and will continue to look for templates that are gradually less and
less specific until it reaches the least specific template location.

More specifics on this can be found in the [Hugo Documentation](https://gohugo.io/templates/lookup-order/#lookup-rules)

Creating custom output format
-----------------------------

In order to configure Hugo to generate a "custom" type of file, you will need to configure a new custom output
format, but before you do that you need to settle on what mediatype this custom output will use. More than
likely, you will need to create a new custom mediatype as well. All of which can be done in the `config.toml`
or `hugo.toml` file.

```toml
[mediaTypes]
  [mediaTypes."text/redirects"]
    suffixes = ["html"]

[outputFormats]
  [outputFormats.Redirects]
    name = "redirects"
    baseName = ""
    isPlainText = true
    mediaType = "text/redirects"
    permalinkable = false
```

In order to generate this custom output, you will need to place a template for it in the `layouts/_defaults` folder.

Hugo Methods and Function
--------------------------

Here is where I should provide some definition to what differentiates methods from functions. It would be nice if I
understood this more thoroughly my self.

- dict = returns a dictionary structure.
