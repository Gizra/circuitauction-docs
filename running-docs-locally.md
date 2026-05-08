# Running the Docs Locally

These docs are served with [Docsify](https://docsify.js.org/) — no build step required, the markdown files are rendered in the browser at runtime.

## Prerequisites

- Node.js and npm installed

## Steps

From the repo root, install `docsify-cli` globally and start the local server:

```bash
npm i -g docsify-cli
docsify serve .
```

Then open [http://localhost:3000](http://localhost:3000) in your browser.

{% hint style="info" %}
Files are watched and the browser reloads automatically when you edit a markdown file.
{% endhint %}

## Alternative: any static HTTP server

Since Docsify is fully client-side, any static file server will also work (no live reload):

```bash
# Python
python3 -m http.server 3000

# PHP
php -S localhost:3000
```
