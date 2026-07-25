# Xiao Ziheng - Academic Homepage

This repository contains the source code and academic content for [lumia-xiao.github.io](https://lumia-xiao.github.io/), the personal homepage of **Xiao Ziheng**, Senior Research Fellow at the Energy Research Institute @ NTU (ERI@N), Nanyang Technological University, Singapore.

> **Template provenance:** This personal homepage is built from the open-source [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll template and has been substantially customized with Xiao Ziheng's own biography, publications, teaching records, projects, photographs, and CV materials. Academic Pages and its upstream theme authors are acknowledged below; this repository is not the upstream Academic Pages project.

## Research

The site presents research in power electronics and artificial intelligence, with an emphasis on:

- Medium-voltage DC systems
- Dual active bridge converters
- LLC and CLLC resonant converters
- Multilevel and multiphase DC-DC converters
- Wireless power transfer
- Data-driven modelling, transfer learning, and AI-assisted converter design

## Site Contents

- [About](https://lumia-xiao.github.io/): biography, research interests, awards, and academic service
- [Publications](https://lumia-xiao.github.io/publications/): journal articles, abstracts, figures, citations, and DOI links
- [Talks](https://lumia-xiao.github.io/talks/): conference talks and presentations
- [Teaching](https://lumia-xiao.github.io/teaching/): postgraduate course history at NTU
- [Portfolio](https://lumia-xiao.github.io/portfolio/): conference, research, and academic activity photographs
- [CV](https://lumia-xiao.github.io/cv/): web CV plus downloadable one-page and full PDF versions
- [Students](https://lumia-xiao.github.io/students/): student mentoring and co-mentoring records

## Repository Structure

| Path | Purpose |
|---|---|
| `_pages/` | Main pages, including About, CV, Publications, Teaching, and Students |
| `_publications/` | Publication metadata, abstracts, figures, citations, and DOI links |
| `_talks/` | Conference talks and presentations |
| `_teaching/` | Teaching records |
| `_portfolio/` | Academic activity and conference galleries |
| `_data/` | Navigation and localized interface data |
| `images/` | Profile, publication, and portfolio images |
| `files/` | Downloadable CV files |
| `assets/` and `_sass/` | JavaScript and site styling |

## Local Development

The site is built with Jekyll and deployed through GitHub Pages.

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```

The local preview is available at [http://localhost:4000](http://localhost:4000). Changes to `_config.yml` require restarting the Jekyll process.

Docker is also supported:

```bash
docker compose up --build
```

## Content Maintenance

Add or update academic records by editing the Markdown files in the relevant collection. Publication and portfolio images displayed by the site use WebP assets for faster loading. Regenerate optimized images after replacing source PNG or JPG files:

```bash
python -m pip install Pillow
python scripts/optimize_site_images.py
```

Before publishing, verify front matter, local links, image references, and the generated Jekyll site.

## Technology and Attribution

This site uses [Jekyll](https://jekyllrb.com/) and is based on the open-source [Academic Pages](https://github.com/academicpages/academicpages.github.io) theme, which is derived from [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes). Site content and personal materials belong to Xiao Ziheng; theme components remain subject to their respective open-source licenses.

## Contact

For corrections related to this website, open an [issue](https://github.com/Lumia-Xiao/Lumia-Xiao.github.io/issues). Academic contact information is available on the [homepage](https://lumia-xiao.github.io/).
