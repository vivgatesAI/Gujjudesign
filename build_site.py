import json, os, textwrap

styles = [
  {"id":1,"name":"Pithora Painting","category":"Folk & Painting Traditions","desc":"Ritual painting tradition of the Rathwa and related communities, known for horse motifs, deities, narrative bands, and ceremonial symbolism.","prompt":"Incorporate Gujarat Pithora painting aesthetics: ritual folk mural composition, stylized horses, deities, dotted decorative bands, earthy pigments, ceremonial symbolism, dense narrative layout, handcrafted tribal energy."},
  {"id":2,"name":"Mata ni Pachedi","category":"Folk & Painting Traditions","desc":"Temple cloth painting tradition with sacred figures, shrine-like layouts, red-black-white palette, and devotional storytelling.","prompt":"Use Mata ni Pachedi style from Gujarat: temple-cloth composition, hand-painted sacred iconography, shrine framing, red black and white palette, devotional symmetry, folk textile illustration."},
  {"id":3,"name":"Warli Painting","category":"Folk & Painting Traditions","desc":"Minimal tribal painting language using geometric human figures, village scenes, and rhythmic circular movement; included here through South Gujarat influence.","prompt":"Apply South Gujarat-influenced Warli style: minimal tribal mural art, white geometric stick figures, village life scenes, circular dance motifs, mud-wall backdrop, simple symbolic storytelling."},
  {"id":4,"name":"Tribal Wall Painting (Rathwa / Bhil)","category":"Folk & Painting Traditions","desc":"Regional wall art featuring local symbols, animals, gods, geometric bands, and celebratory color.","prompt":"Use Gujarat tribal wall painting aesthetics inspired by Rathwa and Bhil traditions: vivid folk mural, animals, sacred symbols, geometric borders, flat colors, handmade wall-art texture."},
  {"id":5,"name":"Sanjhi-style Ritual Floor/Wall Art","category":"Folk & Painting Traditions","desc":"Ephemeral ritual art with cutwork or powdered patterns adapted into regional floor and wall compositions.","prompt":"Incorporate Gujarati ritual floor and wall art inspired by Sanjhi-style patterning: intricate stencil-like symmetry, devotional motifs, radial floral geometry, handcrafted ceremonial detail."},
  {"id":6,"name":"Bandhani (Bandhej Tie-Dye)","category":"Textile & Surface Design Traditions","desc":"Iconic resist-dyed textile tradition using tied dots, fields, circles, and symbolic patterning in vibrant colorways.","prompt":"Use Gujarat Bandhani design language: tie-dye dot clusters, concentric resist patterns, vibrant festive colors, fine textile grain, handcrafted bandhej rhythm, celebratory surface design."},
  {"id":7,"name":"Leheriya","category":"Textile & Surface Design Traditions","desc":"Wave-pattern resist dye aesthetic featuring diagonal ripples and fluid chromatic motion.","prompt":"Incorporate Gujarati Leheriya-inspired textile aesthetics: flowing diagonal wave bands, tie-dye softness, rhythmic stripes, festive color gradients, handcrafted resist-dye texture."},
  {"id":8,"name":"Patola (Double Ikat Weaving)","category":"Textile & Surface Design Traditions","desc":"Highly prized double ikat silk tradition with jewel-like symmetry, geometric precision, and complex woven motifs.","prompt":"Use Gujarat Patola double-ikat aesthetics: jewel-toned symmetry, geometric precision, woven motif grids, rich silk sensibility, ceremonial luxury, crisp repeating pattern language."},
  {"id":9,"name":"Single Ikat (Rajkot Ikat)","category":"Textile & Surface Design Traditions","desc":"A softer ikat tradition with blurred resist-dyed edges and woven rhythmic geometry.","prompt":"Apply Rajkot Ikat style from Gujarat: softly feathered ikat edges, woven geometric repeats, elegant textile rhythm, artisanal resist-dye character, balanced heritage palette."},
  {"id":10,"name":"Ajrakh Block Printing","category":"Textile & Surface Design Traditions","desc":"Complex block-printed textile art with indigo, madder, black, symmetry, and star-floral geometry.","prompt":"Use Gujarat Ajrakh aesthetics: intricate hand block print, indigo madder black palette, star geometry, floral medallions, layered natural-dye look, precise symmetrical repeats."},
  {"id":11,"name":"Batik (Gujarat adaptation)","category":"Textile & Surface Design Traditions","desc":"Wax-resist textile art adapted into local color sensibilities and decorative patterning.","prompt":"Incorporate Gujarat-adapted batik style: wax-resist crackle texture, layered dye fields, flowing textile motifs, artisanal handcrafted surface, rich decorative composition."},
  {"id":12,"name":"Rogan Painting","category":"Textile & Surface Design Traditions","desc":"Rare cloth-painting tradition using castor-oil-based paste to create raised, ornamental, often symmetrical imagery.","prompt":"Use Gujarat Rogan painting aesthetics: ornate flowing floral-tree motifs, raised paint feel, mirrored composition, luminous cloth surface, detailed hand-drawn ornamentation."},
  {"id":13,"name":"Kalamkari (Gujarat trade-influenced variant)","category":"Textile & Surface Design Traditions","desc":"Narrative cloth art with pen-drawn floral and figurative detail, adapted through regional trade and influence.","prompt":"Apply Gujarat-influenced Kalamkari aesthetics: hand-drawn textile storytelling, floral vines, figurative linework, natural dye feel, ornate borders, heritage narrative composition."},
  {"id":14,"name":"Mashru Weaving","category":"Textile & Surface Design Traditions","desc":"Glossy striped woven textile combining silk-like sheen with cotton comfort, often featuring saturated bands.","prompt":"Use Gujarat Mashru weaving inspiration: lustrous striped textile, satin sheen, bold color bands, woven luxury, historical garment sensibility, rhythmic linear elegance."},
  {"id":15,"name":"Tangaliya Weaving","category":"Textile & Surface Design Traditions","desc":"Distinctive dot-weave textile with raised bead-like patterning embedded in the cloth.","prompt":"Incorporate Tangaliya weaving from Gujarat: dotted bead-like woven texture, raised pattern clusters, handcrafted pastoral textile, earthy modern geometry, tactile woven detail."},
  {"id":16,"name":"Vankar Weaving","category":"Textile & Surface Design Traditions","desc":"Handloom weaving heritage associated with traditional community knowledge, utility, and regional pattern sensibility.","prompt":"Use Gujarat Vankar weaving aesthetics: handloom texture, understated stripes and checks, artisan-woven structure, heritage cloth sensibility, tactile thread character."},
  {"id":17,"name":"Khadi","category":"Textile & Surface Design Traditions","desc":"Handspun, handwoven textile emphasizing texture, material honesty, and understated craft beauty.","prompt":"Apply Gujarat khadi aesthetics: handspun irregular texture, breathable woven plain, natural fiber softness, minimalist craft honesty, subtle artisanal slub detail."},
  {"id":18,"name":"Zari Embroidery","category":"Textile & Surface Design Traditions","desc":"Metal-thread embellishment creating luminous ornament, borders, and ceremonial richness.","prompt":"Use Gujarat zari embroidery style: metallic thread shimmer, ceremonial floral borders, luxurious ornament, fine detailing, festive textile richness, regal craft finish."},
  {"id":19,"name":"Aari Embroidery","category":"Textile & Surface Design Traditions","desc":"Hook-based embroidery known for fluid curving motifs, florals, and continuous stitched flow.","prompt":"Incorporate Gujarat Aari embroidery: fluid hook-stitched floral scrolls, graceful curves, dense ornamental fills, textile elegance, refined handcrafted detailing."},
  {"id":20,"name":"Mochi Embroidery","category":"Textile & Surface Design Traditions","desc":"Fine chain-stitch embroidery associated with leatherwork and textiles, often richly patterned.","prompt":"Use Gujarat Mochi embroidery aesthetics: intricate chain-stitch craftsmanship, dense floral motifs, artisan precision, colorful threadwork, heritage luxury textile detailing."},
  {"id":21,"name":"Kutch Embroidery","category":"Textile & Surface Design Traditions","desc":"Broad umbrella term covering richly diverse embroidery traditions from Kutch, often bold, mirrored, and highly tactile.","prompt":"Apply Kutch embroidery aesthetics from Gujarat: vivid threads, mirror accents, bold folk motifs, dense handcrafted surfaces, celebratory textile richness, artisan patch-like detail."},
  {"id":22,"name":"Rabari Embroidery","category":"Textile & Surface Design Traditions","desc":"Pastoral embroidery tradition with mirrors, strong motifs, and vibrant narrative craft identity.","prompt":"Use Rabari embroidery style from Gujarat: bold mirror work, vibrant thread motifs, nomadic pastoral ornament, dense handcrafted texture, striking folk textile character."},
  {"id":23,"name":"Ahir Embroidery","category":"Textile & Surface Design Traditions","desc":"Embroidery tradition known for curving lines, floral forms, and bright compositional movement.","prompt":"Incorporate Gujarat Ahir embroidery: flowing floral motifs, bright thread palette, graceful curvilinear stitching, mirror highlights, folk elegance, richly embellished textile surface."},
  {"id":24,"name":"Sodha Rajput Embroidery","category":"Textile & Surface Design Traditions","desc":"Refined embroidery with geometric order, vivid contrasts, and stately handcrafted beauty.","prompt":"Use Gujarat Sodha Rajput embroidery aesthetics: structured geometric motifs, bright thread contrasts, mirrored accents, aristocratic folk craft, detailed textile surface."},
  {"id":25,"name":"Meghwal Embroidery","category":"Textile & Surface Design Traditions","desc":"Embroidery associated with strong color, geometric fields, and community-specific motif vocabularies.","prompt":"Apply Meghwal embroidery style from Gujarat: vibrant geometric stitched motifs, strong color blocks, folk symbolism, handcrafted density, textile ornament with cultural character."},
  {"id":26,"name":"Mutwa Embroidery","category":"Textile & Surface Design Traditions","desc":"Exceptionally fine micro-embroidery with extraordinary precision and small-scale geometric detailing.","prompt":"Use Gujarat Mutwa embroidery aesthetics: ultra-fine micro-stitch detail, miniature geometric precision, delicate mirror highlights, jewel-like textile craftsmanship, intricate handcrafted refinement."},
  {"id":27,"name":"Soof Embroidery","category":"Textile & Surface Design Traditions","desc":"Counted-thread geometric embroidery producing elegant angular forms and highly structured pattern logic.","prompt":"Incorporate Gujarat Soof embroidery: counted-thread geometry, angular motifs, precise symmetrical structure, fine handcrafted textile precision, restrained yet intricate folk design."},
  {"id":28,"name":"Pakko Embroidery","category":"Textile & Surface Design Traditions","desc":"Dense, solid embroidery style with strong filled forms and enduring decorative weight.","prompt":"Use Gujarat Pakko embroidery style: dense filled stitching, bold motif solidity, mirror accents, highly tactile handcrafted surface, strong decorative impact."},
  {"id":29,"name":"Kharek Embroidery","category":"Textile & Surface Design Traditions","desc":"Structured embroidery style marked by rectilinear logic and strong counted divisions.","prompt":"Apply Gujarat Kharek embroidery aesthetics: rectilinear counted-thread motifs, bold geometric divisions, vivid threadwork, handcrafted pattern discipline, textile structure and rhythm."},
  {"id":30,"name":"Mirror Work (Shisha Embroidery)","category":"Textile & Surface Design Traditions","desc":"Reflective embellishment tradition using inset mirrors to animate textile surfaces with light.","prompt":"Use Gujarat shisha mirror-work aesthetics: sparkling inset mirrors, bright embroidered surrounds, festive textile surface, reflective folk ornament, handcrafted celebratory richness."},
  {"id":31,"name":"Appliqué Work (Katab)","category":"Textile & Surface Design Traditions","desc":"Layered cloth-cut decoration building motifs through stitched shapes and contrasting color blocks.","prompt":"Incorporate Gujarat Katab appliqué: layered cut-cloth motifs, stitched silhouettes, bold color contrast, handcrafted textile collage, graphic ornamental patterning."},
  {"id":32,"name":"Patchwork Textile Art","category":"Textile & Surface Design Traditions","desc":"Composed textile surfaces assembled from varied fragments, patterns, and tactile histories.","prompt":"Use Gujarat patchwork textile aesthetics: assembled fabric fragments, stitched composition, mixed folk patterns, tactile layering, colorful handcrafted collage effect."},
  {"id":33,"name":"Lippan Kaam","category":"Craft & Material Arts","desc":"Mud-and-mirror relief work creating raised geometric and floral surfaces on walls, especially in Kutch.","prompt":"Apply Gujarat Lippan Kaam style: mud-relief wall art, inset mirrors, desert-earth palette, raised geometric and floral motifs, handcrafted architectural texture."},
  {"id":34,"name":"Terracotta Pottery","category":"Craft & Material Arts","desc":"Earthen pottery tradition shaped by hand and kiln, often with tactile simplicity and ritual/domestic function.","prompt":"Use Gujarat terracotta pottery aesthetics: warm earthen clay, handmade vessel forms, matte fired texture, subtle incised ornament, rustic artisanal authenticity."},
  {"id":35,"name":"Clay Idol Making","category":"Craft & Material Arts","desc":"Sculptural craft tradition of devotional and festive clay figures with hand-shaped expressiveness.","prompt":"Incorporate Gujarat clay idol-making style: hand-sculpted devotional figures, earthen materiality, painted accents, ritual craftsmanship, expressive artisanal form."},
  {"id":36,"name":"Wood Carving (Saurashtra/Kutch)","category":"Craft & Material Arts","desc":"Decorative and architectural carving tradition featuring floral, figural, and geometric motifs.","prompt":"Use Gujarat wood carving aesthetics from Saurashtra and Kutch: carved floral panels, deep relief detail, heritage craftsmanship, warm timber tone, ornate architectural character."},
  {"id":37,"name":"Stone Carving","category":"Craft & Material Arts","desc":"Chiseled decorative stonework found in sacred and civic contexts, often rich in pattern and relief.","prompt":"Apply Gujarat stone carving style: chiseled relief ornament, floral and geometric motifs, heritage monument craftsmanship, tactile mineral texture, intricate carved depth."},
  {"id":38,"name":"Marble Carving","category":"Craft & Material Arts","desc":"Refined sculptural carving in marble emphasizing delicacy, polish, and devotional ornament.","prompt":"Use Gujarat marble carving aesthetics: polished pale stone, delicate relief carving, sacred ornament, floral precision, luminous sculptural craftsmanship."},
  {"id":39,"name":"Lacquer Work (Lac-turned wood)","category":"Craft & Material Arts","desc":"Turned wood finished with lacquer for smooth, glossy, colorful decorative objects.","prompt":"Incorporate Gujarat lacquered woodcraft: turned wooden forms, glossy lacquer finish, bright concentric bands, artisanal toy-craft charm, polished decorative surface."},
  {"id":40,"name":"Metal Craft (Brass, Bell Metal)","category":"Craft & Material Arts","desc":"Functional and decorative metalwork shaped into vessels, ritual objects, and crafted forms.","prompt":"Use Gujarat brass and bell-metal craft aesthetics: hand-worked metal surfaces, hammered glow, traditional vessel forms, artisanal patina, heritage utility and ornament."},
  {"id":41,"name":"Copper Bell Making (Kutch)","category":"Craft & Material Arts","desc":"Distinctive pastoral bell craft with forged copper-alloy surfaces and resonant handcrafted form.","prompt":"Apply Gujarat Kutch copper bell-making style: forged pastoral bells, weathered metallic patina, handcrafted rivets and contours, rustic artisanal authenticity."},
  {"id":42,"name":"Silver Jewelry Craft (Kutchi/Tribal)","category":"Craft & Material Arts","desc":"Bold tribal and regional jewelry traditions with heavy silver forms, pendants, cuffs, and symbolic ornament.","prompt":"Use Gujarat Kutchi tribal silver jewelry aesthetics: bold hammered silver, chunky adornment, ethnic ornament, engraved detail, handcrafted heritage luxury."},
  {"id":43,"name":"Beadwork (Torans, ornaments)","category":"Craft & Material Arts","desc":"Decorative bead craft creating torans, hangings, and ornaments through patterned repetition and color.","prompt":"Incorporate Gujarat beadwork aesthetics: colorful bead-pattern construction, decorative hangings, geometric ornament, handcrafted festive shimmer, toran-inspired detailing."},
  {"id":44,"name":"Leather Craft (Footwear, bags)","category":"Craft & Material Arts","desc":"Handmade leather goods enriched by stitch, form, and decorative embellishment.","prompt":"Use Gujarat leather craft inspiration: hand-stitched artisanal leather, embossed and embroidered details, heritage footwear and bag aesthetics, warm material richness."},
  {"id":45,"name":"Bamboo Craft","category":"Craft & Material Arts","desc":"Lightweight craft tradition using split bamboo in utility and decorative objects.","prompt":"Apply Gujarat bamboo craft aesthetics: split bamboo weaving, natural cane tones, lightweight handcrafted structure, eco-artisan material beauty, rhythmic linear pattern."},
  {"id":46,"name":"Cane Weaving","category":"Craft & Material Arts","desc":"Interlaced cane surfaces creating texture, translucency, and structural rhythm in everyday objects.","prompt":"Use Gujarat cane weaving style: interlaced natural fibers, airy woven pattern, warm neutral palette, handcrafted furniture and basket texture, elegant material geometry."},
  {"id":47,"name":"Stepwell Architecture (Vav)","category":"Architectural & Sculptural Styles","desc":"Monumental subterranean architecture with descending terraces, carved columns, and dramatic geometric depth.","prompt":"Incorporate Gujarat vav stepwell architecture: descending stone terraces, carved pillars, monumental symmetry, sacred water architecture, dramatic perspective and shadow."},
  {"id":48,"name":"Maru-Gurjara Temple Architecture","category":"Architectural & Sculptural Styles","desc":"Highly ornate western Indian temple style defined by profuse carving, articulated towers, and precise stone ornament.","prompt":"Use Maru-Gurjara temple architecture from Gujarat: intricately carved sandstone temple forms, soaring shikhara, ornate columns, sculptural detail, sacred symmetry."},
  {"id":49,"name":"Jain Temple Marble Art","category":"Architectural & Sculptural Styles","desc":"Exquisite marble temple carving marked by filigreed ceilings, purity of material, and devotional intricacy.","prompt":"Apply Gujarat Jain temple marble art aesthetics: luminous white marble, ultra-fine carved ceilings, sacred precision, serene ornament, celestial geometric detail."},
  {"id":50,"name":"Haveli Wood Architecture","category":"Architectural & Sculptural Styles","desc":"Traditional mansion architecture with carved facades, balconies, brackets, and rich wooden detail.","prompt":"Use Gujarat haveli wood architecture: carved timber facades, jharokha balconies, ornamental brackets, heritage urban craft, warm richly detailed wood texture."},
  {"id":51,"name":"Islamic-Geometric Indo-Saracenic Design","category":"Architectural & Sculptural Styles","desc":"Sultanate-era design vocabulary blending Islamic geometry, arches, and local craftsmanship in stone and structure.","prompt":"Incorporate Gujarat Sultanate Indo-Saracenic aesthetics: pointed arches, geometric stone ornament, Islamic patterns, carved facades, historic syncretic architectural elegance."},
  {"id":52,"name":"Torana (Ceremonial gateways)","category":"Architectural & Sculptural Styles","desc":"Decorative gateway tradition with symbolic framing, festivity, and processional significance.","prompt":"Use Gujarat torana gateway aesthetics: ceremonial entrance framing, carved symbolic motifs, festive vertical composition, sacred threshold design, ornate decorative structure."},
  {"id":53,"name":"Jali (Lattice Stone Carving)","category":"Architectural & Sculptural Styles","desc":"Perforated stone screens producing intricate geometry, filtered light, and cooling shadow patterns.","prompt":"Apply Gujarat jali stone-carving aesthetics: perforated lattice geometry, filtered sunlight, delicate stone screenwork, sacred architectural pattern, elegant shadow play."},
  {"id":54,"name":"Garba (Dance + Costume Art)","category":"Performing & Visual Culture","desc":"Festive dance culture combining circular movement, embroidered costume, mirror work, rhythm, and communal spectacle.","prompt":"Use Gujarat Garba aesthetics: swirling circular dance energy, embroidered costumes, mirror work sparkle, festive color, rhythmic celebratory motion, Navratri atmosphere."},
  {"id":55,"name":"Dandiya Raas","category":"Performing & Visual Culture","desc":"Stick dance tradition marked by paired choreography, vivid garments, and kinetic celebratory patterns.","prompt":"Incorporate Gujarat Dandiya Raas style: dynamic stick dance motion, colorful festive garments, mirrored textiles, rhythmic paired composition, energetic celebration."},
  {"id":56,"name":"Bhavai Folk Theatre","category":"Performing & Visual Culture","desc":"Portable folk theatre tradition with dramatic costume, satire, storytelling, and performative visual identity.","prompt":"Apply Gujarat Bhavai folk theatre aesthetics: expressive costume, dramatic stage presence, folk storytelling mood, colorful performance design, artisanal theatricality."},
  {"id":57,"name":"Puppetry (Kathputli – regional forms)","category":"Performing & Visual Culture","desc":"Regional puppetry traditions with stylized costume, painted faces, and narrative performance craft.","prompt":"Use Gujarat regional puppetry aesthetics: handcrafted puppets, painted faces, folk costume detailing, theatrical staging, playful artisanal storytelling."},
  {"id":58,"name":"Folk Costume Design","category":"Performing & Visual Culture","desc":"Regional clothing traditions of Kutch and Saurashtra featuring embroidery, mirrors, silhouette, and layered ornament.","prompt":"Incorporate Gujarat folk costume design: Kutchi and Saurashtra dress, mirror embroidery, layered textiles, bold silhouette, festive jewelry, richly decorated apparel."},
  {"id":59,"name":"Rangoli (Sathiya patterns)","category":"Ritual & Decorative Arts","desc":"Threshold and ritual floor art using auspicious motifs, geometric patterning, and everyday sacred decoration.","prompt":"Use Gujarat rangoli and sathiya aesthetics: auspicious threshold patterns, bright powdered color, geometric folk motifs, symmetrical ritual floor art, festive welcome design."},
  {"id":60,"name":"Mandana-style floor art","category":"Ritual & Decorative Arts","desc":"Regional floor-art overlap emphasizing geometric, symbolic, and ritualized linear compositions.","prompt":"Apply Gujarat regional Mandana-like floor art: chalked geometric ritual motifs, linear symmetry, hand-drawn courtyard design, sacred domestic ornament."},
  {"id":61,"name":"Toran (Decorative door hangings)","category":"Ritual & Decorative Arts","desc":"Decorative hanging tradition using fabric, beads, mirrors, leaves, or embroidered motifs to ornament entrances.","prompt":"Use Gujarat toran hanging aesthetics: decorative doorway garland, embroidered or beaded motifs, festive symmetry, welcoming threshold ornament, handcrafted folk detail."},
  {"id":62,"name":"Pichwai","category":"Ritual & Decorative Arts","desc":"Devotional painted-cloth tradition centered on Krishna imagery, lotuses, cows, ornamented borders, and sacred atmosphere.","prompt":"Incorporate Gujarat-region Pichwai influence: devotional cloth painting, lotus and cow motifs, ornate shrine backdrop, sacred stillness, richly detailed ceremonial composition."}
]

