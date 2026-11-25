// news-image-20261125 — entrypoint (Node 22, standard library only).
//
// The entry is the finished front page that ships beside this file:
// a newspaper layout for Wednesday 25 November 2026 (masthead, hero
// illustration, six story cards), composed by compose.py from the
// AI-generated hero in assets/ and rendered text.
//
// This program only moves those bytes to the grader's output folder,
// so both runs write an identical entry.png.
//
// Local run:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const IMAGE_NAME = 'entry.png';
const IMAGE_PATH = fileURLToPath(new URL(`./${IMAGE_NAME}`, import.meta.url));

// The grader sets /output; MAKEFUN_OUTPUT_DIR stands in for it locally.
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const image = readFileSync(IMAGE_PATH);

// Refuse to hand the grader a broken file: a PNG must start with its
// eight-byte signature, and the gate caps it at 1 MiB.
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!image.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error(`${IMAGE_NAME} is not a PNG (bad magic bytes)`);
}
if (image.byteLength > 1024 * 1024) {
  throw new Error(`${IMAGE_NAME} is ${image.byteLength} bytes, over the 1 MiB cap`);
}

mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, IMAGE_NAME), image);

console.log(`wrote ${join(outDir, IMAGE_NAME)} (${image.byteLength} bytes)`);
