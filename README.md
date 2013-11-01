Greetings!

This is the repository for the Open Science Collaboration blog.

If you have questions, wish to improve the site or report a problem; please add an [issue](https://github.com/CenterForOpenScience/osc/issues) to our issue tracker.

## Procedures

For detailed procedures, refer to the [wiki](https://github.com/CenterForOpenScience/osc/wiki). We welcome help with documentation!

This blog is built with [Pelican](http://blog.getpelican.com/).

### Content

If you would like instructions for how to make changes or edit using pull requests (if you want to make a change but can't get push/pull access from the maintainer, or maybe just because you want to do it this way!) scroll down to the section marked "Posting An Article By Submitting A Pull Request".

Editors will be added to the repository and given push/pull access.

Because we're using Github, you can optionally use [prose.io](http://prose.io) for a wiki interface to add/edit files.

(Sheila has made a [blos prose.io](http://prose.io/#CenterForOpenScience/osc) page you can use.)

There's not much to it, and you can use other files as examples. You
put markdown files in `site/content/` to publish them immediately, or
add `Status: draft` to the header of the file to make it a draft.
Pages can be added to the `site/content/pages/` folder. Images live in
`site/content/images/` and are included in posts by using `{{filename}}/images/myimage.jpg`.

### Operations

When git (or prose.io) pushes to github, it calls a command on the
webserver to update the blog automatically. We're updated to the latest
version of pelican, and Jeff is currently in charge of updates. The webserver
is hosted at digitalocean and is served up by nginx. In terms of backup, we have files on Github and the server. Volunters for ops will get in touch with Jeff
for access to the server.

### Posting an Article By Submitting a Pull Request

1) "Fork the repository":   Go to this page (<https://github.com/CenterForOpenScience/osc>) and click the icon labeled "Fork" in the corner.  You should see an animation of a fork holding a book down on a copying machine, and when that's done it should bring you to the copied/forked repository on your account.  Now you have a copy of the OSC blog that you can edit.  It should be at the url <https://github.com/$YOURUSERNAME/osc/>, NOT <https://github.com/CenterForOpenScience/osc/>.

2) "Make a local copy":  You can edit files using the Github interface, but you can't add them, which is what you want to do here.  So you need to make a local copy - a copy on your computer.  (Copies on Github are called "remote" copies.)  To do that you need to go to your command line.  For Mac or Linux, go to your terminal.  For Windows, you need something called Git Bash. (Try here if you're having trouble: <https://openhatch.org/wiki/Open_Source_Comes_to_Campus/Harvard/Laptop_setup#Goal_.233:_install_git>).  Once you're successfully at a terminal/command prompt, type "git clone URL".  The specific URL you want is found in the righthand sidebar of the repository's main page under "HTTPS clone URL".

3) "Make changes":  Now that you've got your local copy, you can use it the way you'd use any directory on your computer.  To add a new post, you want to put your markdown file in site/content/.  Any images should go in site/content/images/.  If you don't want the post to go live immediately, make sure it has the line "Status: draft". 

4) "Submit changes":  This is a multistep proccess:
  - type "git add ." to add all changes you've made to git's internal tracker
  - type "git commit -m "" " with a brief explanation of your change (for instance "added headshot and draft of 'Power'") between the quote marks
  - type "git push origin master" which should send the changes back to your remote personal repository

5) "Send pull request":
   - Once you have sent the changes to your remote personal branch (the one that should be at the url <https://github.com/$YOURUSERNAME/osc/>) you need to submit a pull request to the OSC blog.  To do so, look at the right sidebar of your repository. Under "Code" and "Issue Tracker" should be "Pull Requests".  Click that, and it should bring you to a mostly empty page with a bright green button labeled "New Pull Request".  Github should automatically identify the change you want to make, and offer you the option to make a pull request out of the change (this button is more subtle, but should be near the top of the page with bold blue text on white).  Click that, and it should create a change.

Contributors to the blog should be notified that you've submitted a pull request and can make the changes.  If time is of the essence, feel free to email any of us on or off list to make sure someone sees it.
