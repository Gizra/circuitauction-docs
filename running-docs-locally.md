# Running the Docs Locally

These docs are served with [Docsify](https://docsify.js.org/) — no build step required, the markdown files are rendered in the browser at runtime.

## Prerequisites

- Node.js and npm installed

## Steps

From the repo root, start the local server with `npx` (no global install needed):

```bash
npx -y docsify-cli serve .
```

Or install `docsify-cli` globally once and run it directly:

```bash
npm i -g docsify-cli
docsify serve .
```

Then open [http://localhost:3000](http://localhost:3000) in your browser.

### Using a different port

If port 3000 is already in use, pass the `-p` flag:

```bash
npx -y docsify-cli serve . -p 3001
```

Then open [http://localhost:3001](http://localhost:3001) instead.

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
