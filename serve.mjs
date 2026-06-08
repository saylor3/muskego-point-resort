// serve.mjs — zero-dependency static file server for local preview.
// Serves the project root at http://localhost:3000
// Usage: node serve.mjs   (optionally PORT=4000 node serve.mjs)

import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { join, extname, normalize, sep } from 'node:path';

const ROOT = process.cwd();
const PORT = process.env.PORT || 3000;

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.mp4': 'video/mp4',
  '.webm': 'video/webm',
};

const server = createServer(async (req, res) => {
  try {
    let urlPath = decodeURIComponent(
      new URL(req.url, `http://localhost:${PORT}`).pathname
    );
    if (urlPath.endsWith('/')) urlPath += 'index.html';

    let filePath = normalize(join(ROOT, urlPath));
    // Prevent path traversal outside the project root.
    if (filePath !== ROOT && !filePath.startsWith(ROOT + sep)) {
      res.writeHead(403);
      res.end('Forbidden');
      return;
    }

    try {
      const s = await stat(filePath);
      if (s.isDirectory()) filePath = join(filePath, 'index.html');
    } catch {
      // fall through to readFile, which will 404
    }

    const data = await readFile(filePath);
    res.writeHead(200, {
      'Content-Type': MIME[extname(filePath).toLowerCase()] || 'application/octet-stream',
      'Cache-Control': 'no-store',
    });
    res.end(data);
  } catch {
    res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end('<h1>404 Not Found</h1>');
  }
});

server.listen(PORT, () => {
  console.log(`Serving ${ROOT}`);
  console.log(`→ http://localhost:${PORT}`);
});
