import svgutils

svg = svgutils.transform.fromfile('./jacobroberts/static/github-mark.svg')
svg = svgutils.compose.SVG('./jacobroberts/static/github-mark.svg')
svg.scale(1/3.7)
figure = svgutils.compose.Figure(26, 26, svg)
figure.save('./jacobroberts/static/github-mark-26.svg')