#!/usr/bin/env python3

import EpistemicGraph

eg = EpistemicGraph.EG('mail-in', 'png', True)

# Primary claim
primary_claim = 'Mail-in voting is better than just in-person voting.'
primary = eg.node('none', primary_claim, [], primary=True)

# Arguments for/against
higher_part = eg.node('for', 'Higher participation\n(evidence?)', [primary])

more_informed = eg.node('for', 'voters are more informed\n(evidence?)', [primary])

atk_surface = eg.node('against', 'greater attack surface area\n(evidence?)', [primary])

# Title
eg.finish(f'\nArguments For & Against:\n{primary_claim}')

