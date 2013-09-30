Greetings!

This is the repository for the Open Science Collaboration blog.

If you have questions, wish to improve the site or report a problem; please add an [issue](https://github.com/CenterForOpenScience/osc/issues) to our issue tracker.

## Procedures

For detailed procedures, refer to the [wiki](https://github.com/CenterForOpenScience/osc/wiki). We welcome help with documentation!

This blog is built with [Pelican](http://blog.getpelican.com/).

### Content

Editors will be added to the repository and given push/pull access.

Because we're using Github, you can optionally use [prose.io](http://prose.io) for a wiki interface to add/edit files.

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


