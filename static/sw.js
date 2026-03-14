const CACHE_NAME = 'techspire-v1';
const ASSETS = ['/', '/static/css/style.css', '/static/js/main.js', '/static/images/logo.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(ASSETS)));
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});