root = r"C:\Users\vivek\.openclaw\workspace\gujarat-art-styles"
os.makedirs(os.path.join(root, 'data'), exist_ok=True)
os.makedirs(os.path.join(root, 'images'), exist_ok=True)

for s in styles:
    s['slug'] = f"{s['id']:02d}-" + ''.join(c.lower() if c.isalnum() else '-' for c in s['name']).strip('-')
    while '--' in s['slug']:
        s['slug'] = s['slug'].replace('--','-')
    s['image'] = f"images/{s['slug']}.png"

with open(os.path.join(root, 'data', 'styles.json'), 'w', encoding='utf-8') as f:
    json.dump(styles, f, indent=2, ensure_ascii=False)

batch = []
for s in styles:
    batch.append({
        'name': s['slug'],
        'prompt': f"Create a museum-quality visual hero image representing {s['name']} from Gujarat, India. {s['desc']} Visual emphasis on authentic materials, motifs, patterns, color systems, and composition. Make it richly detailed, beautiful, educational, and unmistakably rooted in Gujarati craft traditions. Avoid text, watermarks, collage labels, or modern branding.",
        'resolution': '2K',
        'aspect_ratio': '4:5'
    })
with open(os.path.join(root, 'data', 'batch-config.json'), 'w', encoding='utf-8') as f:
    json.dump(batch, f, indent=2, ensure_ascii=False)

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Gujarat Art Styles Atlas</title>
  <style>
    :root {
      --bg: #f6f0e6;
      --paper: rgba(255,255,255,0.72);
      --text: #241714;
      --muted: #6e564d;
      --accent: #a12f2b;
      --accent-2: #c98b00;
      --deep: #4f2019;
      --line: rgba(79,32,25,0.12);
      --shadow: 0 20px 60px rgba(71,40,25,.12);
      --radius: 24px;
      --font: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0; font-family: var(--font); color: var(--text);
      background:
        radial-gradient(circle at 20% 10%, rgba(201,139,0,.16), transparent 24%),
        radial-gradient(circle at 80% 0%, rgba(161,47,43,.12), transparent 24%),
        linear-gradient(180deg, #f9f3eb, #f3ebdf 40%, #f8f2ea 100%);
      min-height: 100vh;
    }
    header {
      padding: 64px 24px 32px;
      position: relative;
      overflow: hidden;
    }
    .wrap { max-width: 1320px; margin: 0 auto; }
    .eyebrow { text-transform: uppercase; letter-spacing: .18em; font-size: 12px; color: var(--accent); font-weight: 700; }
    h1 { font-size: clamp(40px, 8vw, 88px); line-height: .95; margin: 16px 0; max-width: 900px; }
    .lead { max-width: 860px; font-size: 18px; line-height: 1.7; color: var(--muted); }
    .hero-grid { display: grid; grid-template-columns: 1.4fr .8fr; gap: 24px; margin-top: 36px; }
    .glass {
      background: var(--paper); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,.5);
      border-radius: var(--radius); box-shadow: var(--shadow);
    }
    .hero-card { padding: 28px; }
    .pillbar { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 18px; }
    .pill { padding: 10px 14px; border-radius: 999px; background: rgba(161,47,43,.08); color: var(--deep); font-size: 13px; }
    .stats { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; }
    .stat { padding: 20px; }
    .stat strong { display: block; font-size: 30px; }
    .toolbar { position: sticky; top: 0; z-index: 10; padding: 16px 24px; backdrop-filter: blur(12px); background: rgba(246,240,230,.78); border-top: 1px solid transparent; border-bottom: 1px solid var(--line); }
    .toolbar-inner { max-width: 1320px; margin: 0 auto; display:flex; gap:16px; align-items:center; flex-wrap:wrap; }
    input, select { border:1px solid var(--line); background:white; border-radius: 14px; padding: 14px 16px; font: inherit; color: var(--text); }
    input { flex:1 1 260px; min-width:220px; }
    select { min-width: 220px; }
    .grid { max-width: 1320px; margin: 28px auto 80px; padding: 0 24px; display: grid; grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 22px; }
    .card { overflow: hidden; display:flex; flex-direction:column; }
    .art {
      aspect-ratio: 4 / 5; position: relative; overflow: hidden; background:
      linear-gradient(135deg, rgba(161,47,43,.18), rgba(201,139,0,.10)),
      repeating-linear-gradient(45deg, rgba(161,47,43,.05), rgba(161,47,43,.05) 10px, rgba(255,255,255,.08) 10px, rgba(255,255,255,.08) 20px);
    }
    .art img { width: 100%; height: 100%; object-fit: cover; display:block; }
    .badge { position: absolute; top: 14px; left: 14px; padding: 8px 10px; border-radius: 999px; background: rgba(255,255,255,.82); font-size: 11px; letter-spacing: .08em; text-transform: uppercase; }
    .content { padding: 18px; display:flex; flex-direction:column; gap:14px; }
    .title-row { display:flex; justify-content:space-between; gap:12px; align-items:flex-start; }
    h3 { margin: 0; font-size: 22px; line-height: 1.1; }
    .num { color: var(--accent); font-weight: 800; font-size: 14px; min-width: 32px; text-align:right; }
    .desc { color: var(--muted); font-size: 14px; line-height: 1.65; }
    .prompt { background: rgba(79,32,25,.04); border:1px solid var(--line); border-radius: 18px; padding: 14px; font-size: 13px; line-height: 1.55; color: var(--deep); }
    .actions { display:flex; gap:10px; }
    button {
      border: none; cursor: pointer; border-radius: 14px; padding: 12px 14px; font: inherit; font-weight: 700;
      background: var(--deep); color: white;
    }
    button.secondary { background: white; color: var(--deep); border:1px solid var(--line); }
    footer { max-width:1320px; margin:0 auto; padding:0 24px 60px; color:var(--muted); }
    .empty { padding: 40px 24px; text-align:center; color: var(--muted); }
    @media (max-width: 900px) { .hero-grid { grid-template-columns: 1fr; } }
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <div class="eyebrow">Gujarat craft atlas</div>
      <h1>62 art styles from Gujarat, turned into a visual prompt library.</h1>
      <p class="lead">A design-first website that maps folk painting, textile traditions, craft practices, architecture, performance, and ritual arts from Gujarat. Every card includes a reusable AI style prompt so any designer can borrow the visual language without losing its roots.</p>
      <div class="hero-grid">
        <div class="glass hero-card">
          <strong>What this is</strong>
          <p class="lead" style="font-size:16px;margin:14px 0 0;max-width:none;">Browse all major styles, inspect their visual DNA, and copy prompts to infuse them into brand systems, packaging, illustrations, spatial concepts, interfaces, campaign art, editorial layouts, and generative-image workflows.</p>
          <div class="pillbar">
            <div class="pill">Folk painting</div><div class="pill">Textile systems</div><div class="pill">Embroidery grammars</div><div class="pill">Architectural motifs</div><div class="pill">Ritual surfaces</div><div class="pill">AI-ready prompts</div>
          </div>
        </div>
        <div class="stats">
          <div class="glass stat"><strong>62</strong><span>Styles mapped</span></div>
          <div class="glass stat"><strong>6</strong><span>Major categories</span></div>
          <div class="glass stat"><strong>1-click</strong><span>Prompt copy</span></div>
          <div class="glass stat"><strong>Visual</strong><span>Gallery-first browse</span></div>
        </div>
      </div>
    </div>
  </header>
  <div class="toolbar">
    <div class="toolbar-inner">
      <input id="search" placeholder="Search styles, motifs, materials, communities..." />
      <select id="category"><option value="">All categories</option></select>
    </div>
  </div>
  <main>
    <section id="grid" class="grid"></section>
    <div id="empty" class="empty" hidden>No styles match that filter.</div>
  </main>
  <footer>Built in the workspace as a Gujarat visual style reference. Use prompts as a starting point, then refine with specific color palettes, materials, subjects, and composition requirements for your own AI design workflows.</footer>
  <script>
    let DATA = [];
    const grid = document.getElementById('grid');
    const search = document.getElementById('search');
    const category = document.getElementById('category');
    const empty = document.getElementById('empty');

    function copyPrompt(text, btn){
      navigator.clipboard.writeText(text).then(() => {
        const old = btn.textContent; btn.textContent = 'Copied';
        setTimeout(() => btn.textContent = old, 1400);
      });
    }

    function render(){
      const q = search.value.toLowerCase().trim();
      const cat = category.value;
      const items = DATA.filter(item => {
        const hay = `${item.name} ${item.category} ${item.desc} ${item.prompt}`.toLowerCase();
        return (!q || hay.includes(q)) && (!cat || item.category === cat);
      });
      grid.innerHTML = '';
      empty.hidden = items.length !== 0;
      items.forEach(item => {
        const card = document.createElement('article');
        card.className = 'card glass';
        const imgError = `this.style.display='none'; this.parentElement.style.background+='';`;
        card.innerHTML = `
          <div class="art">
            <div class="badge">${item.category}</div>
            <img src="${item.image}" alt="${item.name}" loading="lazy" onerror="${imgError}" />
          </div>
          <div class="content">
            <div class="title-row"><h3>${item.name}</h3><div class="num">${String(item.id).padStart(2,'0')}</div></div>
            <div class="desc">${item.desc}</div>
            <div class="prompt">${item.prompt}</div>
            <div class="actions">
              <button data-prompt="${item.prompt.replace(/"/g,'&quot;')}">Copy prompt</button>
              <button class="secondary" data-style="${item.name.replace(/"/g,'&quot;')}">Use style</button>
            </div>
          </div>`;
        const [copyBtn, useBtn] = card.querySelectorAll('button');
        copyBtn.onclick = () => copyPrompt(item.prompt, copyBtn);
        useBtn.onclick = () => copyPrompt(`Create a design using ${item.name} from Gujarat as the primary visual language. ${item.prompt}`, useBtn);
        grid.appendChild(card);
      });
    }

    fetch('data/styles.json').then(r => r.json()).then(data => {
      DATA = data;
      [...new Set(DATA.map(d => d.category))].sort().forEach(c => {
        const o = document.createElement('option'); o.value = c; o.textContent = c; category.appendChild(o);
      });
      render();
    });
    search.addEventListener('input', render);
    category.addEventListener('change', render);
  </script>
</body>
</html>'''

with open(os.path.join(root, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print('Built site scaffold with', len(styles), 'styles')
