```Hinode
#  _   _ _                 _
# | | | (_)_ __   ___   __| | ___
# | |_| | | '_ \ / _ \ / _` |/ _ \
# |  _  | | | | | (_) | (_| |  __/
# |_| |_|_|_| |_|\___/ \__,_|\___|
#
```

Hinode
------

Hinode is a template for the Hugo static site generator, written by [Mark
Dumay](https://github.com/markdumay). It's primary emphasis is on providing
a theme that allows for versioned documentation of Open Source software projects, although it can easily be adapted to
suit any desired purpose, it excels at providing a layout for documentation based websites.

As has been pointed out numerous times in this website, a project is only as good as the developer who created
it. Hugo stands out in excellence due to it's creator [Bjorn Erik Pedersen](https://github.com/bep), in
the same manner, Hinode stands out due to it's creator [Mark Dumay](https://github.com/markdumay). Working
with him is a pleasure, and his professionalism is superior.

### Hinode Section Layouts

There are three primary section layouts for the hinode template: Lists, Cards, and Navs.

The most basic sectional layout is the list layout, as it provides no additional configuration options except for the basic configuration options
available to all sectional layouts. Do not get this confused with being the default layout, which is the card layout. The card layout also provides
the most amount of configuration options. 

So to recap, "Lists" are the most basic, but "cards" are the default.

Below we list the configuration fields for those sectional layouts.

T.B.D.

#### Basic/List

List sections only contain the basic set of configuration options, which the other two available layouts build on top of. Because fundamentally speaking
all sectional layouts are lists. Of course with the rest of Hinode's configuration, the configuration of these layouts is performed in yaml.

### Distinguishing Reference and Links notation in Hugo and Hinode.

When inquired as to what the actual difference is between a reference shortcode and a link shortcode, the
author of Hinode, Mark Dumay, gave [this answer](https://github.com/gethinode/hinode/discussions/1279#discussioncomment-11138588).

    Let me clarify a few concepts first:

        ref and relref are shortcodes provided by Hugo. They resolve to the path of a content page.
        link is a custom shortcode maintained by the Hinode theme. It resolves to both content pages and site assets.
        Hinode implements a render hook to handle native markdown links since release v0.26.0.

    Hugo treats content pages differently than (static) site assets and page resources. In general, you cannot use relref and ref to reference a static asset such as an pdf file. Hinode tries to simplify (unify) the handling of content pages and site assets. You can use standard Markdown links to reference both a content page and a site asset.

        Note

        Both relref and ref are not really necessary when using the Hinode theme. The documentation only mentions them for backwards compatibility.

    Consider the following example. I have a static asset available on the path ./static/img/logo512x512.png. I want the browser to open this file when I click on it. Hugo publishes static assets without the static base folder. You can use the following markdown link to reference this static file and let the browser decide what to do with it. Most browsers will simply display the image file.

    `[Logo](/img/logo512x512.png)`

    I hope this clarifies the concept of links. Feel free to share your experiences and let us know how we can improve the documentation further.

### Creating Modules for Hinode

Below is the process followed for creating modules for the Hinode theme.

1. Navigate to [The Hinode Module Template](https://github.com/gethinode/mod-template), and click on the "Use
   this template" button.
2. Fill out all the pertinent information in order to create a repository for the module you are creating.
3. Then clone the repository to your local machine to begin development.
4. Create a "develop" branch of that repository. `git branch develop`
5. Assuming you use VSCode, perform a project wide find and replace, finding `gethinode/mod-template` and
   replacing it with `{$OWNER}/mod-{$YOUR_MODULE_NAME}`. Ignoring entries in package-lock.json, as npm will
   handle this for you automatically.
6. Then perform another project wide find and replace, this time finding `mod-template` and replacing it with
   `mod-{$Your_MODULE}`.
7. Make changes as desired or needed in the `README.md`, `package.json`, and `.gitignore`.
8. Cd into the `examplesite` directory and run `hugo mod get -u ./... && hugo mod get -u`
9. Stage all files for commit `git add -a`, and use `npx git-cz` to generate a conventional commit message.
   Then push everything in the develop branch to your remote repository. `git push --set-upstream origin
   develop`.
10. Use NPM to install the dependencies for your module as development dependencies. Use `npm install
   --save-dev {$NPM_Package}` or `npm install -D {$NPM_Package}` or `npm i -D {$NPM_PACKAGE}` to accomplish
   this.
11. Modify the `postinstall` script in `package.json`, copying required files from `dist` folder of the NPM
    Package to the `dist` folder at the base of the repository. This folder does not have to exist, and will
    be created. The `cpy` package has been installed previously for this purpose. Facilitation of the `--flat`
    flag is necessary in order to flatten the files in the destination directory. More information on the
    particulars of this step can be found in [the hinode module create guide.](https://gethinode.com/guides/modules/#step-3---exposing-the-katex-distribution-files)
12. Critically, the next step is to actually install everything, which will most importantly run the
    postinstall script, and copy the required files to the dist folder. If you happen by chance to skip this
    step, as I did at first, your module will fail consecutively to produce a valid result.
13. Next modify where hugo is to mount the required files and folders of the module in the `config.toml` file.
    Take note, the folders `layouts`, `assets`, and `static` are all previously assigned a mount point. This
    is to prevent file mount conflicts, and ensure local folders are not replaced by mount points during use
    of the module.
14. Create the custom files needed to appropriately load and/or use the features provided by your module. This
    can be through the addition of a shortcode, or through the additional loading of javascript in the site.
15. Modify the `hugo.toml` file in the `examplesite` directory to mount the files located in the `dist` folder
    to their correct place in the website build tree.
16. Once complete, you will want to run the script `npm run mod:update` to install the hugo modules and check
    for any needed updates.
17. If you did not create a shortcode for your modules, modify the base template of the example site,
    `examplesite/layouts/_default` to include the required dependencies of our module.
18. Next, in order to test your module, you will need to add the required content to test it to the front page
    of your website. This is done by editing `examplesite/content/_index.md`.
19. When you have completed modifying the example site, start up the development server to test your module
    out. `npm run start`

Be aware that your module might respond differently when used in a full production site, than it did in the
example site. 

#### Loading of JS will not work if solely performed in shortcode.

If you attempt to load a resource solely through adding it to a shortcode template this will not work. You
will need to include it as part of the site layout, through creation of a module layout file.

### Troubleshooting

Somewhat similar to troubleshooting docker builds, troubleshooting failed mod builds is like flying blind.
Since most of the transpilation occurs in the computer memory, it is difficult to spot exactly where things
went wrong. 

#### Error "head/styesheet.html not found"

Make sure the folder is actually named "head" and not "header".
