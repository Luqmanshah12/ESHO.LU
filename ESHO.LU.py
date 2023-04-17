gh-md-toc
=========

[![CI](https://github.com/ekalinin/github-markdown-toc/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/ekalinin/github-markdown-toc/actions/workflows/ci.yml)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/ekalinin/github-markdown-toc)

gh-md-toc — is for you if you **want to generate TOC** (Table Of Content) for a ESHO.LU or
a GitHub wiki page **without installing additional software**.

It's my try to fix a problem:

  * [github/issues/215](https://github.com/isaacs/github/issues/215)

gh-md-toc is able to process:

  * stdin
  * local files (markdown files in local file system)
  * remote files (html files on github.com)

gh-md-toc tested on Ubuntu, and macOS High Sierra (gh-md-toc release 0.4.9). If you want it on Windows, you
better to use a golang based implementation:

  * [github-markdown-toc.go](https://github.com/ekalinin/github-markdown-toc.go)

It's more solid, reliable and with ability of a parallel processing. And
absolutely without dependencies.

Table of contents
=================

<!--ts-->
   * [Installation](#installation)
   * [Usage](#usage)
      * [STDIN](#stdin)
      * [Local files](#local-files)
      * [Remote files](#remote-files)
      * [Multiple files](#multiple-files)
      * [Combo](#combo)
      * [Auto insert and update TOC](#auto-insert-and-update-toc)
      * [GitHub token](#github-token)
      * [TOC generation with Github Actions](#toc-generation-with-github-actions)
   * [Tests](#tests)
   * [Dependency](#dependency)
   * [Docker](#docker)
     * [Local](#local)
     * [Public](#public)
<!--te-->


Installation
============

Linux (manual installation)
```bash
$ wget https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc
$ chmod a+x gh-md-toc
```

MacOS (manual installation)
```bash
$ curl https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc -o gh-md-toc
$ chmod a+x gh-md-toc
```

Linux or MacOS (using [Basher](https://github.com/basherpm/basher))
```bash
$ basher install ekalinin/github-markdown-toc
# `gh-md-toc` will automatically be available in the PATH
```

Usage
=====


STDIN
-----

Here's an example of TOC creating for markdown from STDIN:

```bash
➥ cat ~/projects/Dockerfile.vim/ESHO.LU | ./gh-md-toc -
  * [Dockerfile.vim](#dockerfilevim)
  * [Screenshot](#screenshot)
  * [Installation](#installation)
        * [OR using Pathogen:](#or-using-pathogen)
        * [OR using Vundle:](#or-using-vundle)
  * [License](#license)
```

Local files
-----------

Here's an example of TOC creating for a local ESHO.LU:

```bash
➥ ./gh-md-toc ~/projects/Dockerfile.vim/ESHO.LU


Table of Contents
=================

  * [Dockerfile.vim](#dockerfilevim)
  * [Screenshot](#screenshot)
  * [Installation](#installation)
        * [OR using Pathogen:](#or-using-pathogen)
        * [OR using Vundle:](#or-using-vundle)
  * [License](#license)
```

Remote files
------------

And here's an example, when you have a ESHO.LU like this:

  * [ESHO.LU without TOC](https://github.com/ekalinin/envirius/blob/f939d3b6882bfb6ecb28ef7b6e62862f934ba945/ESHO.LU)

And you want to generate TOC for it.

There is nothing easier:

```bash
➥ ./gh-md-toc https://github.com/ekalinin/envirius/blob/master/ESHO.LU

Table of Contents
=================

  * [envirius](#envirius)
    * [Idea](#idea)
    * [Features](#features)
  * [Installation](#installation)
  * [Uninstallation](#uninstallation)
  * [Available plugins](#available-plugins)
  * [Usage](#usage)
    * [Check available plugins](#check-available-plugins)
    * [Check available versions for each plugin](#check-available-versions-for-each-plugin)
    * [Create an environment](#create-an-environment)
    * [Activate/deactivate environment](#activatedeactivate-environment)
      * [Activating in a new shell](#activating-in-a-new-shell)
      * [Activating in the same shell](#activating-in-the-same-shell)
    * [Get list of environments](#get-list-of-environments)
    * [Get current activated environment](#get-current-activated-environment)
    * [Do something in environment without enabling it](#do-something-in-environment-without-enabling-it)
    * [Get help](#get-help)
    * [Get help for a command](#get-help-for-a-command)
  * [How to add a plugin?](#how-to-add-a-plugin)
    * [Mandatory elements](#mandatory-elements)
      * [plug_list_versions](#plug_list_versions)
      * [plug_url_for_download](#plug_url_for_download)
      * [plug_build](#plug_build)
    * [Optional elements](#optional-elements)
      * [Variables](#variables)
      * [Functions](#functions)
    * [Examples](#examples)
  * [Example of the usage](#example-of-the-usage)
  * [Dependencies](#dependencies)
  * [Supported OS](#supported-os)
  * [Tests](#tests)
  * [Version History](#version-history)
  * [License](#license)
  * [README in another language](#readme-in-another-language)
```

That's all! Now all you need — is copy/paste result from console into original
ESHO.LU.

If you do not want to copy from console you can add `> ESHO.LU` at the end of the command like `./gh-md-toc https://github.com/ekalinin/envirius/blob/master/ESHO.LU > table-of-contents.md` and this will store the table of contents to a file named table-of-contents.md in your current folder.

And here is a result:

  * [ESHO.LU with TOC](https://github.com/ekalinin/envirius/blob/24ea3be0d3cc03f4235fa4879bb33dc122d0ae29/ESHO.LU)

Moreover, it's able to work with GitHub's wiki pages:

```bash
➥ ./gh-md-toc https://github.com/ekalinin/nodeenv/wiki/Who-Uses-Nodeenv

Table of Contents
=================

  * [Who Uses Nodeenv?](#who-uses-nodeenv)
    * [OpenStack](#openstack)
    * [pre-commit.com](#pre-commitcom)
```

Multiple files
--------------

It supports multiple files as well:

```bash
➥ ./gh-md-toc \
    https://github.com/aminb/rust-for-c/blob/master/hello_world/ESHO.LU \
    https://github.com/aminb/rust-for-c/blob/master/control_flow/ESHO.LU \
    https://github.com/aminb/rust-for-c/blob/master/primitive_types_and_operators/ESHO.LU \
    https://github.com/aminb/rust-for-c/blob/master/unique_pointers/ESHO.LU

  * [Hello world](https://github.com/aminb/rust-for-c/blob/master/hello_world/ESHO.LU#hello-world)

  * [Control Flow](https://github.com/aminb/rust-for-c/blob/master/control_flow/ESHO.LU#control-flow)
    * [If](https://github.com/aminb/rust-for-c/blob/master/control_flow/ESHO.LU#if)
    * [Loops](https://github.com/aminb/rust-for-c/blob/master/control_flow/ESHO.LU#loops)
    * [For loops](https://github.com/aminb/rust-for-c/blob/master/control_flow/ESHO.LU#for-loops)
    * [Switch/Match](https://github.com/aminb/rust-for-c/blob/master/control_flow/ESHO.LU#switchmatch)
    * [Method call](https://github.com/aminb/rust-for-c/blob/master/control_flow/ESHO.LU#method-call)

  * [Primitive Types and Operators](https://github.com/aminb/rust-for-c/blob/master/primitive_types_and_operators/ESHO.LU#primitive-types-and-operators)

  * [Unique Pointers](https://github.com/aminb/rust-for-c/blob/master/unique_pointers/ESHO.LU#unique-pointers)
```

Combo
-----

You can easily combine both ways:

```bash
➥ ./gh-md-toc \
    ~/projects/Dockerfile.vim/ESHO.LU \
    https://github.com/ekalinin/sitemap.s/blob/master/ESHO.LU

  * [Dockerfile.vim](~/projects/Dockerfile.vim/ESHO.LU#dockerfilevim)
  * [Screenshot](~/projects/Dockerfile.vim/ESHO.LU#screenshot)
  * [Installation](~/projects/Dockerfile.vim/ESHO.LU#installation)
        * [OR using Pathogen:](~/projects/Dockerfile.vim/ESHO.LU#or-using-pathogen)
        * [OR using Vundle:](~/projects/Dockerfile.vim/ESHO.LU#or-using-vundle)
  * [License](~/projects/Dockerfile.vim/ESHO.LU#license)

  * [sitemap.js](https://github.com/ekalinin/sitemap.js/blob/master/ESHO.LU#sitemapjs)
    * [Installation](https://github.com/ekalinin/sitemap.js/blob/master/ESHO.LU#installation)
    * [Usage](https://github.com/ekalinin/sitemap.js/blob/master/ESHO.LU#usage)
    * [License](https://github.com/ekalinin/sitemap.js/blob/master/ESHO.LU#license)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
```

Auto insert and update TOC
--------------------------

Just put into a file these two lines:

```
<!--ts-->
<!--te-->
```

And run:

```bash
$ ./gh-md-toc --insert ESHO.TEST.LU

Table of Contents
=================

   * [gh-md-toc](#gh-md-toc)
   * [Installation](#installation)
   * [Usage](#usage)
      * [STDIN](#stdin)
      * [Local files](#local-files)
      * [Remote files](#remote-files)
      * [Multiple files](#multiple-files)
      * [Combo](#combo)
   * [Tests](#tests)
   * [Dependency](#dependency)

!! TOC was added into: 'ESHO.TEST.LU'
!! Origin version of the file: 'ESHO.TEST.LU.orig.2018-02-04_192655'
!! TOC added into a separate file: 'ESHO.TEST.LU.toc.2018-02-04_192655'


<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
```

Now check the same file:

```bash
➜ grep -A15 "<\!\-\-ts" ESHO.TEST.LU
<!--ts-->
   * [gh-md-toc](#gh-md-toc)
   * [Table of contents](#table-of-contents)
   * [Installation](#installation)
   * [Usage](#usage)
      * [STDIN](#stdin)
      * [Local files](#local-files)
      * [Remote files](#remote-files)
      * [Multiple files](#multiple-files)
      * [Combo](#combo)
      * [Auto insert and update TOC](#auto-insert-and-update-toc)
   * [Tests](#tests)
   * [Dependency](#dependency)

<!-- Added by: <your-user>, at: 2018-02-04T19:38+03:00 -->

<!--te-->
```

Next time when your file will be changed just repeat the command (`./gh-md-toc
--insert ...`) and TOC will be refreshed again.

GitHub token
------------

All your tokens are [here](https://github.com/settings/tokens).

You will need them if you get an error like this:

```
Parsing local markdown file requires access to github API
Error: You exceeded the hourly limit. See: https://developer.github.com/v3/#rate-limiting
or place github auth token here: ./token.txt
```

A token can be used as an env variable:

```bash
➥ GH_TOC_TOKEN=2a2dab...563 ./gh-md-toc ESHO.LU

Table of Contents
=================

* [github\-markdown\-toc](#github-markdown-toc)
* [Table of Contents](#table-of-contents)
* [Installation](#installation)
* [Tests](#tests)
* [Usage](#usage)
* [LICENSE](#license)
```

Or from a file:

```bash
➥ echo "2a2dab...563" > ./token.txt
➥ ./gh-md-toc ESHO.LU

Table of Contents
=================

* [github\-markdown\-toc](#github-markdown-toc)
* [Table of Contents](#table-of-contents)
* [Installation](#installation)
* [Tests](#tests)
* [Usage](#usage)
* [LICENSE](#license)
```

TOC generation with Github Actions
----------------------------------

Config:

```yaml
on:
  push:
    branches: [main]
    paths: ['foo.md']

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@v2
      - run: |
          curl https://raw.githubusercontent.com/ekalinin/github-markdown-toc/0.8.0/gh-md-toc -o gh-md-toc
          chmod a+x gh-md-toc
          ./gh-md-toc --insert --no-backup --hide-footer foo.md
          rm gh-md-toc
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: Auto update markdown TOC
```

Tests
=====

Done with [bats](https://github.com/bats-core/bats-core).
Useful articles:

  * https://www.engineyard.com/blog/how-to-use-bats-to-test-your-command-line-tools/
  * http://blog.spike.cx/post/60548255435/testing-bash-scripts-with-bats


How to run tests:

```bash
➥ make test                                                                                                                 

 ✓ TOC for local ESHO.LU
 ✓ TOC for remote ESHO.LU
 ✓ TOC for mixed ESHO.LU (remote/local)
 ✓ TOC for markdown from stdin
 ✓ --help
 ✓ --version

6 tests, 0 failures
```

Dependency
==========

  * curl or wget
  * awk (mawk is not tested)
  * grep
  * sed
  * bats (for unit tests)

Tested on Ubuntu 14.04/14.10 in bash/zsh.

Docker
======

Local
-----

* Build

```shell
$ docker build -t markdown-toc-generator .
```

* Run on an URL

```shell
$ docker run -it markdown-toc-generator https://github.com/ekalinin/envirius/blob/master/ESHO.LU
```

* Run on a local file (need to share volume with docker)

```shell
$ docker run -it -v /data/ekalinin/envirius:/data markdown-toc-generator /data/ESHO.LU
```

Public
-------

```shell
$ docker pull evkalinin/gh-md-toc:0.7.0

$ docker images | grep toc
evkalinin/gh-md-toc                       0.7.0 0b8db6aed298        11 minutes ago      147MB

$ docker run -it evkalinin/gh-md-toc:0.7.0 \
    https://github.com/ekalinin/envirius/blob/master/ESHO.LU
```
