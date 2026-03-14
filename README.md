---
title: "Spatial Mechanics - Collaboration Guide"
description: "Contributing guide for Spatial Mechanics course content"
tableOfContents: true
sidebar:
  order: 999
---

# Spatial Mechanics

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Contributors Welcome](https://img.shields.io/badge/contributors-welcome-orange)

**Read this course at:** [https://siliconwit.com/education/spatial-mechanics/](https://siliconwit.com/education/spatial-mechanics/)

A course on 3D kinematics and spatial mechanism analysis for mechatronic systems. Covers kinematic joints, degrees of freedom, transformation matrices, spatial rotations, matrix methods for link modeling, advanced spatial mechanisms, and computer simulation with Python.

## Lessons

| # | Title |
|---|-------|
| 1 | Kinematic Joints and Degrees of Freedom |
| 2 | Planar Transformations and Mathematical Foundations |
| 3 | 3D Rotation Matrices and Spatial Transformations |
| 4 | Elementary Matrix Methods and Link Modeling |
| 5 | Advanced Spatial Mechanisms Analysis |
| 6 | Computer Simulation and System Integration |

## File Structure

```
spatial-mechanics/
├── index.mdx
├── kinematic-joints-degrees-freedom.mdx
├── planar-transformations-foundations.mdx
├── spatial-rotations-transformations.mdx
├── matrix-methods-link-modeling.mdx
├── advanced-spatial-mechanisms.mdx
├── computer-simulation-integration.mdx
└── README.md
```

## How to Contribute

1. Fork the repository: [SiliconWit/spatial-mechanics](https://github.com/SiliconWit/spatial-mechanics)
2. Create a feature branch: `git checkout -b feature/your-topic`
3. Make your changes and commit with a clear message
4. Push to your fork and open a Pull Request against `main`
5. Describe what you changed and why in the PR description

## Content Standards

- All lesson files use `.mdx` format
- `<BionicText>` may be used in later content sections but not in lesson intro paragraphs
- Code blocks should include a title attribute:
  ````mdx
  ```python title="rotation_matrix.py"
  import numpy as np
  R = Rz(theta) @ Ry(phi) @ Rx(psi)
  ```
  ````
- Use Starlight components (`<Tabs>`, `<TabItem>`, `<Steps>`, `<Card>`) where appropriate
- Keep paragraphs concise and focused on practical application
- Include working Python examples that readers can run directly
- Mathematical notation uses LaTeX in MDX

## Local Development

Clone the main site repository and initialize submodules:

```bash
git clone --recurse-submodules <main-repo-url>
cd siliconwit-com
npm install
npm run dev
```

To test a production build:

```bash
npm run build
```

## License

This course content is released under the [MIT License](LICENSE).
