

# Installing and serving Jekyll using [Bundler](https://bundler.io/)

Serving using [Bundler](https://bundler.io/) is advantageous
over a `jekyll serve` if you want to recreate the enviroment
using a `Gemfile`.

Select the environment:
```
$ bundle config set path '~/ruby/gh-pages'
```

Install the dependencies:
```
$ bundle install
```

Serve the pages:
```
$ bundle exec jekyll serve
```
