Greetings!

This is the repository for the [Open Science Collaboration blog](http://osc.centerforopenscience.org/pages/about.html).

If you have questions, wish to improve the site or report a problem; please add an [issue](https://github.com/CenterForOpenScience/osc/issues) to our issue tracker.  Or you can contact us by joining our [mailing list](https://groups.google.com/forum/#!forum/oscblog).

FAQ:

* What's in this repository?  How does the blog run?
* How do I add a new post to the blog?
* How can I contribute in other ways, such as a code or documentation contributions?
* You're a "collaboration"?  How do you make decisions?  How is the project coordinated?

## What's in this repository?  How does the blog run?

This repository houses the software that runs the OSC blog.  The blog is built with [Pelican](http://blog.getpelican.com/).  Pelican is a minimalistic static-site generator built using Python.  There are two main folders within the repository.  The one named `Pelican-Mockingbird` contains template files for the site using our chosen theme, Mockingbird.  The one named `Site` contains the content for the blog, including images, pages and blog posts.  There are a few other files in the main repository.  `Build.py` and `requirements.txt` are needed for people trying to run a local version of the site (you can learn more about that by reading "How can I contribute in other ways?"). `_prose.yml` is a file to configure prose.io, a tool we use to help non-technical contributors add their posts to the site.

Comments are handled via [Disqus](http://disqus.com/) and need to be better documented!

The blog runs on an open source server named [Nginx](http://wiki.nginx.org/Main) and is hosted at [digitalocean](https://www.digitalocean.com/).  When git (or prose.io) pushes to github, it calls a command on the webserver to update the blog automatically.  Volunters interested in maintaing the server should get in touch with Jeff Spies.

## How do I add a new post to the blog?

There are three main ways to add a new post to the blog: by pushing to Github, by using Prose.io, or by sending a file to a member of the team who can add it for you.  To find a member to post, just email the oscblog mailing list and put "CONTENT:" at the beginning of the subject line.

For adding via Github or Prose.io, it's useful to know the following:

Posts are written in [Markdown](http://daringfireball.net/projects/markdown/) and live in `site/content/`.  You can use the file [2013-10-05-Test.md](https://github.com/CenterForOpenScience/osc/blob/master/site/content/2013-10-05-Test.md) as a template (or any other post file, really).  Posts with _Status: draft_ will not show up on the main blog, and can instead be viewed by going to `http://osc.centerforopenscience.org/drafts/slug-name.html_` where `slug-name` equals the value of the line `slug: slug-name`.  (For instance, the test file can be viewed at ['http://osc.centerforopenscience.org/drafts/this-is-a-test.html'](http://osc.centerforopenscience.org/drafts/this-is-a-test.html).  To make a post "live", remove the line `Status:draft`.  Images for posts live in 
`site/content/images/` and are included in posts by using `{{filename}}/images/myimage.jpg`.

### Adding a new post via Github

These instructions are written with the assumption that you're new to Git/Github/version control systems.  Feel free to skip what you already know!  There are six main steps you need to take.

#### Make sure you have Git installed.

If you're on Windows, look for the program 'Git Bash'.  On Mac or Linux, go to your terminal, type `git --version` and press enter.  If the terminal spits out a version number, you have git installed.

If you do not have git installed, go to [this page](https://openhatch.org/wiki/Open_Source_Comes_to_Campus/Harvard/Laptop_setup#Goal_.233:_install_git) and follow the instructions there.

#### Fork the osc repository.

Once you've got a Github account, go to this page (<https://github.com/CenterForOpenScience/osc>) and click the icon labeled "Fork" in the corner.  You should see an animation of a fork holding a book down on a copying machine.  When that's done it should bring you to the copied/forked repository on your account.  Now you have a copy of the OSC blog that you can edit.  It should be at the url `https://github.com/$YOURUSERNAME/osc/`, NOT `https://github.com/CenterForOpenScience/osc/`.

#### Make a local copy.

You can edit files using the Github interface, but you can't add them, which is what you need to do to add a post.  So you need to make a local copy - a copy on your computer.  (Copies on Github are called "remote" copies.)  To do that, go to your terminal (or to Git Bash, if you're using Windows) and type at the command prompt: "git clone $URL".  The specific URL you want is found in the righthand sidebar of the repository's main page under the words "HTTPS clone URL".

#### Make changes.

Now that you've got your local copy, you can use it the way you'd use any directory on your computer.  To add a new post, you want to put your markdown file in site/content/.  Any images should go in site/content/images/.  If you don't want the post to go live immediately, make sure it has the line `Status: draft`. 

#### Submit changes.

This is a multi-step process.  You need to:

Type `git status` to get a list of all the files you've changed or added.  They should be color-highlighted.

Type `git add $file` for each of the files you've changed.  This makes sure git is tracking those changes.

Type `git commit -m "I made these changes"` with a brief explanation of your changes between the quote marks (for instance "added headshot and draft of 'Power'").

Type `git push origin master` which should send the changes back to your remote personal repository.

#### Send a pull request.

Once you have sent the changes to your remote personal branch (the one that should be at the url <https://github.com/$YOURUSERNAME/osc/>) you need to submit a pull request to the OSC blog.  To do so, look at the right sidebar of your repository. Under `Code` and `Issue Tracker` should be `Pull Requests`.  Click that, and it should bring you to a mostly empty page with a bright green button labeled "New Pull Request".  Github should automatically identify the change you want to make, and offer you the option to make a pull request out of the change (this button is more subtle, but should be near the top of the page with bold blue text on white).  Click that, and it should create a change.

Contributors to the blog should be notified that you've submitted a pull request and can make the changes.  If time is of the essence, feel free to email any of us on or off list to make sure someone sees it.
  
### Adding a new post via Prose.io

Sheila has made a [blos prose.io](http://prose.io/#CenterForOpenScience/osc) page you can use.  If you're unfamiliar with how Prose.io works, [this website](http://developmentseed.org/blog/2012/june/25/prose-a-content-editor-for-github/) has a good guide.

## Can I help in other ways besides adding blog posts, such as code contributions or documentation?  How would I do that?

Yes, you absolutely can!  To find issues to work on, either look in the [issue tracker](https://github.com/CenterForOpenScience/osc/issues) or ask on the mailing list [mailing list](https://groups.google.com/forum/#!forum/oscblog).  Most issues will involve setting up a the blog locally, where you can see and test changes.

To set up a local copy of the blog, fork and clone the repository (if those terms are confusing to you, see the instructions in the answer to _How do I add a new post to the blog?_)  Once you've cloned the repository, make sure you're in the main directory.

The first step is to make sure that you have all the required programs/libraries to run the project.  These are listed in `requirements.txt`.  You can check manually, or you can type `pip install -r requirements.txt`.  (If you don't have pip, you can download it [here](http://www.pip-installer.org/en/latest/installing.html).)  Once you've installed the requirements, type `python build.py`.

This will generate a directory called `output`.  (You won't find this in the Github repository, since we [ignore](https://help.github.com/articles/ignoring-files) generated files.)  You can look within `output` to find individual, freshly generated pages, including the main page (`output/index.html`).  Whenever you add new content by adding it to `site/content`, or changed the templates in `Pelican-Mockingbird/`, you'll need to run `build.py` again.

## You're a "collaboration"?  How do you make decisions?  How is the project coordinated?

Decision-making is done in a mostly ad hoc fashion via the [mailing list](https://groups.google.com/forum/#!forum/oscblog).  Coordinating documents and policies can be found in this [google docs folder](https://drive.google.com/?tab=mo&authuser=0#folders/0B0wYQQnuuHxJOUJkWW53XzlPYnc).  




