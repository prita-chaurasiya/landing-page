import urllib.request
import re

req = urllib.request.Request('https://ngowebsite.in/ngo-software', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    print('HTML length:', len(html))
    css_links = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', html)
    print('CSS links:', css_links)
    fonts = re.findall(r'fonts\.googleapis\.com[^\'"]+', html)
    print('Fonts:', fonts)
    
    # Save a snippet of head and first sections
    with open('ngowebsite_source.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Saved ngowebsite_source.html')
except Exception as e:
    print('Error:', e)

