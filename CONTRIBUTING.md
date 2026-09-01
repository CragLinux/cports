# Contributing to astro-cports

> **This is the Astro fork of Chimera's `cports`, not upstream cports.**
> See [`README.md`](README.md) for provenance. Contributions here flow to
> the Astro distribution, not to Chimera. The packaging system, API, and
> the bulk of the templates are Chimera's work under their BSD license
> ([`COPYING.md`](COPYING.md)); please contribute distribution-agnostic
> template fixes to Chimera upstream where their policies allow.

## AI-assisted contributions are welcome here

Unlike upstream, this fork **explicitly welcomes AI-assisted and
AI-authored contributions.** The bar is the work, not the tool that
helped write it. What we require of any contribution, human- or
machine-assisted:

- **You own it.** A human contributor is accountable for every change:
  you understand it, you can defend it in review, and your name is on it.
- **It is verified.** The change builds and, where applicable, boots /
  passes the relevant Astro CI gate. "The AI said so" is not evidence;
  a green build log is. State how you verified it in the PR.
- **It is honest.** Disclose AI involvement if it was substantial, cite
  the sources the analysis rests on (upstream code, manpages, specs),
  and never fabricate reproduction steps or test results.

Contributions that are unverified, that misrepresent testing, or that no
human is prepared to own will be declined — same as any low-quality
change, regardless of how they were produced.

## Getting started

First you will need to fork this repository on GitHub. This is not different
from any other project.

We suggest to avoid using GitHub's web editor for contributions, especially
for templates, since those need testing. Therefore, if you do not know at
least the basics of Git, use some of the public resources to get familiar.

Also read [`USING_GIT.md`](USING_GIT.md) if you are unfamiliar with Git.

Once you have that, clone your fork and prepare the changes.

## Preparing your changes

Whether you are creating a new template or modifying an existing one, you
should follow the manual (see [`Packaging.md`](Packaging.md)) which should be
able to answer all or at least most questions.

Always ensure to follow the expected style and other basics to make the
reviewer's job easier.

## Committing changes

Generally, you should have one commit per template. The commits should be
atomic, i.e. every commit should build on its own. When you have a batch
of templates and they depend on each other, order your commits properly.

Using a correct commit message is also important:

* New packages should use `category/pkgname: new package`. For
  example, `main/coolproject: new package`.
* Updates should similarly use `category/pkgname: update to <version>`.
* Non-update changes to templates should use `category/pkgname: custom message`.
* Removals should use `category/pkgname: remove`.
* Changes to `cbuild` should use `cbuild: custom message`.
* Changes to other parts should use the same format but relating to the thing
  they change, e.g. for `Packaging.md` changes it's `packaging: ...` and so on.
* Changes to multiple things in a category should use `*`, e.g. for `user/foo`
  and `user/bar` changes it's `user/*`, and for a global cleanup `*/*: title`
  may be used.

Commit messages as well as things such as package descriptions should be
written in American English and be grammatically correct.

It is your responsibility to verify that submitted changes do build. If the
CI fails, fix any issues that you are capable of fixing yourself.

## Creating a pull request

Once you have committed your changes, create a GitHub pull request. The best
way to do that is to push your changes into a custom branch. When you `git push`
into that branch, the command line will offer you a link to create your PR.

## Getting review

If there are any issues with your PR, a reviewer will point them out and possibly
suggest changes. Follow any review instructions until the changes are approved.

There is no CLA in Chimera, likewise there is no copyright assignment or any
such thing.

## Getting your changes merged

Congratulations! At this point, your changes should have made them into the
repository. As always, do not hesitate to join us in one of our communication
channels if anything is unclear.
