const https = require('https');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.VENICE_API_KEY || 'VENICE-INFERENCE-KEY-z_7RhuAfMuH7oSEN_E8ASA1nzv4PtglzuoH7yuiLZW';
const MODEL = 'nano-banana-2';

const configPath = process.argv[2];
if (!configPath) {
  console.error('Usage: node generate_batch_nano_banana_2.js <config.json> [output-dir]');
  process.exit(1);
}
const outputDir = process.argv[3] || 'output';

let items;
try {
  items = JSON.parse(fs.readFileSync(configPath, 'utf8'));
} catch (e) {
  console.error('Error reading config:', e.message);
  process.exit(1);
}

function fileExistsNonEmpty(p) {
  try { return fs.existsSync(p) && fs.statSync(p).size > 1024; } catch { return false; }
}

function generateImage(item, index) {
  return new Promise((resolve) => {
    const filePath = path.join(outputDir, `${item.name}.png`);
    if (fileExistsNonEmpty(filePath)) {
      console.log(`⏭️  [${index + 1}/${items.length}] Skipping existing: ${item.name}.png`);
      return resolve({ name: item.name, success: true, skipped: true });
    }

    console.log(`\n[${index + 1}/${items.length}] Generating with ${MODEL}: ${item.name}...`);

    const payload = JSON.stringify({
      model: MODEL,
      prompt: item.prompt,
      resolution: item.resolution || '2K',
      aspect_ratio: item.aspect_ratio || '4:5',
      steps: item.steps || 1,
      cfg_scale: item.cfg_scale || 7.5,
      seed: item.seed || Math.floor(Math.random() * 1000000),
      hide_watermark: false,
      return_binary: false,
      safe_mode: true
    });

    const options = {
      hostname: 'api.venice.ai',
      path: '/api/v1/image/generate',
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(payload)
      },
      timeout: 180000
    };

    const startTime = Date.now();
    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        const duration = ((Date.now() - startTime) / 1000).toFixed(1);
        try {
          const parsed = JSON.parse(data);
          if (parsed.images?.[0]) {
            fs.mkdirSync(outputDir, { recursive: true });
            fs.writeFileSync(filePath, Buffer.from(parsed.images[0], 'base64'));
            console.log(`✅ Saved: ${item.name}.png in ${duration}s`);
            resolve({ name: item.name, success: true });
          } else {
            console.log(`❌ No image for ${item.name}:`, parsed.error || parsed.message || 'Unknown error');
            resolve({ name: item.name, success: false, error: parsed.error || parsed.message || 'Unknown error' });
          }
        } catch (e) {
          console.log(`❌ Parse error for ${item.name}:`, e.message);
          resolve({ name: item.name, success: false, error: e.message });
        }
      });
    });

    req.on('error', e => {
      console.log(`❌ Request error for ${item.name}:`, e.message);
      resolve({ name: item.name, success: false, error: e.message });
    });

    req.on('timeout', () => {
      console.log(`❌ Timeout for ${item.name}`);
      req.destroy();
      resolve({ name: item.name, success: false, error: 'Timeout' });
    });

    req.write(payload);
    req.end();
  });
}

async function main() {
  console.log(`🎨 Venice Batch Image Generator (${MODEL})`);
  console.log('================================');
  console.log(`Total images: ${items.length}`);
  const results = [];
  for (let i = 0; i < items.length; i++) {
    const result = await generateImage(items[i], i);
    results.push(result);
    if (i < items.length - 1) await new Promise(r => setTimeout(r, 1800));
  }
  console.log('\n================================');
  const successCount = results.filter(r => r.success).length;
  const skippedCount = results.filter(r => r.skipped).length;
  console.log(`Done. Success: ${successCount}/${items.length}, skipped existing: ${skippedCount}`);
}

main().catch(err => { console.error(err); process.exit(1); });
