from pathlib import Path

base = Path('media/produtos')
base.mkdir(parents=True, exist_ok=True)
files = {
    'vestido_floral.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="560" viewBox="0 0 700 560">
  <defs>
    <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f6e5df"/>
      <stop offset="100%" stop-color="#f2e9f1"/>
    </linearGradient>
  </defs>
  <rect width="700" height="560" fill="url(#g1)"/>
  <g transform="translate(140,120)">
    <path d="M60 50 Q130 -20 200 50 L220 300 Q140 330 60 300 Z" fill="#f3c6c0" stroke="#d38d88" stroke-width="8"/>
    <path d="M200 50 Q260 20 320 50 L300 300 Q240 330 200 300 Z" fill="#f8e2d7" stroke="#d38d88" stroke-width="8"/>
    <circle cx="150" cy="140" r="26" fill="#ffb8b0"/>
    <circle cx="90" cy="170" r="18" fill="#ffd8d2"/>
    <circle cx="210" cy="190" r="18" fill="#ffd8d2"/>
  </g>
  <text x="350" y="450" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="40" fill="#6d4a47">Vestido Floral</text>
  <text x="350" y="494" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="22" fill="#8f6a6a">feminino delicado</text>
</svg>''',
    'camiseta_basica.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="560" viewBox="0 0 700 560">
  <defs>
    <linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#eaf4ff"/>
      <stop offset="100%" stop-color="#d8f0ff"/>
    </linearGradient>
  </defs>
  <rect width="700" height="560" fill="url(#g2)"/>
  <g transform="translate(120,100)">
    <path d="M80 50 L120 20 L200 20 L240 50 L260 120 L260 320 Q180 360 100 320 Z" fill="#ffffff" stroke="#8cbcd6" stroke-width="10"/>
    <path d="M80 50 Q110 60 120 50" fill="#d0e8ff"/>
    <path d="M240 50 Q210 60 200 50" fill="#d0e8ff"/>
    <circle cx="180" cy="220" r="46" fill="#cde6f7"/>
  </g>
  <text x="350" y="450" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="40" fill="#446f8d">Camiseta Básica</text>
  <text x="350" y="494" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="22" fill="#5f82a2">conforto diário</text>
</svg>''',
    'short_jeans.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="560" viewBox="0 0 700 560">
  <defs>
    <linearGradient id="g3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f2f4f8"/>
      <stop offset="100%" stop-color="#dce3ea"/>
    </linearGradient>
  </defs>
  <rect width="700" height="560" fill="url(#g3)"/>
  <g transform="translate(150,120)">
    <path d="M60 80 C 80 10 140 10 160 80 L170 320 Q120 360 70 320 Z" fill="#7f9ebd" stroke="#5f7d9a" stroke-width="8"/>
    <path d="M160 80 C 180 10 240 10 260 80 L250 320 Q200 360 150 320 Z" fill="#5981bc" stroke="#4d6d91" stroke-width="8"/>
    <path d="M100 170 L120 180 L180 180 L200 170" stroke="#3f5c80" stroke-width="8" fill="none"/>
    <path d="M120 260 L130 290" stroke="#3f5c80" stroke-width="8"/>
    <path d="M220 260 L210 290" stroke="#3f5c80" stroke-width="8"/>
  </g>
  <text x="350" y="450" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="40" fill="#314969">Short Jeans</text>
  <text x="350" y="494" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="22" fill="#5f7091">casual premium</text>
</svg>''',
    'sandalia_rasteira.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="560" viewBox="0 0 700 560">
  <defs>
    <linearGradient id="g4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f9f1e8"/>
      <stop offset="100%" stop-color="#f7e6dc"/>
    </linearGradient>
  </defs>
  <rect width="700" height="560" fill="url(#g4)"/>
  <g transform="translate(140,180)">
    <path d="M100 80 C120 30 180 30 200 80 L290 100 Q310 260 120 260 Z" fill="#e4b08b" stroke="#b97f5f" stroke-width="9"/>
    <path d="M190 100 L220 70" stroke="#ad7a5f" stroke-width="18" stroke-linecap="round"/>
    <path d="M160 120 L210 90" stroke="#d3a07d" stroke-width="14" stroke-linecap="round"/>
  </g>
  <text x="350" y="450" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="40" fill="#7e5a48">Sandália Rasteira</text>
  <text x="350" y="494" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="22" fill="#9c7a62">pronta para o verão</text>
</svg>''',
    'conjunto_infantil.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="560" viewBox="0 0 700 560">
  <defs>
    <linearGradient id="g5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f4f7ff"/>
      <stop offset="100%" stop-color="#e5eeff"/>
    </linearGradient>
  </defs>
  <rect width="700" height="560" fill="url(#g5)"/>
  <g transform="translate(140,120)">
    <path d="M90 90 C110 20 180 20 210 90 L220 210 Q175 260 130 210 Z" fill="#ffd8e0" stroke="#f5b5c4" stroke-width="8"/>
    <path d="M170 90 C190 20 260 20 290 90 L300 210 Q255 260 210 210 Z" fill="#ffe8af" stroke="#f0c482" stroke-width="8"/>
    <circle cx="200" cy="320" r="64" fill="#b5d9fe"/>
    <circle cx="260" cy="320" r="64" fill="#f5b3ed"/>
  </g>
  <text x="350" y="450" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="40" fill="#5d74b1">Conjunto Infantil</text>
  <text x="350" y="494" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="22" fill="#7b8fbd">acolhedor e alegre</text>
</svg>''',
    'jaqueta_jeans.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="560" viewBox="0 0 700 560">
  <defs>
    <linearGradient id="g6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e8eef7"/>
      <stop offset="100%" stop-color="#d5e2ef"/>
    </linearGradient>
  </defs>
  <rect width="700" height="560" fill="url(#g6)"/>
  <g transform="translate(120,120)">
    <path d="M90 70 L150 20 L240 20 L300 70 L320 210 Q250 280 180 210 Z" fill="#6c8db1" stroke="#4d6e91" stroke-width="10"/>
    <path d="M170 180 L170 260" stroke="#3f5c77" stroke-width="14"/>
    <path d="M220 180 L220 260" stroke="#3f5c77" stroke-width="14"/>
    <circle cx="195" cy="110" r="12" fill="#e7f5ff"/>
  </g>
  <text x="350" y="450" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="40" fill="#3f5d82">Jaqueta Jeans</text>
  <text x="350" y="494" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="22" fill="#607196">corte impecável</text>
</svg>''',
    'blusa_de_trico.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="560" viewBox="0 0 700 560">
  <defs>
    <linearGradient id="g7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff1e8"/>
      <stop offset="100%" stop-color="#f4d8cd"/>
    </linearGradient>
  </defs>
  <rect width="700" height="560" fill="url(#g7)"/>
  <g transform="translate(140,110)">
    <path d="M90 70 C120 20 180 20 210 70 L230 240 Q190 300 120 240 Z" fill="#d9a591" stroke="#b0725f" stroke-width="10"/>
    <path d="M210 70 C240 20 300 20 330 70 L350 240 Q310 300 240 240 Z" fill="#f2c8b2" stroke="#b0725f" stroke-width="10"/>
    <path d="M140 160 C160 140 230 140 250 160" stroke="#c38e81" stroke-width="16" fill="none"/>
  </g>
  <text x="350" y="450" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="40" fill="#8a5d50">Blusa de Tricô</text>
  <text x="350" y="494" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="22" fill="#a57a6d">aconchegante</text>
</svg>''',
    'tenis_casual.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="560" viewBox="0 0 700 560">
  <defs>
    <linearGradient id="g8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#eff8ef"/>
      <stop offset="100%" stop-color="#d9efdb"/>
    </linearGradient>
  </defs>
  <rect width="700" height="560" fill="url(#g8)"/>
  <g transform="translate(140,180)">
    <path d="M80 120 C120 80 240 80 280 120 Q340 170 300 220 L120 220 Z" fill="#b0d1b1" stroke="#7ca07f" stroke-width="12"/>
    <path d="M120 190 C140 170 180 160 220 170" stroke="#fff" stroke-width="12" fill="none"/>
    <path d="M160 205 L170 188" stroke="#fff" stroke-width="10"/>
    <path d="M210 205 L220 188" stroke="#fff" stroke-width="10"/>
  </g>
  <text x="350" y="450" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="40" fill="#4a7a56">Tênis Casual</text>
  <text x="350" y="494" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="22" fill="#6c8f6f">design elegante</text>
</svg>''',
    'vestido_infantil.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="560" viewBox="0 0 700 560">
  <defs>
    <linearGradient id="g9" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f9ecff"/>
      <stop offset="100%" stop-color="#f2d7ff"/>
    </linearGradient>
  </defs>
  <rect width="700" height="560" fill="url(#g9)"/>
  <g transform="translate(130,120)">
    <path d="M90 80 Q130 10 190 80 L230 110 Q210 260 150 300 90 260 70 110 Z" fill="#f6c8eb" stroke="#d69bd1" stroke-width="10"/>
    <path d="M190 80 Q230 10 290 80 L270 110 Q250 260 190 300 130 260 110 110 Z" fill="#f2d2f6" stroke="#d69bd1" stroke-width="10"/>
    <path d="M140 250 C170 230 220 230 250 250" stroke="#e8b7db" stroke-width="16" fill="none"/>
  </g>
  <text x="350" y="450" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="40" fill="#9c5d9c">Vestido Infantil</text>
  <text x="350" y="494" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="22" fill="#b184b6">fofo e delicado</text>
</svg>''',
    'bolsa_tiracolo.svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="560" viewBox="0 0 700 560">
  <defs>
    <linearGradient id="g10" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff7ec"/>
      <stop offset="100%" stop-color="#ffe6cb"/>
    </linearGradient>
  </defs>
  <rect width="700" height="560" fill="url(#g10)"/>
  <g transform="translate(150,160)">
    <path d="M80 120 C120 80 300 80 340 120 L340 220 C340 280 280 320 220 320 C160 320 100 280 100 220 Z" fill="#d4a278" stroke="#b27a53" stroke-width="10"/>
    <path d="M210 120 L210 40" stroke="#b27a53" stroke-width="18" stroke-linecap="round"/>
    <path d="M270 120 L270 40" stroke="#b27a53" stroke-width="18" stroke-linecap="round"/>
    <path d="M180 220 L180 260" stroke="#b27a53" stroke-width="14"/>
    <path d="M260 220 L260 260" stroke="#b27a53" stroke-width="14"/>
  </g>
  <text x="350" y="450" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="40" fill="#8b694f">Bolsa Tiracolo</text>
  <text x="350" y="494" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="22" fill="#9f7d62">sofisticada e prática</text>
</svg>''',
}
for name, content in files.items():
    (base / name).write_text(content, encoding='utf-8')
print('updated', len(files), 'product SVG files')
