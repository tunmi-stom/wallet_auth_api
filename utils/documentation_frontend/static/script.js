const BASE = 'https://wallet-auth-api.onrender.com';

function scrollTo(id) {
  document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}

function toggle(id) {
  var num = id.slice(-1);
  var bdy = document.getElementById('bdy' + num);
  var tgl = document.getElementById('tgl' + num);
  var hdr = document.getElementById('hdr' + num);
  var open = bdy.style.display !== 'none';
  bdy.style.display = open ? 'none' : 'block';
  tgl.classList.toggle('open', !open);
  hdr.classList.toggle('collapsed', open);
}

function switchTab(btn, show, hide) {
  btn.parentElement.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById(show).style.display = 'block';
  document.getElementById(hide).style.display = 'none';
}

function cp(btn) {
  var block = btn.nextElementSibling;
  if (block.style.display === 'none') block = block.nextElementSibling;
  navigator.clipboard.writeText(block.innerText).then(() => {
    btn.textContent = 'copied!';
    setTimeout(() => btn.textContent = 'copy', 1500);
  }).catch(() => {});
}

function fmt(obj) {
  return JSON.stringify(obj, null, 2)
    .replace(/"([^"]+)":/g, '<span class="k">"$1"</span>:')
    .replace(/: "([^"]*)"/g, ': <span class="s">"$1"</span>')
    .replace(/: (\d+)/g, ': <span class="n">$1</span>');
}

async function call(btnId, resId, outId, url, opts) {
  var btn = document.getElementById(btnId);
  var res = document.getElementById(resId);
  var out = document.getElementById(outId);
  btn.disabled = true;
  btn.textContent = '... Sending';
  res.style.display = 'block';
  out.innerHTML = '<span style="color:var(--text3)">Waiting for response…</span>';
  try {
    var r = await fetch(url, opts);
    const text = await r.text();

    let data;
    try {
      data = JSON.parse(text);
    } catch {
      data = { raw: text || "No response body" };
    }
    var statusClass = r.ok ? 'ok' : (r.status === 422 ? 'warn' : 'err');
    out.innerHTML = '<span class="badge-inline ' + statusClass + '" style="font-size:11px;padding:2px 8px;border-radius:4px;margin-bottom:8px;display:inline-block">' + r.status + (r.ok ? ' OK' : '') + '</span>\n\n' + fmt(data);
  } catch (e) {
    out.innerHTML =
  '<span class="badge-inline ' + statusClass +
  '" style="font-size:11px;padding:2px 8px;border-radius:4px;margin-bottom:8px;display:inline-block">' +
  r.status + (r.ok ? ' OK' : '') +
  '</span>\n\n' + fmt(data);
  }
  btn.disabled = false;
  btn.textContent = 'Send';
}

function tryHome() {
  call('h-btn', 'h-res', 'h-out', BASE + '/', {});
}
function tryNonce() {
  call('n-btn', 'n-res', 'n-out', BASE + '/auth/nonce', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      address: document.getElementById('n-addr').value,
      chain_id: parseInt(document.getElementById('n-chain').value) || 1
    })
  });
}
function tryVerify() {
  call('v-btn', 'v-res', 'v-out', BASE + '/auth/verify', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      address: document.getElementById('v-addr').value,
      chain_id: parseInt(document.getElementById('v-chain').value) || 1,
      signature: document.getElementById('v-sig').value
    })
  });
}